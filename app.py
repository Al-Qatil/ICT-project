import streamlit as st
import math

# ─────────────────────────────────────────────
#  PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Mech Converter | Muhammad Bin Akrma",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
#  CUSTOM CSS  — Professional Light Theme
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=DM+Sans:wght@400;500;700&family=JetBrains+Mono:wght@400;500&display=swap');

:root {
    --bg:           #f0f4f8;
    --surface:      #ffffff;
    --border:       #dde3ec;
    --border-soft:  #eaeef4;
    --accent:       #1a56db;
    --accent-light: #e8f0fe;
    --gold:         #d97706;
    --gold-light:   #fef3c7;
    --green:        #059669;
    --green-light:  #d1fae5;
    --text:         #1e293b;
    --muted:        #64748b;
    --shadow-sm:    0 1px 3px rgba(0,0,0,.08), 0 1px 2px rgba(0,0,0,.05);
    --shadow-md:    0 4px 16px rgba(0,0,0,.08), 0 2px 6px rgba(0,0,0,.05);
    --radius:       14px;
    --radius-sm:    8px;
}

html, body, .stApp {
    background: var(--bg) !important;
    font-family: 'Inter', sans-serif !important;
    color: var(--text) !important;
}

.stApp {
    background-image:
        radial-gradient(circle at 15% 10%, rgba(26,86,219,.07) 0%, transparent 45%),
        radial-gradient(circle at 85% 85%, rgba(14,165,233,.06) 0%, transparent 45%) !important;
    background-color: #f0f4f8 !important;
}

