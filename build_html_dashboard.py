"""
Builds a single-page interactive HTML application (index.html)
embedding all 500 roles and responsibilities with live search,
pillar filtering, progress tracking, and detailed card modals.
"""
import json

def build_html():
    with open("roles_500_data.json", "r", encoding="utf-8") as f:
        roles_data = json.load(f)

    roles_json_str = json.dumps(roles_data)

    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>L&T Temporary Structural Engineering Excellence | 500 Roles & Responsibilities (12-Year Specialist)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    :root {{
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
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.5;
      -webkit-font-smoothing: antialiased;
    }}

    /* Top Navigation Bar */
    header {{
      background: linear-gradient(135deg, var(--primary) 0%, #001A38 100%);
      color: white;
      padding: 1.5rem 2rem;
      border-bottom: 4px solid var(--accent);
      box-shadow: var(--shadow-lg);
      position: sticky;
      top: 0;
      z-index: 100;
    }}

    .header-container {{
      max-width: 1400px;
      margin: 0 auto;
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 1rem;
    }}

    .brand {{
      display: flex;
      align-items: center;
      gap: 1rem;
    }}

    .brand-badge {{
      background: var(--accent);
      color: var(--primary);
      font-weight: 800;
      font-size: 0.9rem;
      padding: 0.25rem 0.6rem;
      border-radius: 4px;
      letter-spacing: 0.5px;
    }}

    .brand-title h1 {{
      font-size: 1.4rem;
      font-weight: 700;
      letter-spacing: -0.3px;
    }}

    .brand-title p {{
      font-size: 0.85rem;
      color: #94A3B8;
    }}

    .header-stats {{
      display: flex;
      gap: 1.5rem;
      align-items: center;
    }}

    .stat-box {{
      text-align: right;
    }}

    .stat-num {{
      font-size: 1.4rem;
      font-weight: 800;
      color: var(--accent);
    }}

    .stat-label {{
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: #CBD5E1;
    }}

    /* Progress Bar */
    .progress-container {{
      background: rgba(255, 255, 255, 0.1);
      border-radius: 9999px;
      height: 8px;
      width: 180px;
      overflow: hidden;
      margin-top: 4px;
    }}

    .progress-bar {{
      background: var(--accent);
      height: 100%;
      width: 0%;
      transition: width 0.3s ease;
    }}

    /* Layout */
    .main-container {{
      max-width: 1400px;
      margin: 2rem auto;
      padding: 0 1.5rem;
      display: grid;
      grid-template-columns: 320px 1fr;
      gap: 2rem;
    }}

    @media (max-width: 1024px) {{
      .main-container {{
        grid-template-columns: 1fr;
      }}
    }}

    /* Sidebar Filters */
    .sidebar {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 1.5rem;
      box-shadow: var(--shadow-sm);
      position: sticky;
      top: 100px;
      max-height: calc(100vh - 120px);
      overflow-y: auto;
    }}

    .sidebar-section {{
      margin-bottom: 1.5rem;
    }}

    .sidebar-title {{
      font-size: 0.85rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: var(--text-muted);
      margin-bottom: 0.75rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .search-input {{
      width: 100%;
      padding: 0.65rem 0.85rem;
      border: 1px solid var(--border-dark);
      border-radius: 8px;
      font-size: 0.9rem;
      font-family: inherit;
      transition: all 0.2s;
      background: #F8FAFC;
    }}

    .search-input:focus {{
      outline: none;
      border-color: var(--primary-light);
      background: #FFFFFF;
      box-shadow: 0 0 0 3px rgba(10, 75, 154, 0.15);
    }}

    .pillar-list {{
      display: flex;
      flex-direction: column;
      gap: 0.4rem;
    }}

    .pillar-btn {{
      background: transparent;
      border: 1px solid transparent;
      padding: 0.5rem 0.75rem;
      border-radius: 6px;
      text-align: left;
      font-size: 0.85rem;
      font-weight: 500;
      color: var(--text);
      cursor: pointer;
      display: flex;
      justify-content: space-between;
      align-items: center;
      transition: all 0.15s;
    }}

    .pillar-btn:hover {{
      background: #F1F5F9;
      border-color: var(--border);
    }}

    .pillar-btn.active {{
      background: #EFF6FF;
      color: var(--primary);
      font-weight: 600;
      border-color: #BFDBFE;
    }}

    .pillar-badge {{
      font-size: 0.75rem;
      padding: 0.15rem 0.45rem;
      border-radius: 9999px;
      background: #E2E8F0;
      color: #475569;
    }}

    .pillar-btn.active .pillar-badge {{
      background: var(--primary);
      color: white;
    }}

    .filter-pills {{
      display: flex;
      flex-wrap: wrap;
      gap: 0.4rem;
    }}

    .filter-pill {{
      padding: 0.35rem 0.65rem;
      border-radius: 9999px;
      font-size: 0.75rem;
      font-weight: 600;
      border: 1px solid var(--border-dark);
      background: white;
      cursor: pointer;
      transition: all 0.15s;
    }}

    .filter-pill:hover {{
      border-color: var(--text-muted);
    }}

    .filter-pill.active {{
      background: var(--primary);
      color: white;
      border-color: var(--primary);
    }}

    /* Content Area */
    .content-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1rem;
      flex-wrap: wrap;
      gap: 1rem;
    }}

    .content-title h2 {{
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--primary);
    }}

    .content-title p {{
      font-size: 0.85rem;
      color: var(--text-muted);
    }}

    .actions-bar {{
      display: flex;
      gap: 0.5rem;
    }}

    .btn {{
      padding: 0.45rem 0.85rem;
      border-radius: 6px;
      font-size: 0.8rem;
      font-weight: 600;
      border: 1px solid var(--border-dark);
      background: white;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.4rem;
      transition: all 0.15s;
    }}

    .btn:hover {{
      background: #F8FAFC;
      border-color: #94A3B8;
    }}

    .btn-primary {{
      background: var(--primary);
      color: white;
      border-color: var(--primary);
    }}

    .btn-primary:hover {{
      background: var(--primary-light);
    }}

    /* Cards Grid */
    .cards-grid {{
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }}

    .role-card {{
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 1.25rem;
      box-shadow: var(--shadow-sm);
      transition: all 0.2s ease;
      position: relative;
    }}

    .role-card:hover {{
      border-color: #94A3B8;
      box-shadow: var(--shadow);
    }}

    .role-card.read {{
      border-left: 5px solid #10B981;
      background: #FDFDFE;
    }}

    .card-top {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 0.6rem;
      gap: 1rem;
    }}

    .card-id-title {{
      display: flex;
      align-items: flex-start;
      gap: 0.75rem;
    }}

    .card-check {{
      margin-top: 0.25rem;
      width: 18px;
      height: 18px;
      cursor: pointer;
      accent-color: #10B981;
    }}

    .card-id {{
      font-family: 'JetBrains Mono', monospace;
      font-weight: 700;
      font-size: 0.8rem;
      background: #F1F5F9;
      color: #475569;
      padding: 0.15rem 0.45rem;
      border-radius: 4px;
      border: 1px solid #E2E8F0;
      white-space: nowrap;
    }}

    .card-title {{
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--primary);
      line-height: 1.35;
    }}

    .badge {{
      font-size: 0.7rem;
      font-weight: 700;
      padding: 0.2rem 0.5rem;
      border-radius: 9999px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      white-space: nowrap;
    }}

    .badge-critical {{
      background: #FEE2E2;
      color: #991B1B;
      border: 1px solid #FCA5A5;
    }}

    .badge-strategic {{
      background: #EDE9FE;
      color: #5B21B6;
      border: 1px solid #C4B5FD;
    }}

    .badge-high {{
      background: #FEF3C7;
      color: #92400E;
      border: 1px solid #FCD34D;
    }}

    .card-desc {{
      font-size: 0.9rem;
      color: #334155;
      margin-bottom: 0.85rem;
      padding-left: 2.1rem;
    }}

    .card-meta-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 0.6rem;
      background: #F8FAFC;
      border-radius: 8px;
      padding: 0.75rem 1rem;
      margin-left: 2.1rem;
      font-size: 0.8rem;
      border: 1px solid #F1F5F9;
    }}

    .meta-item strong {{
      color: #475569;
      display: block;
      font-size: 0.7rem;
      text-transform: uppercase;
      letter-spacing: 0.4px;
    }}

    .meta-item span {{
      color: #1E293B;
      font-weight: 500;
    }}

    .code-tag {{
      font-family: 'JetBrains Mono', monospace;
      color: var(--teal);
    }}

    .empty-state {{
      text-align: center;
      padding: 4rem 2rem;
      background: white;
      border-radius: 12px;
      border: 1px dashed var(--border-dark);
    }}

    .empty-state h3 {{
      font-size: 1.1rem;
      color: var(--text-muted);
      margin-bottom: 0.5rem;
    }}
  </style>
