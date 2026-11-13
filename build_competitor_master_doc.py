"""
Builds the definitive Master Word Document:
L_and_T_vs_Tata_Projects_and_Competitors_Temporary_Structures_Master_Compendium.docx
Embedding all 8 high-resolution technical diagrams, deep competitor comparative intelligence,
and real working nature across Tier-1 contractors.
"""
import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL

from doc_sections.helpers import (
    set_cell_background, set_cell_margins, set_cell_borders, 
    set_table_styling, add_heading_1, add_heading_2, add_heading_3,
    add_heading_4, add_body_p, add_bullet_p, add_callout
)

IMAGES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "images")

def add_figure_with_caption(doc, filename, caption, width_in=6.2):
    img_path = os.path.join(IMAGES_DIR, filename)
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(8)
        p_img.paragraph_format.space_after = Pt(2)
        run_img = p_img.add_run()
        run_img.add_picture(img_path, width=Inches(width_in))
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(0)
        p_cap.paragraph_format.space_after = Pt(10)
        r_cap = p_cap.add_run(f"Figure: {caption}")
        r_cap.font.name = "Arial"
        r_cap.font.size = Pt(8.5)
        r_cap.font.bold = True
        r_cap.font.color.rgb = RGBColor(0, 45, 98)
    else:
        print(f"[WARNING] Image file not found: {filename}")

