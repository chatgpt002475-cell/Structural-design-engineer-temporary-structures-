import docx
from docx.shared import Inches, Pt, RGBColor
from doc_sections.helpers import (
    set_cell_background, set_cell_margins, set_cell_borders, 
    set_table_styling, add_heading_1, add_heading_2, add_heading_3,
    add_body_p, add_bullet_p, add_callout, add_code_block
)

def build_section3_automation(doc):
    add_heading_1(doc, "Section 3: Work Automation, Digitalization & Modern Engineering Tools")
    
    add_body_p(doc,
        "The digital transformation of temporary works engineering at Larsen & Toubro has shifted the discipline from manual 2D drafting and repetitive hand calculations to fully integrated computational design, parametric BIM modeling, automated numerical analysis pipelines, and real-time IoT structural telemetry. This automation eliminates human calculation error, accelerates design cycle times from weeks to hours, and provides live structural feedback during high-risk erection operations.",
        bold_prefix="The Automation Imperative: "
    )
    
    # 3.1 Structural Analysis Automation via OpenSTAAD & MIDAS MCT
    add_heading_2(doc, "3.1 Structural Analysis Automation via OpenSTAAD & MIDAS Civil API")
    add_body_p(doc,
        "Modeling large-scale multi-tier scaffolding towers (e.g., 25-meter tall staging for high pier caps or heavy flyover decks) requires thousands of nodes, members, and complex load combinations. L&T design engineers automate this process through Python scripts interfacing directly with STAAD.Pro via OpenSTAAD COM technology or MIDAS Civil through MCT commands and REST API."
    )
    
    add_bullet_p(doc, "Python scripts ingest viaduct deck geometry (super-elevation, longitudinal gradient, curve radius) and automatically generate the 3D nodal grid, assigning vertical cup-lock standards, horizontal ledgers, and plan/sway diagonal bracing.", bold_prefix="Automated Parametric Geometry: ")
    add_bullet_p(doc, "The script computes deck self-weight, variable concrete thickness, formwork dead load, dynamic impact allowance, and wind pressure, mapping these directly as nodal or member loads.", bold_prefix="Automated Load Generation: ")
    add_bullet_p(doc, "STAAD analysis is invoked headlessly. The Python pipeline extracts axial compression forces in every prop standard, runs Euler-Perry buckling equations against allowable capacities, and highlights overstressed members in red in automated 3D visual plots.", bold_prefix="Post-Processing & Capacity Checks: ")
    
    add_body_p(doc, "Below is an industrial Python snippet demonstrating headless OpenSTAAD automation for staging tower analysis:")
    
    code_staad = '''# ==============================================================================
# OpenSTAAD Automation Engine for Staging Tower Analysis
# Larsen & Toubro - EDRC / CMPD Digital Engineering Automation
# ==============================================================================
import win32com.client
import math

class StagingTowerAutomation:
    def __init__(self, filename):
        print(f"Connecting to OpenSTAAD for: {filename}")
        self.os_obj = win32com.client.Dispatch("StaadPro.OpenSTAAD")
        self.os_geometry = self.os_obj.Geometry
        self.os_property = self.os_obj.Property
        self.os_load = self.os_obj.Load
        self.os_output = self.os_obj.Output

    def create_tower(self, nx, ny, nz, dx, dy, dz):
        """Generates parametric multi-tier cup-lock tower grid."""
        node_id = 1
        node_map = {}
        for y in range(ny + 1):
            for x in range(nx + 1):
                for z in range(nz + 1):
                    self.os_geometry.CreateNode(node_id, x * dx, y * dy, z * dz)
                    node_map[(x, y, z)] = node_id
                    node_id += 1
        print(f"Generated {node_id - 1} nodes successfully.")
        return node_map

    def extract_critical_members(self, allowable_capacity_kn=35.0):
        """Extracts max axial compression in standards and flags overstress."""
        num_beams = self.os_geometry.GetMemberCount()
        overstressed = []
        for beam_id in range(1, num_beams + 1):
            # Extract axial force Fx at end 1 and end 2 (kilonewtons)
            fx1 = self.os_output.GetMemberEndForce(beam_id, 0, 1) # node 1, Fx
            fx2 = self.os_output.GetMemberEndForce(beam_id, 1, 1) # node 2, Fx
            max_comp = max(abs(fx1), abs(fx2))
            if max_comp > allowable_capacity_kn:
                ratio = max_comp / allowable_capacity_kn
                overstressed.append((beam_id, max_comp, ratio))
        print(f"Extraction complete. {len(overstressed)} members exceed safe capacity.")
        return overstressed
'''
    add_code_block(doc, code_staad, caption="OpenSTAAD Headless Python Automation Snippet")
    
    # 3.2 Computational Design & Parametric BIM Modeling
    add_heading_2(doc, "3.2 Computational Design & Parametric Modeling (Grasshopper & Tekla API)")
    add_body_p(doc,
        "In complex viaduct alignments featuring continuous horizontal curves, variable deck widths, and spiraled super-elevations, manual falsework detailing results in frequent site fit-up clashes. L&T utilizes Rhino/Grasshopper and Dynamo to parametrically drive formwork geometry from the road centerline alignment."
    )
    add_bullet_p(doc, "Grasshopper scripts adapt shutter surface curves dynamically based on bridge pier stationing, super-elevation cross-slopes, and vertical vertical curve offsets.", bold_prefix="Algorithmic Surface Modeling: ")
    add_bullet_p(doc, "Tekla Structures Open API is utilized to generate structural steel fabrication models for launching gantries, segment lifters, and heavy crosshead staging. Tekla automatically generates cutting plans, CNC machine files, weld schedules, and exact bolt counts, cutting fabrication turnaround time by 60%.", bold_prefix="Automated Tekla Detailing: ")
    
    # 3.3 Automated Engineering Calculation Suites
    add_heading_2(doc, "3.3 Automated Engineering Calculation Engines (Python & VBA)")
    add_body_p(doc,
        "To enforce standardized quality across all site engineering cells, L&T deploys centralized calculation suites for critical daily temporary works designs:"
    )
    add_bullet_p(doc, "Solves CIRIA 108, DIN 18218, and ACI 347R lateral pressure algorithms simultaneously. It determines the transition depth from hydrostatic to plastic/arching behavior based on pour rate (m/hr), concrete temperature (°C), slump flow, and cement type (OPC, PPC, GGBS). It automatically computes required tie-rod spacing and waler moments.", bold_prefix="1. Concrete Lateral Pressure Engine: ")
    add_bullet_p(doc, "Calculates crane boom configuration, counterweight requirements, outrigger reactions, ground bearing pressure under crane mats, and dual-crane load sharing with center-of-gravity (CG) shifts during slewing and luffing.", bold_prefix="2. Heavy Rigging & Crane Mat Suite: ")
    add_bullet_p(doc, "Calculates required bridge camber profiles for balanced cantilever form travelers, predicting concrete instantaneous deflection, long-term creep and shrinkage, form traveler elastic deflection under wet concrete, and tendon prestressing lift.", bold_prefix="3. Form Traveler Camber Engine: ")
    
    # 3.4 IoT-Enabled Structural Health Monitoring (SHM)
    add_heading_2(doc, "3.4 Real-Time IoT Structural Health Monitoring (SHM) for Temporary Structures")
    add_body_p(doc,
        "During high-risk operations—such as segmental launching gantry stepping, balanced cantilever segment casting, and multi-tier deep excavation strutting—L&T equips temporary structures with live IoT sensor telemetry. Structural integrity is continuously monitored via cloud dashboards, triggering automated alarms when safety thresholds are breached."
    )
    
    # Table of IoT Sensors in Temporary Works
    add_heading_3(doc, "Table 3.1: IoT Sensor Deployment Matrix in L&T Temporary Works")
    sensor_table = doc.add_table(rows=6, cols=4)
    s_headers = ["Sensor Typology", "Application System", "Measurement Parameter", "Threshold Action & Trigger"]
    s_data = [
        ("Vibrating Wire Strain Gauges", "Launching Gantry Main Chords, Deep Excavation Struts", "Micro-strain (epsilon) -> Member Axial Stress (MPa)", "Amber Alert at 75% allowable stress; Red Stoppage Alert at 85% allowable stress."),
        ("Wireless Bi-Axial Tiltmeters", "Staging Towers, Bridge Piers, Gantry Support Legs", "Angular inclination / plumbness deviation (degrees / mm/m)", "Warning at 0.15 deg (2.6 mm/m); Mandatory Halt at 0.25 deg (4.4 mm/m)."),
        ("Hydraulic Pressure Transducers", "Strand Jacks, Heavy Lifting Gantries, Preloading Jacks", "Hydraulic pressure (bar) -> Applied J-force (kN)", "Alert on 10% load imbalance between synchronized jacks; Auto-cut off."),
        ("Ultrasonic Wind Anemometers", "Launching Gantry Nose & Tail, Tower Cranes", "3-second gust wind velocity (m/s and km/h)", "Warning at 10 m/s (36 km/h); Cease Launching & Secure Gantry at 12 m/s (43 km/h)."),
        ("Displacement LVDTs & String Pots", "Cantilever Nose, Form Traveler Front Shutter", "Deflection under wet concrete or stepping (mm)", "Real-time camber verification against theoretical MIDAS prediction model.")
    ]
    for c_idx, h in enumerate(s_headers):
        sensor_table.cell(0, c_idx).paragraphs[0].add_run(h)
    for r_idx, row in enumerate(s_data):
        for c_idx, val in enumerate(row):
            sensor_table.cell(r_idx + 1, c_idx).paragraphs[0].add_run(val)
    set_table_styling(sensor_table, col_widths=[1.5, 1.8, 1.6, 1.6], header_bg="002D62")
    
    # 3.5 4D BIM & Digital Construction Rehearsal
    add_heading_2(doc, "3.5 4D BIM & Digital Construction Rehearsal (Synchro 4D & Navisworks)")
    add_body_p(doc,
        "Prior to physical mobilization, complex erection sequences are digitally rehearsed using 4D BIM platforms (Bentley Synchro 4D and Autodesk Navisworks). The 3D geometry of the temporary equipment (launching gantry, crane booms, mobile scaffolding) is linked directly with the Primavera P6 construction schedule."
    )
    add_bullet_p(doc, "Automated clash detection flags spatial conflicts between launching gantry outriggers, pier cap rebar cages, existing overhead high-tension power cables, and adjacent metro viaducts.", bold_prefix="Clash Detection: ")
    add_bullet_p(doc, "The site erection crew visualizes step-by-step segment feeding, epoxy application, dry-jointing, temporary prestressing (PT bars), permanent strand stressing, and gantry advance days before physical execution.", bold_prefix="Digital Rehearsal: ")
    
    # 3.6 AI & Machine Learning in Temporary Works
    add_heading_2(doc, "3.6 Artificial Intelligence & Machine Learning Applications")
    add_bullet_p(doc, "Machine learning algorithms optimize the layout of scaffolding towers and waler beam spacing, minimizing steel tonnage while satisfying deflection and stress constraints.", bold_prefix="Generative Staging Optimization: ")
    add_bullet_p(doc, "Predictive maintenance algorithms analyze hydraulic pressure waveforms and pump motor vibrations, forecasting hydraulic valve seal failures or winch brake wear before critical lifting operations.", bold_prefix="Predictive Maintenance: ")
    add_bullet_p(doc, "Computer vision algorithms mounted on site drones inspect scaffolding grids, automatically identifying missing diagonal braces, improperly seated couplers, or unsupported sole plates against GFC drawings.", bold_prefix="Computer Vision QA/QC: ")

    print("Section 3 built successfully.")