</head>
<body>

  <!-- Top Header -->
  <header>
    <div class="header-container">
      <div class="brand">
        <span class="brand-badge">L&T CONSTRUCTION</span>
        <div class="brand-title">
          <h1>Temporary Structural Engineering Excellence</h1>
          <p>EDRC • CMPD • FED • SE&HLD | 500 Roles & Responsibilities (12-Year Senior Engineering Manager / Chief Specialist)</p>
        </div>
      </div>
      <div class="header-stats">
        <div class="stat-box">
          <div class="stat-num" id="totalReadCount">0 / 500</div>
          <div class="stat-label">Roles Understood</div>
          <div class="progress-container">
            <div class="progress-bar" id="progressBar"></div>
          </div>
        </div>
      </div>
    </div>
  </header>

  <!-- Main Container -->
  <div class="main-container">
    
    <!-- Sidebar Filters -->
    <aside class="sidebar">
      <div class="sidebar-section">
        <div class="sidebar-title">Instant Search</div>
        <input type="text" id="searchInput" class="search-input" placeholder="Search keywords, codes, tools...">
      </div>

      <div class="sidebar-section">
        <div class="sidebar-title">
          <span>Engineering Pillars</span>
          <span style="cursor:pointer; color: var(--primary);" id="resetPillars">All</span>
        </div>
        <div class="pillar-list" id="pillarList">
          <button class="pillar-btn active" data-pillar="all">
            <span>All 10 Pillars</span>
            <span class="pillar-badge">500</span>
          </button>
          <button class="pillar-btn" data-pillar="1">
            <span>1. Governance & Policy</span>
            <span class="pillar-badge">50</span>
          </button>
          <button class="pillar-btn" data-pillar="2">
            <span>2. CMS & Erection Schemes</span>
            <span class="pillar-badge">50</span>
          </button>
          <button class="pillar-btn" data-pillar="3">
            <span>3. FSLE & Launching Gantries</span>
            <span class="pillar-badge">50</span>
          </button>
          <button class="pillar-btn" data-pillar="4">
            <span>4. Deep Excavation & Marine</span>
            <span class="pillar-badge">50</span>
          </button>
          <button class="pillar-btn" data-pillar="5">
            <span>5. Advanced Non-Linear FEA</span>
            <span class="pillar-badge">50</span>
          </button>
          <button class="pillar-btn" data-pillar="6">
            <span>6. Digital, BIM 4D & IoT SHM</span>
            <span class="pillar-badge">50</span>
          </button>
          <button class="pillar-btn" data-pillar="7">
            <span>7. BS 5975, PTL/PTS & QA</span>
            <span class="pillar-badge">50</span>
          </button>
          <button class="pillar-btn" data-pillar="8">
            <span>8. Forensic & Disaster Risk</span>
            <span class="pillar-badge">50</span>
          </button>
          <button class="pillar-btn" data-pillar="9">
            <span>9. Client & Proof Check</span>
            <span class="pillar-badge">50</span>
          </button>
          <button class="pillar-btn" data-pillar="10">
            <span>10. Pre-Bid & Mentorship</span>
            <span class="pillar-badge">50</span>
          </button>
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

      <div class="sidebar-section">
        <div class="sidebar-title">Study Status</div>
        <div class="filter-pills" id="statusFilters">
          <button class="filter-pill active" data-status="all">All</button>
          <button class="filter-pill" data-status="read">Understood</button>
          <button class="filter-pill" data-status="unread">To Review</button>
        </div>
      </div>
    </aside>

    <!-- Main Content Area -->
    <main>
      <div class="content-header">
        <div class="content-title">
          <h2 id="activePillarTitle">All 10 Engineering Pillars (500 Roles & Responsibilities)</h2>
          <p id="resultsCount">Showing 500 of 500 roles</p>
        </div>
        <div class="actions-bar">
          <button class="btn" id="markAllReadBtn">Mark Filtered as Read</button>
          <button class="btn" id="clearAllReadBtn">Reset Progress</button>
          <button class="btn btn-primary" onclick="window.print()">Print / PDF</button>
        </div>
      </div>

      <!-- Cards Grid -->
      <div class="cards-grid" id="cardsGrid"></div>
    </main>
  </div>

  <!-- Embed Roles Data -->
  <script>
    const ROLES = {roles_json_str};
    let readStatus = JSON.parse(localStorage.getItem('lt_tw_roles_read') || '{{}}');

    let activePillar = 'all';
    let activeRisk = 'all';
    let activeStatus = 'all';
    let searchQuery = '';

    const cardsGrid = document.getElementById('cardsGrid');
    const searchInput = document.getElementById('searchInput');
    const resultsCount = document.getElementById('resultsCount');
    const activePillarTitle = document.getElementById('activePillarTitle');
    const totalReadCount = document.getElementById('totalReadCount');
    const progressBar = document.getElementById('progressBar');

    function updateProgress() {{
      const readCount = Object.values(readStatus).filter(Boolean).length;
      totalReadCount.textContent = `${{readCount}} / 500`;
      const pct = Math.round((readCount / 500) * 100);
      progressBar.style.width = `${{pct}}%`;
    }}

    function toggleRead(id) {{
      readStatus[id] = !readStatus[id];
      localStorage.setItem('lt_tw_roles_read', JSON.stringify(readStatus));
      updateProgress();
      renderRoles();
    }}

    function filterRoles() {{
      return ROLES.filter(r => {{
        // Pillar filter
        if (activePillar !== 'all' && r.pillar_id !== parseInt(activePillar)) return false;

        // Risk filter
        if (activeRisk !== 'all' && r.risk_level.toLowerCase() !== activeRisk.toLowerCase()) return false;

        // Status filter
        const isRead = !!readStatus[r.id];
        if (activeStatus === 'read' && !isRead) return false;
        if (activeStatus === 'unread' && isRead) return false;

        // Search query
        if (searchQuery) {{
          const q = searchQuery.toLowerCase();
          const matchTitle = r.title.toLowerCase().includes(q);
          const matchDesc = r.description.toLowerCase().includes(q);
          const matchContext = r.operational_context.toLowerCase().includes(q);
          const matchTools = r.codes_and_tools.toLowerCase().includes(q);
          const matchDeliv = r.deliverable.toLowerCase().includes(q);
          if (!matchTitle && !matchDesc && !matchContext && !matchTools && !matchDeliv) return false;
        }}

        return true;
      }});
    }}

    function renderRoles() {{
      const filtered = filterRoles();
      resultsCount.textContent = `Showing ${{filtered.length}} of 500 roles`;

      if (filtered.length === 0) {{
        cardsGrid.innerHTML = `
          <div class="empty-state">
            <h3>No matching roles found</h3>
            <p>Try modifying your search criteria or resetting filters.</p>
          </div>
        `;
        return;
      }}

      cardsGrid.innerHTML = filtered.map(r => {{
        const isRead = !!readStatus[r.id];
        const badgeClass = r.risk_level === 'Critical' ? 'badge-critical' : (r.risk_level === 'Strategic' ? 'badge-strategic' : 'badge-high');
        
        return `
          <div class="role-card ${{isRead ? 'read' : ''}}">
            <div class="card-top">
              <div class="card-id-title">
                <input type="checkbox" class="card-check" ${{isRead ? 'checked' : ''}} onchange="toggleRead(${{r.id}})">
                <span class="card-id">#${{String(r.id).padStart(3, '0')}}</span>
                <div class="card-title">${{r.title}}</div>
              </div>
              <span class="badge ${{badgeClass}}">${{r.risk_level}}</span>
            </div>
            <div class="card-desc">${{r.description}}</div>
            <div class="card-meta-grid">
              <div class="meta-item">
                <strong>Operational Context / Unit</strong>
                <span>${{r.operational_context}}</span>
              </div>
              <div class="meta-item">
                <strong>Governing Codes & Software</strong>
                <span class="code-tag">${{r.codes_and_tools}}</span>
              </div>
              <div class="meta-item">
                <strong>Mandatory Deliverable</strong>
                <span>${{r.deliverable}}</span>
              </div>
            </div>
          </div>
        `;
      }}).join('');
    }}

    // Event Listeners
    searchInput.addEventListener('input', (e) => {{
      searchQuery = e.target.value.trim();
      renderRoles();
    }});

    // Pillar Buttons
    document.querySelectorAll('.pillar-btn').forEach(btn => {{
      btn.addEventListener('click', () => {{
        document.querySelectorAll('.pillar-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        activePillar = btn.getAttribute('data-pillar');
        activePillarTitle.textContent = btn.querySelector('span').textContent;
        renderRoles();
      }});
    }});

    // Risk Filters
    document.querySelectorAll('#riskFilters .filter-pill').forEach(pill => {{
      pill.addEventListener('click', () => {{
        document.querySelectorAll('#riskFilters .filter-pill').forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        activeRisk = pill.getAttribute('data-risk');
        renderRoles();
      }});
    }});

    // Status Filters
    document.querySelectorAll('#statusFilters .filter-pill').forEach(pill => {{
      pill.addEventListener('click', () => {{
        document.querySelectorAll('#statusFilters .filter-pill').forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        activeStatus = pill.getAttribute('data-status');
        renderRoles();
      }});
    }});

    // Bulk actions
    document.getElementById('markAllReadBtn').addEventListener('click', () => {{
      const filtered = filterRoles();
      filtered.forEach(r => {{ readStatus[r.id] = true; }});
      localStorage.setItem('lt_tw_roles_read', JSON.stringify(readStatus));
      updateProgress();
      renderRoles();
    }});

    document.getElementById('clearAllReadBtn').addEventListener('click', () => {{
      if (confirm('Reset all reading progress?')) {{
        readStatus = {{}};
        localStorage.removeItem('lt_tw_roles_read');
        updateProgress();
        renderRoles();
      }}
    }});

    // Initial setup
    updateProgress();
    renderRoles();
  </script>
</body>
</html>
'''
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("index.html built successfully.")

if __name__ == "__main__":
    build_html()
