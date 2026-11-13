# Temporary Structural Engineering Excellence & Work Automation (Larsen & Toubro)

> **Repository:** `Structural-design-engineer-temporary-structures-`  
> **Corporate Divisions:** Larsen & Toubro Construction — Heavy Civil Infrastructure (HCI IC), Transportation Infrastructure (TI IC), Buildings & Factories (B&F IC), Hydro & Tunneling  
> **Engineering Centers:** Engineering Design and Research Centre (EDRC) | Construction Methods Planning Department (CMPD) | Formwork Engineering Department (FED) | Special Equipment & Heavy Lifting Division (SE&HLD)  
> **Interactive Localhost Dashboard:** [http://localhost:8080](http://localhost:8080)  
> **Master Reference Documents:**  
> 1. `L_and_T_Temporary_Structural_Engineer_Comprehensive_Master_Guide_2_to_12_Years.docx` (Complete Master Guide)  
> 2. `L_and_T_500_Roles_and_Responsibilities_12_Years_Specialist.docx` (Dedicated 500-Roles Word Compendium)  
> 3. `500_ROLES_AND_RESPONSIBILITIES_12_YEARS_SPECIALIST.md` (Full Markdown Dossier)  
> 4. `roles_500_data.json` (Structured JSON Database)

---

## Interactive Localhost Dashboard (500 Roles & Responsibilities)

The repository includes a web dashboard running on **`http://localhost:8080`** for studying and tracking all **500 roles and responsibilities** of a **12-Year Senior Engineering Manager / Chief Specialist (Temporary Structures)** at L&T.

### Dashboard Capabilities:
- **Instant Search:** Search across all 500 roles by keyword (e.g. `MIDAS`, `PTL`, `FSLE`, `1000T`, `wind`, `camber`, `strut`, `tandem`, `patent`, `ANSYS`).
- **Pillar Filtering:** Filter by any of the 10 engineering pillars (50 roles each).
- **Risk Level Badges:** Filter by `Critical`, `Strategic`, or `High` risk classifications.
- **Reading Progress Tracker:** Interactive checkboxes to mark each role as "Read & Understood", with real-time percentage progress bar and persistent `localStorage`.
- **Print & PDF Export:** One-click print-ready styling for formal physical documentation.

To start the server manually anytime:
```bash
python server.py
# Open your browser and navigate to: http://localhost:8080
```

---

## The 10 Engineering Pillars (500 Roles Overview)

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                  L&T 500 ROLES & RESPONSIBILITIES COMPENDIUM (12-YEAR CHIEF SPECIALIST)          │
├───────────────────┬──────────────────────────────────────────────────────────────────────────────┤
│ Pillar 01 (#001-050)│ Strategic Leadership, Mega-Project Governance, Policy & Risk Charters        │
│ Pillar 02 (#051-100)│ Construction Method Statements (CMS), Erection Schemes & Kinematics          │
│ Pillar 03 (#101-150)│ Heavy Mechanization, 1000T FSLE, Launching Gantries & Form Travelers         │
│ Pillar 04 (#151-200)│ Deep Excavation (D-Walls), Pipe Strut Preloading, Marine Piling Jetties      │
│ Pillar 05 (#201-250)│ Advanced Structural Mechanics, Non-linear P-Delta FEA, Dynamics & Fatigue    │
│ Pillar 06 (#251-300)│ Digital Engineering, OpenSTAAD/MIDAS API Automation, 4D BIM & IoT SHM       │
│ Pillar 07 (#301-350)│ BS 5975 Governance, Cat 0-3 Independence, PTL/PTS Protocols & Quality Audits│
│ Pillar 08 (#351-400)│ Forensic Engineering, Collapse Prevention, FMEA & Disaster Recovery          │
│ Pillar 09 (#401-450)│ Client, Statutory Authorities (NHSRCL, DMRC, CRS) & Proof Consultant Defense │
│ Pillar 10 (#451-500)│ Commercial Tendering, Pre-Bid Estimation, Patenting & 1-on-1 Mentorship      │
└───────────────────┴──────────────────────────────────────────────────────────────────────────────┘
```

---

## Repository Structure & Deliverables

```
├── index.html                                                                          # Interactive Web App Dashboard
├── server.py                                                                           # Localhost HTTP Server (port 8080)
├── roles_500_data.json                                                                 # Structured Database of all 500 Roles
├── 500_ROLES_AND_RESPONSIBILITIES_12_YEARS_SPECIALIST.md                               # Markdown Compendium of 500 Roles
├── L_and_T_500_Roles_and_Responsibilities_12_Years_Specialist.docx                    # Dedicated 500-Roles Word Document
├── L_and_T_Temporary_Structural_Engineer_Comprehensive_Master_Guide_2_to_12_Years.docx  # Master Guide (2-12+ Years)
├── generate_master_doc.py                                                              # Master .docx Builder
├── generate_500_roles.py                                                               # 500-Roles Generator
├── build_html_dashboard.py                                                             # Dashboard Builder
├── build_500_roles_word_and_md.py                                                      # Word/Markdown 500-Roles Builder
├── automation_tools/                                                                   # Automation Scripts
│   ├── formwork_concrete_pressure_calculator.py                                        # CIRIA 108 / DIN 18218 / ACI 347R Engine
│   ├── rigging_and_crane_mat_optimizer.py                                             # Heavy Tandem Lift & Ground Bearing Analyzer
│   └── launching_girder_deflection_monitor.py                                          # Real-Time IoT Stepping & Telemetry Simulator
└── templates_and_checklists/                                                           # Governance Checklists
    ├── Permit_to_Load_Permit_to_Strike_Checklist.md                                    # 12-Point PTL & PTS Statutory Checklist
    ├── BS5975_Temporary_Works_Design_Brief_Template.md                                 # Standardized Design Brief (TWDB) Form
    └── Category_0_to_3_Design_Check_Matrix.md                                         # BS 5975 / L&T Check Allocation Matrix
```

---

## Running the Automation Engines

```bash
# 1. Start Local Dashboard Server
python server.py

# 2. Run Lateral Concrete Formwork Pressure Calculator
python automation_tools/formwork_concrete_pressure_calculator.py

# 3. Run Tandem Rigging & Crane Mat Ground Bearing Optimizer
python automation_tools/rigging_and_crane_mat_optimizer.py

# 4. Run Launching Girder Deflection & Telemetry Monitor
python automation_tools/launching_girder_deflection_monitor.py
```