def build_competitor_master_doc():
    print("=" * 80)
    print("Building Competitor Deep-Dive & Real Working Nature Word Document (.docx)...")
    print("=" * 80)

    doc = docx.Document()

    # Configure Margins
    for s in doc.sections:
        s.top_margin = Inches(0.9)
        s.bottom_margin = Inches(0.9)
        s.left_margin = Inches(0.9)
        s.right_margin = Inches(0.9)

    # Header & Footer
    header = doc.sections[0].header
    p_h = header.paragraphs[0]
    p_h.text = "L&T vs TATA PROJECTS vs AFCONS | Temporary Structures Engineering & Real Working Nature"
    p_h.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    if p_h.runs:
        p_h.runs[0].font.name = "Arial"
        p_h.runs[0].font.size = Pt(8)
        p_h.runs[0].font.color.rgb = RGBColor(120, 130, 140)

    footer = doc.sections[0].footer
    p_f = footer.paragraphs[0]
    p_f.text = "L&T-TATA-AFCONS-INDUSTRY-COMPENDIUM-2026 | Comprehensive Working Culture & Visual Atlas | Confidential"
    p_f.alignment = WD_ALIGN_PARAGRAPH.LEFT
    if p_f.runs:
        p_f.runs[0].font.name = "Arial"
        p_f.runs[0].font.size = Pt(8)
        p_f.runs[0].font.color.rgb = RGBColor(120, 130, 140)

    # Title Block
    add_heading_1(doc, "TEMPORARY STRUCTURAL ENGINEERING IN TIER-1 CONTRACTORS")
    add_heading_2(doc, "Real Working Nature, Operational Culture, Design Ecosystems & Technical Visual Atlas: Larsen & Toubro vs Tata Projects Limited vs Afcons vs Competitors")

    add_callout(doc,
        "An exhaustive comparative intelligence report and engineering handbook detailing the real working life, technical hierarchies, software stacks, approval friction, equipment ownership, and construction realities of Temporary Structural Engineers across India's largest infrastructure conglomerates.",
        title="INDUSTRY INTELLIGENCE REPORT",
        alert_type="info"
    )

    # SECTION 1: COMPETITOR COMPARATIVE ANALYSIS
    add_heading_1(doc, "Section 1: The Tier-1 Infrastructure Competitive Landscape")
    add_body_p(doc,
        "Temporary structural engineering is the true engine room of profitability and risk in heavy infrastructure contracting. A permanent bridge or tunnel is designed once by consulting engineers, but the contractor's temporary works engineering team must invent, verify, fabricate, and erect the physical machinery that brings that design into reality.",
        bold_prefix="The Contracting Crucible: "
    )

    add_figure_with_caption(doc, "competitor_matrix_comparison.png", "Comparative Capability Benchmark across Tier-1 Infrastructure Contractors (0 to 10 Scale)")

    # Detailed Company Profiles
    add_heading_2(doc, "1.1 Larsen & Toubro Construction (The Self-Reliant Giant)")
    add_bullet_p(doc, "Centralized in EDRC (Chennai HQ, Mumbai, Delhi, Kolkata). Over 250+ dedicated in-house temporary works and construction methods structural engineers across FED (Formwork), CMPD (Construction Methods), and SE&HLD (Special Equipment).", bold_prefix="Engineering Nerve Center: ")
    add_bullet_p(doc, "High vertical integration. L&T designs and owns massive proprietary equipment fleets, including 1000-Ton Full Span Launching Equipment (FSLE) for high-speed rail, over 40+ segmental launching gantries, and tens of thousands of tons of modular steel staging.", bold_prefix="Equipment Ownership: ")
    add_bullet_p(doc, "Strict adherence to BS 5975:2019 and PAS 8811. Every temporary item requires a formal Temporary Works Register entry, Category 1/2/3 check, and digital Permit to Load (PTL) before concrete pour. Zero tolerance for unapproved site modifications.", bold_prefix="Governance & Safety: ")
    add_bullet_p(doc, "High technical rigor, intense peer reviews, highly demanding delivery schedules. Design engineers frequently rotate to major project sites for 6-12 month stints to experience erection reality.", bold_prefix="Working Culture: ")
    add_bullet_p(doc, "AutoCAD, STAAD.Pro Advanced, MIDAS Civil, PLAXIS 2D/3D, ANSYS, Rhino/Grasshopper, Bentley Synchro 4D, Python OpenSTAAD automation.", bold_prefix="Primary Software Stack: ")

    add_heading_2(doc, "1.2 Tata Projects Limited - TPL (The Fast-Track Digital Innovator)")
    add_bullet_p(doc, "Operates through its Engineering & Technology (E&T) centers in Mumbai, Hyderabad, and Delhi NCR, complemented by Tata Consulting Engineers (TCE) for mega-package proof checking.", bold_prefix="Engineering Center: ")
    add_bullet_p(doc, "Hybrid ownership model. While owning a significant fleet of tower cranes and staging, TPL aggressively partners with specialized international formwork firms (Doka, PERI, MFE) and heavy lifting specialists (Sarens, Mammoet) for turnkey launching and climbing solutions.", bold_prefix="Equipment Strategy: ")
    add_bullet_p(doc, "Strong focus on precast modular construction, composite structural steel erection, and high-speed building cycles (e.g. Central Vista New Parliament Building, Noida Jewar International Airport, Mumbai Metro Line 3 Packages).", bold_prefix="Signature Focus: ")
    add_bullet_p(doc, "Emphasizes Tata Safety Management System (TSMS), digital project control towers, real-time drone reality capture, and digital twin monitoring powered by Tata Elxsi and TCS.", bold_prefix="Digital Innovation: ")
    add_bullet_p(doc, "Tekla Structures, Revit, STAAD.Pro, MIDAS Civil, Navisworks, Primavera P6, custom Tata digital control suites.", bold_prefix="Software Stack: ")

    add_heading_2(doc, "1.3 Afcons Infrastructure - Shapoorji Pallonji (The Extreme Civil Specialists)")
    add_bullet_p(doc, "Specializes in extreme civil challenges: the Chenab Railway Arch Bridge (highest in the world), Atal Tunnel (Rohtang Pass), deep marine breakwaters, and difficult underground metro packages.", bold_prefix="Specialization: ")
    add_bullet_p(doc, "Owns India's largest specialized marine temporary fleet: heavy jack-up barges, spud-leg construction barges, floating crane vessels, and customized cable-crane systems.", bold_prefix="Marine & Rigging Fleet: ")
    add_bullet_p(doc, "Bold, site-driven engineering culture. Afcons temporary structural engineers work intimately with site project managers and crane operators, designing heavy-duty, robust, field-forgiving steel structures.", bold_prefix="Working Culture: ")

    add_heading_2(doc, "1.4 Hindustan Construction Company - HCC (The Pioneers of Hydro & Mega Bridges)")
    add_bullet_p(doc, "Decades of heritage building iconic structures like the Bandra-Worli Sea Link, Bogibeel Bridge (longest rail-cum-road bridge in India), and nuclear containment structures.", bold_prefix="Heritage: ")
    add_bullet_p(doc, "Masters of balanced cantilever form travelers (FT/CLC), heavy marine cofferdams, and deep hydro tunnel slipforms.", bold_prefix="Technical Core: ")

    add_heading_2(doc, "1.5 Dilip Buildcon Limited - DBL (The High-Velocity Highway Champions)")
    add_bullet_p(doc, "Extreme velocity execution. DBL operates an enormous captive machinery fleet, standardizing highway overpass staging and culvert shuttering to achieve record-breaking daily outputs.", bold_prefix="Execution Philosophy: ")
    add_bullet_p(doc, "Lean engineering team focused on repetitive modular standardization, rapid turnaround calculations, and eliminating assembly bottlenecks.", bold_prefix="Engineering Approach: ")

    # SECTION 2: REAL WORKING NATURE OF A 12-YEAR CHIEF SPECIALIST
    add_heading_1(doc, "Section 2: Real Working Nature & Daily Life of a 12-Year Specialist")
    add_body_p(doc,
        "A 12-year experienced Senior Engineering Manager / Chief Specialist in temporary works does not merely sit in an air-conditioned office running finite element models. Their real working life is a high-octane blend of crisis management, executive client defense, high-stakes site inspections, forensic troubleshooting, and strategic asset governance.",
        bold_prefix="The Reality of the Role: "
    )

    add_heading_2(doc, "2.1 The Daily Operational Routine (A Day in the Life)")
    add_bullet_p(doc, "07:30 AM - Reviewing live cloud IoT telemetry dashboards (strain gauges, tiltmeters, wind speeds) from overnight launching gantry advances on the high-speed rail corridor.", bold_prefix="Early Morning Telemetry Check: ")
    add_bullet_p(doc, "09:00 AM - Emergency site video conference: A deep excavation station strut on Mumbai Metro Line 3 showed an overnight 350 kN thermal surge due to sudden ambient temperature spike; reviewing strain data and authorizing hydraulic pressure relief.", bold_prefix="Crisis Response: ")
    add_bullet_p(doc, "11:00 AM - Defending a Category 3 Launching Gantry Erection Scheme before client proof consultants (SYSTRA / Cowi / DMRC), presenting non-linear P-Delta stability and dynamic wind flutter calculations.", bold_prefix="Client Proof Defense: ")
    add_bullet_p(doc, "02:30 PM - Mentorship masterclass for 15 Assistant Engineering Managers on effective length factors (k) for multi-tier cup-lock towers and Dywidag tie-rod prestress torque verification.", bold_prefix="Talent Incubation: ")
    add_bullet_p(doc, "04:30 PM - Pre-bid temporary works estimation review for a new 4-lane cable-stayed river bridge tender, optimizing temporary steel tonnage from 4,500 MT to 3,100 MT through modular re-use.", bold_prefix="Pre-Bid Commercials: ")
    add_bullet_p(doc, "06:30 PM - Executing formal Permit to Load (PTL) review for a 200-ton tandem crane precast portal beam lift over live railway tracks scheduled during an upcoming 3-hour midnight mega-block.", bold_prefix="Statutory PTL Authorization: ")

    # SECTION 3: VISUAL ATLAS & TECHNICAL DEEP DIVES
    add_heading_1(doc, "Section 3: Engineering Visual Atlas & Structural Schematics")
    add_body_p(doc,
        "The following engineering schematics illustrate the core structural systems, free-body diagrams, and kinematics governed by a Senior Engineering Manager across major infrastructure verticals."
    )

    add_heading_2(doc, "3.1 Overhead Segmental Launching Gantry (LG 1200T)")
    add_figure_with_caption(doc, "launching_gantry_schematic.png", "Overhead Segmental Launching Gantry (LG 1200T) - Structural Kinematics & Support Reactions")
    add_body_p(doc,
        "The launching gantry represents the pinnacle of mechanized temporary structures in bridge construction. Spanning 45m to 60m with lifting capacities up to 1200 tons, the gantry undergoes four distinct structural configurations during its cycle: (1) Segment feeding, (2) Dry-jointing & temporary post-tensioning, (3) Permanent post-tensioning and load transfer, and (4) Self-launching / stepping advance to the next span. The cantilever front nose must be designed with upward camber compensation to ensure the tip clears the forward pier cap bearing seat under dead load sag."
    )

    add_heading_2(doc, "3.2 Balanced Cantilever Form Traveler (FT / CLC 250T)")
    add_figure_with_caption(doc, "form_traveler_schematic.png", "Balanced Cantilever Form Traveler (FT / CLC 250T) - Free-Body Equilibrium & Anchor Forces")
    add_body_p(doc,
        "Used for long-span bridges across major rivers and deep gorges where ground falsework is impossible. The form traveler acts as a heavy cantilever truss anchored to the hardened concrete deck behind it via high-tensile Dywidag tie-down bars. The front pivot shoe acts as a massive fulcrum transmitting downward reactions of 2000 to 4500 kN, while the rear anchor bars resist tensile pullout forces with a mandatory safety factor FOS >= 2.0."
    )

    add_heading_2(doc, "3.3 Deep Station Excavation Diaphragm Wall Multi-Tier Strutting")
    add_figure_with_caption(doc, "deep_excavation_dwall_strutting.png", "Underground Metro Station Deep Excavation Strutting System & King Post Plunge Columns")
    add_body_p(doc,
        "In dense urban environments (Delhi Metro, Chennai Metro, Mumbai Metro Line 3), deep station boxes reach depths of 25m to 30m adjacent to sensitive heritage buildings. The temporary support system combines 1000mm-1200mm reinforced concrete Diaphragm Walls restrained by up to 5 tiers of heavy circular pipe struts (813mm to 1016mm dia). Hydraulic preloading of 1500 to 2500 kN per strut is mandatory to lock in lateral earth resistance and restrict ground surface settlement to less than 12 mm."
    )

    add_heading_2(doc, "3.4 Modular Tubular Staging Tower Mechanics (Cup-lock / Ring-lock)")
    add_figure_with_caption(doc, "cuplock_staging_tower_mechanics.png", "Modular Cup-lock / Ring-lock Staging Tower - Buckling Modes, Effective Lengths & Jack Spindle Limits")
    add_body_p(doc,
        "Ground falsework failures account for the overwhelming majority of temporary structure collapses. A staging tower with complete diagonal bracing behaves as a non-sway frame with effective length factor k = 1.0 (Euler capacity ~ 45 kN per standard). Omission of plan/sway bracing converts the tower into a sway frame with k = 2.0 to 2.5, causing a catastrophic 75% drop in buckling capacity! Over-extension of top/bottom jack spindles beyond 300 mm introduces extreme eccentric bending, triggering domino failure."
    )

    add_heading_2(doc, "3.5 Tandem Heavy Crane Rigging & Outrigger Crane Mats")
    add_figure_with_caption(doc, "tandem_crane_rigging_geometry.png", "Tandem Crane Heavy Lift Rigging Triangle, Sling Multiplier & Ground Bearing Pressure")
    add_body_p(doc,
        "Dual-crane tandem lifts require sophisticated rigging analysis. The sling tension is governed by T = (W * DAF) / (n * sin(theta)). Sling angles below 60 degrees exponentially increase tension and induce horizontal compressive crushing into the lifted girder. Outrigger ground bearing pressures under 250T-500T crawler cranes often reach 250 to 350 kPa, mandating engineered steel-reinforced timber mats to spread the reaction below the ground Safe Bearing Capacity (SBC)."
    )

    add_heading_2(doc, "3.6 Concrete Lateral Pressure Distribution on Vertical Formwork")
    add_figure_with_caption(doc, "concrete_lateral_pressure_curves.png", "Fresh Concrete Lateral Pressure Depth Envelopes: CIRIA 108 vs DIN 18218 vs ACI 347R")
    add_body_p(doc,
        "Formwork bursting occurs when placement rates outpace concrete setting kinetics. In hot Indian summer conditions (T = 28°C to 35°C), concrete stiffens rapidly, causing lateral pressure to peak at 40 to 48 kN/m2. In cold winter conditions (T = 10°C), hydration is retarded, causing lateral pressure to surge to 80 to 90 kN/m2 (+79% increase!), which will burst standard formwork unless tie-rod spacing is dramatically reduced or pour rates are curtailed."
    )

    add_heading_2(doc, "3.7 Real-Time IoT Structural Health Monitoring Architecture")
    add_figure_with_caption(doc, "iot_shm_telemetry_architecture.png", "Real-Time IoT Structural Health Monitoring (SHM) Telemetry Architecture for Heavy Temporary Works")
    add_body_p(doc,
        "Modern tier-1 temporary structures are instrumented with industrial IoT sensor telemetry. Vibrating wire strain gauges monitor gantry chord stress; wireless bi-axial tiltmeters detect 0.001-degree staging tilts; hydraulic pressure transducers verify multi-jack synchronization; and ultrasonic anemometers monitor 3-second gust wind speeds. Cloud engines automatically broadcast SMS stop-work alerts and trigger audible sirens when safety thresholds are approached."
    )

    output_filename = "L_and_T_vs_Tata_Projects_and_Competitors_Temporary_Structures_Master_Compendium.docx"
    doc.save(output_filename)
    file_size_kb = os.path.getsize(output_filename) / 1024
    print("=" * 80)
    print(f"Competitor Master Document Generated: {output_filename} ({file_size_kb:.2f} KB)")
    print("=" * 80)

if __name__ == "__main__":
    build_competitor_master_doc()
