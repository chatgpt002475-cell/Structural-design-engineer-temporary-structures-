import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from doc_sections.helpers import (
    set_cell_background, set_cell_margins, set_cell_borders, 
    set_table_styling, add_heading_1, add_heading_2, add_heading_3,
    add_body_p, add_bullet_p, add_callout
)

def build_cover_and_intro(doc):
    # Set standard margins for normal section
    sections = doc.sections
    for s in sections:
        s.top_margin = Inches(1.0)
        s.bottom_margin = Inches(1.0)
        s.left_margin = Inches(1.0)
        s.right_margin = Inches(1.0)
        
    # --- COVER PAGE ---
    cover_table = doc.add_table(rows=1, cols=1)
    cover_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = cover_table.cell(0, 0)
    cell.width = Inches(6.5)
    set_cell_background(cell, "002D62") # L&T Navy
    set_cell_margins(cell, top=280, bottom=280, left=240, right=240)
    
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_org = p.add_run("LARSEN & TOUBRO LIMITED\n")
    r_org.font.name = "Arial"
    r_org.font.size = Pt(13)
    r_org.font.bold = True
    r_org.font.color.rgb = RGBColor(255, 191, 0) # L&T Gold/Amber
    
    r_div = p.add_run("CONSTRUCTION BUSINESS • HEAVY CIVIL INFRASTRUCTURE • BUILDINGS & FACTORIES\nTRANSPORTATION INFRASTRUCTURE • HYDRO & TUNNELING\n\n")
    r_div.font.name = "Arial"
    r_div.font.size = Pt(8.5)
    r_div.font.color.rgb = RGBColor(220, 230, 242)
    
    r_title = p.add_run("TEMPORARY STRUCTURAL ENGINEERING\nEXCELLENCE & WORK AUTOMATION\n")
    r_title.font.name = "Arial"
    r_title.font.size = Pt(21)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(255, 255, 255)
    
    r_sub = p.add_run("A Comprehensive Professional Master Guide & Technical Blueprint: Roles, Major Responsibilities, Engineering Deep-Dives, Automation Workflows, and Competency Roadmaps (2 to 12+ Years Experience)\n\n")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(11)
    r_sub.font.italic = True
    r_sub.font.color.rgb = RGBColor(200, 220, 240)
    
    r_meta = p.add_run("ENGINEERING DESIGN AND RESEARCH CENTRE (EDRC)\nCONSTRUCTION METHODS PLANNING DEPARTMENT (CMPD)\nFORMWORK ENGINEERING DEPARTMENT (FED) & SPECIAL EQUIPMENT DIVISION\n\n")
    r_meta.font.name = "Arial"
    r_meta.font.size = Pt(9)
    r_meta.font.bold = True
    r_meta.font.color.rgb = RGBColor(255, 191, 0)
    
    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_before = Pt(16)
    p_sp.paragraph_format.space_after = Pt(8)
    
    # Document Metadata Box
    meta_table = doc.add_table(rows=5, cols=2)
    meta_data = [
        ("Document Reference:", "L&T-EDRC-CMPD-TSE-GUIDE-2026-REV-3.0"),
        ("Subject:", "Temporary Works Design Engineering, Heavy Erection Schemes & Work Automation"),
        ("Target Experience Range:", "2 Years (Junior/Senior Design Engineer) to 12+ Years (Senior Engineering Manager / Chief Specialist)"),
        ("Governing Standards:", "BS 5975:2019, IS 14687, IRC:87, IRC:6, IS 800:2007, CIRIA 108, DIN 18218, EN 12812, ACI 347R"),
        ("Operational Verticals:", "Heavy Civil IC (Metros, High Speed Rail, Special Bridges), B&F IC (Tall Towers, Stadiums), TI IC (Expressways)")
    ]
    for r_idx, (k, v) in enumerate(meta_data):
        row = meta_table.rows[r_idx]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width = Inches(2.2)
        c1.width = Inches(4.3)
        c0.paragraphs[0].add_run(k).bold = True
        c1.paragraphs[0].add_run(v)
    set_table_styling(meta_table, col_widths=[2.2, 4.3], header_bg="1E5AA8", alt_bg="F8F9FA")
    
    doc.add_page_break()
    
    # --- EXECUTIVE SUMMARY ---
    add_heading_1(doc, "Executive Summary & The Philosophy of Temporary Works")
    
    add_body_p(doc, 
        "Temporary structures in heavy infrastructure construction represent the highest-risk, most dynamic, and mechanically demanding discipline in structural engineering. Unlike permanent structures—which are designed for well-defined ultimate limit states under static geometry and standardized environmental conditions—temporary structures are constantly reconfigured, repeatedly assembled and struck, subjected to asymmetrical construction loads, and operated under stringent cycle-time pressures.",
        bold_prefix="The Operational Reality: "
    )
    
    add_callout(doc,
        "\"Temporary structures carry permanent loads with zero margin for error. A temporary falsework or launching gantry collapse leads to catastrophic structural loss, irreversible project delay, and unacceptable risk to human life. In Larsen & Toubro, temporary works engineering is governed by the highest tier of engineering rigor, procedural control, and structural safety.\"",
        title="L&T CORE STRUCTURAL MANDATE",
        alert_type="danger"
    )
    
    add_body_p(doc,
        "This master document establishes the exhaustive competency, operational, and technical blueprint for Temporary Structural Engineers across Larsen & Toubro (L&T Construction). It maps the professional development, responsibilities, and required technical depth across four distinct career tiers: 2–4 years (Design Engineer / Senior Engineer), 5–7 years (Senior Design Engineer / Assistant Engineering Manager), 8–10 years (Engineering Manager / Lead Temporary Works Coordinator), and 11–12+ years (Senior Engineering Manager / Chief Specialist).",
        bold_prefix="Scope and Purpose: "
    )
    
    add_body_p(doc,
        "Furthermore, this guide details the work automation paradigm transforming L&T's engineering ecosystem: from OpenSTAAD and Python computational design pipelines to automated BIM 4D construction staging, Tekla dynamic detailing, and real-time IoT structural health monitoring during heavy bridge launches and deep excavation strutting.",
        bold_prefix="Digital Transformation & Automation: "
    )
    
    # --- SECTION 1 ---
    add_heading_1(doc, "Section 1: Organizational Ecosystem & Procedural Governance at L&T")
    
    add_heading_2(doc, "1.1 The L&T Temporary Works Organizational Framework")
    add_body_p(doc,
        "Within Larsen & Toubro Construction, temporary works engineering is executed through a synergistic multi-tier network spanning central design offices, specialist equipment divisions, and dedicated site engineering cells:"
    )
    
    add_bullet_p(doc, "Engineering Design and Research Centre (EDRC): The apex engineering nerve center located in Chennai, Mumbai, Delhi, and Kolkata. EDRC houses the structural specialists responsible for global scheme design, independent Category 3 design checks, specialized equipment structural design, and coordination with client proof consultants.", bold_prefix="1. EDRC: ")
    add_bullet_p(doc, "Construction Methods Planning Department (CMPD): Responsible for devising the comprehensive construction methodology, erection sequencing, cycle-time studies, plant & equipment selection, and heavy lift planning from pre-bid to execution.", bold_prefix="2. CMPD: ")
    add_bullet_p(doc, "Formwork Engineering Department (FED): Specialist wing dedicated to modular formwork systems, custom steel shutters, climbing systems, table forms, and wall/column formwork optimization across all ICs.", bold_prefix="3. FED: ")
    add_bullet_p(doc, "Special Equipment & Heavy Lifting Division (SE&HLD): Manages the procurement, mechanical design, hydraulic power units, load testing, commissioning, and periodic recertification of Launching Gantries (LG), Segment Lifters, Straddle Carriers, Form Travelers (FT), and Derrick Cranes.", bold_prefix="4. SE&HLD: ")
    add_bullet_p(doc, "Site Temporary Works Cell: Dedicated on-project engineering team led by the Temporary Works Coordinator (TWC) and site Temporary Works Designers (TWD) who oversee daily fabrication, erection, inspection, and the statutory Permit to Load / Permit to Strike process.", bold_prefix="5. Site TW Cell: ")
    
    add_heading_2(doc, "1.2 Procedural Governance: BS 5975:2019 & L&T Corporate Safety Directives")
    add_body_p(doc,
        "L&T enforces strict procedural control over temporary works aligned with BS 5975:2019 (Code of Practice for Temporary Works Procedures and the Permissible Stress Design of Falsework) and PAS 8811:2014. Under this protocol, every temporary structural element must be formally registered, categorized, checked, inspected, and released through an immutable paper and digital audit trail."
    )
    
    # Table of Check Categories
    add_heading_3(doc, "Table 1.1: L&T Temporary Works Design Check Categorization Matrix")
    cat_table = doc.add_table(rows=5, cols=4)
    cat_headers = ["Category", "Risk Level & Criteria", "Independence of Checker", "Typical Structural Systems"]
    cat_rows = [
        ("Cat 0", "Standard / Low Risk: Simple, off-the-shelf catalog equipment. Standard manufacturer configuration without modification.", "Site Engineer / Supervisor visual check against standard approved tables.", "Trench boxes < 1.5m, standard scaffolding < 2m, single-tier prop systems, shallow edge protections."),
        ("Cat 1", "Medium Risk: Non-complex site designs. Standard components with bespoke combinations. Moderate consequence of failure.", "Independent engineer within the same site team or design office, not involved in the original design.", "Cup-lock staging towers < 6m, standard retaining shoring < 3m, cantilevered bracket platforms, secondary pier cap falsework."),
        ("Cat 2", "High Risk: Complex bespoke temporary structures. High consequence of failure. Interaction with permanent works.", "Independent design team within EDRC or CMPD who did not participate in the original concept or design.", "Heavy bridge staging towers > 6m, deep excavation strutting & waling, multi-tier cofferdams, customized pier shutters, heavy crane loading platforms."),
        ("Cat 3", "Major / Catastrophic Risk: High-consequence, innovative, or unprecedented temporary structures. Complex soil-structure or mechanical interaction.", "Completely independent external engineering organization or accredited Proof Consultant.", "Segmental Launching Gantries (LG), Form Travelers (FT/CLC), 1000T FSLE, Marine Piling Jetties, Tunnel Shaft Temporary Bulkheads, Cable-Stayed Pylon Erection Gantries.")
    ]
    for c_idx, h in enumerate(cat_headers):
        cat_table.cell(0, c_idx).paragraphs[0].add_run(h)
    for r_idx, row in enumerate(cat_rows):
        for c_idx, val in enumerate(row):
            cat_table.cell(r_idx + 1, c_idx).paragraphs[0].add_run(val)
    set_table_styling(cat_table, col_widths=[0.8, 1.8, 1.8, 2.1], header_bg="002D62")
    
    add_heading_2(doc, "1.3 The Mandatory Permit to Load (PTL) & Permit to Strike (PTS) Protocol")
    add_body_p(doc,
        "No temporary structure at any L&T site may receive physical construction loads (wet concrete, precast segments, heavy plant) without an authorized Permit to Load (PTL). Similarly, no formwork or falsework may be loosened, decentered, or struck without an authorized Permit to Strike (PTS)."
    )
    
    add_callout(doc,
        "Mandatory Safety Rule: The Permit to Load is not merely an inspection sign-off; it is a legally binding verification that:\n"
        "1. Erection matches the approved Category 2 or 3 'Good for Construction' (GFC) drawing exactly.\n"
        "2. All bracing, ties, couplers, base jacks, and ground compaction criteria have been physically verified and torqued.\n"
        "3. Concrete cube crushing results confirm the permanent structure or support foundation has attained design striking/bearing strength.\n"
        "Striking formwork without a signed PTS constitutes a Zero-Tolerance Safety Violation.",
        title="ZERO-TOLERANCE SAFETY DIRECTIVE",
        alert_type="danger"
    )

    print("Cover and Section 1 built successfully.")
