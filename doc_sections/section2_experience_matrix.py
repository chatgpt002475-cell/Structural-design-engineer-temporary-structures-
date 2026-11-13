import docx
from docx.shared import Inches, Pt, RGBColor
from doc_sections.helpers import (
    set_cell_background, set_cell_margins, set_cell_borders, 
    set_table_styling, add_heading_1, add_heading_2, add_heading_3,
    add_heading_4, add_body_p, add_bullet_p, add_callout
)

def build_section2_experience_matrix(doc):
    add_heading_1(doc, "Section 2: Detailed Career Progression & Roles (2 to 12+ Years Experience)")
    
    add_body_p(doc,
        "A Temporary Structural Engineer at Larsen & Toubro operates at the critical intersection of structural theory, heavy mechanical systems, geotechnical engineering, and live construction execution. Progression from 2 to 12+ years represents an evolution from component-level hand calculations and 2D detailing to system-level numerical modeling, mega-project construction method leadership, and executive risk governance.",
        bold_prefix="The Progression Paradigm: "
    )
    
    # Overview Summary Table across Experience Bands
    add_heading_3(doc, "Table 2.1: Career Evolution & Competency Matrix Across Experience Bands")
    exp_summary_table = doc.add_table(rows=5, cols=5)
    headers = ["Experience Band", "Typical L&T Designation", "Primary Technical Scope", "Key Software & Tools", "Leadership & Governance Role"]
    data = [
        ("2 – 4 Years", "Design Engineer / Senior Engineer", "Conventional formwork, wall/column shutters, cup-lock/ring-lock staging towers, pier cap staging, basic shoring.", "AutoCAD, MS Excel (VBA), STAAD.Pro (basic), Mathcad.", "Individual contributor; prepares Cat 1 design calculations & drawings; conducts site pre-pour staging checks."),
        ("5 – 7 Years", "Senior Design Engineer / Assistant Engineering Manager (AEM)", "Segmental launching gantries, balanced cantilever form travelers (FT/CLC), deep excavation strutting/waling, cofferdams, piling jetties.", "STAAD.Pro Advanced, MIDAS Civil, PLAXIS 2D, Tekla Structures, Python.", "Lead structural designer for complex temporary schemes; performs Cat 2 design checks; coordinates cycle time optimization with site."),
        ("8 – 10 Years", "Engineering Manager (EM) / Lead Temporary Works Coordinator (TWC)", "Construction Method Statements (CMS), tandem heavy crane rigging, soil-structure interaction, dynamic wind/seismic staging analysis, pre-bid estimation.", "MIDAS Civil (staged construction), PLAXIS 3D, ANSYS (FEA joints), Synchro 4D BIM, Python API.", "Departmental / Project Lead; manages team of 5–15 engineers; signs off on Cat 2/3 designs; interfaces with Client Proof Consultants and NHAI/DMRC/MAHSR."),
        ("11 – 12+ Years", "Senior Engineering Manager (SEM) / Chief Specialist", "Full-span launching equipment (FSLE 1000T), mega-project temporary works governance, forensic failure investigation, proprietary patent design, L&T SOPs.", "Advanced multi-physics FEA, bespoke automation pipelines, IoT SHM cloud architectures, Executive C-suite tools.", "Apex technical authority; oversees pan-project risk governance; leads catastrophic risk mitigation; acts as expert witness and technical mentor.")
    ]
    for c_idx, h in enumerate(headers):
        exp_summary_table.cell(0, c_idx).paragraphs[0].add_run(h)
    for r_idx, row in enumerate(data):
        for c_idx, val in enumerate(row):
            exp_summary_table.cell(r_idx + 1, c_idx).paragraphs[0].add_run(val)
    set_table_styling(exp_summary_table, col_widths=[1.1, 1.3, 1.8, 1.2, 1.6], header_bg="002D62")
    
    doc.add_paragraph().paragraph_format.space_after = Pt(8)
    
    # =========================================================================
    # BAND 1: 2 to 4 YEARS
    # =========================================================================
    add_heading_2(doc, "2.1 Band 1: 2 to 4 Years Experience – Junior / Senior Temporary Works Design Engineer")
    
    add_body_p(doc,
        "Engineers at this tier operate as core design production engineers. Having consolidated their fundamental structural mechanics from university, they master the practical physics of wet concrete, timber flexure, steel tube buckling, and coupler slip under real site conditions.",
        bold_prefix="Profile & Focus: "
    )
    
    add_heading_3(doc, "2.1.1 Core Responsibilities & Daily Operational Routine")
    add_bullet_p(doc, "Prepares detailed structural design calculations for conventional wall, column, slab, and pier cap formwork and staging schemes in compliance with IS 14687, IS 800, and IRC:87.", bold_prefix="Design Execution: ")
    add_bullet_p(doc, "Develops Good-for-Construction (GFC) temporary works fabrication and erection drawings in AutoCAD, incorporating comprehensive bill of materials (BOM), cutting lists, and tie-rod locations.", bold_prefix="Drafting & Detailing: ")
    add_bullet_p(doc, "Performs daily site staging inspections, verifying jack extensions (< 300mm), cup-lock wedge tightness, diagonal bracing connectivity, base plate bearing, and sole plate packing.", bold_prefix="Site Verification: ")
    add_bullet_p(doc, "Calculates lateral concrete pressure envelopes based on ambient temperature, pour rate, and concrete admixtures (retarders) using CIRIA 108 and DIN 18218 formulations.", bold_prefix="Pressure Modeling: ")
    add_bullet_p(doc, "Maintains the site Temporary Works Register (TWR) for low-to-medium risk schemes (Cat 0 and Cat 1) and assists the TWC during Permit to Load inspections.", bold_prefix="QA/QC & Register: ")
    
    add_heading_3(doc, "2.1.2 Technical Scope & Structural Systems Mastered")
    add_bullet_p(doc, "Plywood sheathing (12mm, 18mm, 21mm film-faced birch/pine), secondary timber/steel runners (H20 timber beams, aluminium extruded joists, ISMC 75/100 steel channels), primary waler channels (back-to-back ISMC 100/125/150).", bold_prefix="Wall & Column Formwork: ")
    add_bullet_p(doc, "High-strength Dywidag tie rods (15mm with 90 kN safe working load, 20mm with 160 kN safe working load), water stops, cast-in tie cones, and anchor plates.", bold_prefix="Tie Systems: ")
    add_bullet_p(doc, "Cup-lock and Ring-lock tubular scaffolding systems (48.3mm OD x 3.2mm wall thickness, yield 235–355 MPa), modular prop towers, heavy-duty shore frames (e.g. Doka Staxo, Peri Up, L&T heavy-duty props).", bold_prefix="Staging & Shoring: ")
    add_bullet_p(doc, "Pier cap staging cradles, steel collar brackets friction-clamped or anchored around circular/rectangular concrete piers to eliminate ground staging.", bold_prefix="Pier Cap Systems: ")
    add_bullet_p(doc, "Basic trench shoring, aluminum trench boxes, sheet piles up to 4m cantilever depth in cohesive/cohesionless soils.", bold_prefix="Excavation Shoring: ")
    
    add_heading_3(doc, "2.1.3 Mathematical Formulations & Daily Calculations Executed")
    add_body_p(doc, "The 2–4 year engineer performs hand calculations and standardized Excel/VBA computations for:")
    add_bullet_p(doc, "Plywood sheathing flexure (sigma = M/Z <= f_b, allowable ~ 12 to 18 MPa), rolling shear stress (tau = 1.5 * V / (b*h) <= f_v, allowable ~ 1.2 to 1.8 MPa), and deflection limit (delta <= L/360 or 2.5 mm).", bold_prefix="1. Sheathing Checks: ")
    add_bullet_p(doc, "Bending moment and shear checks on H20 timber beams (allowable moment M_allow = 5.0 kNm, allowable shear V_allow = 11.0 kN, EI = 450 kNm2) and steel walers (IS 800:2007 working stress / limit state methods).", bold_prefix="2. Runner & Waler Sizing: ")
    add_bullet_p(doc, "Effective length factor (k) determination for cup-lock standards based on ledger spacing (1.0m, 1.5m, 2.0m). Application of Euler-Perry formula to determine safe compressive load (typically derated from 45 kN at 1.0m lift to 22 kN at 2.0m lift).", bold_prefix="3. Prop Buckling & Derating: ")
    add_bullet_p(doc, "Sole plate ground bearing pressure check: q = (P_prop + P_dead) / A_sole_plate <= Safe Bearing Capacity (SBC) of compacted ground (typically 100–150 kPa).", bold_prefix="4. Ground Bearing: ")
    
    add_callout(doc,
        "Critical Site Rule for 2-4 Year Engineers: Base jacks and U-head jacks must never be extended beyond the manufacturer's certified limit (typically 300 mm to 350 mm maximum free spindle length). Excessive spindle extension dramatically increases the unbraced length, triggering eccentric Euler buckling at a fraction of the rated vertical capacity.",
        title="SAFETY TRAP TO PREVENT: JACK SPINDLE OVER-EXTENSION",
        alert_type="warning"
    )
    
    # =========================================================================
    # BAND 2: 5 to 7 YEARS
    # =========================================================================
    add_heading_2(doc, "2.2 Band 2: 5 to 7 Years Experience – Senior Design Engineer / Assistant Engineering Manager (AEM)")
    
    add_body_p(doc,
        "At the 5–7 year stage, the engineer transitions to designing complex, highly mechanized, and safety-critical temporary structures. They operate with high autonomy, leading design packages for viaduct launching schemes, deep excavations, and heavy marine temporary works, while supervising junior engineers.",
        bold_prefix="Profile & Focus: "
    )
    
    add_heading_3(doc, "2.2.1 Core Responsibilities & Technical Leadership")
    add_bullet_p(doc, "Performs full global and local structural design of Segmental Launching Gantries (Overhead and Underhung LGs), Segment Lifters, and Balanced Cantilever Form Travelers (FT / CLC).", bold_prefix="Mechanized Equipment Design: ")
    add_bullet_p(doc, "Designs deep basement and metro station excavation support systems, including Diaphragm Wall (D-wall) multi-level steel strutting, walers, king posts, and rock anchor ties.", bold_prefix="Deep Excavation Engineering: ")
    add_bullet_p(doc, "Conducts independent Category 2 design checks and peer reviews of falsework schemes submitted by project sub-contractors or junior EDRC designers.", bold_prefix="Category 2 Checking: ")
    add_bullet_p(doc, "Optimizes cycle time: redesigns shuttering and prestressing schemes to compress segmental erection cycles from 7 days down to 3–4 days per span, yielding substantial cost savings.", bold_prefix="Value Engineering: ")
    add_bullet_p(doc, "Designs marine temporary works, including temporary steel piling jetties, spud-leg construction barges, steel sheet-pile cofferdams, and underwater tremie concrete sealing plugs.", bold_prefix="Marine Temporary Works: ")
    add_bullet_p(doc, "Coordinates with client proof consultants (DMRC, NHAI, High-Speed Rail NHSRCL) to secure technical approvals and clearances for GFC drawings.", bold_prefix="Client Interfacing: ")
    
    add_heading_3(doc, "2.2.2 Structural Typologies & Advanced Mechanical Systems")
    add_bullet_p(doc, "Twin box or triangular truss steel girders (lengths 40m–60m, capacity 300T–1200T), front launching nose, rear C-frame, main support legs (MSL), intermediate support legs (ISL), and motorized motorized trolley hoists.", bold_prefix="Launching Gantries (LG): ")
    add_bullet_p(doc, "Triangulated top truss or underslung systems with hydraulic advancement cylinders, rear anchor tie bars clamped to cured cantilever box girder decks, and hydraulic hanging rods for bottom slab and web shutters.", bold_prefix="Form Travelers (CLC / FT): ")
    add_bullet_p(doc, "Heavy steel waler beams (built-up plate girders or twin ISMB 600 with cover plates), pipe struts (610mm to 1016mm dia, 12mm–20mm wall thickness), preloading hydraulic jacks (1000–3000 kN capacity) to minimize wall deflection.", bold_prefix="Deep Excavation Strutting: ")
    add_bullet_p(doc, "Driving and extraction templates, tubular steel piles (600mm–1200mm dia), steel crossheads, longitudinal stringers, timber/steel running decks designed for 100T crawler cranes and transit mixers.", bold_prefix="Marine Piling Jetties: ")
    
    add_heading_3(doc, "2.2.3 Advanced Structural Mechanics & Calculations Handled")
    add_bullet_p(doc, "Second-order geometric non-linearity (P-Delta effects) on slender gantry legs and tall heavy-duty staging towers under combined vertical thrust and longitudinal traction/braking forces.", bold_prefix="P-Delta & Non-linear Analysis: ")
    add_bullet_p(doc, "Web crippling, flange bucking, and lateral torsional buckling (LTB) of launching girder chords under moving point loads exerted by segment hoist wheel bogeys.", bold_prefix="Plate Buckling & Stability: ")
    add_bullet_p(doc, "Kinematics and stability calculations during gantry longitudinal launching (stepping): cantilever nose deflection limits (delta_max <= L_nose / 400), counterweight requirements, overturning factor of safety (FOS >= 1.50 under dead + launching wind).", bold_prefix="Launching Kinematics: ")
    add_bullet_p(doc, "Friction and sliding interfaces: PTFE (Teflon) sliding on mirror-polished stainless steel sheets (friction coefficient mu = 0.03 to 0.08), multi-roller tank skates, hydraulic push-pull cylinder stroke force sizing.", bold_prefix="Friction & Hydraulics: ")
    
    add_callout(doc,
        "Critical Engineering Directive for 5-7 Year Engineers: During gantry launching / stepping, wind speeds must be continuously monitored via calibrated anemometers mounted on the gantry nose and rear tail. If 3-second gust wind speed exceeds 10 m/s (36 km/h), launching operations must be immediately suspended and the gantry tied down. Full mechanical tie-down clamps to pier caps are mandatory for out-of-service storm winds (up to 45–50 m/s).",
        title="GANTRY ADVANCE & LAUNCHING WIND PROTOCOL",
        alert_type="danger"
    )
    
    # =========================================================================
    # BAND 3: 8 to 10 YEARS
    # =========================================================================
    add_heading_2(doc, "2.3 Band 3: 8 to 10 Years Experience – Engineering Manager (EM) / Lead Temporary Works Coordinator")
    
    add_body_p(doc,
        "An Engineering Manager (8–10 years) operates as the technical authority and strategic coordinator for temporary works across multi-billion-rupee packages. They bridge the gap between structural concept, detailed numerical simulation, heavy rigging safety, and commercial pre-bid competitiveness.",
        bold_prefix="Profile & Focus: "
    )
    
    add_heading_3(doc, "2.3.1 Core Responsibilities & Strategic Delivery")
    add_bullet_p(doc, "Authors comprehensive Construction Method Statements (CMS), Erection Schemes, and Temporary Works Design Briefs for mega-infrastructure contracts.", bold_prefix="Erection Scheme Authoring: ")
    add_bullet_p(doc, "Engineers complex tandem heavy crane lifts (e.g. 250T–600T crawler/all-terrain cranes lifting precast portal beams or steel truss spans over active railways or highways).", bold_prefix="Tandem Rigging Engineering: ")
    add_bullet_p(doc, "Leads stage-by-stage construction sequential analysis in MIDAS Civil and soil-structure interaction (SSI) modeling in PLAXIS 3D, accounting for creep, shrinkage, and locked-in construction stresses.", bold_prefix="Advanced Stage Analysis: ")
    add_bullet_p(doc, "Serves as the Project Temporary Works Coordinator (TWC), establishing the project-wide Temporary Works Register (TWR), delegating check categories, and chairing PTL approval committees.", bold_prefix="TWC Governance: ")
    add_bullet_p(doc, "Interfaces between Permanent Works Designers, Proof Consultants, and Client Authorities (e.g. NHSRCL Bullet Train, DMRC, MMRDA, Indian Railways CRS) to align camber curves, reactions, and bearing settlements.", bold_prefix="Interface Management: ")
    add_bullet_p(doc, "Develops pre-bid temporary works cost estimates: formwork repetition cycles, specialized launching equipment capex/amortization, and temporary steel tonnage optimization.", bold_prefix="Commercial & Tendering: ")
    add_bullet_p(doc, "Conducts Failure Mode and Effect Analysis (FMEA) and structural risk assessments on all critical erection stages.", bold_prefix="Risk Management & FMEA: ")
    
    add_heading_3(doc, "2.3.2 Deep Technical Engineering Domains")
    add_bullet_p(doc, "Rigging geometry, sling tension vectors, dynamic amplification factors (DAF = 1.15 to 1.30), center-of-gravity (CG) envelope shift, outrigger mat pressure distributions, and crane capacity derating (maximum 75%–80% of rated load chart for tandem lifts).", bold_prefix="Heavy Rigging & Lift Engineering: ")
    add_bullet_p(doc, "Wind buffeting and aerodynamic drag on long cantilever spans during form traveler casting; vortex-induced vibration (VIV) checks on slender temporary staging towers > 30m height; seismic load combination during temporary stage.", bold_prefix="Dynamic Wind & Seismic: ")
    add_bullet_p(doc, "3D finite element stress concentration analysis using ANSYS on critical gantry pins, trunnion brackets, cast-steel launching saddles, and strand jack anchor plates.", bold_prefix="Local FEA & Connection Detailing: ")
    add_bullet_p(doc, "Predicting long-term time-dependent deflection, tendon prestress friction and wobble losses, and calculating target theoretical pre-camber profiles for form travelers so that final deck matches design profile within +/- 5 mm.", bold_prefix="Pre-camber & Deflection Alignment: ")
    
    add_callout(doc,
        "Critical Rigging Mandate: In any dual-crane (tandem) lift, a formal Lift Plan must be authored, simulated, and stamped by an 8-10+ Year Engineering Manager. The plan must incorporate: (1) Sling angle factor = 1 / sin(theta), ensuring theta >= 60 deg, (2) Crane capacity utilization capped at 75%, (3) Mat bearing pressure verified against tested ground CBR/SBC, (4) Continuous radio-frequency communication and synchronized slewing/hoisting.",
        title="MANDATORY TANDEM LIFTING PROTOCOL",
        alert_type="warning"
    )
    
    # =========================================================================
    # BAND 4: 11 to 12+ YEARS
    # =========================================================================
    add_heading_2(doc, "2.4 Band 4: 11 to 12+ Years Experience – Senior Engineering Manager (SEM) / Chief Specialist")
    
    add_body_p(doc,
        "With 11 to 12+ years of specialized experience, the Senior Engineering Manager / Chief Specialist is an executive technical authority across L&T Construction. This leader steers mega-project engineering policies, spearheads heavy mechanization innovations, resolves forensic structural disputes, and mentors the organization's next generation of structural leaders.",
        bold_prefix="Profile & Focus: "
    )
    
    add_heading_3(doc, "2.4.1 Executive Responsibilities & Mega-Project Leadership")
    add_bullet_p(doc, "Directs the temporary works strategy for national landmark mega-projects (e.g. Mumbai Trans Harbour Link MTHL Atal Setu, Ahmedabad-Mumbai High Speed Rail MAHSR, Chenab Arch Bridge, Underground Metro Networks).", bold_prefix="Mega-Project Direction: ")
    add_bullet_p(doc, "Pioneers custom heavy mechanization systems: such as the 1000-Ton Full Span Launching Equipment (FSLE)—comprising 1000T Straddle Carriers, 1000T Transporters, and 1000T Launchers for 40-meter full span precast box girders.", bold_prefix="Heavy Mechanization Innovation: ")
    add_bullet_p(doc, "Authors and standardizes L&T Corporate Technical Manuals, Standard Operating Procedures (SOPs), and Temporary Works Quality Directives enforced across all construction sites.", bold_prefix="Institutional Governance: ")
    add_bullet_p(doc, "Leads forensic investigations into structural near-misses, deformations, or collapses across industry projects; determines root causes and implements pan-company safety lockdowns and design modifications.", bold_prefix="Forensic Engineering & Disaster Prevention: ")
    add_bullet_p(doc, "Patents innovative erection methods, modular high-capacity falsework systems, and automated climbing formwork mechanisms to expand L&T's intellectual property and competitive edge.", bold_prefix="Patenting & Innovation: ")
    add_bullet_p(doc, "Drives decarbonization in temporary works: spearheading circular economy steel reutilization, high-strength low-carbon alloys, and lightweight modular aluminum shuttering systems.", bold_prefix="Sustainability & Decarbonization: ")
    add_bullet_p(doc, "Mentors, coaches, and structures competency development roadmaps for over 50+ junior, mid-level, and senior temporary works design engineers across EDRC and site cells.", bold_prefix="Talent Incubation: ")
    
    add_callout(doc,
        "Chief Specialist Creed: 'True engineering excellence in temporary works is measured not only by what we construct, but by the structural failures that never occurred. Our role is to foresee every conceivable mode of instability, material fatigue, hydraulic imbalance, and human error long before steel is hoisted at site.'",
        title="EXECUTIVE LEADERSHIP CREED",
        alert_type="info"
    )

    print("Section 2 built successfully.")
