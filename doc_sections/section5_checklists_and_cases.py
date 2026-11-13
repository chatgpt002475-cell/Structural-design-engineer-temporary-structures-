import docx
from docx.shared import Inches, Pt, RGBColor
from doc_sections.helpers import (
    set_cell_background, set_cell_margins, set_cell_borders, 
    set_table_styling, add_heading_1, add_heading_2, add_heading_3,
    add_heading_4, add_body_p, add_bullet_p, add_callout
)

def build_section5_checklists_and_cases(doc):
    add_heading_1(doc, "Section 5: Standard Operating Procedures, Inspection Checklists & Governance Templates")
    
    add_body_p(doc,
        "Procedural control is the foundation of structural safety in temporary works. Under L&T's governance model, no temporary structural component may be erected, loaded, or struck without systematic documentation in the Temporary Works Register (TWR) and formal sign-offs via Permit to Load (PTL) and Permit to Strike (PTS).",
        bold_prefix="Procedural Control: "
    )
    
    # 5.1 Temporary Works Register Master Template
    add_heading_2(doc, "5.1 Temporary Works Register (TWR) Master Template")
    twr_table = doc.add_table(rows=5, cols=6)
    twr_headers = ["Item Ref", "Description of Temporary Works", "Cat", "Designer / Checker", "GFC Drawing No.", "PTL Status"]
    twr_data = [
        ("TWR-01", "Pier Cap Staging Tower (Pier P12 - H = 14.5m)", "Cat 2", "EDRC (Des: RK / Chk: AS)", "L&T-PKG-DWG-TW-0102", "APPROVED (PTL-2026-088)"),
        ("TWR-02", "Launching Gantry Main Truss Launching Setup", "Cat 3", "SE&HLD / Ext Proof: Bureau Veritas", "L&T-LG-1200T-DWG-0045", "PENDING (Site Check in prog)"),
        ("TWR-03", "Station Box D-Wall 3rd Level Strutting (CH 1420)", "Cat 2", "EDRC Geotech / Site TW Cell", "L&T-METRO-TW-STR-0301", "APPROVED (Preloaded 1800 kN)"),
        ("TWR-04", "Cantilever Deck Edge Shuttering (Span S14-S15)", "Cat 1", "Site TWD (Des: VN / Chk: ML)", "L&T-VIADUCT-SHUT-008", "APPROVED (PTL-2026-092)")
    ]
    for c_idx, h in enumerate(twr_headers):
        twr_table.cell(0, c_idx).paragraphs[0].add_run(h)
    for r_idx, row in enumerate(twr_data):
        for c_idx, val in enumerate(row):
            twr_table.cell(r_idx + 1, c_idx).paragraphs[0].add_run(val)
    set_table_styling(twr_table, col_widths=[0.8, 2.0, 0.6, 1.4, 1.4, 1.3], header_bg="002D62")
    
    # 5.2 12-Point Mandatory Permit to Load (PTL) Checklist
    add_heading_2(doc, "5.2 The 12-Point Mandatory Permit to Load (PTL) Pre-Pour Checklist")
    add_body_p(doc,
        "Prior to authorizing concrete placement or segment erection onto any temporary structure, the Temporary Works Coordinator (TWC) and Lead Site Engineer must jointly inspect and verify every item on this checklist:"
    )
    
    ptl_table = doc.add_table(rows=13, cols=3)
    p_headers = ["No.", "Physical Verification Item", "Acceptance Criteria & L&T Standard"]
    p_items = [
        ("1", "Foundation & Sole Plate Bearing", "Ground compacted to >= 95% MDD. Timber sole plate (min 50mm) or steel sleeper seated uniformly without air voids."),
        ("2", "Base Jack Spindle Extension", "Spindle extension measured <= 300 mm. No loose or unthreaded adjusters. Base plates centered on sole plates."),
        ("3", "Plumbness & Alignment", "Overall verticality of staging towers within 1:500 or max 15 mm over total height. Measured using laser plumb/total station."),
        ("4", "Cup-lock / Ring-lock Joint Wedge Tightness", "All cups hammered tight with 500g hammer until metallic ringing sound is produced. No unseated top cups."),
        ("5", "Diagonal Plan & Sway Bracing", "Diagonal bracing installed in both orthogonal directions at designated bays and connected with drop-forged right-angle couplers."),
        ("6", "Top U-Head Jack Extension & Centering", "Spindle extension <= 300 mm. Primary waler beams centered in U-head; hardwood wedges nailed where gap exceeds 5 mm."),
        ("7", "Waler Beam & Runner Bearing", "No flange buckling or lateral twist in steel channels. Runners seated flush on walers with web stiffeners at point supports."),
        ("8", "Tie Rod Installation & Torque", "Dywidag tie rods installed with approved anchor plates and waler washers. Torqued to specified prestress (approx. 25-35 kNm)."),
        ("9", "Concrete Pour Rate & Sensor Setup", "Maximum pour rate marked on permit board (e.g. max 1.5 m/hr). Calibrated wireless tiltmeters and strain gauges zeroed."),
        ("10", "Concrete Discharge Surge Anchor", "Concrete pump pipeline anchored securely to independent permanent pier or ground; never tied directly to staging towers!"),
        ("11", "Access Platforms & Safe Edge Protection", "Guard rails installed at 1.0m height with intermediate rail and 150mm toe board. Working platform fully decked and tied."),
        ("12", "Emergency Staging Watch Crew Assigned", "Dedicated staging watchman equipped with whistle, flashlight, and laser deflection targets stationed underneath during pour.")
    ]
    for c_idx, h in enumerate(p_headers):
        ptl_table.cell(0, c_idx).paragraphs[0].add_run(h)
    for r_idx, (num, item, crit) in enumerate(p_items):
        ptl_table.cell(r_idx + 1, 0).paragraphs[0].add_run(num)
        ptl_table.cell(r_idx + 1, 1).paragraphs[0].add_run(item)
        ptl_table.cell(r_idx + 1, 2).paragraphs[0].add_run(crit)
    set_table_styling(ptl_table, col_widths=[0.4, 2.3, 3.8], header_bg="1E5AA8")
    
    # 5.3 Permit to Strike (PTS) Protocol
    add_heading_2(doc, "5.3 The Permit to Strike (PTS) Protocol & Striking Sequence")
    add_body_p(doc,
        "Premature removal of formwork or falsework causes excessive deflection, cracking, or catastrophic punching shear failure in newly cast green concrete. The PTS protocol mandates:"
    )
    add_bullet_p(doc, "Striking cannot proceed based solely on elapsed time. Compressive strength must be verified by crushing site-cured concrete companion cubes (cured under identical field conditions as the structural member).", bold_prefix="Companion Cube Crushing: ")
    add_bullet_p(doc, "Slab and beam props must achieve at least 70% of 28-day characteristic cube strength (f_ck) before prop loosening, and 100% f_ck before back-prop removal.", bold_prefix="Minimum Strength Thresholds: ")
    add_bullet_p(doc, "For flexural members (beams, box girders, cantilevers), falsework must be struck systematically starting from mid-span and progressing outward toward the supports. For cantilevers, striking begins from the free tip moving toward the root. Decentering must be uniform across all jacks.", bold_prefix="Symmetrical Striking Sequence: ")
    add_bullet_p(doc, "Immediately upon releasing main falsework in multi-story construction, designated back-props must be reinstalled snug to share loads across multiple hardened floor slabs.", bold_prefix="Back-Propping Regime: ")
    
    # Section 6: Landmark L&T Projects
    add_heading_1(doc, "Section 6: Landmark L&T Projects & Case Studies")
    
    add_body_p(doc,
        "Larsen & Toubro's reputation as India's premier infrastructure conglomerate has been forged through the successful execution of extraordinary temporary works engineering on national landmark projects.",
        bold_prefix="Engineering in Action: "
    )
    
    add_heading_2(doc, "6.1 Mumbai Trans Harbour Link (MTHL / Atal Setu) – Marine Temporary Works")
    add_bullet_p(doc, "Engineered over 5.5 kilometers of temporary steel piling jetties traversing ecologically sensitive intertidal mudflats. Jetties were designed to support 100-ton crawler cranes, heavy multi-axle transporters, and continuous transit mixer traffic, withstanding harsh tidal currents and saline corrosion.", bold_prefix="Access Jetties: ")
    add_bullet_p(doc, "Specialized marine launching gantries erected spans up to 180 meters in length (Orthotropic Steel Decks - OSD) weighing up to 2,500 metric tons, utilizing synchronized strand-jacking and barge-mounted floating cranes.", bold_prefix="OSD Erection Schemes: ")
    
    add_heading_2(doc, "6.2 Mumbai-Ahmedabad High-Speed Rail (MAHSR Bullet Train) – 1000T FSLE")
    add_bullet_p(doc, "To construct hundreds of kilometers of high-speed rail viaduct with 40-meter, 975-ton precast full-span box girders, L&T engineered the 1000T Full Span Launching Equipment (FSLE) suite.", bold_prefix="Full Span Launching: ")
    add_bullet_p(doc, "Encompasses the 1000T Straddle Carrier (lifting segments in the casting yard), 1000T Multi-Axle Girder Transporter (navigating over finished viaduct deck), and 1000T Launching Gantry (erecting and seating girders onto pier bearings in a blistering 24-hour cycle per span).", bold_prefix="Mechanized Suite: ")
    
    add_heading_2(doc, "6.3 Metro Rail Underground Stations – Deep Excavation Strutting")
    add_bullet_p(doc, "Underground metro stations (Delhi Metro, Chennai Metro, Mumbai Metro Line 3) required excavations up to 28 meters depth adjacent to fragile colonial-era heritage buildings and active roadways.", bold_prefix="Deep Urban Excavation: ")
    add_bullet_p(doc, "Engineered 1000mm-thick Diaphragm Walls restrained by up to 5 tiers of heavy circular steel pipe struts (813mm to 1016mm diameter) preloaded with hydraulic jacks to 2500 kN per strut. Finite element PLAXIS modeling ensured ground surface settlement was restricted to less than 12 mm.", bold_prefix="Preloaded Strutting: ")
    
    add_heading_2(doc, "6.4 Balanced Cantilever Bridges – Form Travelers (CLC / FT)")
    add_bullet_p(doc, "Long-span balanced cantilever bridges over major rivers (Ganga, Godavari, Brahmaputra) were constructed using custom L&T Form Travelers casting 3m to 5m segment lengths weighing up to 250 tons in mid-air.", bold_prefix="Balanced Cantilever: ")
    add_bullet_p(doc, "Precise daily calculation of pre-camber curves, form traveler deflections, and asymmetric wind moments enabled flawless closure pours with less than 3 mm vertical misalignment between opposing cantilevers.", bold_prefix="Closure Alignment: ")
    
    # Section 7: Conclusion
    add_heading_1(doc, "Section 7: Conclusion & Strategic Roadmap for L&T Engineers")
    
    add_body_p(doc,
        "Temporary structural engineering is the true backbone of construction delivery. While the world sees and celebrates the finished bridge, skyscraper, or metro line, it is the temporary launching gantry, the deep excavation strutting, the form traveler, and the staging tower that made the permanent structure physically possible.",
        bold_prefix="The Core Takeaway: "
    )
    
    add_body_p(doc,
        "For an engineer journeying from 2 to 12+ years of experience within Larsen & Toubro, professional mastery requires equal devotion to mathematical rigor, site execution realities, procedural safety discipline, and cutting-edge work automation. By mastering the codes, embracing Python/BIM automation, adhering strictly to the Permit to Load governance, and cultivating an uncompromising commitment to structural safety, an L&T temporary works engineer shapes the future of modern infrastructure.",
        bold_prefix="The Path Forward: "
    )

    print("Section 5, 6, and 7 built successfully.")
