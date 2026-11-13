"""
Generates high-resolution infographic for L&T PIE Awards AI Innovation Ecosystem.
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "images")
os.makedirs(OUTPUT_DIR, exist_ok=True)

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']

def draw_pie_awards_infographic():
    fig, ax = plt.subplots(figsize=(14, 8), dpi=300)
    ax.set_facecolor('#F8FAFC')
    fig.patch.set_facecolor('#FFFFFF')

    # Central Core: L&T PIE AWARDS - AI INNOVATION ENGINE
    core = patches.FancyBboxPatch((28, 20), 24, 8, boxstyle="round,pad=0.5",
                                 facecolor='#002D62', edgecolor='#FFBF00', lw=3)
    ax.add_patch(core)
    ax.text(40, 25, 'L&T PIE AWARDS INNOVATION APEX', ha='center', va='center', color='#FFBF00', fontweight='bold', fontsize=11)
    ax.text(40, 22.5, 'Next-Gen AI & Digital Transformation in Temporary Structures\nEDRC • CMPD • FED • Special Equipment Division', ha='center', va='center', color='white', fontsize=8)

    # 6 Innovation Engines around the core
    innovations = [
        ("INNOVATION 01: VisionScaffold AI™",
         "Autonomous Drone & Edge Vision for Pre-Pour Staging Verification",
         "• Scans 25m staging towers in 90 seconds\n• Detects unseated cups & loose wedges via audio-vision\n• Spindle extension verification (±2mm accuracy)\n• Auto-generates statutory Permit to Load (PTL)",
         5, 27, '#0D7680'),

        ("INNOVATION 02: NeuroLaunch-Twin™",
         "Physics-Informed Neural Network (PINN) for Launching Gantries",
         "• Real-time kinematic predictor for 1000T/1200T LGs\n• Forecasts nose sag & rail friction spikes 45s ahead\n• Synchronized hydraulic closed-loop throttle\n• Compresses launch cycle by 18 hours per span",
         5, 12, '#1E5AA8'),

        ("INNOVATION 03: StrutGuard AI™",
         "Predictive Thermal & Geotechnical Deep Excavation Intelligence",
         "• Surrogate ML model trained on PLAXIS 3D data\n• Forecasts thermal strut thrust (+450 kN summer surge)\n• Closed-loop hydraulic preloading relief\n• Saves 1,800 MT steel (₹14 Cr) via wall optimization",
         5, -3, '#DC2626'),

        ("INNOVATION 04: GenerativeFalsework-X™",
         "Multi-Objective Generative AI for Parametric Staging Design",
         "• Graph Neural Network (GNN) optimizing 3D scaffolding\n• Ingests IFC bridge alignments & superelevations\n• Auto-extracts Tekla shop drawings & CNC cutting files\n• Slashes steel tonnage by 22% (Design time: 4 hours)",
         51, 27, '#7C3AED'),

        ("INNOVATION 05: CamberPredict-AI™",
         "Self-Calibrating Deep Learning for Balanced Cantilever Bridges",
         "• Bayesian DL predicting concrete creep & shrinkage\n• Real-time maturity meter sensor fusion\n• 100% first-time closure pour accuracy (±3mm)\n• Eliminates expensive deck grinding & shimming",
         51, 12, '#D97706'),

        ("INNOVATION 06: CraneGuard Tandem-AI™",
         "Computer Vision & Spatial LiDAR for Zero-Blindspot Tandem Lifts",
         "• Dual-crane synchronized 3D point cloud tracking\n• Real-time sling angle monitoring (theta >= 60°)\n• Continuous outrigger ground bearing pressure map\n• Zero railway mega-block overruns",
         51, -3, '#15803D')
    ]

    for title, subtitle, bullets, x, y, col in innovations:
        box = patches.FancyBboxPatch((x, y), 24, 11, boxstyle="round,pad=0.4",
                                     facecolor='#FFFFFF', edgecolor=col, lw=2.5)
        ax.add_patch(box)

        # Header tag
        tag = patches.FancyBboxPatch((x, y+8.5), 24, 2.5, boxstyle="round,pad=0.2",
                                     facecolor=col, edgecolor=col, lw=1)
        ax.add_patch(tag)
        ax.text(x + 12, y + 9.75, title, ha='center', va='center', color='white', fontweight='bold', fontsize=8)

        # Subtitle
        ax.text(x + 1.0, y + 7.2, subtitle, ha='left', va='center', color=col, fontweight='bold', fontsize=7)

        # Bullets
        ax.text(x + 1.0, y + 3.5, bullets, ha='left', va='center', color='#1E293B', fontsize=6.8, linespacing=1.35)

        # Connecting dashed lines to center core
        mid_x = x + 12
        mid_y = y + 5.5
        ax.plot([mid_x, 40], [mid_y, 24], color=col, lw=1.5, ls='--', alpha=0.5)

    ax.set_xlim(0, 80)
    ax.set_ylim(-5, 42)
    ax.set_title('LARSEN & TOUBRO - PIE AWARDS: REVOLUTIONARY AI & DIGITAL ECOSYSTEM IN TEMPORARY STRUCTURES\nAutonomous Vision, Physics-Informed Neural Networks, Generative Design & IoT Edge Safety Intelligence',
                 fontweight='bold', fontsize=11, pad=15, color='#002D62')
    ax.axis('off')

    filepath = os.path.join(OUTPUT_DIR, "ai_pie_awards_innovation_ecosystem.png")
    fig.savefig(filepath, dpi=300, bbox_inches='tight')
    plt.close(fig)
    print(f"Generated: ai_pie_awards_innovation_ecosystem.png ({os.path.getsize(filepath) / 1024:.1f} KB)")

if __name__ == '__main__':
    draw_pie_awards_infographic()
