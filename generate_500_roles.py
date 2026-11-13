"""
Generator script to compile all 500 Granular Roles & Responsibilities for a
12-Year Experienced Senior Engineering Manager / Chief Specialist in Temporary Structures at L&T.
"""
import json
import os

PILLARS = [
    ("Pillar 01", "Strategic Leadership, Mega-Project Governance & Policy", 1, 50),
    ("Pillar 02", "Construction Method Statements (CMS) & Erection Schemes", 51, 100),
    ("Pillar 03", "Heavy Mechanization, FSLE & Launching Gantry Engineering", 101, 150),
    ("Pillar 04", "Deep Excavation, Geotechnical & Marine Temporary Works", 151, 200),
    ("Pillar 05", "Advanced Structural Mechanics, Non-linear FEA & Dynamics", 201, 250),
    ("Pillar 06", "Digital Engineering, BIM 4D, Computational Automation & IoT SHM", 251, 300),
    ("Pillar 07", "BS 5975, Cat 0-3 Checks, Safety Directives & Quality Assurance", 301, 350),
    ("Pillar 08", "Forensic Engineering, Catastrophic Failure Prevention & Risk", 351, 400),
    ("Pillar 09", "Client, Proof Consultant & Statutory Regulatory Interfacing", 401, 450),
    ("Pillar 10", "Commercial, Pre-Bid Estimation, Patenting & Mentorship", 451, 500)
]

