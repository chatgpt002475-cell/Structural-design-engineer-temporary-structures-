"""
Upgrades index.html into a multi-tab Master Engineering Web Portal:
- Tab 1: 500 Roles & Responsibilities Explorer (with search, filter, check-off)
- Tab 2: Competitor Landscape & Real Working Nature (L&T vs Tata Projects vs Afcons vs HCC vs DBL)
- Tab 3: Visual Atlas of Temporary Structures (8 High-Res Schematics with Deep Technical Breakdown)
- Tab 4: Interactive Engineering Calculation Labs (Live in-browser calculators)
- Tab 5: Landmark Mega-Projects Case Studies (MAHSR, MTHL, Chenab, Metro D-Walls)
- Tab 6: 🏆 PIE Awards AI Innovation Showcase (6 Breakthrough Multi-Crore AI Proposals)
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
      padding: 0.75rem 1.15rem;
      color: #CBD5E1;
      font-size: 0.82rem;
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

    .portal-container {
      max-width: 1440px;
      margin: 2rem auto;
      padding: 0 1.5rem;
    }

    .tab-content { display: none; }
    .tab-content.active { display: block; }

    /* Tab 1 Layout */
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

    /* Cards */
    .cards-grid { display: flex; flex-direction: column; gap: 0.85rem; }
    .role-card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 1.15rem;
      box-shadow: var(--shadow-sm);
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

    /* Section Card */
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
    .gallery-desc { font-size: 0.85rem; color: #475569; }

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

    /* PIE Awards Grid */
    .pie-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(380px, 1fr));
      gap: 1.5rem;
      margin-top: 1.5rem;
    }
    .pie-card {
      background: white;
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 1.5rem;
      box-shadow: var(--shadow-sm);
      border-top: 5px solid var(--accent);
      transition: all 0.2s;
    }
    .pie-card:hover { box-shadow: var(--shadow-lg); border-color: var(--primary-light); }
    .pie-tag {
      font-size: 0.7rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.5px;
      padding: 0.2rem 0.5rem; border-radius: 4px; background: #EFF6FF; color: var(--primary); display: inline-block; margin-bottom: 0.5rem;
    }
    .pie-savings {
      background: #ECFDF5; color: #047857; font-weight: 800; font-size: 0.8rem; padding: 0.25rem 0.6rem; border-radius: 4px; float: right; border: 1px solid #A7F3D0;
    }
  </style>
</head>
<body>

  <header>
    <div class="header-top">
      <div class="brand">
        <span class="brand-badge">L&T CONSTRUCTION</span>
        <div class="brand-title">
          <h1>Temporary Structural Engineering Excellence Portal</h1>
          <p>EDRC • CMPD • FED • SE&HLD | Roles, Competitor Intelligence, Visual Atlas & PIE Awards AI Showcase</p>
        </div>
      </div>
      <div>
        <a href="L_and_T_PIE_Awards_AI_Innovation_Master_Dossier.docx" class="brand-badge" style="text-decoration:none; background: #FFBF00; color: #002D62; font-size: 0.8rem; padding: 0.4rem 0.8rem; font-weight:800;">
          🏆 Download PIE Awards Dossier (.docx)
        </a>
      </div>
    </div>
    
    <div class="nav-tabs">
      <div class="nav-tab active" data-tab="tab-roles">1. 500 Roles & Responsibilities Explorer</div>
      <div class="nav-tab" data-tab="tab-competitors">2. Competitor Working Nature (L&T vs Tata vs Afcons)</div>
      <div class="nav-tab" data-tab="tab-gallery">3. Engineering Visual Atlas (8 High-Res Schematics)</div>
      <div class="nav-tab" data-tab="tab-calculators">4. Interactive Engineering Labs</div>
      <div class="nav-tab" data-tab="tab-projects">5. Landmark Mega-Projects Case Studies</div>
      <div class="nav-tab" data-tab="tab-pie" style="color:var(--accent); font-weight:800;">6. 🏆 PIE Awards AI Innovation Showcase</div>
    </div>
  </header>

  <div class="portal-container">

    <!-- TAB 1: 500 ROLES EXPLORER -->
    <div class="tab-content active" id="tab-roles">
      <div class="roles-layout">
        <aside class="sidebar">
          <div class="sidebar-section">
            <div class="sidebar-title">Instant Search</div>
            <input type="text" id="searchInput" class="search-input" placeholder="Search keywords, codes, tools...">
          </div>

          <div class="sidebar-section">
            <div class="sidebar-title">Engineering Pillars</div>
            <div class="pillar-list">
              <button class="pillar-btn active" data-pillar="all"><span>All 10 Pillars</span><span class="pillar-badge">500</span></button>
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

    <!-- TAB 2: COMPETITOR LANDSCAPE -->
    <div class="tab-content" id="tab-competitors">
      <div class="section-card">
        <h2 class="section-title">Tier-1 Contractor Comparative Analysis</h2>
        <p class="section-subtitle">Real operational intelligence across India's largest infrastructure conglomerates: Larsen & Toubro vs Tata Projects vs Afcons vs HCC vs Dilip Buildcon.</p>
        
        <div style="text-align:center; margin-bottom: 2rem;">
          <img src="assets/images/competitor_matrix_comparison.png" alt="Competitor Comparison Chart" style="max-width:100%; border-radius:8px; border:1px solid var(--border);">
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
    </div>

    <!-- TAB 3: VISUAL ATLAS -->
    <div class="tab-content" id="tab-gallery">
      <div class="section-card">
        <h2 class="section-title">Engineering Visual Atlas: Technical Schematics & Mechanics</h2>
        <p class="section-subtitle">High-resolution, engineering-grade illustrations of the core temporary structural systems governed by Senior Engineering Managers.</p>

        <div class="gallery-grid">
          <div class="gallery-card">
            <img src="assets/images/launching_gantry_schematic.png" class="gallery-img" onclick="window.open(this.src)">
            <div class="gallery-body">
              <div class="gallery-title">1. Overhead Launching Gantry (LG 1200T)</div>
              <div class="gallery-desc">Support reactions, front launching nose cantilever deflection (L/400), and motorized winch trolley load transfer.</div>
            </div>
          </div>
          <div class="gallery-card">
            <img src="assets/images/form_traveler_schematic.png" class="gallery-img" onclick="window.open(this.src)">
            <div class="gallery-body">
              <div class="gallery-title">2. Balanced Cantilever Form Traveler (FT 250T)</div>
              <div class="gallery-desc">Front pivot fulcrum shoe and rear hold-down Dywidag 32mm tie bars clamped to cured deck (FOS &gt;= 2.0).</div>
            </div>
          </div>
          <div class="gallery-card">
            <img src="assets/images/deep_excavation_dwall_strutting.png" class="gallery-img" onclick="window.open(this.src)">
            <div class="gallery-body">
              <div class="gallery-title">3. Deep Station Excavation D-Wall Strutting</div>
              <div class="gallery-desc">Preloaded pipe struts (813mm-1016mm dia), waling beams, hydraulic preloading (2500 kN), and settlement control (&lt;= 12mm).</div>
            </div>
          </div>
          <div class="gallery-card">
            <img src="assets/images/cuplock_staging_tower_mechanics.png" class="gallery-img" onclick="window.open(this.src)">
            <div class="gallery-body">
              <div class="gallery-title">4. Cup-lock & Ring-lock Staging Tower Mechanics</div>
              <div class="gallery-desc">Buckling effective lengths (k=1.0 braced vs k=2.0 sway), jack spindle extension limits (&lt;= 300 mm).</div>
            </div>
          </div>
          <div class="gallery-card">
            <img src="assets/images/tandem_crane_rigging_geometry.png" class="gallery-img" onclick="window.open(this.src)">
            <div class="gallery-body">
              <div class="gallery-title">5. Heavy Tandem Crane Rigging & Outrigger Mats</div>
              <div class="gallery-desc">Sling angle multiplier (1/sin theta, theta &gt;= 60°), CG eccentricity, and crane mat ground bearing pressure.</div>
            </div>
          </div>
          <div class="gallery-card">
            <img src="assets/images/concrete_lateral_pressure_curves.png" class="gallery-img" onclick="window.open(this.src)">
            <div class="gallery-body">
              <div class="gallery-title">6. Concrete Lateral Pressure Depth Envelopes</div>
              <div class="gallery-desc">CIRIA 108 vs DIN 18218 vs ACI 347R depth profiles, and winter cold weather surge mechanics (+79% spike).</div>
            </div>
          </div>
          <div class="gallery-card">
            <img src="assets/images/iot_shm_telemetry_architecture.png" class="gallery-img" onclick="window.open(this.src)">
            <div class="gallery-body">
              <div class="gallery-title">7. IoT Structural Health Monitoring Architecture</div>
              <div class="gallery-desc">Vibrating wire strain gauges, tiltmeters, LoRaWAN/4G edge gateway, InfluxDB, and automated SMS alarms.</div>
            </div>
          </div>
          <div class="gallery-card">
            <img src="assets/images/competitor_matrix_comparison.png" class="gallery-img" onclick="window.open(this.src)">
            <div class="gallery-body">
              <div class="gallery-title">8. Tier-1 Contractor Capability Benchmark</div>
              <div class="gallery-desc">Multi-dimensional radar/bar comparison: L&T vs Tata Projects vs Afcons vs HCC vs Dilip Buildcon.</div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 4: INTERACTIVE LABS -->
    <div class="tab-content" id="tab-calculators">
      <div class="section-card">
        <h2 class="section-title">Interactive Engineering Calculation Labs</h2>
        <div class="calc-grid">
          <div class="calc-card">
            <div class="calc-header">1. Lateral Concrete Pressure Lab (CIRIA 108)</div>
            <div class="form-group"><label class="form-label">Total Pour Height H (m):</label><input type="number" id="lab1_h" class="form-control" value="6.0" step="0.5"></div>
            <div class="form-group"><label class="form-label">Rate of Placement R (m/hr):</label><input type="number" id="lab1_r" class="form-control" value="2.0" step="0.2"></div>
            <div class="form-group"><label class="form-label">Concrete Temperature T (°C):</label><input type="number" id="lab1_t" class="form-control" value="28" step="1"></div>
            <button class="btn btn-primary" onclick="calcLab1()" style="width:100%; margin-top:0.5rem; padding:0.5rem; border-radius:6px; background:#002D62; color:white; border:none; cursor:pointer;">Calculate Lateral Pressure</button>
            <div class="result-box">
              <div class="result-title">Governing Design Pressure (P_max)</div>
              <div class="result-val" id="lab1_val">46.1 kN/m²</div>
              <div style="font-size:0.75rem; color:#475569; margin-top:0.35rem;" id="lab1_details">Dywidag 15mm Tie Spacing: 1.0m x 1.95m</div>
            </div>
          </div>
          <div class="calc-card">
            <div class="calc-header">2. Tandem Lift & Crane Mat GBP Lab</div>
            <div class="form-group"><label class="form-label">Gross Lifted Load (MT):</label><input type="number" id="lab2_w" class="form-control" value="120" step="5"></div>
            <div class="form-group"><label class="form-label">Sling Angle θ (deg, min 60°):</label><input type="number" id="lab2_theta" class="form-control" value="60" step="5"></div>
            <div class="form-group"><label class="form-label">Crane Mat Area (m²):</label><input type="number" id="lab2_mat" class="form-control" value="6.0" step="0.5"></div>
            <button class="btn btn-primary" onclick="calcLab2()" style="width:100%; margin-top:0.5rem; padding:0.5rem; border-radius:6px; background:#002D62; color:white; border:none; cursor:pointer;">Calculate Rigging & GBP</button>
            <div class="result-box">
              <div class="result-title">Peak Ground Bearing Pressure (GBP)</div>
              <div class="result-val" id="lab2_val">221.1 kPa</div>
              <div style="font-size:0.75rem; color:#475569; margin-top:0.35rem;" id="lab2_details">Factored Tension / Sling: 43.7 MT (4 Legs)</div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 5: MEGA-PROJECTS CASE STUDIES -->
    <div class="tab-content" id="tab-projects">
      <div class="section-card">
        <h2 class="section-title">Landmark Mega-Projects: Temporary Works Engineering Triumphs</h2>
        <div style="display:flex; flex-direction:column; gap:1.5rem; margin-top:1.5rem;">
          <div style="background:#F8FAFC; border:1px solid var(--border); border-radius:10px; padding:1.5rem;">
            <h3 style="color:var(--primary); margin-bottom:0.5rem;">1. Mumbai-Ahmedabad High-Speed Rail (MAHSR Bullet Train) – 1000T FSLE</h3>
            <p style="font-size:0.85rem; color:#334155;">L&T designed the 1000-Ton Full Span Launching Equipment (FSLE) suite: 1000T Straddle Carrier, Transporter, and Launcher achieving span erection in 24 hours.</p>
          </div>
          <div style="background:#F8FAFC; border:1px solid var(--border); border-radius:10px; padding:1.5rem;">
            <h3 style="color:var(--primary); margin-bottom:0.5rem;">2. Mumbai Trans Harbour Link (MTHL / Atal Setu) – Marine Piling Jetties</h3>
            <p style="font-size:0.85rem; color:#334155;">Engineered over 5.5 km of heavy steel piling access jetties carrying 100T crawler cranes and transit mixers in severe 6-meter tides.</p>
          </div>
          <div style="background:#F8FAFC; border:1px solid var(--border); border-radius:10px; padding:1.5rem;">
            <h3 style="color:var(--primary); margin-bottom:0.5rem;">3. Chenab Railway Arch Bridge (Afcons Infrastructure) – 359m Gorge Span</h3>
            <p style="font-size:0.85rem; color:#334155;">Engineered custom cable crane systems spanning 915 meters with 20-ton payload capacity, synchronizing dual cableways to erect steel arch segments in mid-air.</p>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 6: PIE AWARDS AI INNOVATION SHOWCASE -->
    <div class="tab-content" id="tab-pie">
      <div class="section-card">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:1rem;">
          <div>
            <h2 class="section-title" style="margin-bottom:0.25rem;">🏆 L&T PIE Awards: Breakthrough AI Innovation Proposals</h2>
            <p class="section-subtitle" style="margin-bottom:0;">6 High-Impact AI Engineering Inventions Engineered to Win Chairman's & PIE Awards</p>
          </div>
          <a href="L_and_T_PIE_Awards_AI_Innovation_Master_Dossier.docx" class="brand-badge" style="text-decoration:none; background:#002D62; color:#FFBF00; border:1px solid #FFBF00; padding:0.5rem 1rem;">
            📥 Download Jury Submission Dossier (.docx)
          </a>
        </div>

        <div style="text-align:center; margin: 2rem 0;">
          <img src="assets/images/ai_pie_awards_innovation_ecosystem.png" alt="PIE Awards Ecosystem" style="max-width:100%; border-radius:10px; border:1px solid var(--border); box-shadow:var(--shadow);">
        </div>

        <div class="pie-grid">
          
          <!-- PIE 1 -->
          <div class="pie-card">
            <span class="pie-savings">Saves ₹4.8 Cr</span>
            <span class="pie-tag">Zero Harm / Computer Vision</span>
            <h3 style="color:var(--primary); font-size:1.15rem; margin:0.5rem 0;">1. VisionScaffold AI™</h3>
            <p style="font-size:0.85rem; color:#334155; margin-bottom:0.75rem;"><strong>Autonomous Drone & Edge Vision for Pre-Pour Staging Audits:</strong> Scans 25m staging towers in 90 seconds using YOLOv10 and stereo depth. Measures spindle extensions to ±2mm, detects unseated cup wedges, and verifies acoustic hammer-strike frequency (>2.8 kHz = locked).</p>
            <div style="font-size:0.75rem; color:var(--teal); font-family:'JetBrains Mono', monospace;">Patent: Optical-Acoustic Joint Seating Verification</div>
          </div>

          <!-- PIE 2 -->
          <div class="pie-card">
            <span class="pie-savings">Saves ₹12.5 Cr</span>
            <span class="pie-tag">Physics-Informed ML / Heavy Plant</span>
            <h3 style="color:var(--primary); font-size:1.15rem; margin:0.5rem 0;">2. NeuroLaunch-Twin™</h3>
            <p style="font-size:0.85rem; color:#334155; margin-bottom:0.75rem;"><strong>Physics-Informed Neural Network (PINN) for Launching Gantries:</strong> Embeds Timoshenko beam mechanics and P-Delta equations into deep learning. Predicts cantilever nose sag and support leg anomalies 45s ahead, auto-throttling hydraulic advance to prevent derailment.</p>
            <div style="font-size:0.75rem; color:var(--teal); font-family:'JetBrains Mono', monospace;">Patent: Closed-Loop Real-Time Gantry Kinematic Control</div>
          </div>

          <!-- PIE 3 -->
          <div class="pie-card">
            <span class="pie-savings">Saves ₹14.2 Cr</span>
            <span class="pie-tag">Geotechnical / Deep Excavation</span>
            <h3 style="color:var(--primary); font-size:1.15rem; margin:0.5rem 0;">3. StrutGuard AI™</h3>
            <p style="font-size:0.85rem; color:#334155; margin-bottom:0.75rem;"><strong>Predictive Deep Excavation Thermal-Soil Intelligence:</strong> Surrogate model trained on 10,000 PLAXIS 3D runs. Predicts summer thermal thrust surges (+450 kN), modulating hydraulic pressure relief jacks. Saves 1,800 MT steel by optimizing strut wall thickness.</p>
            <div style="font-size:0.75rem; color:var(--teal); font-family:'JetBrains Mono', monospace;">Patent: Autonomous Thermal-Geotechnical Load Regulation</div>
          </div>

          <!-- PIE 4 -->
          <div class="pie-card">
            <span class="pie-savings">Saves ₹8.5 Cr</span>
            <span class="pie-tag">Generative Design / Automation</span>
            <h3 style="color:var(--primary); font-size:1.15rem; margin:0.5rem 0;">4. GenerativeFalsework-X™</h3>
            <p style="font-size:0.85rem; color:#334155; margin-bottom:0.75rem;"><strong>Multi-Objective Generative AI for Parametric Falsework:</strong> Graph Neural Networks ingest 3D IFC bridge geometry, synthesizing thousands of valid staging grids. Simultaneously minimizes steel tonnage (22% reduction) and auto-generates Tekla CNC cutting plans in 4 hours.</p>
            <div style="font-size:0.75rem; color:var(--teal); font-family:'JetBrains Mono', monospace;">Patent: Generative GNN Synthesis for Structural Falsework</div>
          </div>

          <!-- PIE 5 -->
          <div class="pie-card">
            <span class="pie-savings">Saves ₹3.2 Cr</span>
            <span class="pie-tag">Special Bridges / Deep Learning</span>
            <h3 style="color:var(--primary); font-size:1.15rem; margin:0.5rem 0;">5. CamberPredict-AI™</h3>
            <p style="font-size:0.85rem; color:#334155; margin-bottom:0.75rem;"><strong>Bayesian Deep Learning for Balanced Cantilever Bridges:</strong> Fuses IRC:112 creep models with wireless concrete maturity meters and robotic total stations, self-calibrating camber profiles after every pour. Achieves ±3mm closure accuracy, zero grinding.</p>
            <div style="font-size:0.75rem; color:var(--teal); font-family:'JetBrains Mono', monospace;">Patent: Self-Calibrating Bayesian Camber Regulation</div>
          </div>

          <!-- PIE 6 -->
          <div class="pie-card">
            <span class="pie-savings">Zero Railway Overruns</span>
            <span class="pie-tag">Spatial LiDAR / Heavy Rigging</span>
            <h3 style="color:var(--primary); font-size:1.15rem; margin:0.5rem 0;">6. CraneGuard Tandem-AI™</h3>
            <p style="font-size:0.85rem; color:#334155; margin-bottom:0.75rem;"><strong>Spatial 3D LiDAR & Vision for Zero-Blindspot Tandem Lifts:</strong> Fuses dual-crane point clouds, tracking CG eccentricity and sling angles (theta &gt;= 60°). Provides in-cabin Augmented Reality HUD, preventing boom collapse during tight railway mega-blocks.</p>
            <div style="font-size:0.75rem; color:var(--teal); font-family:'JetBrains Mono', monospace;">Patent: Synchronized Tandem Crane Load Sharing HUD</div>
          </div>

        </div>
      </div>
    </div>

  </div>

  <script>
    document.querySelectorAll('.nav-tab').forEach(tab => {
      tab.addEventListener('click', () => {
        document.querySelectorAll('.nav-tab').forEach(t => t.classList.remove('active'));
        document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
        tab.classList.add('active');
        const target = tab.getAttribute('data-tab');
        document.getElementById(target).classList.add('active');
      });
    });

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
    print("Master portal index.html with PIE Awards Tab built successfully.")

if __name__ == "__main__":
    build_full_portal()
