"""
Generates:
1. 500_ROLES_AND_RESPONSIBILITIES_12_YEARS_SPECIALIST.md
2. L_and_T_500_Roles_and_Responsibilities_12_Years_Specialist.docx
"""
import json
import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from doc_sections.helpers import (
    set_cell_background, set_cell_margins, set_cell_borders, 
    set_table_styling, add_heading_1, add_heading_2, add_heading_3,
    add_body_p, add_bullet_p, add_callout
)

def build_documents():
    with open("roles_500_data.json", "r", encoding="utf-8") as f:
        roles = json.load(f)

    # 1. Build Markdown File
    print("Building Markdown File: 500_ROLES_AND_RESPONSIBILITIES_12_YEARS_SPECIALIST.md...")
    md_lines = [
        "# Larsen & Toubro Construction",
        "## Master Compendium of 500 Roles & Responsibilities",
        "### Designation: Senior Engineering Manager / Chief Specialist (Temporary Structures - 12+ Years Experience)",
        "**Divisions:** EDRC • CMPD • FED • Special Equipment Division (SE&HLD)",
        "**Local Host Dashboard:** [http://localhost:8080](http://localhost:8080)",
        "\n---\n"
    ]

    current_pillar = 0
    for r in roles:
        if r["pillar_id"] != current_pillar:
            current_pillar = r["pillar_id"]
            md_lines.append(f"\n## Pillar {current_pillar:02d}: {r['pillar_name']}\n")
            md_lines.append("| ID | Role & Technical Responsibility | Operational Unit | Standards & Tools | Deliverable | Risk |")
            md_lines.append("|:---:|---|---|---|---|:---:|")

        desc_escaped = r['description'].replace("|", "/")
        title_escaped = r['title'].replace("|", "/")
        context_escaped = r['operational_context'].replace("|", "/")
        tools_escaped = r['codes_and_tools'].replace("|", "/")
        deliv_escaped = r['deliverable'].replace("|", "/")
        
        md_lines.append(f"| **#{r['id']:03d}** | **{title_escaped}**<br>{desc_escaped} | {context_escaped} | `{tools_escaped}` | {deliv_escaped} | `{r['risk_level']}` |")

    with open("500_ROLES_AND_RESPONSIBILITIES_12_YEARS_SPECIALIST.md", "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))
    print("Markdown file built successfully.")

    # 2. Build Word Document (.docx)
    print("Building Word Document: L_and_T_500_Roles_and_Responsibilities_12_Years_Specialist.docx...")
    doc = docx.Document()

    # Configure Margins
    for s in doc.sections:
        s.top_margin = Inches(0.8)
        s.bottom_margin = Inches(0.8)
        s.left_margin = Inches(0.8)
        s.right_margin = Inches(0.8)

    # Cover / Header
    header = doc.sections[0].header
    p_h = header.paragraphs[0]
    p_h.text = "LARSEN & TOUBRO | 500 Roles & Responsibilities (12-Year Specialist - Temporary Structures)"
    p_h.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    if p_h.runs:
        p_h.runs[0].font.name = "Arial"
        p_h.runs[0].font.size = Pt(8)
        p_h.runs[0].font.color.rgb = RGBColor(120, 130, 140)

    footer = doc.sections[0].footer
    p_f = footer.paragraphs[0]
    p_f.text = "L&T-EDRC-CMPD-500-ROLES-12YRS | Local Dashboard: http://localhost:8080 | Confidential & Proprietary"
    p_f.alignment = WD_ALIGN_PARAGRAPH.LEFT
    if p_f.runs:
        p_f.runs[0].font.name = "Arial"
        p_f.runs[0].font.size = Pt(8)
        p_f.runs[0].font.color.rgb = RGBColor(120, 130, 140)

    # Title Block
    add_heading_1(doc, "Larsen & Toubro - Temporary Structural Engineering Excellence")
    add_heading_2(doc, "Master Compendium: 500 Granular Roles & Responsibilities (12-Year Senior Engineering Manager / Chief Specialist)")
    
    add_callout(doc,
        "This master document encapsulates the complete 500 roles, technical responsibilities, governance mandates, and automation duties of a 12-Year Experienced Senior Engineering Manager / Chief Specialist in Temporary Structures at Larsen & Toubro. Also accessible interactively on localhost: http://localhost:8080.",
        title="L&T EXECUTIVE TECHNICAL DIRECTIVE",
        alert_type="info"
    )

    # Group into tables by pillar
    pillars_dict = {}
    for r in roles:
        p_id = r["pillar_id"]
        if p_id not in pillars_dict:
            pillars_dict[p_id] = {"name": r["pillar_name"], "roles": []}
        pillars_dict[p_id]["roles"].append(r)

    for p_id, p_info in pillars_dict.items():
        add_heading_2(doc, f"Pillar {p_id:02d}: {p_info['name']} (Roles #{p_info['roles'][0]['id']:03d} - #{p_info['roles'][-1]['id']:03d})")
        
        table = doc.add_table(rows=len(p_info["roles"]) + 1, cols=5)
        headers = ["ID", "Title & Detailed Technical Responsibility", "Unit / Context", "Governing Codes & Tools", "Risk Level"]
        for c_idx, h in enumerate(headers):
            table.cell(0, c_idx).paragraphs[0].add_run(h)

        for r_idx, r_item in enumerate(p_info["roles"]):
            row_cells = table.rows[r_idx + 1].cells
            row_cells[0].paragraphs[0].add_run(f"#{r_item['id']:03d}").bold = True
            
            p_desc = row_cells[1].paragraphs[0]
            r_t = p_desc.add_run(f"{r_item['title']}\n")
            r_t.bold = True
            r_t.font.color.rgb = RGBColor(0, 45, 98)
            p_desc.add_run(r_item['description'])
            
            row_cells[2].paragraphs[0].add_run(r_item['operational_context'])
            row_cells[3].paragraphs[0].add_run(r_item['codes_and_tools'])
            
            r_risk = row_cells[4].paragraphs[0].add_run(r_item['risk_level'])
            r_risk.bold = True
            if r_item['risk_level'] == "Critical":
                r_risk.font.color.rgb = RGBColor(180, 20, 20)
            elif r_item['risk_level'] == "Strategic":
                r_risk.font.color.rgb = RGBColor(100, 30, 180)

        set_table_styling(table, col_widths=[0.6, 2.8, 1.2, 1.2, 0.7], header_bg="002D62")
        doc.add_paragraph().paragraph_format.space_after = Pt(8)

    docx_path = "L_and_T_500_Roles_and_Responsibilities_12_Years_Specialist.docx"
    doc.save(docx_path)
    file_size_kb = os.path.getsize(docx_path) / 1024
    print(f"Word Document Built Successfully: {docx_path} ({file_size_kb:.2f} KB)")

if __name__ == "__main__":
    build_documents()
