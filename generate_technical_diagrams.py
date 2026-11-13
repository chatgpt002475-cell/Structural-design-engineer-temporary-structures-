"""
Generates high-resolution engineering schematics and comparison charts
for Temporary Structural Engineering at L&T and Tier-1 Competitors.
"""
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "images")
os.makedirs(OUTPUT_DIR, exist_ok=True)

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']

def save_fig(fig, filename):
    filepath = os.path.join(OUTPUT_DIR, filename)
    fig.savefig(filepath, dpi=300, bbox_inches='tight')
    plt.close(fig)
    print(f"Generated: {filename} ({os.path.getsize(filepath) / 1024:.1f} KB)")

# ==============================================================================
# 1. LAUNCHING GANTRY SCHEMATIC
# ==============================================================================
def draw_launching_gantry():
    fig, ax = plt.subplots(figsize=(14, 6), dpi=300)
    ax.set_facecolor('#F8FAFC')
    fig.patch.set_facecolor('#FFFFFF')

    # Ground line & Piers
    ax.axhline(0, color='#64748B', lw=2, ls='--')
    
    # Pier P1 and Pier P2
    pier1 = patches.Rectangle((20, 0), 4, 15, facecolor='#94A3B8', edgecolor='#334155', lw=2)
    pier2 = patches.Rectangle((60, 0), 4, 15, facecolor='#94A3B8', edgecolor='#334155', lw=2)
    pier3 = patches.Rectangle((100, 0), 4, 15, facecolor='#CBD5E1', edgecolor='#94A3B8', lw=1.5, ls=':')
    ax.add_patch(pier1)
    ax.add_patch(pier2)
    ax.add_patch(pier3)

    ax.text(22, 7.5, 'Pier P1\n(Rear)', ha='center', va='center', fontweight='bold', color='#1E293B', fontsize=9)
    ax.text(62, 7.5, 'Pier P2\n(Front)', ha='center', va='center', fontweight='bold', color='#1E293B', fontsize=9)
    ax.text(102, 7.5, 'Pier P3\n(Target)', ha='center', va='center', color='#64748B', fontsize=9)

    # Pier Caps
    pcap1 = patches.Rectangle((18, 15), 8, 2.5, facecolor='#64748B', edgecolor='#1E293B', lw=1.5)
    pcap2 = patches.Rectangle((58, 15), 8, 2.5, facecolor='#64748B', edgecolor='#1E293B', lw=1.5)
    pcap3 = patches.Rectangle((98, 15), 8, 2.5, facecolor='#CBD5E1', edgecolor='#94A3B8', lw=1.5, ls=':')
    ax.add_patch(pcap1)
    ax.add_patch(pcap2)
    ax.add_patch(pcap3)

    # Main Gantry Truss (Length: 10m to 105m -> 95m total length)
    # Rear C-frame at x=15, Main Legs at x=22 and x=62, Launch Nose x=75 to x=105
    truss = patches.Rectangle((12, 21), 60, 5, facecolor='#002D62', edgecolor='#001A38', lw=2, alpha=0.9)
    ax.add_patch(truss)

    # Triangulated Nose Truss (Tapered)
    nose_x = [72, 105, 72]
    nose_y = [26, 23.5, 21]
    nose = patches.Polygon(xy=list(zip(nose_x, nose_y)), facecolor='#1E5AA8', edgecolor='#002D62', lw=2, alpha=0.9)
    ax.add_patch(nose)

    # Internal Truss Bracing (X-bracing pattern)
    for x in range(12, 72, 6):
        ax.plot([x, x+6], [21, 26], color='#FFBF00', lw=1.5)
        ax.plot([x, x+6], [26, 21], color='#FFBF00', lw=1.5)

    for x in range(72, 102, 6):
        taper_top = 26 - (x - 72) * (2.5 / 33)
        taper_bot = 21 + (x - 72) * (2.5 / 33)
        ax.plot([x, x+6], [taper_bot, taper_top], color='#FFBF00', lw=1.5)
        ax.plot([x, x+6], [taper_top, taper_bot], color='#FFBF00', lw=1.5)

    # Support Legs
    # Rear Leg (MSL1)
    msl1 = patches.Rectangle((21, 17.5), 2, 3.5, facecolor='#D97706', edgecolor='#78350F', lw=2)
    # Front Leg (MSL2)
    msl2 = patches.Rectangle((61, 17.5), 2, 3.5, facecolor='#D97706', edgecolor='#78350F', lw=2)
    ax.add_patch(msl1)
    ax.add_patch(msl2)

    # Hoist Trolley & Segment
    trolley = patches.Rectangle((36, 26), 8, 2, facecolor='#DC2626', edgecolor='#991B1B', lw=1.5)
    ax.add_patch(trolley)
    # Hanger cables
    ax.plot([38, 38], [26, 17], color='#475569', lw=2, ls='-')
    ax.plot([42, 42], [26, 17], color='#475569', lw=2, ls='-')
    # Precast Box Segment
    segment = patches.Rectangle((34, 12), 12, 5, facecolor='#E2E8F0', edgecolor='#475569', lw=2)
    ax.add_patch(segment)
    ax.text(40, 14.5, 'Precast Box Segment\n(Weight: 60T - 120T)', ha='center', va='center', fontweight='bold', fontsize=8, color='#0F172A')

    # Annotations & Callouts
    ax.annotate('Front Launching Nose (28m - 35m)\nTapered Cantilever (L/400 Camber)', xy=(90, 24), xytext=(85, 32),
                arrowprops=dict(facecolor='#002D62', shrink=0.05, width=1.5, headwidth=6),
                fontweight='bold', fontsize=9, color='#002D62', ha='center',
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#EFF6FF', edgecolor='#BFDBFE'))

    ax.annotate('Main Support Leg (MSL)\nWith Hydraulic Vertical Jacks', xy=(62, 19), xytext=(62, 10),
                arrowprops=dict(facecolor='#D97706', shrink=0.05, width=1.5, headwidth=6),
                fontweight='bold', fontsize=9, color='#B45309', ha='center',
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#FEF3C7', edgecolor='#FCD34D'))

    ax.annotate('Motorized Winch Trolley\nCapacity: 1200 kN', xy=(40, 28), xytext=(40, 33),
                arrowprops=dict(facecolor='#DC2626', shrink=0.05, width=1.5, headwidth=6),
                fontweight='bold', fontsize=9, color='#991B1B', ha='center',
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#FEE2E2', edgecolor='#FCA5A5'))

    ax.set_xlim(5, 115)
    ax.set_ylim(-2, 38)
    ax.set_title('LARSEN & TOUBRO - OVERHEAD SEGMENTAL LAUNCHING GANTRY (LG 1200T)\nStructural Kinematics, Component Hierarchy & Load Transfer Mechanism',
                 fontweight='bold', fontsize=12, pad=15, color='#002D62')
    ax.axis('off')

    save_fig(fig, 'launching_gantry_schematic.png')

# ==============================================================================
# 2. BALANCED CANTILEVER FORM TRAVELER SCHEMATIC
# ==============================================================================
def draw_form_traveler():
    fig, ax = plt.subplots(figsize=(12, 6.5), dpi=300)
    ax.set_facecolor('#F8FAFC')
    fig.patch.set_facecolor('#FFFFFF')

    # Concrete Box Girder (Already cast segment)
    c_deck = patches.Rectangle((5, 10), 30, 8, facecolor='#94A3B8', edgecolor='#334155', lw=2)
    ax.add_patch(c_deck)
    ax.text(20, 14, 'Previously Cast & Stressed\nCantilever Box Segment', ha='center', va='center', fontweight='bold', color='white', fontsize=10)

    # Newly Cast Segment under Form Traveler
    new_seg = patches.Rectangle((35, 10), 15, 8, facecolor='#FEF3C7', edgecolor='#D97706', lw=2, ls='--')
    ax.add_patch(new_seg)
    ax.text(42.5, 14, 'Wet Concrete Segment\n(Pour in Progress: 3.5m - 5.0m)\nWeight: 150T - 250T', ha='center', va='center', fontweight='bold', color='#92400E', fontsize=8.5)

    # Form Traveler Main Top Truss
    # Main longitudinal girder (x=15 to 55, y=21 to 23)
    ax.plot([15, 53], [21, 21], color='#002D62', lw=4) # Bottom chord
    ax.plot([25, 45], [29, 29], color='#002D62', lw=4) # Top chord
    # Diagonal truss members
    ax.plot([15, 25], [21, 29], color='#002D62', lw=3)
    ax.plot([25, 35], [29, 21], color='#002D62', lw=3)
    ax.plot([35, 45], [21, 29], color='#002D62', lw=3)
    ax.plot([45, 53], [29, 21], color='#002D62', lw=3)
    # Vertical posts
    ax.plot([25, 25], [21, 29], color='#002D62', lw=3)
    ax.plot([35, 35], [21, 29], color='#002D62', lw=3)
    ax.plot([45, 45], [21, 29], color='#002D62', lw=3)

    # Front Main Pivot / Wheel Shoe on cured concrete
    front_shoe = patches.Rectangle((33.5, 18), 3, 3, facecolor='#D97706', edgecolor='#78350F', lw=2)
    ax.add_patch(front_shoe)
    ax.text(35, 19.5, 'Front Shoe\n(R_max)', ha='center', va='center', fontsize=7, color='white', fontweight='bold')

    # Rear Tie-Down Dywidag Bars (Clamped to cured deck)
    ax.plot([16, 16], [18, 21], color='#DC2626', lw=3.5)
    ax.plot([18, 18], [18, 21], color='#DC2626', lw=3.5)
    ax.plot([14, 20], [18, 18], color='#991B1B', lw=4) # Anchor beam
    ax.annotate('Rear Hold-Down Anchor\nDywidag Prestress Bars (32mm)\nSafety FOS >= 2.0', xy=(17, 19.5), xytext=(12, 26),
                arrowprops=dict(facecolor='#DC2626', shrink=0.05, width=1.5, headwidth=6),
                fontweight='bold', fontsize=8.5, color='#991B1B', ha='center',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#FEE2E2', edgecolor='#FCA5A5'))

    # Front Hanging Rods (Suspending bottom and web shutters)
    ax.plot([45, 45], [9, 29], color='#0D7680', lw=3, ls='-')
    ax.plot([52, 52], [9, 21], color='#0D7680', lw=3, ls='-')

    # Bottom Shutter Cradle Beam
    bot_cradle = patches.Rectangle((34, 7), 18, 2, facecolor='#0D7680', edgecolor='#042F2E', lw=2)
    ax.add_patch(bot_cradle)
    ax.text(43, 8, 'Bottom Formwork Cradle Beam (Twin ISMB 500)', ha='center', va='center', color='white', fontweight='bold', fontsize=8)

    # Hydraulic Advancement Cylinder
    ax.plot([24, 33], [19.5, 19.5], color='#FFBF00', lw=5)
    ax.text(28.5, 20.3, 'Advance Cylinder', ha='center', va='bottom', fontsize=7.5, fontweight='bold', color='#B45309')

    ax.set_xlim(2, 60)
    ax.set_ylim(4, 34)
    ax.set_title('BALANCED CANTILEVER FORM TRAVELER (CLC / FT 250T)\nStructural Free-Body Equilibrium: Front Pivot Fulcrum & Rear Tie-Down Mechanism',
                 fontweight='bold', fontsize=12, pad=15, color='#002D62')
    ax.axis('off')

    save_fig(fig, 'form_traveler_schematic.png')

# ==============================================================================
# 3. DEEP EXCAVATION D-WALL STRUTTING SCHEMATIC
# ==============================================================================
def draw_deep_excavation():
    fig, ax = plt.subplots(figsize=(12, 7), dpi=300)
    ax.set_facecolor('#F8FAFC')
    fig.patch.set_facecolor('#FFFFFF')

    # Soil Layers (Left & Right of excavation)
    # Ground surface at y=30
    ax.fill_between([0, 15], [30, 30], [0, 0], color='#E2E8F0', alpha=0.8)
    ax.fill_between([45, 60], [30, 30], [0, 0], color='#E2E8F0', alpha=0.8)

    # Diaphragm Walls (D-Walls: Left x=15 to 17, Right x=43 to 45, depth y=2 to 32)
    dwall_l = patches.Rectangle((15, 2), 2, 30, facecolor='#64748B', edgecolor='#1E293B', lw=2)
    dwall_r = patches.Rectangle((43, 2), 2, 30, facecolor='#64748B', edgecolor='#1E293B', lw=2)
    ax.add_patch(dwall_l)
    ax.add_patch(dwall_r)

    # Excavated Pit (Between x=17 and 43, from y=30 down to y=8)
    pit = patches.Rectangle((17, 8), 26, 22, facecolor='#FFFBEB', edgecolor='none')
    ax.add_patch(pit)

    # Final Base Slab & Blinding
    base_slab = patches.Rectangle((17, 8), 26, 2.5, facecolor='#94A3B8', edgecolor='#334155', lw=1.5)
    ax.add_patch(base_slab)
    ax.text(30, 9.25, 'Reinforced Concrete Base Slab (T = 1500mm)', ha='center', va='center', fontweight='bold', fontsize=8, color='white')

    # King Post plunge column at center x=30
    king_post = patches.Rectangle((29.4, 2), 1.2, 30, facecolor='#334155', edgecolor='#0F172A', lw=2)
    ax.add_patch(king_post)
    ax.text(30, 4, 'Bored King Post\nPlunge Column', ha='center', va='center', color='white', fontsize=7, fontweight='bold')

    # Multi-Tier Steel Pipe Struts (4 Tiers: y=27, y=22, y=17, y=12)
    strut_levels = [(27, 'Tier 1 Strut (610mm dia / Preload: 800 kN)'),
                    (22, 'Tier 2 Strut (813mm dia / Preload: 1800 kN)'),
                    (17, 'Tier 3 Strut (1016mm dia / Preload: 2500 kN)'),
                    (12, 'Tier 4 Strut (1016mm dia / Preload: 2500 kN)')]

    for y_lvl, label in strut_levels:
        # Waler beams at D-wall face
        waler_l = patches.Rectangle((17, y_lvl-0.8), 1.5, 1.6, facecolor='#D97706', edgecolor='#78350F', lw=1.5)
        waler_r = patches.Rectangle((41.5, y_lvl-0.8), 1.5, 1.6, facecolor='#D97706', edgecolor='#78350F', lw=1.5)
        ax.add_patch(waler_l)
        ax.add_patch(waler_r)

        # Pipe Strut
        strut = patches.Rectangle((18.5, y_lvl-0.5), 23, 1.0, facecolor='#002D62', edgecolor='#001A38', lw=1.5)
        ax.add_patch(strut)

        # Hydraulic Preload Jack symbol
        jack = patches.Rectangle((38, y_lvl-0.7), 2.5, 1.4, facecolor='#DC2626', edgecolor='#991B1B', lw=1)
        ax.add_patch(jack)

        ax.text(30, y_lvl + 1.2, label, ha='center', va='bottom', fontsize=7.5, fontweight='bold', color='#002D62')

    # Earth Pressure & Surface Settlement Envelope
    ax.plot([5, 15], [30, 28.5], color='#DC2626', lw=2, ls='--')
    ax.text(8, 31, 'Settlement Trough\n(Max delta_v <= 12mm)', ha='center', va='bottom', color='#DC2626', fontsize=8, fontweight='bold')

    ax.annotate('Diaphragm Wall (1000mm - 1200mm)\nReinforced Concrete (f_ck = 40 MPa)', xy=(16, 16), xytext=(6, 16),
                arrowprops=dict(facecolor='#1E293B', shrink=0.05, width=1.5, headwidth=6),
                fontweight='bold', fontsize=8, color='#1E293B', ha='center',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#F1F5F9', edgecolor='#CBD5E1'))

    ax.annotate('Hydraulic Preloading Jack\nThermal Sensor Strain Gauge', xy=(39.2, 17), xytext=(48, 17),
                arrowprops=dict(facecolor='#DC2626', shrink=0.05, width=1.5, headwidth=6),
                fontweight='bold', fontsize=8, color='#991B1B', ha='center',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='#FEE2E2', edgecolor='#FCA5A5'))

    ax.set_xlim(0, 60)
    ax.set_ylim(0, 36)
    ax.set_title('UNDERGROUND METRO STATION DEEP EXCAVATION STRUTTING SYSTEM\nMulti-Tier Preloaded Tubular Steel Struts, Walers, King Posts & Ground Settlement Control',
                 fontweight='bold', fontsize=11, pad=15, color='#002D62')
    ax.axis('off')

    save_fig(fig, 'deep_excavation_dwall_strutting.png')

# ==============================================================================
# 4. CUPLOCK / RINGLOCK STAGING TOWER MECHANICS
# ==============================================================================
def draw_staging_tower():
    fig, ax = plt.subplots(figsize=(10, 7), dpi=300)
    ax.set_facecolor('#F8FAFC')
    fig.patch.set_facecolor('#FFFFFF')

    # Sole Plates & Compacted Bed (y=2 to 4)
    bed = patches.Rectangle((5, 1), 30, 2, facecolor='#E2E8F0', edgecolor='#94A3B8', lw=1.5)
    ax.add_patch(bed)
    ax.text(20, 2, 'Compacted Subgrade (MDD >= 95%, Tested SBC >= 180 kPa)', ha='center', va='center', fontsize=8, fontweight='bold', color='#475569')

    # Timber Sole Plates
    sp1 = patches.Rectangle((8, 3), 6, 0.8, facecolor='#B45309', edgecolor='#78350F', lw=1.5)
    sp2 = patches.Rectangle((26, 3), 6, 0.8, facecolor='#B45309', edgecolor='#78350F', lw=1.5)
    ax.add_patch(sp1)
    ax.add_patch(sp2)
    ax.text(11, 3.4, 'Hardwood Sole Plate (50mm)', ha='center', va='center', fontsize=6.5, color='white')

    # Base Jacks (y=3.8 to 6.0) -> Max extension 300mm limit
    ax.plot([11, 11], [3.8, 6.0], color='#DC2626', lw=4)
    ax.plot([29, 29], [3.8, 6.0], color='#DC2626', lw=4)
    ax.text(4, 5.0, 'Base Jack Spindle\n<= 300mm Max Extension!', ha='right', va='center', fontsize=8, fontweight='bold', color='#DC2626')
    ax.annotate('', xy=(11, 6.0), xytext=(11, 3.8), arrowprops=dict(arrowstyle='<->', color='#DC2626', lw=1.5))

    # Standards (Verticals: x=11 and x=29, lifts every 1.5m from y=6 to 24)
    ax.plot([11, 11], [6, 24], color='#002D62', lw=5)
    ax.plot([29, 29], [6, 24], color='#002D62', lw=5)

    # Horizontal Ledgers at 1.5m intervals (y=6, 9, 12, 15, 18, 21, 24)
    for y in [6, 9, 12, 15, 18, 21, 24]:
        ax.plot([11, 29], [y, y], color='#1E5AA8', lw=3)
        # Cup-lock node joints
        ax.plot(11, y, 'o', color='#FFBF00', markersize=7)
        ax.plot(29, y, 'o', color='#FFBF00', markersize=7)

    # Diagonal Sway Bracing (Alternate Bays)
    ax.plot([11, 29], [6, 12], color='#0D7680', lw=2.5, ls='--')
    ax.plot([29, 11], [12, 18], color='#0D7680', lw=2.5, ls='--')
    ax.plot([11, 29], [18, 24], color='#0D7680', lw=2.5, ls='--')

    # Top U-Head Jacks (y=24 to 26.2)
    ax.plot([11, 11], [24, 26.2], color='#DC2626', lw=4)
    ax.plot([29, 29], [24, 26.2], color='#DC2626', lw=4)
    ax.text(36, 25.1, 'Top U-Head Spindle\n<= 300mm Max Extension!', ha='left', va='center', fontsize=8, fontweight='bold', color='#DC2626')

    # Primary Waler Channel Beams (y=26.2 to 27.5)
    waler = patches.Rectangle((7, 26.2), 26, 1.4, facecolor='#334155', edgecolor='#0F172A', lw=2)
    ax.add_patch(waler)
    ax.text(20, 26.9, 'Primary Waler Channels (Twin ISMC 150)', ha='center', va='center', color='white', fontweight='bold', fontsize=8)

    # Secondary Runners (H20 Timber Beams / ISMC 75)
    for x in range(8, 33, 4):
        runner = patches.Rectangle((x-0.8, 27.6), 1.6, 2.0, facecolor='#FFBF00', edgecolor='#B45309', lw=1.5)
        ax.add_patch(runner)

    # Plywood Sheathing & Wet Concrete Deck
    ply = patches.Rectangle((6, 29.6), 28, 0.6, facecolor='#B45309', edgecolor='#78350F', lw=1.5)
    deck = patches.Rectangle((6, 30.2), 28, 3.5, facecolor='#FEF3C7', edgecolor='#D97706', lw=2)
    ax.add_patch(ply)
    ax.add_patch(deck)
    ax.text(20, 31.95, 'Wet Concrete Slab (Deck Load: 25-35 kN/m² + Dynamic Impact)', ha='center', va='center', fontweight='bold', color='#92400E', fontsize=8.5)

    # Effective Length Comparison Annotation
    ax.text(20, 15, 'Braced Tower: k = 1.0 (L_e = 1.5m)\nEuler Capacity = 45.0 kN / leg\n\nUnbraced Sway: k = 2.0\nEuler Capacity drops to 11.2 kN!',
            ha='center', va='center', fontsize=8, fontweight='bold', color='#002D62',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#EFF6FF', edgecolor='#BFDBFE'))

    ax.set_xlim(2, 42)
    ax.set_ylim(0, 36)
    ax.set_title('MODULAR TUBULAR STAGING TOWER (CUP-LOCK / RING-LOCK SYSTEM)\nBuckling Mechanics, Effective Length (k-factor), Spindle Extension Limits & Load Spread',
                 fontweight='bold', fontsize=11, pad=15, color='#002D62')
    ax.axis('off')

    save_fig(fig, 'cuplock_staging_tower_mechanics.png')

# ==============================================================================
# 5. TANDEM CRANE RIGGING GEOMETRY & GROUND BEARING PRESSURE
# ==============================================================================
def draw_tandem_crane_rigging():
    fig, ax = plt.subplots(figsize=(12, 6.5), dpi=300)
    ax.set_facecolor('#F8FAFC')
    fig.patch.set_facecolor('#FFFFFF')

    # Crane Booms (Crane 1 at left x=10, Crane 2 at right x=50)
    ax.plot([5, 20], [3, 26], color='#D97706', lw=6) # Boom 1
    ax.plot([55, 40], [3, 26], color='#1E5AA8', lw=6) # Boom 2

    ax.text(5, 1, 'Crane 1 (250T)\nCrawler Crane', ha='center', va='center', fontweight='bold', fontsize=8.5, color='#D97706')
    ax.text(55, 1, 'Crane 2 (250T)\nCrawler Crane', ha='center', va='center', fontweight='bold', fontsize=8.5, color='#1E5AA8')

    # Crane Hook Blocks
    hook1 = patches.Circle((20, 26), 1.0, facecolor='#334155', edgecolor='#0F172A', lw=1.5)
    hook2 = patches.Circle((40, 26), 1.0, facecolor='#334155', edgecolor='#0F172A', lw=1.5)
    ax.add_patch(hook1)
    ax.add_patch(hook2)

    # Spreader Beam (Connecting hooks or slung below)
    spreader = patches.Rectangle((18, 20), 24, 1.8, facecolor='#002D62', edgecolor='#001A38', lw=2)
    ax.add_patch(spreader)
    ax.text(30, 20.9, 'Engineered Heavy Spreader Beam (Capacity: 300 MT)', ha='center', va='center', color='white', fontweight='bold', fontsize=8)

    # Top Rigging Slings (From Hooks to Spreader Beam Ends)
    ax.plot([20, 20], [25, 21.8], color='#475569', lw=3)
    ax.plot([40, 40], [25, 21.8], color='#475569', lw=3)

    # Bottom Slings to Precast Bridge Girder
    # Sling angles theta >= 60 deg
    ax.plot([22, 26], [20, 11], color='#DC2626', lw=3.5)
    ax.plot([38, 34], [20, 11], color='#DC2626', lw=3.5)

    # Sling angle arc & label
    ax.text(23.5, 17, 'theta >= 60°\n(Mandatory L&T Limit)', ha='center', va='center', fontsize=7.5, fontweight='bold', color='#DC2626')

    # Precast Prestressed Concrete U-Girder / Box Girder
    girder = patches.Rectangle((24, 7), 12, 4, facecolor='#94A3B8', edgecolor='#334155', lw=2)
    ax.add_patch(girder)
    ax.text(30, 9, 'Precast Metro U-Girder\nGross Weight: 160 MT\n(incl. Rigging & DAF=1.20)', ha='center', va='center', color='white', fontweight='bold', fontsize=8)

    # Center of Gravity & Eccentricity
    ax.plot(29, 9, 'o', color='#FFBF00', markersize=9)
    ax.text(29, 6, 'CG Offset (e = 250mm)\nLoad Share: C1=55% / C2=45%', ha='center', va='top', fontsize=7.5, fontweight='bold', color='#B45309')

    # Outrigger Ground Bearing Pressure (GBP) callout box
    ax.text(30, 2, 'MANDATORY TANDEM LIFTING CRITERIA:\n• Crane Chart Derating: Maximum 75% Net Rated Capacity\n• Dynamic Amplification Factor: DAF = 1.15 to 1.25\n• Crane Mat Ground Bearing Pressure: q_peak <= Soil Allowable SBC\n• Synchronized Radio Communication & Dedicated Rigging Master',
            ha='center', va='center', fontsize=8, fontweight='bold', color='#002D62',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#EFF6FF', edgecolor='#BFDBFE'))

    ax.set_xlim(0, 60)
    ax.set_ylim(-1, 30)
    ax.set_title('TANDEM HEAVY CRANE RIGGING GEOMETRY & LOAD DISTRIBUTION\nSling Angle Multiplier (1/sin theta), Center of Gravity Shift & Outrigger Pad Sizing',
                 fontweight='bold', fontsize=11, pad=15, color='#002D62')
    ax.axis('off')

    save_fig(fig, 'tandem_crane_rigging_geometry.png')

# ==============================================================================
# 6. COMPETITOR COMPARISON MATRIX (L&T vs TATA PROJECTS vs AFCONS vs HCC vs DBL)
# ==============================================================================
def draw_competitor_comparison():
    fig, ax = plt.subplots(figsize=(13, 7.5), dpi=300)
    ax.set_facecolor('#FFFFFF')
    fig.patch.set_facecolor('#FFFFFF')

    companies = ['Larsen & Toubro\n(L&T Construction)', 'Tata Projects\nLimited (TPL)', 'Afcons\nInfrastructure', 'Hindustan Constr.\nCo. (HCC)', 'Dilip Buildcon\nLtd (DBL)']
    
    # 5 Key Metrics (Scores out of 10)
    metrics = [
        'Dedicated In-House TW Design (EDRC/FED)',
        'Heavy Mechanization Fleet (FSLE/LGs)',
        'Digital Automation & IoT Telemetry',
        'BS 5975 Strict Procedural Governance',
        'Executive Compensation & Specialist Band'
    ]

    # Scores
    scores = np.array([
        [9.8, 8.2, 8.8, 7.5, 6.2],  # In-House TW Design
        [9.9, 8.4, 9.1, 7.8, 7.0],  # Heavy Mechanization Fleet
        [9.5, 8.6, 7.9, 6.8, 5.5],  # Digital Automation & IoT
        [9.7, 8.8, 8.5, 7.2, 5.8],  # BS 5975 Governance
        [9.2, 9.0, 8.7, 7.6, 6.8]   # Executive Compensation
    ])

    x = np.arange(len(metrics))
    width = 0.16
    colors = ['#002D62', '#1E5AA8', '#D97706', '#0D7680', '#64748B']

    for idx, (comp, col) in enumerate(zip(companies, colors)):
        rects = ax.bar(x + (idx - 2) * width, scores[:, idx], width, label=comp, color=col, edgecolor='#0F172A', lw=0.8)
        # Add labels on top of bars
        for rect in rects:
            height = rect.get_height()
            ax.annotate(f'{height:.1f}',
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 2), textcoords="offset points",
                        ha='center', va='bottom', fontsize=6.5, fontweight='bold')

    ax.set_ylabel('Competency & Maturity Score (0 - 10)', fontweight='bold', fontsize=10, color='#0F172A')
    ax.set_title('TIER-1 INFRASTRUCTURE CONTRACTORS: TEMPORARY STRUCTURAL ENGINEERING CAPABILITY BENCHMARK\nComprehensive Industry Analysis: L&T vs Tata Projects vs Afcons vs HCC vs Dilip Buildcon',
                 fontweight='bold', fontsize=11, pad=15, color='#002D62')
    ax.set_xticks(x)
    ax.set_xticklabels(metrics, fontweight='bold', fontsize=8.5)
    ax.legend(loc='upper right', frameon=True, facecolor='#F8FAFC', edgecolor='#CBD5E1', fontsize=8.5)
    ax.set_ylim(0, 11.5)
    ax.grid(axis='y', ls=':', alpha=0.6)

    save_fig(fig, 'competitor_matrix_comparison.png')

# ==============================================================================
# 7. CONCRETE LATERAL PRESSURE DEPTH CURVES
# ==============================================================================
def draw_pressure_curves():
    fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300)
    ax.set_facecolor('#F8FAFC')
    fig.patch.set_facecolor('#FFFFFF')

    # Depth from 0 to 8 meters
    depth = np.linspace(0, 8, 100)
    gamma = 25.0 # kN/m3

    # Hydrostatic
    p_hydro = gamma * depth

    # CIRIA 108 (R = 2.0 m/hr, T = 28 deg C)
    p_max_ciria = 46.11
    p_ciria = np.minimum(p_hydro, p_max_ciria)

    # ACI 347R (R = 2.0 m/hr, T = 28 deg C)
    p_max_aci = 43.10
    p_aci = np.minimum(p_hydro, p_max_aci)

    # DIN 18218 (Flowable F3 concrete)
    p_max_din = 45.76
    p_din = np.minimum(p_hydro, p_max_din)

    # CIRIA 108 Winter Cold Weather (T = 10 deg C -> Higher pressure!)
    # K factor increases from 0.61 to 1.91
    p_max_winter = 82.5
    p_ciria_winter = np.minimum(p_hydro, p_max_winter)

    # Plot curves (Depth increasing downwards)
    ax.plot(p_hydro, depth, color='#64748B', lw=2, ls='--', label='Full Hydrostatic Limit (gamma * H)')
    ax.plot(p_ciria, depth, color='#002D62', lw=3, label='CIRIA 108 Design (R=2m/h, T=28°C Summer) -> 46.1 kN/m²')
    ax.plot(p_aci, depth, color='#DC2626', lw=2.5, ls='-.', label='ACI 347R-14 (R=2m/h, T=28°C) -> 43.1 kN/m²')
    ax.plot(p_din, depth, color='#0D7680', lw=2.5, ls=':', label='DIN 18218 (Flowable Consistency F3) -> 45.8 kN/m²')
    ax.plot(p_ciria_winter, depth, color='#D97706', lw=3, label='CIRIA 108 Winter Condition (T=10°C) -> 82.5 kN/m² (+79%!)')

    ax.set_xlabel('Lateral Concrete Pressure on Shuttering (kN/m²)', fontweight='bold', fontsize=10, color='#0F172A')
    ax.set_ylabel('Depth below Concrete Pour Surface (Meters)', fontweight='bold', fontsize=10, color='#0F172A')
    ax.set_title('CONCRETE LATERAL PRESSURE DISTRIBUTION ON VERTICAL FORMWORK\nInternational Code Formulations Comparison & Winter Temperature Surge Mechanics',
                 fontweight='bold', fontsize=11, pad=15, color='#002D62')
    ax.invert_yaxis() # Depth increases downwards
    ax.grid(True, ls=':', alpha=0.6)
    ax.legend(loc='lower right', frameon=True, facecolor='#FFFFFF', edgecolor='#CBD5E1', fontsize=8.5)

    save_fig(fig, 'concrete_lateral_pressure_curves.png')

# ==============================================================================
# 8. IoT STRUCTURAL HEALTH MONITORING TELEMETRY ARCHITECTURE
# ==============================================================================
def draw_iot_shm_architecture():
    fig, ax = plt.subplots(figsize=(12, 6.5), dpi=300)
    ax.set_facecolor('#F8FAFC')
    fig.patch.set_facecolor('#FFFFFF')

    # 4 Architecture Blocks: Sensors -> Edge Gateway -> Cloud Broker / DB -> Web Telemetry & SMS Alerts
    blocks = [
        ('FIELD SENSOR TIER\n(Physical Asset)', 3, '#002D62', [
            '• Vibrating Wire Strain Gauges (Gantry Chords)',
            '• Bi-Axial Tiltmeters (0.001° Accuracy)',
            '• Hydraulic Pressure Transducers (Strand Jacks)',
            '• Ultrasonic Anemometers (Wind Gusts m/s)',
            '• Laser Deflection String Pots (Camber)'
        ]),
        ('EDGE GATEWAY TIER\n(Site Container)', 15, '#1E5AA8', [
            '• RS485 / Modbus to MQTT Protocol Convertor',
            '• LoRaWAN Long-Range Transceivers (2.5 km)',
            '• Local Ring-Buffer Flash Storage',
            '• Dual SIM 4G/5G Cellular Uplink',
            '• 24V DC Solar & Battery Backup'
        ]),
        ('CLOUD INGESTION TIER\n(AWS / Azure)', 27, '#0D7680', [
            '• MQTT Broker (Mosquitto / AWS IoT Core)',
            '• High-Frequency Time-Series DB (InfluxDB)',
            '• Automated Rule Evaluation Engine',
            '• Python Anomaly Detection Algorithms',
            '• Secure REST API & WebSockets'
        ]),
        ('EXECUTIVE COMMAND TIER\n(Real-Time Web)', 39, '#D97706', [
            '• Live Grafana Web Telemetry Dashboard',
            '• 3D Digital Twin Synchronous Stress Map',
            '• Twilio SMS & WhatsApp Broadcast Alert',
            '• Automated Stop-Work Audio Siren at Site',
            '• Category 3 Statutory Audit Archive'
        ])
    ]

    for title, x_pos, col, items in blocks:
        box = patches.FancyBboxPatch((x_pos, 4), 9.5, 18, boxstyle="round,pad=0.3",
                                     facecolor='#FFFFFF', edgecolor=col, lw=2.5)
        ax.add_patch(box)

        # Header banner
        banner = patches.FancyBboxPatch((x_pos, 18.5), 9.5, 3.5, boxstyle="round,pad=0.2",
                                        facecolor=col, edgecolor=col, lw=1)
        ax.add_patch(banner)
        ax.text(x_pos + 4.75, 20.25, title, ha='center', va='center', color='white', fontweight='bold', fontsize=8)

        # Bullet items
        for idx, itm in enumerate(items):
            ax.text(x_pos + 0.6, 16.5 - idx * 2.3, itm, ha='left', va='center', fontsize=7, color='#1E293B', fontweight='500')

    # Interconnecting Arrows
    for arrow_x in [12.8, 24.8, 36.8]:
        ax.annotate('', xy=(arrow_x + 1.8, 13), xytext=(arrow_x - 0.2, 13),
                    arrowprops=dict(facecolor='#DC2626', shrink=0.05, width=2.5, headwidth=8))

    ax.set_xlim(1, 50)
    ax.set_ylim(2, 24)
    ax.set_title('LARSEN & TOUBRO - REAL-TIME IoT STRUCTURAL HEALTH MONITORING (SHM) ARCHITECTURE\nContinuous Sensor Telemetry, Edge Processing, Cloud Anomaly Detection & Emergency Stop-Work Automation',
                 fontweight='bold', fontsize=11, pad=15, color='#002D62')
    ax.axis('off')

    save_fig(fig, 'iot_shm_telemetry_architecture.png')

if __name__ == '__main__':
    print("Generating premium technical engineering diagrams...")
    draw_launching_gantry()
    draw_form_traveler()
    draw_deep_excavation()
    draw_staging_tower()
    draw_tandem_crane_rigging()
    draw_competitor_comparison()
    draw_pressure_curves()
    draw_iot_shm_architecture()
    print("All diagrams generated successfully!")
