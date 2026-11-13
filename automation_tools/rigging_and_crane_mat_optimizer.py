"""
================================================================================
LARSEN & TOUBRO - CMPD / SE&HLD HEAVY RIGGING & LIFTING AUTOMATION
AUTOMATION SUITE 02: TANDEM CRANE RIGGING & OUTRIGGER CRANE MAT OPTIMIZER
Compliant with: BS 7121 (Safe Use of Cranes), OSHA 1926.1400, and L&T Heavy Lift SOPs
================================================================================
"""

import math

def calculate_tandem_lift(
    load_weight_tonnes=120.0,       # Total weight of precast / steel element (MT)
    rigging_gear_weight_tonnes=6.0,  # Shackles, spreader beam, grommets (MT)
    daf=1.20,                       # Dynamic Amplification Factor (typically 1.15 - 1.25)
    sling_angle_deg=60.0,           # Angle between sling and horizontal (min 60 deg)
    num_slings=4,                   # Number of lifting legs
    crane1_capacity_chart_tonnes=150.0,# Crane 1 net rated capacity at operating radius
    crane2_capacity_chart_tonnes=150.0,# Crane 2 net rated capacity at operating radius
    share_crane1=0.55,              # Load share on Crane 1 based on CG eccentricity
    crane_gross_weight_tonnes=110.0,# Crane self weight with counterweights
    mat_length_m=3.0,               # Outrigger mat length
    mat_width_m=2.0,                # Outrigger mat width
    allowable_sbc_kpa=180.0         # Ground safe bearing capacity (kPa)
):
    print("=" * 80)
    print(" L&T HEAVY RIGGING & TANDEM CRANE LIFT OPTIMIZATION ENGINE")
    print("=" * 80)

    # 1. Gross Lifted Weight
    w_gross = (load_weight_tonnes + rigging_gear_weight_tonnes) * daf
    print(f" Gross Factored Load (incl. Rigging & DAF={daf}): {w_gross:.2f} MT ({w_gross * 9.81:.1f} kN)")

    # 2. Sling Tension Analysis
    theta_rad = math.radians(sling_angle_deg)
    sling_angle_factor = 1.0 / math.sin(theta_rad)
    tension_per_sling_mt = (w_gross / num_slings) * sling_angle_factor
    print(f"\n SLING MECHANICS:")
    print(f" - Number of Sling Legs:                   {num_slings}")
    print(f" - Sling Angle with Horizontal:            {sling_angle_deg:.1f}°")
    print(f" - Sling Angle Multiplier (1/sin theta):   {sling_angle_factor:.3f}")
    print(f" - Factored Tension per Sling Leg:         {tension_per_sling_mt:.2f} MT ({tension_per_sling_mt * 9.81:.1f} kN)")
    
    if sling_angle_deg < 60.0:
        print(" [WARNING] Sling angle is below 60°. L&T Heavy Lift SOP strictly mandates theta >= 60°!")

    # 3. Dual Crane Load Sharing & Capacity Checks
    share_crane2 = 1.0 - share_crane1
    load_c1_mt = w_gross * share_crane1
    load_c2_mt = w_gross * share_crane2

    util_c1 = (load_c1_mt / crane1_capacity_chart_tonnes) * 100.0
    util_c2 = (load_c2_mt / crane2_capacity_chart_tonnes) * 100.0

    print(f"\n TANDEM CRANE UTILIZATION CHECKS:")
    print(f" - Crane 1 (CG Share {share_crane1*100:.0f}%): Load = {load_c1_mt:.2f} MT / Rated {crane1_capacity_chart_tonnes:.1f} MT -> Utilization: {util_c1:.1f}%")
    print(f" - Crane 2 (CG Share {share_crane2*100:.0f}%): Load = {load_c2_mt:.2f} MT / Rated {crane2_capacity_chart_tonnes:.1f} MT -> Utilization: {util_c2:.1f}%")

    max_tandem_util_limit = 75.0 # L&T Safety Directive caps tandem lifts at 75% rated chart
    status_c1 = "SAFE" if util_c1 <= max_tandem_util_limit else "OVERSTRESSED / VIOLATION"
    status_c2 = "SAFE" if util_c2 <= max_tandem_util_limit else "OVERSTRESSED / VIOLATION"
    print(f" - Status Crane 1: {status_c1} (Threshold: <= {max_tandem_util_limit}%)")
    print(f" - Status Crane 2: {status_c2} (Threshold: <= {max_tandem_util_limit}%)")

    # 4. Outrigger Mat Ground Bearing Pressure (GBP)
    # Maximum outrigger reaction under slewed pick condition (approx. 70% of total crane + load weight)
    total_crane_system_mt = crane_gross_weight_tonnes + load_c1_mt
    max_outrigger_reaction_mt = total_crane_system_mt * 0.70
    reaction_kn = max_outrigger_reaction_mt * 9.81

    mat_area_m2 = mat_length_m * mat_width_m
    gbp_actual_kpa = reaction_kn / mat_area_m2

    print(f"\n OUTRIGGER CRANE MAT GROUND BEARING PRESSURE (GBP):")
    print(f" - Max Dynamic Outrigger Reaction:         {max_outrigger_reaction_mt:.2f} MT ({reaction_kn:.1f} kN)")
    print(f" - Spreader Mat Dimensions:                {mat_length_m:.1f} m x {mat_width_m:.1f} m (Area: {mat_area_m2:.2f} m²)")
    print(f" - Actual Peak Ground Bearing Pressure:    {gbp_actual_kpa:.2f} kPa")
    print(f" - Allowable Ground SBC:                   {allowable_sbc_kpa:.2f} kPa")

    gbp_status = "PASSED - SOIL BEARING ADEQUATE" if gbp_actual_kpa <= allowable_sbc_kpa else "FAILED - ENLARGE MAT OR STABILIZE SOIL"
    print(f" - GBP Verification:                       {gbp_status}")
    print("=" * 80)

    return {
        "w_gross_mt": w_gross,
        "tension_per_sling_mt": tension_per_sling_mt,
        "util_crane1": util_c1,
        "util_crane2": util_c2,
        "gbp_actual_kpa": gbp_actual_kpa,
        "gbp_status": gbp_status
    }

if __name__ == "__main__":
    calculate_tandem_lift()
