import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

from doc_sections.cover_and_intro import build_cover_and_intro
from doc_sections.section2_experience_matrix import build_section2_experience_matrix
from doc_sections.section3_automation import build_section3_automation
from doc_sections.section4_technical_knowledge import build_section4_technical_knowledge
from doc_sections.section5_checklists_and_cases import build_section5_checklists_and_cases

def main():
    print("=" * 80)
    print("Building Larsen & Toubro Temporary Structural Engineering Master Guide (.docx)...")
    print("=" * 80)
    
    doc = docx.Document()
    
    # Configure Header and Footer
    section = doc.sections[0]
    header = section.header
    p_h = header.paragraphs[0]
    p_h.text = "LARSEN & TOUBRO | EDRC • CMPD • FED | Temporary Structural Engineering Master Guide"
    p_h.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    if p_h.runs:
        p_h.runs[0].font.name = "Arial"
        p_h.runs[0].font.size = Pt(8)
        p_h.runs[0].font.color.rgb = RGBColor(120, 130, 140)
        
    footer = section.footer
    p_f = footer.paragraphs[0]
    p_f.text = "L&T-EDRC-CMPD-TSE-GUIDE-2026-REV-3.0 | Roles, Competencies & Automation (2 to 12+ Years) | Confidential & Proprietary"
    p_f.alignment = WD_ALIGN_PARAGRAPH.LEFT
    if p_f.runs:
        p_f.runs[0].font.name = "Arial"
        p_f.runs[0].font.size = Pt(8)
        p_f.runs[0].font.color.rgb = RGBColor(120, 130, 140)
        
    # Build all sections sequentially
    print("[1/5] Building Cover Page, Metadata, Executive Summary & Section 1...")
    build_cover_and_intro(doc)
    
    print("[2/5] Building Section 2 (2 to 12+ Years Experience Progression Matrix)...")
    build_section2_experience_matrix(doc)
    
    print("[3/5] Building Section 3 (Work Automation, OpenSTAAD, IoT SHM, 4D BIM)...")
    build_section3_automation(doc)
    
    print("[4/5] Building Section 4 (Technical Knowledge Base, Formulae, Codes, Mechanics)...")
    build_section4_technical_knowledge(doc)
    
    print("[5/5] Building Sections 5, 6, 7 (Checklists, Case Studies & Conclusion)...")
    build_section5_checklists_and_cases(doc)
    
    output_filename = "L_and_T_Temporary_Structural_Engineer_Comprehensive_Master_Guide_2_to_12_Years.docx"
    output_path = os.path.join(os.getcwd(), output_filename)
    
    doc.save(output_path)
    file_size_kb = os.path.getsize(output_path) / 1024
    
    print("=" * 80)
    print(f"Master Document Successfully Generated: {output_filename}")
    print(f"File Size: {file_size_kb:.2f} KB")
    print(f"Absolute Path: {output_path}")
    print("=" * 80)

if __name__ == "__main__":
    main()