/* ── Hero ── */
.hero-banner {
    background: linear-gradient(135deg, #1e40af 0%, #1a56db 45%, #0ea5e9 100%);
    border-radius: 20px;
    padding: 38px 48px;
    margin-bottom: 28px;
    position: relative;
    overflow: hidden;
    box-shadow: 0 10px 40px rgba(26,86,219,.30);
}
.hero-banner::before {
    content:''; position:absolute; top:-80px; right:-80px;
    width:300px; height:300px; border-radius:50%;
    background:rgba(255,255,255,.06);
}
.hero-banner::after {
    content:''; position:absolute; bottom:-100px; left:55%;
    width:240px; height:240px; border-radius:50%;
    background:rgba(255,255,255,.04);
}
.hero-eyebrow {
    font-size:11px; font-weight:700; letter-spacing:3px;
    text-transform:uppercase; color:rgba(255,255,255,.60); margin-bottom:10px;
}
.hero-title {
    font-family:'DM Sans',sans-serif; font-size:clamp(22px,3.5vw,40px);
    font-weight:700; color:#fff; line-height:1.2; margin:0 0 10px; letter-spacing:-.5px;
}
.hero-title span { color:rgba(255,255,255,.75); font-weight:400; }
.hero-sub { font-size:14px; color:rgba(255,255,255,.68); margin-bottom:22px; }
.badge-row { display:flex; gap:10px; flex-wrap:wrap; }
.badge {
    background:rgba(255,255,255,.18); border:1px solid rgba(255,255,255,.28);
    border-radius:20px; padding:5px 18px; font-size:12px; font-weight:600; color:#fff;
}
.badge.gold {
    background:rgba(217,119,6,.28); border-color:rgba(255,200,80,.45); color:#fde68a;
}

/* ── Stats strip ── */
.stat-row { display:flex; gap:14px; flex-wrap:wrap; margin-bottom:28px; }
.stat-chip {
    background:var(--surface); border:1px solid var(--border);
    border-radius:12px; padding:14px 20px;
    display:flex; align-items:center; gap:14px;
    box-shadow:var(--shadow-sm); flex:1; min-width:150px;
}
.stat-icon {
    width:42px; height:42px; border-radius:10px;
    display:flex; align-items:center; justify-content:center; font-size:19px; flex-shrink:0;
}
.si-blue  { background:var(--accent-light); }
.si-green { background:var(--green-light); }
.si-gold  { background:var(--gold-light); }
.si-sky   { background:#e0f2fe; }
.stat-num { font-size:22px; font-weight:700; color:var(--text); line-height:1; }
.stat-lbl { font-size:11px; color:var(--muted); font-weight:500; margin-top:3px; }

/* ── Section heading ── */
.section-head {
    font-family:'DM Sans',sans-serif; font-size:15px; font-weight:700;
    color:var(--text); margin:0 0 16px;
    display:flex; align-items:center; gap:10px;
}
.section-head::after { content:''; flex:1; height:1px; background:var(--border); }

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    background:var(--surface) !important; border-radius:12px !important;
    border:1px solid var(--border) !important; padding:5px !important;
    gap:3px !important; box-shadow:var(--shadow-sm) !important;
}
.stTabs [data-baseweb="tab"] {
    font-family:'Inter',sans-serif !important; font-size:13px !important;
    font-weight:600 !important; color:var(--muted) !important;
    background:transparent !important; border-radius:8px !important;
    padding:10px 22px !important; border:none !important; transition:all .2s !important;
}
.stTabs [aria-selected="true"] {
    background:var(--accent) !important; color:#fff !important;
    box-shadow:0 2px 10px rgba(26,86,219,.35) !important;
}

/* ── Panel cards ── */
.panel {
    background:var(--surface); border:1px solid var(--border);
    border-radius:var(--radius); padding:24px; margin-bottom:16px;
    box-shadow:var(--shadow-sm); transition:box-shadow .2s, border-color .2s;
}
.panel:hover { box-shadow:var(--shadow-md); border-color:#c7d2e2; }
.panel-title {
    font-size:10px; font-weight:700; letter-spacing:2px; text-transform:uppercase;
    color:var(--accent); margin-bottom:18px; display:flex; align-items:center; gap:8px;
}
.dot { width:8px; height:8px; border-radius:50%; background:var(--accent); flex-shrink:0; }

/* ── Result box ── */
.result-box {
    background:linear-gradient(135deg, var(--accent-light) 0%, #f0f7ff 100%);
    border:1.5px solid rgba(26,86,219,.2); border-radius:14px;
    padding:26px 24px; text-align:center; position:relative; overflow:hidden;
}
.result-box::before {
    content:''; position:absolute; top:-40px; right:-40px;
    width:120px; height:120px; border-radius:50%;
    background:rgba(26,86,219,.05);
}
.result-label { font-size:10px; font-weight:700; letter-spacing:2px; text-transform:uppercase; color:var(--accent); margin-bottom:8px; }
.result-value { font-family:'JetBrains Mono',monospace; font-size:clamp(26px,4vw,44px); font-weight:700; color:var(--accent); line-height:1; word-break:break-all; }
.result-unit  { font-size:15px; font-weight:600; color:var(--muted); margin-top:6px; }
.result-formula {
    font-family:'JetBrains Mono',monospace; font-size:11px; color:var(--green);
    margin-top:12px; background:var(--green-light); display:inline-block;
    padding:4px 14px; border-radius:6px; font-weight:500;
}

/* ── Density result ── */
.density-result {
    background:linear-gradient(135deg, #fff8e1 0%, #fffde7 100%);
    border:1.5px solid rgba(217,119,6,.22); border-radius:14px;
    padding:22px; text-align:center; margin-top:14px;
}
.density-result .result-value { color:var(--gold); }
.density-result .result-label { color:var(--gold); }
.density-tag {
    background:#fef9c3; color:#92400e; margin-top:10px;
    display:inline-block; padding:4px 14px; border-radius:6px;
    font-family:'JetBrains Mono',monospace; font-size:11px; font-weight:500;
}

/* ── Tables ── */
.table-wrap {
    background:var(--surface); border:1px solid var(--border);
    border-radius:var(--radius); overflow:hidden; box-shadow:var(--shadow-sm); overflow-x:auto;
}
.data-table { width:100%; border-collapse:collapse; font-size:13px; }
.data-table thead tr { background:var(--accent); }
.data-table th {
    padding:11px 18px; text-align:left; font-size:10px; font-weight:700;
    letter-spacing:1.5px; text-transform:uppercase; color:#fff;
}
.data-table th:first-child { border-radius:0; }
.data-table td {
    padding:10px 18px; color:var(--text);
    border-bottom:1px solid var(--border-soft);
    font-family:'JetBrains Mono',monospace; font-size:12px;
}
.data-table td:first-child { font-family:'Inter',sans-serif; font-weight:500; color:var(--text); }
.data-table tbody tr:hover td { background:#f8faff; }
.data-table .hl td { background:var(--green-light) !important; color:var(--green) !important; font-weight:600; }
.data-table tbody tr:last-child td { border-bottom:none; }

/* ── Widgets ── */
div[data-testid="stNumberInput"] input,
div[data-testid="stTextInput"] input {
    background:#f8fafc !important; border:1.5px solid var(--border) !important;
    border-radius:var(--radius-sm) !important; color:var(--text) !important;
    font-family:'JetBrains Mono',monospace !important; font-size:15px !important;
    padding:10px 14px !important; transition:border-color .2s, box-shadow .2s !important;
}
div[data-testid="stNumberInput"] input:focus,
div[data-testid="stTextInput"] input:focus {
    border-color:var(--accent) !important;
    box-shadow:0 0 0 3px rgba(26,86,219,.12) !important;
    background:#fff !important; outline:none !important;
}
div[data-testid="stSelectbox"] > div > div {
    background:#f8fafc !important; border:1.5px solid var(--border) !important;
    border-radius:var(--radius-sm) !important; color:var(--text) !important; font-size:14px !important;
}
label, .stSelectbox label, .stNumberInput label {
    font-family:'Inter',sans-serif !important; font-size:11px !important;
    font-weight:700 !important; color:var(--muted) !important;
    text-transform:uppercase !important; letter-spacing:.8px !important; margin-bottom:4px !important;
}
.stRadio > div { gap:10px !important; }
.stRadio label { text-transform:none !important; letter-spacing:0 !important; font-size:13px !important; }

/* ── Button ── */
.stButton > button {
    background:var(--accent) !important; color:#fff !important;
    border:none !important; border-radius:var(--radius-sm) !important;
    font-family:'Inter',sans-serif !important; font-size:13px !important;
    font-weight:700 !important; letter-spacing:.5px !important;
    padding:13px 28px !important; width:100% !important;
    transition:all .2s !important; box-shadow:0 4px 14px rgba(26,86,219,.30) !important;
}
.stButton > button:hover {
    background:#1648c0 !important;
    box-shadow:0 6px 22px rgba(26,86,219,.42) !important;
    transform:translateY(-1px) !important;
}

/* ── Arrow divider ── */
.arrow-col {
    display:flex; align-items:center; justify-content:center;
    height:100%; padding-top:36px; font-size:30px; color:#cbd5e1;
}

/* ── Footer ── */
.footer {
    background:var(--surface); border:1px solid var(--border);
    border-radius:var(--radius); padding:18px 28px; margin-top:40px;
    display:flex; align-items:center; justify-content:center;
    gap:10px; font-size:12px; color:var(--muted); font-weight:500;
    box-shadow:var(--shadow-sm);
}
.footer strong { color:var(--accent); }
.footer .sep { color:var(--border-soft); font-size:16px; }

::-webkit-scrollbar { width:6px; height:6px; }
::-webkit-scrollbar-track { background:var(--bg); }
::-webkit-scrollbar-thumb { background:#cbd5e1; border-radius:3px; }
#MainMenu, footer, header { visibility:hidden; }
.block-container { padding-top:2rem !important; padding-bottom:1rem !important; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  DATA
# ─────────────────────────────────────────────
MATERIALS = {
    "Steel (Carbon)": 7850, "Steel (Stainless 304)": 8000,
    "Aluminum (Pure)": 2700, "Aluminum Alloy (6061)": 2700,
    "Copper": 8960, "Brass": 8500, "Cast Iron (Gray)": 7200,
    "Titanium (Grade 5)": 4430, "Nickel": 8908, "Lead": 11340,
    "Zinc": 7133, "Magnesium": 1738, "Gold": 19300, "Silver": 10490,
    "Tungsten": 19250, "Chromium": 7190, "Molybdenum": 10220,
    "ABS Plastic": 1050, "Nylon (PA6)": 1140, "Polycarbonate (PC)": 1200,
    "HDPE": 950, "PTFE (Teflon)": 2200, "PVC (Rigid)": 1400,
    "Epoxy Resin": 1250, "Polypropylene (PP)": 905,
    "Carbon Fiber Composite": 1600, "Fiberglass (GFRP)": 1900,
    "Concrete": 2400, "Granite": 2700, "Glass (Borosilicate)": 2230,
    "Silicon Carbide (SiC)": 3210, "Alumina (Al₂O₃)": 3960,
    "Oak Wood": 700, "Balsa Wood": 120, "Rubber (Natural)": 920,
    "Cork": 120, "Ice": 917, "Water": 1000, "Air (at STP)": 1.225,
}

CATEGORIES = {
    "⚖️  Force":             ("N",    ["N","kN","MN","lbf","kgf","dyn"]),
    "📏  Length":            ("m",    ["m","cm","mm","km","in","ft","yd","mi","μm"]),
    "⚡  Pressure":          ("Pa",   ["Pa","kPa","MPa","GPa","bar","atm","psi","ksi","torr","mmHg"]),
    "🔁  Torque":            ("N·m",  ["N·m","kN·m","N·cm","lbf·ft","lbf·in","kgf·m"]),
    "🏎️  Velocity":          ("m/s",  ["m/s","km/h","ft/s","mph","knot"]),
    "🌡️  Temperature":       ("°C",   ["°C","°F","K","°R"]),
    "💡  Power":             ("W",    ["W","kW","MW","hp","BTU/hr","cal/s"]),
    "🔩  Stress / Strength": ("Pa",   ["Pa","kPa","MPa","GPa","psi","ksi"]),
    "📦  Mass":              ("kg",   ["kg","g","mg","t","lb","oz","slug"]),
    "🌀  Angular Velocity":  ("rad/s",["rad/s","rpm","deg/s","rev/s"]),
    "💧  Viscosity":         ("Pa·s", ["Pa·s","cP","mPa·s","lbf·s/ft²"]),
    "⚡  Energy":            ("J",    ["J","kJ","MJ","cal","kcal","BTU","kWh","eV","ft·lbf"]),
}

FACTORS = {
    "N":1,"kN":1e3,"MN":1e6,"lbf":4.44822,"kgf":9.80665,"dyn":1e-5,
    "m":1,"cm":0.01,"mm":0.001,"km":1000,"in":0.0254,
    "ft":0.3048,"yd":0.9144,"mi":1609.344,"μm":1e-6,
    "Pa":1,"kPa":1e3,"MPa":1e6,"GPa":1e9,"bar":1e5,
    "atm":101325,"psi":6894.757,"ksi":6.894757e6,"torr":133.322,"mmHg":133.322,
    "N·m":1,"kN·m":1e3,"N·cm":0.01,"lbf·ft":1.35582,"lbf·in":0.112985,"kgf·m":9.80665,
    "m/s":1,"km/h":1/3.6,"ft/s":0.3048,"mph":0.44704,"knot":0.514444,
    "W":1,"kW":1e3,"MW":1e6,"hp":745.7,"BTU/hr":0.29307,"cal/s":4.18400,
    "kg":1,"g":0.001,"mg":1e-6,"t":1000,"lb":0.453592,"oz":0.0283495,"slug":14.5939,
    "rad/s":1,"rpm":math.pi/30,"deg/s":math.pi/180,"rev/s":2*math.pi,
    "Pa·s":1,"cP":0.001,"mPa·s":0.001,"lbf·s/ft²":47.8803,
    "J":1,"kJ":1e3,"MJ":1e6,"cal":4.184,"kcal":4184,
    "BTU":1055.06,"kWh":3.6e6,"eV":1.60218e-19,"ft·lbf":1.35582,
}

def convert_temp(val, frm, to):
    if frm == "°C":   c = val
    elif frm == "°F": c = (val - 32) * 5 / 9
    elif frm == "K":  c = val - 273.15
    elif frm == "°R": c = (val - 491.67) * 5 / 9
    if to == "°C":   return c
    if to == "°F":   return c * 9 / 5 + 32
    if to == "K":    return c + 273.15
    if to == "°R":   return (c + 273.15) * 9 / 5

def do_convert(val, frm, to):
    if frm == to: return val
    return val * FACTORS[frm] / FACTORS[to]

# ─────────────────────────────────────────────
#  HERO
# ─────────────────────────────────────────────
st.markdown("""
<div class="hero-banner">
    <div class="hero-eyebrow">⚙ Mechanical Engineering Toolkit</div>
    <div class="hero-title">Unit Converter &amp; <span>Material Density Checker</span></div>
    <div class="hero-sub">Precision calculations for engineers — fast, accurate, and beautifully simple</div>
    <div class="badge-row">
        <span class="badge">👤 Muhammad Bin Akrma</span>
        <span class="badge gold">🎓 Roll No: 25-ME-59</span>
        <span class="badge">🏛 Mechanical Engineering</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  STATS STRIP
# ─────────────────────────────────────────────
st.markdown("""
<div class="stat-row">
  <div class="stat-chip">
    <div class="stat-icon si-blue">📐</div>
    <div><div class="stat-num">12</div><div class="stat-lbl">Unit Categories</div></div>
  </div>
  <div class="stat-chip">
    <div class="stat-icon si-green">🧱</div>
    <div><div class="stat-num">39+</div><div class="stat-lbl">Materials</div></div>
  </div>
  <div class="stat-chip">
    <div class="stat-icon si-gold">⚡</div>
    <div><div class="stat-num">80+</div><div class="stat-lbl">Unit Pairs</div></div>
  </div>
  <div class="stat-chip">
    <div class="stat-icon si-sky">📐</div>
    <div><div class="stat-num">5</div><div class="stat-lbl">Shape Calculators</div></div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  TABS
# ─────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs([
    "⚙️   Unit Converter",
    "🧱   Material Density",
    "📋   Quick Reference",
])

# ══════════════════════════════════════════════
#  TAB 1
# ══════════════════════════════════════════════
with tab1:
    st.markdown('<p class="section-head">⚙️ Choose a Category &amp; Convert</p>', unsafe_allow_html=True)

    cat_name = st.selectbox("Category", list(CATEGORIES.keys()), index=0, label_visibility="collapsed")
    base_unit, units = CATEGORIES[cat_name]
    is_temp = "Temperature" in cat_name

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([5, 1, 5], gap="medium")

    with col1:
        st.markdown('<div class="panel"><div class="panel-title"><span class="dot"></span>INPUT VALUE</div>', unsafe_allow_html=True)
        value_in  = st.number_input("Value", value=1.0, format="%.6g", key="val_in", label_visibility="collapsed")
        unit_from = st.selectbox("From Unit", units, key="uf")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="arrow-col">→</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="panel"><div class="panel-title"><span class="dot"></span>OUTPUT UNIT</div>', unsafe_allow_html=True)
        unit_to = st.selectbox("To Unit", units, index=min(1, len(units)-1), key="ut")
        st.button("⚡  Convert", key="conv_btn")
        st.markdown("</div>", unsafe_allow_html=True)

    # Compute
    try:
        if is_temp:
            result = convert_temp(value_in, unit_from, unit_to)
            formula_str = f"{value_in} {unit_from}  →  {result:.6g} {unit_to}"
        else:
            result = do_convert(value_in, unit_from, unit_to)
            ratio  = FACTORS.get(unit_from, 1) / FACTORS.get(unit_to, 1)
            formula_str = f"Factor: × {ratio:.6g}   |   {value_in} {unit_from} = {result:.6g} {unit_to}"

        fmt = f"{result:.6g}" if abs(result) < 1e10 else f"{result:.4e}"

        st.markdown(f"""
        <div class="result-box" style="margin:18px 0 28px">
            <div class="result-label">Result</div>
            <div class="result-value">{fmt}</div>
            <div class="result-unit">{unit_to}</div>
            <div class="result-formula">{formula_str}</div>
        </div>
        """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Conversion error: {e}")

    # Equivalents table
    st.markdown('<p class="section-head">🔢 All Unit Equivalents at a Glance</p>', unsafe_allow_html=True)

    if is_temp:
        rows = ""
        for u in units:
            try:
                v  = convert_temp(value_in, unit_from, u)
                hl = "hl" if u == unit_to else ""
                rows += f'<tr class="{hl}"><td>{u}</td><td>{v:.6g}</td><td>{"✓ Selected" if u == unit_to else ""}</td></tr>'
            except: pass
    else:
        rows = ""
        try:
            si_val = value_in * FACTORS.get(unit_from, 1)
            for u in units:
                v  = si_val / FACTORS.get(u, 1)
                hl = "hl" if u == unit_to else ""
                rows += f'<tr class="{hl}"><td>{u}</td><td>{v:.6g}</td><td>{"✓ Selected" if u == unit_to else ""}</td></tr>'
        except:
            rows = "<tr><td colspan='3'>Error computing equivalents</td></tr>"

    st.markdown(f"""
    <div class="table-wrap">
    <table class="data-table">
      <thead><tr><th>Unit</th><th>Equivalent Value</th><th>Status</th></tr></thead>
      <tbody>{rows}</tbody>
    </table>
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════
#  TAB 2
# ══════════════════════════════════════════════
with tab2:
    st.markdown('<p class="section-head">🧱 Material Lookup &amp; Mass / Volume Calculator</p>', unsafe_allow_html=True)

    col_a, col_b = st.columns(2, gap="large")

    with col_a:
        st.markdown('<div class="panel"><div class="panel-title"><span class="dot"></span>SELECT MATERIAL</div>', unsafe_allow_html=True)
        search   = st.text_input("🔍 Search material", placeholder="e.g. steel, aluminum, copper…")
        filtered = {k: v for k, v in MATERIALS.items() if search.lower() in k.lower()} if search else MATERIALS
        if not filtered:
            st.warning("No materials found.")
            filtered = MATERIALS
        mat     = st.selectbox("Material", list(filtered.keys()))
        density = MATERIALS[mat]
        st.markdown(f"""
        <div class="density-result">
            <div class="result-label">Density</div>
            <div class="result-value">{density:,}</div>
            <div class="result-unit">kg / m³</div>
            <div class="density-tag">{density/1000:.4f} g/cm³ &nbsp;·&nbsp; {density*0.062428:.4f} lb/ft³</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col_b:
        st.markdown('<div class="panel"><div class="panel-title"><span class="dot"></span>MASS / VOLUME CALCULATOR</div>', unsafe_allow_html=True)
        calc_mode = st.radio("Mode", ["Mass from Volume", "Volume from Mass"], horizontal=True)
        shape     = st.selectbox("Geometry", ["Custom Volume (m³)", "Rectangular Block", "Cylinder", "Sphere", "Hollow Cylinder"])

        vol_m3 = 0.0
        if shape == "Custom Volume (m³)":
            vol_m3 = st.number_input("Volume (m³)", value=0.001, format="%.6f", min_value=0.0)
        elif shape == "Rectangular Block":
            c1, c2, c3 = st.columns(3)
            L = c1.number_input("L (m)", value=0.1, format="%.4f", min_value=0.0)
            W = c2.number_input("W (m)", value=0.1, format="%.4f", min_value=0.0)
            H = c3.number_input("H (m)", value=0.1, format="%.4f", min_value=0.0)
            vol_m3 = L * W * H
        elif shape == "Cylinder":
            c1, c2 = st.columns(2)
            R = c1.number_input("Radius (m)", value=0.05, format="%.4f", min_value=0.0)
            H = c2.number_input("Height (m)", value=0.20, format="%.4f", min_value=0.0)
            vol_m3 = math.pi * R**2 * H
        elif shape == "Sphere":
            R      = st.number_input("Radius (m)", value=0.05, format="%.4f", min_value=0.0)
            vol_m3 = (4/3) * math.pi * R**3
        elif shape == "Hollow Cylinder":
            c1, c2, c3 = st.columns(3)
            Ro = c1.number_input("Outer R (m)", value=0.06, format="%.4f", min_value=0.0)
            Ri = c2.number_input("Inner R (m)", value=0.04, format="%.4f", min_value=0.0)
            H  = c3.number_input("Height (m)",  value=0.20, format="%.4f", min_value=0.0)
            vol_m3 = math.pi * (Ro**2 - Ri**2) * H

        if calc_mode == "Mass from Volume":
            mass_kg = density * vol_m3
            st.markdown(f"""
            <div class="result-box" style="margin-top:16px">
                <div class="result-label">Calculated Mass</div>
                <div class="result-value">{mass_kg:.4f}</div>
                <div class="result-unit">kg</div>
                <div class="result-formula">{mass_kg*1000:.2f} g &nbsp;·&nbsp; {mass_kg*2.20462:.4f} lb</div>
                <div style="font-size:11px;color:#64748b;margin-top:10px">
                    V = {vol_m3:.6f} m³ &nbsp;×&nbsp; ρ = {density:,} kg/m³
                </div>
            </div>""", unsafe_allow_html=True)
        else:
            mass_in  = st.number_input("Mass (kg)", value=1.0, format="%.4f", min_value=0.0)
            vol_calc = mass_in / density if density else 0
            st.markdown(f"""
            <div class="result-box" style="margin-top:10px">
                <div class="result-label">Calculated Volume</div>
                <div class="result-value">{vol_calc:.6f}</div>
                <div class="result-unit">m³</div>
                <div class="result-formula">{vol_calc*1e6:.4f} cm³ &nbsp;·&nbsp; {vol_calc*1e9:.4f} mm³</div>
                <div style="font-size:11px;color:#64748b;margin-top:10px">
                    m = {mass_in} kg &nbsp;÷&nbsp; ρ = {density:,} kg/m³
                </div>
            </div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Full table
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<p class="section-head">📋 Full Material Database</p>', unsafe_allow_html=True)

    cats = st.multiselect(
        "Filter categories",
        ["Metals", "Polymers", "Composites & Ceramics", "Natural Materials"],
        default=["Metals", "Polymers", "Composites & Ceramics", "Natural Materials"],
    )
    mk = list(MATERIALS.keys())
    key_map = {
        "Metals":                  mk[:17],
        "Polymers":                mk[17:25],
        "Composites & Ceramics":   mk[25:32],
        "Natural Materials":       mk[32:],
    }
    show = []
    for c in cats: show += key_map.get(c, [])

    rows = "".join(
        f'<tr class="{"hl" if k == mat else ""}"><td>{k}</td><td>{v:,.3f}</td><td>{v/1000:.4f}</td><td>{v*0.062428:.4f}</td></tr>'
        for k, v in ((k, MATERIALS[k]) for k in show)
    )
    st.markdown(f"""
    <div class="table-wrap">
    <table class="data-table">
      <thead><tr><th>Material</th><th>kg / m³</th><th>g / cm³</th><th>lb / ft³</th></tr></thead>
      <tbody>{rows}</tbody>
    </table>
    </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════
#  TAB 3
# ══════════════════════════════════════════════
with tab3:
    st.markdown('<p class="section-head">📐 Engineering Quick Reference</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown('<p class="section-head">⚡ Key Constants</p>', unsafe_allow_html=True)
        constants = {
            "g — Gravity":            "9.80665 m/s²",
            "R — Gas constant":       "8.314 J/(mol·K)",
            "σ — Stefan-Boltzmann":   "5.67×10⁻⁸ W/(m²·K⁴)",
            "E — Steel (Young's)":    "200 GPa",
            "E — Aluminum (Young's)": "69 GPa",
            "ν — Steel (Poisson)":    "0.30",
            "ν — Aluminum (Poisson)": "0.33",
            "1 atm":                  "101,325 Pa",
            "1 cal":                  "4.184 J",
            "1 hp":                   "745.7 W",
        }
        rows = "".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in constants.items())
        st.markdown(f"""<div class="table-wrap"><table class="data-table">
          <thead><tr><th>Constant</th><th>Value</th></tr></thead>
          <tbody>{rows}</tbody></table></div>""", unsafe_allow_html=True)

    with col2:
        st.markdown('<p class="section-head">🔩 Material Strength (UTS)</p>', unsafe_allow_html=True)
        strengths = {
            "Steel (Mild)":       "400–550 MPa",
            "Steel (High)":       "800–2000 MPa",
            "Aluminum 6061":      "310 MPa",
            "Titanium Ti-6Al-4V": "950 MPa",
            "CFRP Composite":     "600–1500 MPa",
            "Concrete":           "20–50 MPa",
            "Copper":             "210–400 MPa",
            "Nylon 6":            "75–85 MPa",
            "ABS Plastic":        "40–55 MPa",
            "Cast Iron":          "150–400 MPa",
        }
        rows = "".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in strengths.items())
        st.markdown(f"""<div class="table-wrap"><table class="data-table">
          <thead><tr><th>Material</th><th>Tensile Strength</th></tr></thead>
          <tbody>{rows}</tbody></table></div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<p class="section-head">🧮 Core Mechanical Formulas</p>', unsafe_allow_html=True)

    formulas = [
        ("Stress",          "σ = F / A",              "Pa  (N/m²)"),
        ("Strain",          "ε = ΔL / L₀",            "Dimensionless"),
        ("Young's Modulus", "E = σ / ε",               "Pa"),
        ("Torque",          "T = F × r",               "N·m"),
        ("Power",           "P = T × ω",               "W"),
        ("Pressure",        "p = F / A",               "Pa"),
        ("Bernoulli",       "p + ½ρv² + ρgh = const", "Pa"),
        ("Reynolds Number", "Re = ρvD / μ",            "Dimensionless"),
        ("Thermal Stress",  "σ = E × α × ΔT",          "Pa"),
        ("Shear Stress",    "τ = T × r / J",           "Pa"),
    ]
    rows = "".join(f"<tr><td>{n}</td><td>{f}</td><td>{u}</td></tr>" for n, f, u in formulas)
    st.markdown(f"""<div class="table-wrap"><table class="data-table">
      <thead><tr><th>Formula</th><th>Expression</th><th>Unit</th></tr></thead>
      <tbody>{rows}</tbody></table></div>""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  FOOTER
# ─────────────────────────────────────────────
st.markdown("""
<div class="footer">
    ⚙️
    <strong>Mechanical Unit Converter &amp; Material Density Checker</strong>
    <span class="sep">|</span>
    Muhammad Bin Akrma
    <span class="sep">|</span>
    Roll No: 25-ME-59
    <span class="sep">|</span>
    Built with Python &amp; Streamlit
</div>
""", unsafe_allow_html=True)
