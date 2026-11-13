"""
Upgrades index.html into a multi-tab Master Engineering Web Portal:
- Tab 1: 500 Roles & Responsibilities Explorer (with search, filter, check-off)
- Tab 2: Competitor Landscape & Real Working Nature (L&T vs Tata Projects vs Afcons vs HCC vs DBL)
- Tab 3: Visual Atlas of Temporary Structures (8 High-Res Schematics with Deep Technical Breakdown)
- Tab 4: Interactive Engineering Calculation Labs (Live in-browser calculators)
- Tab 5: Landmark Mega-Projects Case Studies (MAHSR, MTHL, Chenab, Metro D-Walls)
"""
import json
import os

HTML_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>L&T Temporary Structural Engineering Excellence | Master Portal & Visual Atlas</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --primary: #002D62;        /* L&T Deep Navy */
      --primary-light: #0A4B9A;
      --secondary: #1E5AA8;
      --accent: #FFBF00;         /* L&T Amber Gold */
      --accent-hover: #E5AC00;
      --teal: #0D7680;
      --critical: #DC2626;
      --strategic: #7C3AED;
      --high: #D97706;
      --bg: #F8FAFC;
      --card-bg: #FFFFFF;
      --text: #0F172A;
      --text-muted: #64748B;
      --border: #E2E8F0;
      --border-dark: #CBD5E1;
      --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
      --shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
      --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.5;
    }

    /* Header & Nav */
    header {
      background: linear-gradient(135deg, var(--primary) 0%, #001A38 100%);
      color: white;
      padding: 1.25rem 2rem 0 2rem;
      border-bottom: 4px solid var(--accent);
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: var(--shadow-lg);
    }

    .header-top {
      max-width: 1440px;
      margin: 0 auto;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 1rem;
      padding-bottom: 1rem;
    }

    .brand { display: flex; align-items: center; gap: 1rem; }
    .brand-badge {
      background: var(--accent);
      color: var(--primary);
      font-weight: 800;
      font-size: 0.85rem;
      padding: 0.25rem 0.6rem;
      border-radius: 4px;
      letter-spacing: 0.5px;
    }
    .brand-title h1 { font-size: 1.35rem; font-weight: 700; }
    .brand-title p { font-size: 0.8rem; color: #94A3B8; }

    .nav-tabs {
      max-width: 1440px;
      margin: 0 auto;
      display: flex;
      gap: 0.5rem;
      overflow-x: auto;
    }

    .nav-tab {
      padding: 0.75rem 1.25rem;
      color: #CBD5E1;
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      border-bottom: 3px solid transparent;
      transition: all 0.2s;
      white-space: nowrap;
    }
    .nav-tab:hover { color: white; }
    .nav-tab.active {
      color: var(--accent);
      border-bottom-color: var(--accent);
      background: rgba(255, 255, 255, 0.05);
    }

    /* Main Container */
    .portal-container {
      max-width: 1440px;
      margin: 2rem auto;
      padding: 0 1.5rem;
    }

    .tab-content { display: none; }
    .tab-content.active { display: block; }

    /* Layout for Tab 1 (Roles Explorer) */
    .roles-layout {
      display: grid;
      grid-template-columns: 320px 1fr;
      gap: 2rem;
    }
    @media (max-width: 1024px) { .roles-layout { grid-template-columns: 1fr; } }

    .sidebar {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 1.5rem;
      box-shadow: var(--shadow-sm);
      position: sticky;
      top: 140px;
      max-height: calc(100vh - 160px);
      overflow-y: auto;
    }

    .sidebar-section { margin-bottom: 1.5rem; }
    .sidebar-title {
      font-size: 0.85rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: var(--text-muted);
      margin-bottom: 0.75rem;
      display: flex;
      justify-content: space-between;
    }

    .search-input {
      width: 100%;
      padding: 0.65rem 0.85rem;
      border: 1px solid var(--border-dark);
      border-radius: 8px;
      font-size: 0.9rem;
      font-family: inherit;
      background: #F8FAFC;
    }
    .search-input:focus {
      outline: none;
      border-color: var(--primary-light);
      background: #FFFFFF;
      box-shadow: 0 0 0 3px rgba(10, 75, 154, 0.15);
    }

    .pillar-btn {
      width: 100%;
      background: transparent;
      border: 1px solid transparent;
      padding: 0.45rem 0.65rem;
      border-radius: 6px;
      text-align: left;
      font-size: 0.8rem;
      font-weight: 500;
      color: var(--text);
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 0.25rem;
      transition: all 0.15s;
    }
    .pillar-btn:hover { background: #F1F5F9; }
    .pillar-btn.active {
      background: #EFF6FF;
      color: var(--primary);
      font-weight: 600;
      border-color: #BFDBFE;
    }
    .pillar-badge {
      font-size: 0.7rem;
      padding: 0.1rem 0.4rem;
      border-radius: 9999px;
      background: #E2E8F0;
    }

    .filter-pills { display: flex; flex-wrap: wrap; gap: 0.35rem; }
    .filter-pill {
      padding: 0.3rem 0.6rem;
      border-radius: 9999px;
      font-size: 0.75rem;
      font-weight: 600;
      border: 1px solid var(--border-dark);
      background: white;
      cursor: pointer;
    }
    .filter-pill.active {
      background: var(--primary);
      color: white;
      border-color: var(--primary);
    }

    /* Role Cards */
    .cards-grid { display: flex; flex-direction: column; gap: 0.85rem; }
    .role-card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 1.15rem;
      box-shadow: var(--shadow-sm);
      transition: all 0.15s ease;
    }
    .role-card:hover { border-color: #94A3B8; box-shadow: var(--shadow); }
    .role-card.read { border-left: 5px solid #10B981; background: #FDFDFE; }

    .card-top { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.5rem; }
    .card-id-title { display: flex; align-items: flex-start; gap: 0.65rem; }
    .card-check { margin-top: 0.25rem; width: 17px; height: 17px; cursor: pointer; accent-color: #10B981; }
    .card-id {
      font-family: 'JetBrains Mono', monospace;
      font-weight: 700;
      font-size: 0.75rem;
      background: #F1F5F9;
      color: #475569;
      padding: 0.15rem 0.4rem;
      border-radius: 4px;
      border: 1px solid #E2E8F0;
    }
    .card-title { font-size: 1rem; font-weight: 700; color: var(--primary); }
    .badge {
      font-size: 0.7rem; font-weight: 700; padding: 0.2rem 0.5rem; border-radius: 9999px; text-transform: uppercase;
    }
    .badge-critical { background: #FEE2E2; color: #991B1B; }
    .badge-strategic { background: #EDE9FE; color: #5B21B6; }
    .badge-high { background: #FEF3C7; color: #92400E; }

    .card-desc { font-size: 0.85rem; color: #334155; margin-bottom: 0.75rem; padding-left: 1.9rem; }
    .card-meta-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 0.5rem;
      background: #F8FAFC;
      border-radius: 8px;
      padding: 0.65rem 0.85rem;
      margin-left: 1.9rem;
      font-size: 0.75rem;
    }
    .meta-item strong { color: #475569; display: block; text-transform: uppercase; font-size: 0.65rem; }
    .meta-item span { color: #1E293B; font-weight: 500; }
    .code-tag { font-family: 'JetBrains Mono', monospace; color: var(--teal); }

    /* Tab 2 & 3: Rich Sections */
    .section-card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 2rem;
      box-shadow: var(--shadow-sm);
      margin-bottom: 2rem;
    }
    .section-title {
      font-size: 1.4rem;
      font-weight: 800;
      color: var(--primary);
      margin-bottom: 0.75rem;
      border-bottom: 2px solid var(--accent);
      padding-bottom: 0.5rem;
    }
    .section-subtitle { font-size: 0.95rem; color: var(--text-muted); margin-bottom: 1.5rem; }

    /* Comparison Table */
    .comp-table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 1rem;
      font-size: 0.85rem;
    }
    .comp-table th {
      background: var(--primary);
      color: white;
      padding: 0.85rem;
      text-align: left;
      font-weight: 700;
    }
    .comp-table td {
      padding: 0.85rem;
      border-bottom: 1px solid var(--border);
      vertical-align: top;
    }
    .comp-table tr:nth-child(even) { background: #F8FAFC; }

    /* Gallery Grid */
    .gallery-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(420px, 1fr));
      gap: 1.5rem;
      margin-top: 1rem;
    }
    .gallery-card {
      background: white;
      border: 1px solid var(--border);
      border-radius: 10px;
      overflow: hidden;
      box-shadow: var(--shadow-sm);
      transition: all 0.2s;
    }
    .gallery-card:hover {
      box-shadow: var(--shadow-lg);
      border-color: var(--primary-light);
    }
    .gallery-img {
      width: 100%;
      height: 240px;
      object-fit: contain;
      background: #F1F5F9;
      border-bottom: 1px solid var(--border);
      cursor: pointer;
    }
    .gallery-body { padding: 1.25rem; }
    .gallery-title { font-size: 1.05rem; font-weight: 700; color: var(--primary); margin-bottom: 0.5rem; }
    .gallery-desc { font-size: 0.85rem; color: #475569; line-height: 1.45; }

    /* Interactive Calculator Widgets */
    .calc-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
      gap: 1.5rem;
    }
    .calc-card {
      background: white;
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 1.5rem;
      box-shadow: var(--shadow-sm);
    }
    .calc-header { font-size: 1.1rem; font-weight: 700; color: var(--primary); margin-bottom: 1rem; }
    .form-group { margin-bottom: 0.85rem; }
    .form-label { display: block; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; margin-bottom: 0.25rem; color: #475569; }
    .form-control {
      width: 100%;
      padding: 0.5rem 0.75rem;
      border: 1px solid var(--border-dark);
      border-radius: 6px;
      font-size: 0.85rem;
    }
    .result-box {
      background: #F0FDF4;
      border: 1px solid #BBF7D0;
      border-radius: 8px;
      padding: 1rem;
      margin-top: 1rem;
    }
    .result-title { font-size: 0.75rem; font-weight: 700; color: #166534; text-transform: uppercase; }
    .result-val { font-size: 1.4rem; font-weight: 800; color: #15803D; }
  </style>
</head>
<body>

  <!-- Header -->
  <header>
    <div class="header-top">
      <div class="brand">
        <span class="brand-badge">L&T CONSTRUCTION</span>
        <div class="brand-title">
          <h1>Temporary Structural Engineering Excellence Portal</h1>
          <p>EDRC • CMPD • FED • SE&HLD | Roles, Competitor Intelligence, Visual Atlas & Interactive Automation</p>
        </div>
      </div>
      <div>
        <a href="L_and_T_vs_Tata_Projects_and_Competitors_Temporary_Structures_Master_Compendium.docx" class="brand-badge" style="text-decoration:none; background: #002D62; color: white; border: 1px solid var(--accent); font-size: 0.8rem; padding: 0.4rem 0.8rem;">
          Download Master Word Report (.docx)
        </a>
      </div>
    </div>
    
    <!-- Navigation Tabs -->
    <div class="nav-tabs">
      <div class="nav-tab active" data-tab="tab-roles">1. 500 Roles & Responsibilities Explorer</div>
      <div class="nav-tab" data-tab="tab-competitors">2. Competitor Working Nature (L&T vs Tata vs Afcons)</div>
      <div class="nav-tab" data-tab="tab-gallery">3. Engineering Visual Atlas (8 High-Res Schematics)</div>
      <div class="nav-tab" data-tab="tab-calculators">4. Interactive Engineering Labs</div>
      <div class="nav-tab" data-tab="tab-projects">5. Landmark Mega-Projects Case Studies</div>
    </div>
  </header>

  <!-- Main Container -->
  <div class="portal-container">

    <!-- TAB 1: 500 ROLES EXPLORER -->
    <div class="tab-content active" id="tab-roles">
      <div class="roles-layout">
        <!-- Sidebar -->
        <aside class="sidebar">
          <div class="sidebar-section">
            <div class="sidebar-title">Instant Search</div>
            <input type="text" id="searchInput" class="search-input" placeholder="Search keywords, codes, tools...">
          </div>

          <div class="sidebar-section">
            <div class="sidebar-title">Engineering Pillars</div>
            <div class="pillar-list">
              <button class="pillar-btn active" data-pillar="all">
                <span>All 10 Pillars</span><span class="pillar-badge">500</span>
              </button>
              <button class="pillar-btn" data-pillar="1"><span>1. Governance & Policy</span><span class="pillar-badge">50</span></button>
              <button class="pillar-btn" data-pillar="2"><span>2. CMS & Erection Schemes</span><span class="pillar-badge">50</span></button>
              <button class="pillar-btn" data-pillar="3"><span>3. FSLE & Launching Gantries</span><span class="pillar-badge">50</span></button>
              <button class="pillar-btn" data-pillar="4"><span>4. Deep Excavation & Marine</span><span class="pillar-badge">50</span></button>
              <button class="pillar-btn" data-pillar="5"><span>5. Advanced Non-Linear FEA</span><span class="pillar-badge">50</span></button>
              <button class="pillar-btn" data-pillar="6"><span>6. Digital, BIM 4D & IoT SHM</span><span class="pillar-badge">50</span></button>
              <button class="pillar-btn" data-pillar="7"><span>7. BS 5975, PTL/PTS & QA</span><span class="pillar-badge">50</span></button>
              <button class="pillar-btn" data-pillar="8"><span>8. Forensic & Disaster Risk</span><span class="pillar-badge">50</span></button>
              <button class="pillar-btn" data-pillar="9"><span>9. Client & Proof Check</span><span class="pillar-badge">50</span></button>
              <button class="pillar-btn" data-pillar="10"><span>10. Pre-Bid & Mentorship</span><span class="pillar-badge">50</span></button>
            </div>
          </div>

          <div class="sidebar-section">
            <div class="sidebar-title">Risk Level</div>
            <div class="filter-pills" id="riskFilters">
              <button class="filter-pill active" data-risk="all">All</button>
              <button class="filter-pill" data-risk="Critical">Critical</button>
              <button class="filter-pill" data-risk="Strategic">Strategic</button>
              <button class="filter-pill" data-risk="High">High</button>
            </div>
          </div>
        </aside>

        <!-- Cards -->
        <main>
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom: 1rem;">
            <div>
              <h2 id="activePillarTitle" style="font-size:1.25rem; color:var(--primary); font-weight:700;">All 10 Engineering Pillars (500 Roles)</h2>
              <p id="resultsCount" style="font-size:0.85rem; color:var(--text-muted);">Showing 500 of 500 roles</p>
            </div>
            <div>
              <span id="totalReadCount" style="font-weight:800; color:var(--primary); font-size:1.1rem;">0 / 500</span> Understood
            </div>
          </div>
          <div class="cards-grid" id="cardsGrid"></div>
        </main>
      </div>
    </div>

    <!-- TAB 2: COMPETITOR LANDSCAPE & REAL WORKING NATURE -->
    <div class="tab-content" id="tab-competitors">
      <div class="section-card">
        <h2 class="section-title">Tier-1 Contractor Comparative Analysis</h2>
        <p class="section-subtitle">Real operational intelligence across India's largest infrastructure conglomerates: Larsen & Toubro vs Tata Projects vs Afcons vs HCC vs Dilip Buildcon.</p>
        
        <div style="text-align:center; margin-bottom: 2rem;">
          <img src="assets/images/competitor_matrix_comparison.png" alt="Competitor Comparison Chart" style="max-width:100%; border-radius:8px; border:1px solid var(--border); box-shadow:var(--shadow-sm);">
        </div>

        <table class="comp-table">
          <thead>
            <tr>
              <th>Evaluation Parameter</th>
              <th>Larsen & Toubro (L&T)</th>
              <th>Tata Projects Limited (TPL)</th>
              <th>Afcons Infrastructure</th>
              <th>Dilip Buildcon (DBL)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>In-House Design Strength</strong></td>
              <td><strong>EDRC/FED/CMPD:</strong> 250+ dedicated structural temporary works engineers. Completely self-reliant.</td>
              <td><strong>E&T Division + TCE:</strong> Strong in-house team with significant reliance on Tata Consulting Engineers.</td>
              <td><strong>Specialized Marine/Bridge Cell:</strong> Highly skilled site-driven design specialists.</td>
              <td><strong>Lean Highway Team:</strong> Focuses on repetitive standardization of flyover falsework.</td>
            </tr>
            <tr>
              <td><strong>Equipment Fleet & Mechanization</strong></td>
              <td><strong>Unrivaled Ownership:</strong> 1000T FSLE, 40+ Launching Gantries, hundreds of strand jacks, vast modular staging.</td>
              <td><strong>Hybrid Model:</strong> Heavy partnerships with Doka, PERI, and Sarens for turnkey systems.</td>
              <td><strong>Marine Superiority:</strong> India's largest fleet of jack-up barges, spud barges, and floating cranes.</td>
              <td><strong>Road Plant Dominance:</strong> Massive captive earthmoving and road machinery fleet.</td>
            </tr>
            <tr>
              <td><strong>Approval & Quality Rigor</strong></td>
              <td><strong>BS 5975 & PTL Mandate:</strong> Zero tolerance for site deviation. Category 3 proof checks strictly enforced.</td>
              <td><strong>Tata Safety (TSMS):</strong> High corporate audit standards and digital gatekeeper control.</td>
              <td><strong>Severe Environment Rigor:</strong> Heavy marine and seismic risk governance.</td>
              <td><strong>Speed-Driven:</strong> Fast-track verification aimed at bonus milestones.</td>
            </tr>
            <tr>
              <td><strong>12-Year Specialist Salary (CTC)</strong></td>
              <td><strong>₹38L – ₹55L CTC</strong> + Senior Leadership incentives & Executive medical.</td>
              <td><strong>₹36L – ₹52L CTC</strong> + Performance bonuses.</td>
              <td><strong>₹34L – ₹48L CTC</strong> + Special project allowances.</td>
              <td><strong>₹32L – ₹50L CTC</strong> + Early completion cash bonuses.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="section-card">
        <h2 class="section-title">The Real Working Life of a 12-Year Senior Engineering Manager</h2>
        <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap:1.5rem; margin-top:1rem;">
          <div style="background:#F8FAFC; padding:1.25rem; border-radius:8px; border-left:4px solid var(--primary);">
            <h4 style="color:var(--primary); margin-bottom:0.5rem;">The Design-Site Dynamic</h4>
            <p style="font-size:0.85rem; color:#475569;">The central design office (EDRC) calculates according to conservative code limits, while site execution managers are pressured by daily progress targets. The 12-year specialist serves as the ultimate arbiter, using deep technical expertise to authorize safe, innovative modifications that prevent site shutdowns.</p>
          </div>
          <div style="background:#F8FAFC; padding:1.25rem; border-radius:8px; border-left:4px solid var(--critical);">
            <h4 style="color:var(--critical); margin-bottom:0.5rem;">Crisis Command & Forensic Troubleshooting</h4>
            <p style="font-size:0.85rem; color:#475569;">When a gantry wheel derailment occurs, a strut experiences extreme thermal surging, or an excavation wall deflects past amber limits, the 12-year specialist assumes emergency structural command, leading real-time telemetry analysis and root-cause prevention.</p>
          </div>
          <div style="background:#F8FAFC; padding:1.25rem; border-radius:8px; border-left:4px solid var(--accent);">
            <h4 style="color:#B45309; margin-bottom:0.5rem;">Client & Proof Consultant Defense</h4>
            <p style="font-size:0.85rem; color:#475569;">Defending multi-million dollar erection schemes before client authorities (NHSRCL, DMRC, NHAI) and international proof checkers (SYSTRA, Cowi, Arup). Proving that launching kinematics, wind flutter, and soil-structure interactions satisfy limit state safety.</p>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 3: ENGINEERING VISUAL ATLAS -->
    <div class="tab-content" id="tab-gallery">
      <div class="section-card">
        <h2 class="section-title">Engineering Visual Atlas: Technical Schematics & Mechanics</h2>
        <p class="section-subtitle">High-resolution, engineering-grade illustrations of the core temporary structural systems governed by Senior Engineering Managers.</p>

        <div class="gallery-grid">
          
          <div class="gallery-card">
            <img src="assets/images/launching_gantry_schematic.png" class="gallery-img" onclick="window.open(this.src)">
            <div class="gallery-body">
              <div class="gallery-title">1. Overhead Launching Gantry (LG 1200T)</div>
              <div class="gallery-desc">Structural kinematics, support reactions on pier caps, front launching nose cantilever deflection (L/400), and motorized winch trolley load transfer.</div>
            </div>
          </div>

          <div class="gallery-card">
            <img src="assets/images/form_traveler_schematic.png" class="gallery-img" onclick="window.open(this.src)">
            <div class="gallery-body">
              <div class="gallery-title">2. Balanced Cantilever Form Traveler (FT 250T)</div>
              <div class="gallery-desc">Free-body equilibrium around the front pivot fulcrum shoe and rear hold-down Dywidag 32mm tie bars clamped to the hardened concrete deck (FOS &gt;= 2.0).</div>
            </div>
          </div>

          <div class="gallery-card">
            <img src="assets/images/deep_excavation_dwall_strutting.png" class="gallery-img" onclick="window.open(this.src)">
            <div class="gallery-body">
              <div class="gallery-title">3. Deep Station Excavation D-Wall Strutting</div>
              <div class="gallery-desc">Multi-tier preloaded tubular pipe struts (813mm-1016mm dia), waling beams, hydraulic preloading (2500 kN), and ground settlement control (&lt;= 12 mm).</div>
            </div>
          </div>

          <div class="gallery-card">
            <img src="assets/images/cuplock_staging_tower_mechanics.png" class="gallery-img" onclick="window.open(this.src)">
            <div class="gallery-body">
              <div class="gallery-title">4. Cup-lock & Ring-lock Staging Tower Mechanics</div>
              <div class="gallery-desc">Buckling length factors (k=1.0 braced vs k=2.0 sway), top/bottom jack spindle extension limits (&lt;= 300 mm), and sole-plate load distribution.</div>
            </div>
          </div>

          <div class="gallery-card">
            <img src="assets/images/tandem_crane_rigging_geometry.png" class="gallery-img" onclick="window.open(this.src)">
            <div class="gallery-body">
              <div class="gallery-title">5. Heavy Tandem Crane Rigging & Outrigger Mats</div>
              <div class="gallery-desc">Sling angle multiplier (1/sin theta with theta &gt;= 60 deg), CG shift eccentricity, crane capacity derating (75%), and ground bearing pressure under mats.</div>
            </div>
          </div>

          <div class="gallery-card">
            <img src="assets/images/concrete_lateral_pressure_curves.png" class="gallery-img" onclick="window.open(this.src)">
            <div class="gallery-body">
              <div class="gallery-title">6. Concrete Lateral Pressure Depth Envelopes</div>
              <div class="gallery-desc">CIRIA 108 vs DIN 18218 vs ACI 347R depth profiles, plastic transition depth, and winter temperature surge mechanics (+79% pressure spike).</div>
            </div>
          </div>

          <div class="gallery-card">
            <img src="assets/images/iot_shm_telemetry_architecture.png" class="gallery-img" onclick="window.open(this.src)">
            <div class="gallery-body">
              <div class="gallery-title">7. IoT Structural Health Monitoring Architecture</div>
              <div class="gallery-desc">Field sensors (strain gauges, tiltmeters, ultrasonic anemometers), LoRaWAN/4G edge gateway, cloud InfluxDB, and automated SMS stop-work alarms.</div>
            </div>
          </div>

          <div class="gallery-card">
            <img src="assets/images/competitor_matrix_comparison.png" class="gallery-img" onclick="window.open(this.src)">
            <div class="gallery-body">
              <div class="gallery-title">8. Tier-1 Contractor Capability Benchmark</div>
              <div class="gallery-desc">Multi-dimensional radar/bar comparison: L&T vs Tata Projects vs Afcons vs HCC vs Dilip Buildcon across design depth, fleet, automation, and governance.</div>
            </div>
          </div>

        </div>
      </div>
    </div>

    <!-- TAB 4: INTERACTIVE ENGINEERING LABS -->
    <div class="tab-content" id="tab-calculators">
      <div class="section-card">
        <h2 class="section-title">Interactive Engineering Calculation Labs</h2>
        <p class="section-subtitle">Live in-browser computational engineering engines adhering to CIRIA 108, BS 7121, IS 800, and IRC:87.</p>

        <div class="calc-grid">
          
          <!-- Calc 1: Concrete Lateral Pressure -->
          <div class="calc-card">
            <div class="calc-header">1. Lateral Concrete Pressure Lab (CIRIA 108)</div>
            <div class="form-group">
              <label class="form-label">Total Pour Height H (m):</label>
              <input type="number" id="lab1_h" class="form-control" value="6.0" step="0.5">
            </div>
            <div class="form-group">
              <label class="form-label">Rate of Placement R (m/hr):</label>
              <input type="number" id="lab1_r" class="form-control" value="2.0" step="0.2">
            </div>
            <div class="form-group">
              <label class="form-label">Concrete Temperature T (°C):</label>
              <input type="number" id="lab1_t" class="form-control" value="28" step="1">
            </div>
            <button class="btn btn-primary" onclick="calcLab1()" style="width:100%; margin-top:0.5rem; padding:0.5rem; border-radius:6px; background:#002D62; color:white; border:none; cursor:pointer;">Calculate Lateral Pressure</button>
            <div class="result-box" id="lab1_result">
              <div class="result-title">Governing Design Pressure (P_max)</div>
              <div class="result-val" id="lab1_val">46.1 kN/m²</div>
              <div style="font-size:0.75rem; color:#475569; margin-top:0.35rem;" id="lab1_details">Dywidag 15mm Tie Spacing: 1.0m x 1.95m</div>
            </div>
          </div>

          <!-- Calc 2: Tandem Rigging & Crane Mat GBP -->
          <div class="calc-card">
            <div class="calc-header">2. Tandem Lift & Crane Mat GBP Lab</div>
            <div class="form-group">
              <label class="form-label">Gross Lifted Load (MT):</label>
              <input type="number" id="lab2_w" class="form-control" value="120" step="5">
            </div>
            <div class="form-group">
              <label class="form-label">Sling Angle θ (deg, min 60°):</label>
              <input type="number" id="lab2_theta" class="form-control" value="60" step="5">
            </div>
            <div class="form-group">
              <label class="form-label">Crane Mat Area (m²):</label>
              <input type="number" id="lab2_mat" class="form-control" value="6.0" step="0.5">
            </div>
            <button class="btn btn-primary" onclick="calcLab2()" style="width:100%; margin-top:0.5rem; padding:0.5rem; border-radius:6px; background:#002D62; color:white; border:none; cursor:pointer;">Calculate Rigging & GBP</button>
            <div class="result-box" id="lab2_result">
              <div class="result-title">Peak Ground Bearing Pressure (GBP)</div>
              <div class="result-val" id="lab2_val">221.1 kPa</div>
              <div style="font-size:0.75rem; color:#475569; margin-top:0.35rem;" id="lab2_details">Factored Tension / Sling: 43.7 MT (4 Legs)</div>
            </div>
          </div>

        </div>
      </div>
    </div>

    <!-- TAB 5: LANDMARK MEGA-PROJECTS CASE STUDIES -->
    <div class="tab-content" id="tab-projects">
      <div class="section-card">
        <h2 class="section-title">Landmark Mega-Projects: Temporary Works Engineering Triumphs</h2>
        <p class="section-subtitle">Real-world case studies from India's most complex infrastructure triumphs.</p>

        <div style="display:flex; flex-direction:column; gap:1.5rem; margin-top:1.5rem;">
          
          <div style="background:#F8FAFC; border:1px solid var(--border); border-radius:10px; padding:1.5rem;">
            <h3 style="color:var(--primary); margin-bottom:0.5rem;">1. Mumbai-Ahmedabad High-Speed Rail (MAHSR Bullet Train) – 1000T FSLE</h3>
            <p style="font-size:0.85rem; color:#334155; margin-bottom:0.75rem;"><strong>The Challenge:</strong> Constructing 350+ km of high-speed rail viaduct over agricultural land and urban corridors using 40-meter full-span box girders weighing 975 metric tons.</p>
            <p style="font-size:0.85rem; color:#334155;"><strong>The L&T Solution:</strong> Designed and commissioned the 1000-Ton Full Span Launching Equipment (FSLE) suite: (1) 1000T Straddle Carrier for casting yards, (2) 1000T Multi-Axle Girder Transporter navigating finished viaduct spans, and (3) 1000T Launching Gantry achieving span erection in 24 hours.</p>
          </div>

          <div style="background:#F8FAFC; border:1px solid var(--border); border-radius:10px; padding:1.5rem;">
            <h3 style="color:var(--primary); margin-bottom:0.5rem;">2. Mumbai Trans Harbour Link (MTHL / Atal Setu) – Marine Piling Jetties</h3>
            <p style="font-size:0.85rem; color:#334155; margin-bottom:0.75rem;"><strong>The Challenge:</strong> Building India's longest sea bridge (21.8 km) across ecologically delicate intertidal mudflats with severe 6-meter tides.</p>
            <p style="font-size:0.85rem; color:#334155;"><strong>The Engineering Triumph:</strong> L&T and Tata Projects engineered over 5.5 km of heavy steel piling access jetties carrying 100T crawler cranes and transit mixers, using reverse circulation drilling (RCD) templates and synchronized marine strand jacking.</p>
          </div>

          <div style="background:#F8FAFC; border:1px solid var(--border); border-radius:10px; padding:1.5rem;">
            <h3 style="color:var(--primary); margin-bottom:0.5rem;">3. Chenab Railway Arch Bridge (Afcons Infrastructure) – 359m Gorge Span</h3>
            <p style="font-size:0.85rem; color:#334155; margin-bottom:0.75rem;"><strong>The Challenge:</strong> Constructing the world's highest railway arch bridge over a 359-meter deep gorge in Jammu & Kashmir subject to 100 km/h wind gusts and extreme seismicity.</p>
            <p style="font-size:0.85rem; color:#334155;"><strong>The Afcons Solution:</strong> Engineered custom cable crane systems spanning 915 meters across the gorge with 20-ton payload capacity, synchronizing dual cableways to erect steel arch segments in mid-air with millimeter accuracy.</p>
          </div>

        </div>
      </div>
    </div>

  </div>

  <!-- Scripts -->
  <script>
    // Tab Switching
    document.querySelectorAll('.nav-tab').forEach(tab => {
      tab.addEventListener('click', () => {
        document.querySelectorAll('.nav-tab').forEach(t => t.classList.remove('active'));
        document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
        tab.classList.add('active');
        const target = tab.getAttribute('data-tab');
        document.getElementById(target).classList.add('active');
      });
    });

    // ROLES DATA & EXPLORER ENGINE
    const ROLES = __ROLES_JSON__;
    let readStatus = JSON.parse(localStorage.getItem('lt_tw_roles_read') || '{}');
    let activePillar = 'all';
    let activeRisk = 'all';
    let searchQuery = '';

    const cardsGrid = document.getElementById('cardsGrid');
    const searchInput = document.getElementById('searchInput');
    const resultsCount = document.getElementById('resultsCount');
    const activePillarTitle = document.getElementById('activePillarTitle');
    const totalReadCount = document.getElementById('totalReadCount');

    function updateProgress() {
      const count = Object.values(readStatus).filter(Boolean).length;
      totalReadCount.textContent = count + ' / 500';
    }

    function toggleRead(id) {
      readStatus[id] = !readStatus[id];
      localStorage.setItem('lt_tw_roles_read', JSON.stringify(readStatus));
      updateProgress();
      renderRoles();
    }

    function filterRoles() {
      return ROLES.filter(r => {
        if (activePillar !== 'all' && r.pillar_id !== parseInt(activePillar)) return false;
        if (activeRisk !== 'all' && r.risk_level.toLowerCase() !== activeRisk.toLowerCase()) return false;
        if (searchQuery) {
          const q = searchQuery.toLowerCase();
          const match = r.title.toLowerCase().includes(q) ||
                        r.description.toLowerCase().includes(q) ||
                        r.operational_context.toLowerCase().includes(q) ||
                        r.codes_and_tools.toLowerCase().includes(q);
          if (!match) return false;
        }
        return true;
      });
    }

    function renderRoles() {
      const filtered = filterRoles();
      resultsCount.textContent = 'Showing ' + filtered.length + ' of 500 roles';

      cardsGrid.innerHTML = filtered.map(r => {
        const isRead = !!readStatus[r.id];
        const badgeClass = r.risk_level === 'Critical' ? 'badge-critical' : (r.risk_level === 'Strategic' ? 'badge-strategic' : 'badge-high');
        return `
          <div class="role-card ${isRead ? 'read' : ''}">
            <div class="card-top">
              <div class="card-id-title">
                <input type="checkbox" class="card-check" ${isRead ? 'checked' : ''} onchange="toggleRead(${r.id})">
                <span class="card-id">#${String(r.id).padStart(3, '0')}</span>
                <div class="card-title">${r.title}</div>
              </div>
              <span class="badge ${badgeClass}">${r.risk_level}</span>
            </div>
            <div class="card-desc">${r.description}</div>
            <div class="card-meta-grid">
              <div class="meta-item"><strong>Unit / Context</strong><span>${r.operational_context}</span></div>
              <div class="meta-item"><strong>Codes & Software</strong><span class="code-tag">${r.codes_and_tools}</span></div>
              <div class="meta-item"><strong>Deliverable</strong><span>${r.deliverable}</span></div>
            </div>
          </div>
        `;
      }).join('');
    }

    searchInput.addEventListener('input', (e) => {
      searchQuery = e.target.value.trim();
      renderRoles();
    });

    document.querySelectorAll('.pillar-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.pillar-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        activePillar = btn.getAttribute('data-pillar');
        activePillarTitle.textContent = btn.querySelector('span').textContent;
        renderRoles();
      });
    });

    document.querySelectorAll('#riskFilters .filter-pill').forEach(pill => {
      pill.addEventListener('click', () => {
        document.querySelectorAll('#riskFilters .filter-pill').forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        activeRisk = pill.getAttribute('data-risk');
        renderRoles();
      });
    });

    // Interactive Lab 1: Concrete Pressure
    function calcLab1() {
      const h = parseFloat(document.getElementById('lab1_h').value);
      const r = parseFloat(document.getElementById('lab1_r').value);
      const t = parseFloat(document.getElementById('lab1_t').value);
      const gamma = 25.0;
      const k = Math.pow(36.0 / (t + 16.0), 2);
      const term1 = 1.0 * Math.sqrt(r);
      const remH = Math.max(0, h - term1);
      let p_ciria = gamma * (term1 + 0.30 * k * Math.sqrt(remH));
      p_ciria = Math.min(p_ciria, gamma * h);
      
      document.getElementById('lab1_val').textContent = p_ciria.toFixed(1) + ' kN/m²';
      const maxArea = (90.0 / p_ciria).toFixed(2);
      document.getElementById('lab1_details').textContent = 'Max Dywidag 15mm Tie Area: ' + maxArea + ' m² (SWL = 90 kN)';
    }

    // Interactive Lab 2: Tandem Rigging & GBP
    function calcLab2() {
      const w = parseFloat(document.getElementById('lab2_w').value);
      const theta = parseFloat(document.getElementById('lab2_theta').value);
      const matArea = parseFloat(document.getElementById('lab2_mat').value);
      const daf = 1.20;
      const gross = (w + 6.0) * daf;
      const rad = theta * Math.PI / 180.0;
      const tension = (gross / 4.0) * (1.0 / Math.sin(rad));
      
      const reaction_kn = (110.0 + gross * 0.55) * 0.70 * 9.81;
      const gbp = reaction_kn / matArea;

      document.getElementById('lab2_val').textContent = gbp.toFixed(1) + ' kPa';
      document.getElementById('lab2_details').textContent = 'Factored Tension / Sling: ' + tension.toFixed(1) + ' MT (Gross Lift: ' + gross.toFixed(1) + ' MT)';
    }

    updateProgress();
    renderRoles();
  </script>
</body>
</html>
'''

def build_full_portal():
    with open("roles_500_data.json", "r", encoding="utf-8") as f:
        roles_data = json.load(f)

    roles_json_str = json.dumps(roles_data)
    final_html = HTML_TEMPLATE.replace("__ROLES_JSON__", roles_json_str)

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(final_html)
    print("Master portal index.html built successfully.")

if __name__ == "__main__":
    build_full_portal()