def generate_500_roles():
    roles = []
    
    # -------------------------------------------------------------------------
    # PILLAR 1: STRATEGIC LEADERSHIP, MEGA-PROJECT GOVERNANCE & POLICY (1-50)
    # -------------------------------------------------------------------------
    p1_items = [
        ("Apex Temporary Works Governance Authority", 
         "Serves as the apex technical authority across L&T Construction ICs (Heavy Civil, TI, B&F), establishing mandatory structural policies, safety charters, and design standards.",
         "EDRC & Corporate Safety Board", "BS 5975:2019, L&T EHS Policy", "Corporate TW Governance Manual", "Strategic"),
        ("Chairing Corporate Temporary Works Safety Committee",
         "Chairs quarterly executive safety reviews to audit project-level compliance with BS 5975 and evaluate risk exposure across multi-billion-rupee packages.",
         "Corporate EHS & Project Directors", "ISO 45001, BS 5975", "Executive TW Safety Audit Minutes", "Strategic"),
        ("Chartering Temporary Works Management Systems (TWMS)",
         "Formulates and enforces the enterprise-wide TWMS protocol defining mandatory steps from design brief initiation to final striking across all project sites.",
         "EDRC & Site TW Cells", "PAS 8811, BS 5975", "L&T Standard TWMS Procedure", "Strategic"),
        ("Appointment & Certification of Project TWCs",
         "Interviews, assesses, and formally certifies Project Temporary Works Coordinators (TWCs), ensuring only verified, qualified engineers hold statutory signing authority.",
         "Talent Development & EDRC", "L&T Competency Framework", "Certified TWC Register & Authority Letters", "Strategic"),
        ("Mega-Project Readiness Clearance Audit",
         "Conducts mandatory technical readiness reviews before initiating first-of-its-kind structural operations (e.g. launching 1000T girders or deep station excavation).",
         "Project Sites (MAHSR, MTHL, Metros)", "IRC:87, BS 5975", "Stage 0 Readiness Clearance Certificate", "Critical"),
        ("Pan-India Temporary Steel Asset Management Strategy",
         "Governs the procurement, redistribution, recertification, and scrap life-cycle of over 100,000 MT of modular temporary steel framing across national projects.",
         "Supply Chain & Plant & Machinery (P&M)", "IS 800, IS 2062", "Strategic Steel Inventory Lifecycle Plan", "Strategic"),
        ("Establishing Category 3 Proof-Checking Mandates",
         "Formulates criteria identifying structures requiring mandatory third-party independent verification by accredited international proof checking consultants.",
         "EDRC & Client Engineering Teams", "FIDIC, BS 5975 Cat 3", "Category 3 Scope & Appointment Protocol", "Critical"),
        ("Zero-Tolerance Safety Protocol Enforcement",
         "Enforces corporate Stop-Work Authority across all projects for any observed deviation from approved Good-for-Construction (GFC) temporary works drawings.",
         "All Construction Sites", "L&T Zero Harm Directive", "Stop-Work Notice & Rectification Directive", "Critical"),
        ("Modularization & Standardization Strategy",
         "Leads R&D initiatives to standardize modular pier-cap brackets, cantilever deck overhang travelers, and column collars, reducing custom fabrication by 40%.",
         "FED & EDRC", "IS 14687, EN 12812", "Standard Modular Shuttering Manual", "High"),
        ("Cross-IC Technical Alignment (HCI, TI, B&F, Hydro)",
         "Facilitates inter-divisional knowledge sharing, transferring heavy civil bridge launching methodologies into building transfers and industrial steel erection.",
         "Inter-IC Technical Council", "L&T Engineering Standards", "Cross-IC Temporary Works Bulletin", "High"),
        ("Establishing Dynamic Wind & Cyclone Protocols",
         "Defines localized extreme-weather shut-down, tie-down, and mechanical locking protocols for tall staging and tower cranes in coastal cyclonic zones.",
         "Coastal Projects (MTHL, Chennai Metro)", "IS 875 Part 3, IRC:6", "Cyclone Emergency Tie-Down Procedure", "Critical"),
        ("Reviewing Pre-Monsoon Staging Integrity Audits",
         "Directs mandatory pre-monsoon audits of all ground-supported falsework, inspecting drainage swales, scour protection, and sole-plate mud pumping.",
         "All River & Highway Bridge Sites", "IRC:87 Clause 7", "Pre-Monsoon Staging Integrity Report", "Critical"),
        ("Managing Specialized Hydraulic Asset Fleet",
         "Oversees the technical health, calibration logs, seal replacements, and certified inspections of over 500 heavy strand jacks, climbing cylinders, and power packs.",
         "SE&HLD (Special Equipment)", "ISO 10100, DIN 19704", "Hydraulic Fleet Health Certification Log", "Strategic"),
        ("Establishing Formwork Striking Strength Directives",
         "Authorizes project-specific striking strength thresholds based on maturity meters and companion field cube testing rather than arbitrary elapsed time.",
         "Concrete Technology Lab & Site QC", "IS 456, ACI 347R", "Striking Strength Approval Directive", "High"),
        ("Overseeing Pan-L&T Formwork Safety Campaigns",
         "Designs annual corporate safety training modules focusing on scaffolding stability, tie-rod torque verification, and falsework collapse prevention.",
         "Corporate HR & Safety", "L&T Institute of Project Management", "Annual Falsework Training Curriculum", "Strategic"),
        ("Resolving Interface Conflicts with Permanent Designers",
         "Arbitrates high-stakes technical disputes between permanent design consultants and site construction teams regarding construction loads and locked-in stresses.",
         "EDRC, Client, Proof Consultants", "IRC:112, Eurocodes", "Technical Dispute Resolution Memo", "Critical"),
        ("Benchmarking International Standards Adoption",
         "Evaluates EN 12812, DIN 18218, and ACI 347R against Indian Standards (IS 14687 / IRC:87), updating L&T design guidelines to exceed global best practices.",
         "EDRC Code Committee", "BSI, BIS, ACI, DIN", "International Standard Alignment Paper", "High"),
        ("Reviewing Critical Heavy Lift Plans (> 200T)",
         "Mandatory corporate signatory on all complex tandem and super-heavy lift engineering plans involving crawler cranes > 500T capacity.",
         "CMPD & Rigging Teams", "BS 7121, OSHA 1926", "Approved Heavy Lift Execution Plan", "Critical"),
        ("Establishing Staging Foundation Verification Guidelines",
         "Mandates plate load testing (PLT) frequencies, Modulus of Subgrade Reaction (ks) validation, and soil cement stabilization criteria under staging beds.",
         "Geotechnical Cell & Sites", "IS 1888, IRC:87", "Staging Bed Preparation & Testing SOP", "Critical"),
        ("Corporate Decarbonization in Temporary Works",
         "Directs life-cycle carbon footprint assessments for temporary works, spearheading high-reusability aluminum formwork and circular steel reuse.",
         "Sustainability Cell", "ISO 14040, GHG Protocol", "Temporary Works Decarbonization Roadmap", "Strategic"),
        ("Formulating Technical Risk Matrices for Tender Bids",
         "Authors the temporary works risk evaluation matrix for multi-thousand crore mega-tenders, highlighting constructability bottlenecks and cost risks.",
         "Pre-Bid Engineering / Tendering", "L&T Tendering Policy", "Pre-Bid Temporary Works Risk Matrix", "Strategic"),
        ("Auditing Site Temporary Works Registers (TWR)",
         "Conducts surprise quality audits of project TWR registers to ensure no unapproved Cat 1, 2, or 3 temporary works are erected or loaded without permits.",
         "Project Sites", "BS 5975:2019", "TWR Quality Audit Scorecard", "Critical"),
        ("Directing Proprietary Mechanism Patenting",
         "Identifies novel site-engineered launching mechanisms, travelers, and slipforms, driving patent applications to safeguard L&T intellectual property.",
         "IPR Cell & Legal", "Indian Patent Act, WIPO", "Patenting Invention Disclosure Form", "Strategic"),
        ("Crisis Management & Emergency Response Command",
         "Serves as chief structural commander during unforeseen site emergencies (e.g., severe barge impact, staging distress, or hydraulic failure).",
         "Crisis Command Cell", "L&T Disaster Protocol", "Emergency Stabilisation Action Plan", "Critical"),
        ("Establishing Vibration & Dynamic Monitoring Limits",
         "Defines vibration velocity thresholds (PPV mm/s) on temporary staging adjacent to active railway tracks and highway corridors.",
         "Rail & Highway Projects", "DIN 4150-3, BS 7385", "Dynamic Vibration Monitoring Guideline", "High"),
        ("Standardizing High-Strength Tie-Rod Engineering",
         "Authors engineering design tables and proof-test protocols for Dywidag 15mm, 20mm, 26mm, and 32mm high-strength tie-rod assemblies.",
         "FED & EDRC", "DIN 488, IS 2090", "High-Strength Tie Rod Design Manual", "High"),
        ("Governing Sub-Contractor Engineering Prequalification",
         "Establishes prequalification criteria for specialized temporary steel fabricators, gantry erection agencies, and heavy rigging subcontractors.",
         "Procurement & Quality", "ISO 9001, L&T Vendor SOP", "Vendor Prequalification Evaluation Log", "High"),
        ("Reviewing Value Engineering Proposals",
         "Critiques and sanctions value engineering proposals submitted by project sites, ensuring cycle time reductions do not compromise safety margins.",
         "EDRC & CMPD", "Society of Value Engineers", "Value Engineering Sanction Memo", "Strategic"),
        ("Establishing Camber Tracking Governance",
         "Mandates pre-camber tracking protocols for balanced cantilever bridges, requiring daily closure alignment checks and temperature compensation.",
         "Special Bridges Projects", "IRC:112, FIB Model Code", "Camber Tracking Governance Directive", "Critical"),
        ("Authoring Forensic Investigation Mandates",
         "Formulates standardized operating procedures for independent forensic investigation teams in the event of structural distress or failure.",
         "Corporate Quality & Legal", "ASCE Forensic Guidelines", "Forensic Investigation Protocol", "Critical"),
        ("Corporate Interface with Technical Universities",
         "Partners with premier institutes (IIT Madras, IIT Bombay) to conduct experimental research on concrete formwork pressure and gantry joint fatigue.",
         "R&D & Academic Cell", "Academic Collaboration Charter", "Joint R&D Research Reports", "Strategic"),
        ("Overseeing Crane Mat Certification Protocols",
         "Establishes structural design verification and mandatory inspection criteria for hardwood timber and fabricated steel crane outrigger mats.",
         "P&M & Safety Cell", "CIRIA C703", "Crane Mat Certification Protocol", "Critical"),
        ("Formulating Safe Jacking & De-centering SOPs",
         "Authors standard operating procedures for the synchronous lowering of mega-staging towers using manifold hydraulic jacks and sand-boxes.",
         "EDRC & CMPD", "DIN 19704, BS 5975", "Synchronous Lowering SOP", "Critical"),
        ("Auditing Cat 2 Design Check Calculations",
         "Reviews sample calculations performed by Assistant Engineering Managers to ensure rigorous compliance with limit state buckling and shear criteria.",
         "EDRC Design Quality", "IS 800:2007", "Cat 2 Quality Audit Assessment", "High"),
        ("Reviewing Marine Temporary Works Safety Charters",
         "Directs maritime temporary works safety policies, including tugboat bollard pull verification, spud barge stability, and tidal current drag calculations.",
         "MTHL & Coastal Port Projects", "DNVGL-ST-N001", "Marine Temporary Works Safety Charter", "Critical"),
        ("Establishing Ultrasonic Bolt Tightening Standards",
         "Enforces ultrasonic elongation measurement and torque-tension calibration for M24, M30, and M36 Grade 8.8 / 10.9 friction-grip gantry bolts.",
         "SE&HLD & Erection Teams", "IS 4000, EN 1090-2", "HSFG Bolt Tightening Protocol", "High"),
        ("Governing Gantry Load Testing Protocols",
         "Authors 125% static and 110% dynamic overload proof-testing procedures for all launching gantries prior to client commissioning.",
         "SE&HLD, Proof Consultant", "BS 7121, IS 13367", "Gantry Commissioning Proof Test Protocol", "Critical"),
        ("Formulating Automated Concrete Pour Rate Limits",
         "Establishes maximum vertical pour rate limits ($R$ m/hr) as a function of temperature and admixtures, preventing formwork hydraulic bursting.",
         "Sites & Quality Team", "CIRIA 108, DIN 18218", "Concrete Pour Rate Compliance Chart", "Critical"),
        ("Directing Temporary Steel Anti-Corrosion Protocols",
         "Establishes inspection, ultrasonic thickness gauging, and recoating intervals for temporary steel members subjected to aggressive marine environments.",
         "Quality & Materials", "ISO 12944", "Steel Asset Anti-Corrosion Standard", "High"),
        ("Mentoring Executive Engineering Leadership",
         "Conducts bi-weekly coaching sessions for Senior Engineering Managers and Chief Specialists, fostering strategic thinking and crisis leadership.",
         "L&T Leadership Academy", "Executive Coaching Framework", "Leadership Mentorship Progress Log", "Strategic"),
        ("Establishing Digital Twin Integration Framework",
         "Pioneers the deployment of cloud-connected digital twins that simulate launching gantry stresses, ambient wind, and deck deflections in real time.",
         "Digital Engineering Cell", "ISO 19650, Industry 4.0", "Digital Twin Strategic Architecture", "Strategic"),
        ("Authoring Falsework Decentering Sequence Directives",
         "Defines mandatory structural release sequences (e.g. mid-span to support) to prevent reverse moment stresses and crushing in young concrete.",
         "EDRC Structural Cell", "IRC:87, IS 456", "Decentering Sequence Directive", "Critical"),
        ("Reviewing Tower Crane Foundation Designs",
         "Inspects and approves customized foundation designs for high-capacity tower cranes anchored into deep basements or bridge pylons.",
         "CMPD & B&F IC", "BS 7121-2, IS 800", "Tower Crane Anchor Approval Certificate", "Critical"),
        ("Establishing Underground Shaft Bulkhead Policies",
         "Directs the structural criteria for temporary thrust walls and bulkheads resisting Tunnel Boring Machine (TBM) breakout hydraulic loads.",
         "Hydro & Tunneling IC", "BS EN 1997, CIRIA C760", "TBM Thrust Wall Design Standard", "Critical"),
        ("Governing Cantilever Pier-Bracket Friction Clamps",
         "Establishes post-tensioning torque, high-tensile bar elongation, and friction coefficient verification protocols for heavy pier bracket collars.",
         "Special Bridges & Metros", "AASHTO, IRC:87", "Friction Bracket Verification Manual", "Critical"),
        ("Establishing AI Computer Vision Inspection Standards",
         "Sets algorithmic accuracy and false-positive thresholds for drone-based automated scaffolding inspection systems.",
         "Digital Innovation Lab", "AI Inspection Standards", "Vision System Certification Protocol", "High"),
        ("Reviewing Heavy Strut Preloading Sequences",
         "Validates sequential hydraulic preloading steps on multi-tier station box struts to prevent adjacent strut load shedding and ground cave-in.",
         "Metro Underground Units", "CIRIA C760", "Multi-Tier Strut Preloading Manual", "Critical"),
        ("Authoring Annual Temporary Works Innovation Awards",
         "Chairs the jury for the annual corporate engineering innovation award, celebrating groundbreaking construction methods and safety breakthroughs.",
         "Corporate Technology Council", "L&T Innovation Portal", "Annual Innovation Selection Dossier", "Strategic"),
        ("Formulating Emergency Gantry Tie-Down Checklists",
         "Drafts rapid 15-minute emergency tie-down checklists executed by site crews upon sudden cyclonic squall or gale warnings.",
         "Site Erection Units", "L&T EHS SOP", "15-Minute Emergency Tie-Down Form", "Critical"),
        ("Corporate Custodian of Structural Engineering Integrity",
         "Serves as the organizational conscience, championing uncompromising structural rigor and refusing commercial shortcuts that compromise safety.",
         "Executive Boardroom & Sites", "Engineers Code of Ethics", "Annual Engineering Integrity Declaration", "Strategic")
    ]
    
    for idx, item in enumerate(p1_items, 1):
        roles.append({
            "id": idx, "pillar_id": 1, "pillar_name": PILLARS[0][1],
            "title": item[0], "description": item[1],
            "operational_context": item[2], "codes_and_tools": item[3],
            "deliverable": item[4], "risk_level": item[5]
        })

    # -------------------------------------------------------------------------
    # PILLAR 2: CONSTRUCTION METHOD STATEMENTS (CMS) & ERECTION SCHEMES (51-100)
    # -------------------------------------------------------------------------
    p2_templates = [
        "Authors comprehensive Construction Method Statements (CMS) for {mech} on {proj}.",
        "Validates step-by-step erection sequence drawings, identifying {risk} during {stage}.",
        "Calculates stability factors of safety (FOS >= 1.50) against overturning under {load}.",
        "Establishes load-sharing ratios and kinematic paths for {equip} navigating {env}.",
        "Authors emergency contingency schemes and retrieval protocols for {system} failure."
    ]
    
    cms_topics = [
        ("Balanced Cantilever Pier-Table Casting", "heavy timber/steel cradles anchored to pier heads", "asymmetric concrete dumping forces", "pier table construction", "IRC:87, IS 456"),
        ("Full-Span Precast Box Girder Launching (40m / 1000T)", "1000T multi-axle transporter and overhead launcher", "longitudinal grade brake slippage", "viaduct erection", "MAHSR High Speed Rail Specs"),
        ("Incremental Launching Method (ILM) of Continuous Steel Girders", "hydraulic push-pull jacks and launch nose", "web buckling over launch bearings", "river valley crossing", "IRC:24, Eurocode 3"),
        ("Cable-Stayed Bridge Pylon Slipforming", "self-climbing hydraulic formwork towers", "wind buffeting at 180m elevation", "tower construction", "DIN 18218, EN 12812"),
        ("Underground Metro Station Top-Down Slabs", "temporary plunge columns and king posts", "soil heave and slab punch-through", "deep excavation", "CIRIA C760, IS 456"),
        ("Heavy Steel Arch Erection via Cable Stay Temporary Towers", "tieback cables, mast towers and strand jacks", "geometric non-linearity under wind", "gorge crossing", "IRC:112, MIDAS Civil"),
        ("Segmental Span-by-Span Erection using Underslung Gantry", "underslung twin truss gantry with C-hooks", "epoxy dry-joint squeezing asymmetry", "urban metro viaduct", "BS 5975, IRC:87"),
        ("Precast Concrete Portal Beam Erection over Live Rail Tracks", "dual 350T crawler cranes in railway mega-block", "crane slew swing radius pinch points", "railway crossing", "IRS Bridge Rules, BS 7121"),
        ("Marine Cofferdam Construction in High Tidal Range (6m)", "interlocking Larssen sheet piles and bracing frames", "piping failure and water boil", "sea inlet foundation", "CIRIA C760, BS EN 1997"),
        ("Nuclear Reactor Dome Ring Liner Heavy Rigging", "1200T heavy lift crane with spreader ring", "dynamic wind gust load magnification", "containment building", "AERB Safety Standards, ASME")
    ]
    
    count = 51
    for title_base, mech, risk, stage, codes in cms_topics:
        roles.append({
            "id": count, "pillar_id": 2, "pillar_name": PILLARS[1][1],
            "title": f"CMS Authoring: {title_base}",
            "description": f"Authors comprehensive, legally binding Construction Method Statements (CMS) defining the structural concept, crane positions, rigging geometry, temporary support reactions, and step-by-step risk mitigation protocols for {mech}.",
            "operational_context": "CMPD / EDRC Major Projects", "codes_and_tools": f"{codes}, AutoCAD, Primavera P6",
            "deliverable": f"Good-For-Construction CMS Report: {title_base}", "risk_level": "Critical"
        })
        count += 1
        roles.append({
            "id": count, "pillar_id": 2, "pillar_name": PILLARS[1][1],
            "title": f"Structural Kinematic Simulation: {title_base}",
            "description": f"Performs multi-step structural kinematic and stability simulations in MIDAS Civil / STAAD Pro, evaluating locked-in reactions, pier torsion, and deflections during {stage}.",
            "operational_context": "EDRC Bridge Engineering", "codes_and_tools": "MIDAS Civil, Python API",
            "deliverable": f"Kinematic Staging Calculation Report: {title_base}", "risk_level": "Critical"
        })
        count += 1
        roles.append({
            "id": count, "pillar_id": 2, "pillar_name": PILLARS[1][1],
            "title": f"Overturning & Aerodynamic Stability Verification: {title_base}",
            "description": f"Evaluates global stability against overturning (FOS >= 1.50) and aerodynamic uplift under {risk}, establishing ballast weights and mechanical hold-down clamp capacities.",
            "operational_context": "CMPD / Site Engineering", "codes_and_tools": "IS 875 Pt 3, BS 5975",
            "deliverable": f"Overturning Stability Check Dossier: {title_base}", "risk_level": "Critical"
        })
        count += 1
        roles.append({
            "id": count, "pillar_id": 2, "pillar_name": PILLARS[1][1],
            "title": f"Permit-to-Work Contingency Architecture: {title_base}",
            "description": f"Formulates contingency rescue, hydraulic bypass, and immediate lock-down protocols for unexpected plant stall or severe squall during {stage}.",
            "operational_context": "Site TW Cell & Safety", "codes_and_tools": "L&T Emergency Protocol",
            "deliverable": f"Emergency Contingency & Abort Plan: {title_base}", "risk_level": "High"
        })
        count += 1
        roles.append({
            "id": count, "pillar_id": 2, "pillar_name": PILLARS[1][1],
            "title": f"Client & Proof Consultant Technical Defense: {title_base}",
            "description": f"Presents, defends, and secures formal approval from client authorities and third-party proof consultants for the complete CMS package of {title_base}.",
            "operational_context": "Executive Client Interface", "codes_and_tools": "FIDIC, Contract Specs",
            "deliverable": f"Signed & Approved Client CMS Clearance: {title_base}", "risk_level": "Strategic"
        })
        count += 1

    # -------------------------------------------------------------------------
    # PILLAR 3: HEAVY MECHANIZATION, FSLE & LAUNCHING GANTRY ENGINEERING (101-150)
    # -------------------------------------------------------------------------
    p3_specs = [
        "Full Span Launching Equipment (FSLE 1000T Launcher) structural design",
        "1000T Multi-Axle Girder Transporter wheel-load bridge deck verification",
        "1000T Casting Yard Straddle Carrier gantry frame and runway rail design",
        "Overhead Segmental Launching Gantry (LG 1200T) twin triangular truss design",
        "Underslung Launching Gantry with sliding C-hooks for tight metro curves",
        "Form Traveler (FT / CLC) 250T balanced cantilever segmental casting rig",
        "Precast Segment Lifter with cantilever beam and rear tie-down Dywidag bars",
        "Heavy Portal Gantry Crane (100T-200T) runway beam and storm rail clamp design",
        "Hydraulic Strand Jack Erection Tower with synchronized 4x350T jacks",
        "Derrick Crane (80T) anchored to bridge pylon for steel truss erection"
    ]
    p3_subtasks = [
        ("Truss Chord & Web Member Limit State Design", "IS 800:2007, EN 1993-1-1", "Sizing high-strength steel hollow/box sections under combined axial thrust and local bending moments."),
        ("Launching Nose Cantilever Deflection & Camber Optimization", "IRC:87, Euler-Bernoulli Elastic Theory", "Calculating tip deflection (L/400 limit) and sizing upward launch nose camber jacks."),
        ("Pin-Hole Bearing Stress & Cast-Steel Shoe FEA Modeling", "ANSYS Workbench, Hertzian Contact Theory", "Analyzing peak von Mises stresses and triaxial stress concentrations at pin trunnions."),
        ("Hydraulic Synchronous Advancement & Rail Friction Analysis", "DIN 19704, Teflon-SS Friction Physics", "Computing jacking stroke thrust, stick-slip friction spikes, and cylinder buckling capacity."),
        ("Out-of-Service Storm Wind Tie-Down & Ballast Engineering", "IS 875 Pt 3, BS 5975", "Designing mechanical claw clamps, tie-back tendons, and counterweights for 50 m/s storm gusts.")
    ]
    
    count = 101
    for spec in p3_specs:
        for sub_title, codes, desc in p3_subtasks:
            roles.append({
                "id": count, "pillar_id": 3, "pillar_name": PILLARS[2][1],
                "title": f"{spec}: {sub_title}",
                "description": f"{desc} Applied to {spec} across mega-infrastructure packages.",
                "operational_context": "SE&HLD / EDRC Special Equipment", "codes_and_tools": codes,
                "deliverable": f"Structural Calculation & Drawing Dossier: {spec} - {sub_title}", "risk_level": "Critical"
            })
            count += 1

    # -------------------------------------------------------------------------
    # PILLAR 4: DEEP EXCAVATION, GEOTECHNICAL & MARINE TEMPORARY WORKS (151-200)
    # -------------------------------------------------------------------------
    p4_specs = [
        "Diaphragm Wall (D-Wall) 1200mm thick multi-tier steel strutting system",
        "Circular Underground Station Shaft ring-beam compression strutting",
        "Ground Anchor Tieback system in weathered basalt / marine clay",
        "Steel Sheet Pile (Larssen 600) Cofferdam for deep river pier well",
        "Underwater Concrete Tremie Sealing Plug against hydrostatic blow-up",
        "Temporary Marine Piling Access Jetty (5.5km) in intertidal mudflats",
        "Spud-Leg Construction Barge mooring and hydrodynamic wave-current analysis",
        "Reverse Circulation Drilling (RCD) Heavy Steel Work Platform",
        "Soldier Piles with Timber Lagging and Steel Walers for urban utilities",
        "Heavy Pile Load Test (PLT 3000T) Reaction Frame and Kentledge Stacking"
    ]
    p4_subtasks = [
        ("Soil-Structure Interaction (SSI) Non-Linear Modeling", "PLAXIS 2D/3D, Mohr-Coulomb/Hardening Soil", "Simulating staged excavation, pore water dissipation, wall deflections and ground surface settlement."),
        ("Waler Beam & Heavy Pipe Strut Structural Sizing", "IS 800:2007, CIRIA C760", "Designing twin built-up plate walers and 813mm-1016mm dia pipe struts with web stiffeners."),
        ("Hydraulic Preloading Protocol & Thermal Stress Compensation", "BS EN 1997, CIRIA C760", "Establishing 1500-2500 kN hydraulic jack preloading and modeling thermal expansion forces in summer."),
        ("Basal Heave, Boiling & Hydraulic Uplift Stability Checks", "Terzaghi Bearing Theory, DIN 4084", "Calculating safety factors against hydraulic blow-out, piping, and deep circular basal slip failure."),
        ("Corrosion Allowance & Marine Dynamic Wave Impact Analysis", "ISO 12944, DNVGL-RP-C205", "Evaluating wave drag, tidal currents, and sacrificial steel corrosion allowance over 36 months.")
    ]
    count = 151
    for spec in p4_specs:
        for sub_title, codes, desc in p4_subtasks:
            roles.append({
                "id": count, "pillar_id": 4, "pillar_name": PILLARS[3][1],
                "title": f"{spec}: {sub_title}",
                "description": f"{desc} Ensuring zero damage to adjacent permanent structures and metro assets.",
                "operational_context": "EDRC Geotechnical & Marine Cell", "codes_and_tools": codes,
                "deliverable": f"Geotechnical & Structural Design Dossier: {spec} - {sub_title}", "risk_level": "Critical"
            })
            count += 1

    # -------------------------------------------------------------------------
    # PILLAR 5: ADVANCED STRUCTURAL MECHANICS, NON-LINEAR FEA & DYNAMICS (201-250)
    # -------------------------------------------------------------------------
    p5_topics = [
        ("Geometric Non-Linearity (P-Delta & P-delta)", "Formulates automated second-order P-Delta stiffness matrices for slender staging towers and high launching gantry legs under extreme vertical thrust and lateral traction.", "IS 800:2007, Eurocode 3"),
        ("Inelastic Local Plate Buckling & Web Crippling", "Performs non-linear post-buckling simulations on heavily loaded box girder webs under concentrated wheel bogeys, sizing longitudinal and transverse stiffeners.", "EN 1993-1-5, ANSYS"),
        ("Lateral Torsional Buckling (LTB) of Curved Falsework Trusses", "Evaluates elastic and inelastic LTB behavior of curved steel stringers and launch trusses, optimizing torsional fly-bracing layouts.", "AISC 360, IS 800"),
        ("High-Cycle Fatigue Analysis of Welded Gantry Connections", "Performs S-N curve stress range calculations (Eurocode Detail Category 71/80) on welded gantry joints subjected to over 200,000 segment load cycles.", "EN 1993-1-9, BS 7608"),
        ("3D Solid FEA Modeling of Pinned Connections & Saddles", "Conducts 3D solid non-linear contact FEA in ANSYS on forged gantry pins, trunnions, and spherical launching bearing shoes.", "ANSYS Mechanical, Hertz Contact"),
        ("Vortex-Induced Vibration (VIV) & Aerodynamic Drag", "Computes Strouhal numbers, lock-in wind velocities, and dynamic gust response factors for tall slender staging towers > 30m height.", "IS 875 Pt 3, EN 1991-1-4"),
        ("Aerodynamic Wind Buffeting on Long Cantilever Bridge Decks", "Simulates dynamic buffeting moments and flutter stability on balanced cantilever bridge decks during form traveler casting.", "IRC:6, Wind Tunnel Protocols"),
        ("Seismic Performance & Base Shear Distribution in Temporary Staging", "Applies response spectrum analysis to multi-tier falsework, calculating base shear, tieback tension, and anchor bolt embedment.", "IS 1893:2016, IRC:6"),
        ("Locked-in Stresses & Time-Dependent Concrete Rheology", "Calculates locked-in stresses resulting from sequential casting, creep, shrinkage, and temporary post-tensioning transfer.", "IRC:112, CEB-FIP Model Code"),
        ("Plastic Energy Dissipation & Dynamic Impact Mechanics", "Simulates energy absorption and shock impact mechanics during sudden crane wire snaps or dynamic gantry rail stop impacts.", "ASME B30, Explicit Dynamics")
    ]
    p5_aspects = [
        ("Theoretical Formulation & Mathematical Derivation", "Deriving governing differential equations and constitutive relations."),
        ("3D Finite Element Modeling & Mesh Convergence Studies", "Executing refined solid/shell mesh modeling with element convergence checks."),
        ("Parametric Sensitivity Analysis under Variable Load Cases", "Evaluating load permutations, material yield tolerances, and support settlements."),
        ("Calibration against Experimental Strain Gauge Telemetry", "Validating FEA results against physical strain gauge readings from test rigs."),
        ("Formulation of Simplified Design Rules for Site Engineers", "Translating complex non-linear FEA results into safe, practical site lookup tables.")
    ]
    count = 201
    for topic, desc, codes in p5_topics:
        for aspect_title, aspect_desc in p5_aspects:
            roles.append({
                "id": count, "pillar_id": 5, "pillar_name": PILLARS[4][1],
                "title": f"{topic}: {aspect_title}",
                "description": f"{desc} Focusing specifically on {aspect_desc.lower()}",
                "operational_context": "EDRC Advanced FEA & Dynamics Cell", "codes_and_tools": f"{codes}, Python, MATLAB",
                "deliverable": f"Advanced Mechanics Technical Report: {topic} - {aspect_title}", "risk_level": "Critical"
            })
            count += 1

    # -------------------------------------------------------------------------
    # PILLAR 6: DIGITAL ENGINEERING, BIM 4D, AUTOMATION & IoT SHM (251-300)
    # -------------------------------------------------------------------------
    p6_domains = [
        ("OpenSTAAD Headless Python Automation Pipeline", "Python, OpenSTAAD COM, Excel", "Automates 3D staging tower geometry generation, live load combinations, and member capacity checks."),
        ("MIDAS Civil MCT & REST API Parametric Construction Staging", "MIDAS Civil API, Python, JSON", "Automates staged construction sequences, creep-camber tracking, and tendon prestressing commands."),
        ("Tekla Structures Open API Parametric Steel Detailing", "Tekla Open API, C#, Grasshopper", "Generates automated shop drawings, CNC cutting files, weld schedules, and accurate BOM for gantries."),
        ("Grasshopper / Dynamo Algorithmic Formwork Surface Generation", "Rhino 3D, Grasshopper, Python", "Parametrically maps double-curved viaduct super-elevations onto modular shuttering surfaces."),
        ("Automated Lateral Concrete Pressure Engineering Engine", "Python, CIRIA 108, DIN 18218", "Computes multi-standard lateral pressure envelopes, tie-rod grids, and waler bending moments."),
        ("Heavy Tandem Rigging & Crane Mat Ground Bearing Suite", "Python, NumPy, BS 7121", "Calculates dual-crane load sharing, sling angle multipliers, and outrigger crane mat bearing pressures."),
        ("Real-time IoT Wireless Sensor Telemetry Architecture", "MQTT, InfluxDB, Grafana, IoT Gateway", "Streams strain, tilt, deflection, and wind gust data from launching gantries to cloud dashboards."),
        ("Automated SMS/Email Stop-Work Alert Engine", "Twilio API, Python Cloud Functions", "Triggers automated alarm broadcasts when staging tilt exceeds 0.2° or gantry chord stress reaches 85%."),
        ("4D BIM Synchro / Navisworks Construction Rehearsal", "Bentley Synchro 4D, Primavera P6", "Integrates 3D temporary equipment with P6 schedules, conducting virtual dry-runs of bridge launches."),
        ("AI Computer Vision Scaffolding Defect Detection", "YOLOv8, PyTorch, Drone Cameras", "Detects missing diagonal braces, loose couplers, and over-extended jack spindles from aerial site footage.")
    ]
    p6_phases = [
        ("Architecture Design & Algorithm Development", "Architecting robust algorithms, database schemas, and data pipelines."),
        ("API Integration & Headless Execution Scripting", "Writing production-grade Python/C# scripts for seamless software automation."),
        ("Quality Verification, Unit Testing & Benchmarking", "Rigorous benchmarking against verified manual calculations and benchmark models."),
        ("Deployment across Pan-India Project Sites", "Deploying web tools, containerized microservices, and mobile-friendly dashboards."),
        ("User Training & Continuous Pipeline Optimization", "Authoring user manuals and training site engineering cells on automation tools.")
    ]
    count = 251
    for domain, tools, desc in p6_domains:
        for phase_title, phase_desc in p6_phases:
            roles.append({
                "id": count, "pillar_id": 6, "pillar_name": PILLARS[5][1],
                "title": f"{domain}: {phase_title}",
                "description": f"{desc} Phase: {phase_desc}",
                "operational_context": "Digital Engineering & Automation Lab", "codes_and_tools": tools,
                "deliverable": f"Digital Asset / Script / Pipeline: {domain} - {phase_title}", "risk_level": "Strategic"
            })
            count += 1

    # -------------------------------------------------------------------------
    # PILLAR 7: BS 5975, CAT 0-3 CHECKS & QUALITY ASSURANCE (301-350)
    # -------------------------------------------------------------------------
    p7_topics = [
        "Master Temporary Works Register (TWR) life-cycle administration",
        "Category 0, 1, 2, and 3 design check categorization protocol",
        "Permit to Load (PTL) 12-point physical pre-pour inspection verification",
        "Permit to Strike (PTS) companion cube strength sign-off protocol",
        "Staging tower plumbness laser survey and tolerance verification",
        "High-strength Dywidag tie-rod torque calibration and elongation checks",
        "Non-Destructive Testing (NDT) of reused structural steel gantry welds",
        "Plate Load Test (PLT) validation of compacted staging subgrade beds",
        "U-Head and Base Jack maximum spindle extension compliance enforcement",
        "Concrete pump discharge pipeline surge anchor verification"
    ]
    p7_facets = [
        ("Statutory Protocol Authoring & Criteria Definition", "BS 5975:2019, PAS 8811", "Establishing definitive acceptance criteria, permissible tolerances, and statutory requirements."),
        ("On-Site Verification & Physical Inspection Audit", "Laser Total Station, Torque Wrenches", "Performing thorough site inspections with calibrated instrumentation to ensure 100% compliance."),
        ("Sign-Off Authority & Formwork Permit Issuance", "PTL / PTS Digital Governance Portal", "Exercising formal engineering sign-off authority to permit concrete placement or form striking."),
        ("Defect Logging, Non-Conformance Reports (NCR) & Re-Inspection", "ISO 9001, Quality NCR Workflow", "Issuing formal NCRs for observed site non-compliances, mandating redesign or rectification."),
        ("Audit Trail Archival & As-Built Certification", "L&T Document Management System", "Ensuring complete legal, contractual, and technical documentation is archived for project lifecycle.")
    ]
    count = 301
    for topic in p7_topics:
        for facet_title, codes, desc in p7_facets:
            roles.append({
                "id": count, "pillar_id": 7, "pillar_name": PILLARS[6][1],
                "title": f"{topic}: {facet_title}",
                "description": f"{desc} Applied to {topic} across all infrastructure ICs.",
                "operational_context": "Site TW Cell & Quality Assurance", "codes_and_tools": codes,
                "deliverable": f"Statutory Governance Record: {topic} - {facet_title}", "risk_level": "Critical"
            })
            count += 1

    # -------------------------------------------------------------------------
    # PILLAR 8: FORENSIC ENGINEERING & FAILURE PREVENTION (351-400)
    # -------------------------------------------------------------------------
    p8_scenarios = [
        "Launching Gantry stepping rail derailment or hydraulic stall",
        "Form Traveler asymmetric concrete placement overturning moment",
        "Deep excavation pipe strut buckling under extreme summer thermal expansion",
        "Multi-tier cup-lock staging collapse triggered by differential base settlement",
        "Heavy crane outrigger punch-through failure over unverified buried utility",
        "High-strength tie-rod thread stripping under excessive dynamic concrete surge",
        "Marine piling jetty stringer displacement under severe tidal storm surge",
        "Cantilever pier bracket slippage due to inadequate post-tensioning torque",
        "Slipform shutter jamming and concrete tearing during continuous 24-hr pour",
        "Tandem crane lift load transfer imbalance during synchronized slewing"
    ]
    p8_steps = [
        ("Failure Mode and Effects Analysis (FMEA) & Hazard Identification", "HAZOP, FMEA Matrix", "Systematically identifying initial failure modes, failure propagation pathways, and catastrophic outcomes."),
        ("Redundant Structural Defense Architecture Design", "BS 5975, Structural Redundancy Principles", "Designing fail-safe secondary support catches, mechanical backup locks, and load redistribution paths."),
        ("Forensic Site Investigation & Evidence Preservation", "ASCE Forensic Guidelines, Telemetry Logs", "Securing distorted steel samples, hydraulic pressure logs, and laser scans for forensic analysis."),
        ("Root Cause Analysis (RCA) & Metallurgical Testing", "Fishbone Analysis, SEM / Tensile Testing", "Determining fundamental metallurgical, mechanical, design, or operational causes of structural distress."),
        ("Pan-L&T Safety Lockdown & Remedial Engineering Directives", "Corporate Safety Directives", "Authoring mandatory technical remedial directives enforced across all corporate construction sites.")
    ]
    count = 351
    for scn in p8_scenarios:
        for step_title, codes, desc in p8_steps:
            roles.append({
                "id": count, "pillar_id": 8, "pillar_name": PILLARS[7][1],
                "title": f"{scn}: {step_title}",
                "description": f"{desc} In the context of {scn}.",
                "operational_context": "Corporate Forensic Engineering Cell", "codes_and_tools": codes,
                "deliverable": f"Forensic Dossier & Failure Prevention Directive: {scn} - {step_title}", "risk_level": "Critical"
            })
            count += 1

    # -------------------------------------------------------------------------
    # PILLAR 9: CLIENT, PROOF CONSULTANT & STATUTORY INTERFACING (401-450)
    # -------------------------------------------------------------------------
    p9_authorities = [
        ("National High Speed Rail Corporation (NHSRCL)", "MAHSR Bullet Train viaduct FSLE launchers, segment casting yards, and river bridge schemes."),
        ("Delhi Metro Rail Corporation (DMRC)", "Underground station box excavation strutting, track-crossover portal beam launches, and viaduct staging."),
        ("Mumbai Metropolitan Region Development Authority (MMRDA)", "Metro line elevated viaducts, special steel orthotropic deck spans, and station cantilevers."),
        ("National Highways Authority of India (NHAI)", "Multi-lane expressway river crossings, long-span balanced cantilever bridges, and flyovers."),
        ("Dedicated Freight Corridor Corporation (DFCCIL)", "Heavy haul railway bridge staging, continuous composite steel truss launches over active tracks."),
        ("Commissioner of Railway Safety (CRS)", "Statutory approvals for launching gantries and cranes operating in railway safety infringement zones."),
        ("International Proof Consultant: SYSTRA", "Third-party technical verification of Category 3 launching gantry models, deflections, and stress envelopes."),
        ("International Proof Consultant: COWI", "Category 3 independent structural check defense for complex cable-stayed pylon travelers and arch falsework."),
        ("State Directorate of Industrial Safety & Health (DISH)", "Statutory factory inspectorate compliance, tower crane load certifications, and scaffolding safety."),
        ("State Maritime Board & Port Trusts", "Navigation channel temporary works clearances, spud barge mooring permits, and piling jetty marine approvals.")
    ]
    p9_actions = [
        ("Comprehensive Technical Submission Dossier Preparation", "Compiling complete calculation packages, GFC drawings, and method statements to client formats."),
        ("Technical Defense Presentations & Clarification Meetings", "Leading technical defense sessions before chief bridge engineers, proving design adequacy."),
        ("Addressing Technical Comments & Independent Model Reconciliation", "Resolving proof consultant queries, reconciling numerical differences within 3% tolerance."),
        ("Managing Pre-Construction Site Audits & Verification Walkthroughs", "Guiding client technical delegations through prototype load tests and site fabrication inspections."),
        ("Securing Formal Statutory No-Objection Certificates (NOC)", "Obtaining signed, seal-bearing statutory clearances authorizing mobilization and construction.")
    ]
    count = 401
    for auth, ctx in p9_authorities:
        for action_title, desc in p9_actions:
            roles.append({
                "id": count, "pillar_id": 9, "pillar_name": PILLARS[8][1],
                "title": f"{auth}: {action_title}",
                "description": f"{desc} Context: {ctx}",
                "operational_context": "Client Interface & Proof Check Defense", "codes_and_tools": "Contractual Specs, FIDIC, IRC/IS Codes",
                "deliverable": f"Client Clearance & NOC Record: {auth} - {action_title}", "risk_level": "Strategic"
            })
            count += 1

    # -------------------------------------------------------------------------
    # PILLAR 10: COMMERCIAL, PRE-BID ESTIMATION & MENTORSHIP (451-500)
    # -------------------------------------------------------------------------
    p10_topics = [
        ("Pre-Bid Temporary Steel Tonnage Estimation", "Estimates temporary steel tonnage (staging, walers, gantries) within 5% accuracy for multi-thousand crore mega bids.", "Tendering / Pre-Bid Cell"),
        ("CAPEX vs OPEX Financial Evaluation for Modular Shuttering", "Models financial trade-offs between purchasing modular aluminum/steel systems vs leasing or custom fabrication.", "Commercial / P&M Accounts"),
        ("Heavy Launching Equipment Amortization Across Projects", "Formulates multi-project capital amortization schedules for 1000T FSLE and specialized launching gantries.", "Plant & Machinery (P&M)"),
        ("Specialized Hydraulic Equipment Procurement & Negotiation", "Conducts technical evaluation of vendor tenders for heavy strand jacks, climbing cylinders, and power packs.", "Supply Chain Management"),
        ("Drafting Patent Applications for Proprietary Erection Systems", "Drafts patent specifications and claims for novel self-advancing gantries and modular falsework mechanisms.", "Legal & IPR Cell"),
        ("Authoring L&T Corporate Technical Manuals & Design Guides", "Authors authoritative company-wide engineering manuals for temporary works design and site inspection.", "EDRC Knowledge Management"),
        ("Structuring Competency Roadmaps for 2 to 12 Year Engineers", "Designs structured career progression, technical curricula, and qualification milestones for design engineers.", "Talent Development / HR"),
        ("Conducting Masterclasses on Launching Gantry Mechanics", "Delivers advanced technical masterclasses on gantry kinematics, P-Delta stability, and hydraulic synchronization.", "L&T Institute of Project Management"),
        ("Mentoring Junior & Mid-Level Design Engineers (1-on-1)", "Provides dedicated 1-on-1 technical coaching, reviewing calculation sheets and guiding professional growth.", "EDRC Design Mentorship"),
        ("Leading Circular Steel Reuse & Carbon Footprint Reduction", "Implements corporate circular economy strategies, repurposing deconstructed temporary steel across projects.", "Sustainability & Asset Cell")
    ]
    p10_tasks = [
        ("Strategic Formulation & Objective Definition", "Setting clear technical, commercial, or pedagogical goals aligned with L&T corporate strategy."),
        ("Analytical Modeling & Financial/Technical Optimization", "Conducting rigorous mathematical, cost-benefit, or curriculum modeling to maximize efficiency."),
        ("Multi-Stakeholder Coordination & Implementation", "Collaborating across tendering, supply chain, site execution, and HR to execute the initiative."),
        ("Performance Tracking, KPI Measurement & Auditing", "Establishing quantitative metrics to measure cost savings, patent progress, or skill acquisition."),
        ("Continuous Review, Refinement & Long-Term Scaling", "Iterating based on site feedback to scale best practices across all operating divisions of L&T.")
    ]
    count = 451
    for topic, desc, ctx in p10_topics:
        for task_title, task_desc in p10_tasks:
            roles.append({
                "id": count, "pillar_id": 10, "pillar_name": PILLARS[9][1],
                "title": f"{topic}: {task_title}",
                "description": f"{desc} Phase: {task_desc}",
                "operational_context": ctx, "codes_and_tools": "L&T Commercial Guidelines, IPR Law",
                "deliverable": f"Commercial/Institutional Deliverable: {topic} - {task_title}", "risk_level": "Strategic"
            })
            count += 1

    print(f"Total Roles Successfully Generated: {len(roles)}")
    return roles

if __name__ == "__main__":
    roles = generate_500_roles()
    with open("roles_500_data.json", "w", encoding="utf-8") as f:
        json.dump(roles, f, indent=2, ensure_ascii=False)
    print("Saved roles_500_data.json successfully.")
