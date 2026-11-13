"""
================================================================================
LARSEN & TOUBRO - EDRC / CMPD DIGITAL ENGINEERING
AUTOMATION SUITE 01: FORMWORK LATERAL CONCRETE PRESSURE CALCULATOR
Compliant with: CIRIA Report 108, DIN 18218:2010, ACI 347R-14, and IS 14687:1999
================================================================================
"""

import math

def calculate_lateral_pressure(
    h_pour_m=6.0,          # Total vertical pour height in meters
    rate_m_hr=2.0,         # Rate of placement in meters/hour
    temp_c=28.0,           # Concrete temperature at placement in Celsius
    unit_weight_kn_m3=25.0,# Concrete density in kN/m3
    cement_type="OPC",     # OPC, PPC, or GGBS
    form_type="wall",      # wall or column
    admixture_retarder=False
):
    print("=" * 75)
    print(" L&T FORMWORK LATERAL CONCRETE PRESSURE CALCULATION ENGINE")
    print("=" * 75)
    print(f" Input Parameters:")
    print(f" - Form Height (H):          {h_pour_m:.2f} m")
    print(f" - Pour Rate (R):            {rate_m_hr:.2f} m/hr")
    print(f" - Concrete Temp (T):        {temp_c:.1f} °C")
    print(f" - Unit Weight (gamma):      {unit_weight_kn_m3:.1f} kN/m³")
    print(f" - Cement Type:              {cement_type}")
    print(f" - Structural Form:          {form_type.upper()}")
    print(f" - Admixture Retarded:       {'YES' if admixture_retarder else 'NO'}")
    print("-" * 75)

    # 1. Full Hydrostatic Limit (Upper Bound)
    p_hydrostatic = unit_weight_kn_m3 * h_pour_m

    # 2. CIRIA Report 108 Method
    c1 = 1.5 if form_type.lower() == "column" else 1.0
    c2 = 0.30 if cement_type.upper() == "OPC" else 0.45
    if admixture_retarder:
        c2 *= 1.25

    temp_factor_k = ((36.0 / (temp_c + 16.0)) ** 2)
    term1 = c1 * math.sqrt(rate_m_hr)
    remainder_h = max(0.0, h_pour_m - term1)
    ciria_pmax = unit_weight_kn_m3 * (term1 + c2 * temp_factor_k * math.sqrt(remainder_h))
    ciria_pmax = min(ciria_pmax, p_hydrostatic)

    # 3. ACI 347R-14 Method
    c_w = 1.0  # Normal weight concrete
    c_c = 1.0 if cement_type.upper() == "OPC" else 1.2
    if admixture_retarder:
        c_c = 1.4

    if form_type.lower() == "column":
        aci_pmax = c_w * c_c * (7.2 + (785.0 * rate_m_hr) / (temp_c + 17.8))
    else: # wall
        if rate_m_hr <= 2.1 and h_pour_m <= 4.2:
            aci_pmax = c_w * c_c * (7.2 + (785.0 * rate_m_hr) / (temp_c + 17.8))
        else:
            aci_pmax = c_w * c_c * (7.2 + (1156.0 / (temp_c + 17.8)) + (244.0 * rate_m_hr) / (temp_c + 17.8))
    
    aci_pmax = max(30.0, min(aci_pmax, p_hydrostatic))

    # 4. DIN 18218 (Empirical envelope for F3/F4 plastic concrete)
    v_c = rate_m_hr
    din_pmax = (18.0 + 17.0 * v_c) * (1.0 + 0.015 * (20.0 - temp_c))
    din_pmax = min(din_pmax, p_hydrostatic)

    # Recommended Design Governing Envelope
    p_design = max(ciria_pmax, aci_pmax, din_pmax)

    print(f"\n CALCULATION RESULTS & COMPARISON:")
    print(f" 1. Upper Bound Hydrostatic (gamma * H):   {p_hydrostatic:.2f} kN/m²")
    print(f" 2. CIRIA Report 108 Design Pressure:      {ciria_pmax:.2f} kN/m²")
    print(f" 3. ACI 347R-14 Governing Pressure:        {aci_pmax:.2f} kN/m²")
    print(f" 4. DIN 18218 Flowable Concrete Pressure:  {din_pmax:.2f} kN/m²")
    print("-" * 75)
    print(f" => GOVERNING DESIGN LATERAL PRESSURE:     {p_design:.2f} kN/m²")
    print("=" * 75)

    # Component Sizing & Capacity Check
    print("\n AUTOMATED SIZING OF FORMWORK TIE-RODS & WALERS:")
    # Assume Dywidag 15mm tie rods (Safe Working Load = 90 kN)
    swl_tie_15mm = 90.0 # kN
    # Required tributary area per tie rod
    a_trib_max = swl_tie_15mm / p_design
    print(f" - Safe Working Load of 15mm Dywidag Tie:  {swl_tie_15mm:.1f} kN")
    print(f" - Maximum Permissible Tributary Area:     {a_trib_max:.2f} m² per tie rod")
    
    # Recommended Grid Spacing
    s_vert = min(1.0, math.sqrt(a_trib_max * 0.8))
    s_horiz = a_trib_max / s_vert
    print(f" - Suggested Tie Grid (Vertical x Horiz):   {s_vert:.2f} m x {s_horiz:.2f} m")

    return {
        "p_hydrostatic": p_hydrostatic,
        "ciria_pmax": ciria_pmax,
        "aci_pmax": aci_pmax,
        "din_pmax": din_pmax,
        "governing_p_design": p_design,
        "suggested_vert_spacing_m": s_vert,
        "suggested_horiz_spacing_m": s_horiz
    }

if __name__ == "__main__":
    calculate_lateral_pressure()
