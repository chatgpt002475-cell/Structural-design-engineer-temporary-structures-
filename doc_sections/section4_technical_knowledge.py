import docx
from docx.shared import Inches, Pt, RGBColor
from doc_sections.helpers import (
    set_cell_background, set_cell_margins, set_cell_borders, 
    set_table_styling, add_heading_1, add_heading_2, add_heading_3,
    add_heading_4, add_body_p, add_bullet_p, add_callout
)

def build_section4_technical_knowledge(doc):
    add_heading_1(doc, "Section 4: Comprehensive Technical Knowledge Base, Formulae & Design Rules")
    
    add_body_p(doc,
        "Temporary structural design requires rigorous application of international codes of practice, advanced structural mechanics, and empirical geotechnical criteria. This section consolidates the mathematical formulations, design standards, and fundamental governing equations utilized daily across L&T engineering offices.",
        bold_prefix="The Engineering Knowledge Core: "
    )
    
    # 4.1 Master Design Codes Directory
    add_heading_2(doc, "4.1 Master Design Codes & International Standards Directory")
    code_table = doc.add_table(rows=10, cols=3)
    c_headers = ["Standard / Code", "Issuing Body & Title", "Application Domain in L&T Temporary Works"]
    c_data = [
        ("BS 5975:2019", "British Standards Institution: Code of practice for temporary works procedures and the permissible stress design of falsework", "Apex procedural governance, design check categorization (Cat 0-3), PTL/PTS protocols, and falsework stability."),
        ("IS 14687:1999", "Bureau of Indian Standards: Guidelines for Falsework for Concrete Structures", "Permissible stresses, timber and steel formwork sizing, lateral load provisions, inspection checklists."),
        ("IRC:87-2018", "Indian Roads Congress: Guidelines for the Design and Erection of Falsework for Road Bridges", "Mandatory standard for highway viaduct falsework, permissible deflections, lateral stability criteria (1.5% to 2.5% lateral load)."),
        ("IRC:6-2017", "Indian Roads Congress: Standard Specifications and Code of Practice for Road Bridges - Loads and Stresses", "Construction live loads, wind loads on bridge staging, braking/traction forces, temperature loads on form travelers."),
        ("IS 800:2007", "Bureau of Indian Standards: General Construction in Steel - Code of Practice", "Working stress & limit state design of steel staging, launching gantries, walers, struts, and truss chords."),
        ("CIRIA Report 108", "Construction Industry Research and Information Association: Concrete Pressure on Formwork", "Governing international formulation for concrete lateral pressure based on pour rate, temperature, and admixtures."),
        ("DIN 18218:2010", "Deutsches Institut für Normung: Pressure of Fresh Concrete on Vertical Formwork", "Formwork pressure prediction for high-workability and self-compacting concrete (SCC)."),
        ("EN 12812:2008", "European Committee for Standardization: Falsework - Performance Requirements and General Design", "Structural classification of falsework (Classes A, B, C), second-order analysis requirements, and testing criteria."),
        ("ACI 347R-14", "American Concrete Institute: Guide to Formwork for Concrete", "Column and wall lateral pressure formulas, safety factors, and stripping strength benchmarks.")
    ]
    for c_idx, h in enumerate(c_headers):
        code_table.cell(0, c_idx).paragraphs[0].add_run(h)
    for r_idx, row in enumerate(c_data):
        for c_idx, val in enumerate(row):
            code_table.cell(r_idx + 1, c_idx).paragraphs[0].add_run(val)
    set_table_styling(code_table, col_widths=[1.4, 2.7, 2.4], header_bg="002D62")
    
    # 4.2 Concrete Lateral Pressure on Vertical Formwork
    add_heading_2(doc, "4.2 Concrete Lateral Pressure Formulations on Vertical Formwork")
    add_body_p(doc,
        "Determining fresh concrete lateral pressure is critical to prevent formwork burst or excessive wall bulging. While fresh concrete behaves as a heavy fluid (hydrostatic pressure p = gamma * h) immediately upon placement, it rapidly develops internal shear strength and particle interlock, causing pressure to peak at a transition height (h_max) and plateau or diminish below that level."
    )
    
    add_heading_3(doc, "4.2.1 Hydrostatic Pressure (Upper Bound Limit)")
    add_body_p(doc, "For rapid pours, deep tremie underwater concrete, or highly retarded Self-Compacting Concrete (SCC), full hydrostatic pressure must be designed for:")
    add_body_p(doc, "P_max = gamma_c * H   (in kN/m2)", bold_prefix="Formula: ")
    add_body_p(doc, "Where gamma_c is the concrete unit weight (typically 24.0 kN/m2 for plain concrete, 25.0 kN/m2 for reinforced concrete, and up to 26.0 kN/m2 for high-density rebar cages), and H is the total pour height in meters.")
    
    add_heading_3(doc, "4.2.2 CIRIA Report 108 Formulation")
    add_body_p(doc, "CIRIA 108 calculates maximum lateral pressure P_max based on pour rate R (m/h), placement temperature T (°C), cement type, and vertical dimension H:")
    add_body_p(doc, "P_max = gamma_c * [ C1 * sqrt(R) + C2 * K * sqrt(H - C1 * sqrt(R)) ]   <= gamma_c * H", bold_prefix="Governing Equation: ")
    add_bullet_p(doc, "C1: Coefficient for size and shape of formwork (C1 = 1.0 for walls, C1 = 1.5 for columns).", bold_prefix="C1: ")
    add_bullet_p(doc, "C2: Constituent coefficient (C2 = 0.3 to 0.45 depending on cement type, e.g. OPC vs Fly Ash / GGBS).", bold_prefix="C2: ")
    add_bullet_p(doc, "K: Temperature factor K = ((36 / (T + 16))^2). At 30°C Indian summer conditions, K = 0.61; at 10°C winter conditions, K = 1.91 (causing a 300% increase in lateral pressure!).", bold_prefix="K Factor: ")
    add_bullet_p(doc, "R: Rate of concrete pour in meters per hour (typically 1.0 to 3.0 m/hr).", bold_prefix="R: ")
    
    add_heading_3(doc, "4.2.3 ACI 347R-14 Formulations")
    add_body_p(doc, "Under US ACI 347R-14, lateral pressure for normal weight concrete with internal vibration is given by:")
    add_bullet_p(doc, "P_max = C_w * C_c * [ 7.2 + (785 * R) / (T + 17.8) ]  (subject to min 30 kN/m2 and max gamma_c * H).", bold_prefix="Columns: ")
    add_bullet_p(doc, "For R <= 2.1 m/hr and H <= 4.2m: P_max = C_w * C_c * [ 7.2 + (785 * R) / (T + 17.8) ]. For R > 2.1 m/hr or H > 4.2m: P_max = C_w * C_c * [ 7.2 + (1156 / (T + 17.8)) + (244 * R) / (T + 17.8) ].", bold_prefix="Walls: ")
    add_bullet_p(doc, "C_w = Unit weight coefficient (1.0 for normal weight); C_c = Chemistry coefficient (1.0 for Type I OPC; 1.2 for blends with > 70% slag or fly ash; 1.4 for retarders).", bold_prefix="Coefficients: ")
    
    # 4.3 Staging Tower Stability & Buckling
    add_heading_2(doc, "4.3 Staging Tower Stability, Buckling & Slenderness Criteria")
    add_body_p(doc,
        "Staging collapses in civil engineering are predominantly triggered by unbraced length instability, eccentric loading, or lack of lateral restraint. The design of multi-tier tubular scaffolding (Cup-lock / Ring-lock) requires precise determination of the effective length factor (k)."
    )
    
    add_heading_3(doc, "4.3.1 Effective Length & Buckling Capacity")
    add_bullet_p(doc, "For fully braced staging towers with diagonal plan and sway bracing in both orthogonal directions at alternate lifts: Effective length factor k = 1.0. Unbraced length L_e = lift height (typically 1.0m, 1.5m, or 2.0m).", bold_prefix="Braced System (Non-Sway): ")
    add_bullet_p(doc, "For towers lacking complete diagonal bracing or where horizontal ledgers are omitted at top/bottom levels: k = 2.0 to 2.5 (Sway mode), reducing Euler buckling capacity by up to 75%!", bold_prefix="Unbraced System (Sway): ")
    add_bullet_p(doc, "Top U-head and bottom base jacks create cantilever spindle extensions. The total effective unbraced length of the top standard is calculated as: L_eff,top = L_lift + 2 * L_spindle. If L_spindle exceeds 350 mm, the standard capacity must be derated by 30% to 50%.", bold_prefix="Jack Extension Derating: ")
    
    add_heading_3(doc, "4.3.2 Mandatory Lateral Load Provision (IRC:87 & BS 5975)")
    add_body_p(doc,
        "Every staging scheme must be designed to resist a mandatory minimum horizontal lateral load applied at the top deck level, acting simultaneously with vertical loads:"
    )
    add_callout(doc,
        "Minimum Lateral Load Rule (IRC:87 Clause 6.4 & BS 5975):\n"
        "H_lateral = Maximum of:\n"
        "1. 2.5% of total vertical Dead Load + Construction Live Load\n"
        "2. Wind pressure p_z acting on the exposed face of formwork and staging elements + 1.0% of vertical load\n"
        "3. Calculated longitudinal and transverse forces from braking, traction, or concrete pump discharge surges.\n"
        "This lateral force must be resisted entirely by structural bracing or anchor ties, with zero reliance on base plate friction.",
        title="MANDATORY 2.5% LATERAL LOAD RULE",
        alert_type="warning"
    )
    
    # 4.4 Wind Load Design for Temporary Structures
    add_heading_2(doc, "4.4 Wind Load Design for Temporary Structures (IS 875 Part 3:2015 & BS 5975)")
    add_body_p(doc,
        "Temporary structures are exposed to severe atmospheric wind forces during their operational life. While permanent bridges are designed for a 50-to-100-year return period, temporary works design permits a reduced return period (typically 2 to 5 years), provided strict site wind monitoring and demobilization thresholds are enforced."
    )
    add_bullet_p(doc, "V_z = V_b * k1 * k2 * k3 * k4. For a 2-year temporary exposure, risk coefficient k1 is taken as 0.71 (compared to 1.0 for permanent 50-year structures), reducing dynamic wind pressure by approximately 50% (since p_z is proportional to V_z^2).", bold_prefix="Design Wind Speed: ")
    add_bullet_p(doc, "For launching gantries with open triangulated truss chords, the solidity ratio (phi = A_solid / A_enclosed) is calculated (typically 0.15 to 0.35). For twin girders, a shielding factor (eta = 0.6 to 0.85) is applied to the leeward girder based on frame spacing ratio (S / B).", bold_prefix="Solidity Ratio & Shielding: ")
    add_bullet_p(doc, "Total drag force F_w = C_f * A_e * p_d * G. In-service operational limit: operations halt at V_wind > 10 m/s; out-of-service storm condition: gantry anchored for full extreme gust speed V_gust.", bold_prefix="Wind Drag Calculation: ")
    
    # 4.5 Foundation & Ground Bearing Pressure Design
    add_heading_2(doc, "4.5 Foundation & Ground Bearing Pressure Design for Heavy Staging")
    add_body_p(doc,
        "Ground failure is the single leading cause of falsework collapse worldwide. Staging legs transmit concentrated point loads (typically 30 kN to 250 kN per leg in heavy towers) to the subgrade. Engineered spreader foundations are non-negotiable."
    )
    add_bullet_p(doc, "Every staging footprint must undergo plate load testing (IS 1888) or dynamic cone penetrometer testing. Compaction must achieve >= 95% Modified Proctor Density (MDD).", bold_prefix="Subgrade Verification: ")
    add_bullet_p(doc, "Load is assumed to distribute through timber sole plates (minimum 50mm thickness hardwood) or steel sleeper beams at an angle of 30° to 45° to the horizontal. Bearing pressure q = P / A_effective <= Safe Bearing Capacity (SBC).", bold_prefix="Spreader Pad Distribution: ")
    add_bullet_p(doc, "Differential settlement between adjacent staging towers must not exceed 5 mm. Greater differential settlement causes rapid redistribution of load, concentrating up to 180% of design load onto a single prop, triggering domino collapse.", bold_prefix="Differential Settlement Limit: ")
    
    # 4.6 Heavy Rigging & Crane Lift Mechanics
    add_heading_2(doc, "4.6 Heavy Rigging & Crane Lift Mechanics")
    add_body_p(doc,
        "When planning tandem crane lifts or heavy precast segment hoisting, rigging geometry dictates sling tension and stability:"
    )
    add_bullet_p(doc, "T_sling = (W_load * DAF) / (n * sin(theta)). Where theta is the sling angle to the horizontal. At theta = 60°, 1/sin(theta) = 1.15; at theta = 30°, 1/sin(theta) = 2.00 (doubling sling load!). L&T strictly prohibits sling angles below 60° without written approval of the Chief Specialist.", bold_prefix="Sling Angle Multiplier: ")
    add_bullet_p(doc, "A Dynamic Amplification Factor (DAF = 1.15 to 1.30) is applied to account for crane hoisting acceleration, slewing snatch, and wind gust buffeting.", bold_prefix="Dynamic Factor (DAF): ")
    add_bullet_p(doc, "Maximum outrigger ground bearing pressure P_out = (W_crane + W_cwt + W_load) / (2 * A_mat) + M_overturning / Z_mat. Steel-reinforced timber or fabricated steel crane mats must distribute this pressure within permissible soil limits.", bold_prefix="Crane Mat Pressure: ")

    print("Section 4 built successfully.")
