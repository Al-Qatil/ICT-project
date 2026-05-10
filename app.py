import streamlit as st
import math

# ─────────────────────────────────────────────
#  PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Mech Unit Converter | 25-ME-59",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─────────────────────────────────────────────
#  CUSTOM CSS  (industrial / blueprint aesthetic)
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Share+Tech+Mono&family=Exo+2:wght@300;400;600&display=swap');

/* ── Root palette ── */
:root {
    --bg:        #0a0e1a;
    --surface:   #0f1628;
    --card:      #141d35;
    --border:    #1e3a5f;
    --accent:    #00d4ff;
    --gold:      #f5a623;
    --green:     #00ff9d;
    --text:      #c8d8f0;
    --muted:     #5a7a9a;
    --danger:    #ff4f5e;
    --glow:      0 0 20px rgba(0,212,255,.35);
}

/* ── Global ── */
html, body, .stApp {
    background-color: var(--bg) !important;
    font-family: 'Exo 2', sans-serif;
    color: var(--text);
}

/* animated grid background */
.stApp::before {
    content: '';
    position: fixed; inset: 0;
    background-image:
        linear-gradient(rgba(0,212,255,.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,212,255,.04) 1px, transparent 1px);
    background-size: 40px 40px;
    pointer-events: none;
    z-index: 0;
}

/* ── Header band ── */
.hero-banner {
    background: linear-gradient(135deg, #0f1e3a 0%, #0a2040 50%, #0f1e3a 100%);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 28px 36px;
    margin-bottom: 28px;
    position: relative;
    overflow: hidden;
    box-shadow: 0 8px 40px rgba(0,0,0,.6), inset 0 1px 0 rgba(0,212,255,.15);
}
.hero-banner::after {
    content: '⚙';
    position: absolute;
    right: -20px; top: -20px;
    font-size: 160px;
    opacity: .04;
    color: var(--accent);
    line-height: 1;
}
.hero-title {
    font-family: 'Orbitron', monospace;
    font-size: clamp(18px, 3vw, 32px);
    font-weight: 900;
    color: var(--accent);
    text-shadow: var(--glow);
    letter-spacing: 2px;
    margin: 0 0 6px 0;
}
.hero-sub {
    font-family: 'Share Tech Mono', monospace;
    font-size: 13px;
    color: var(--muted);
    letter-spacing: 1px;
}
.badge-row { display: flex; gap: 12px; flex-wrap: wrap; margin-top: 14px; }
.badge {
    background: rgba(0,212,255,.1);
    border: 1px solid rgba(0,212,255,.3);
    border-radius: 20px;
    padding: 4px 14px;
    font-family: 'Share Tech Mono', monospace;
    font-size: 12px;
    color: var(--accent);
}
.badge.gold {
    background: rgba(245,166,35,.1);
    border-color: rgba(245,166,35,.4);
    color: var(--gold);
}

/* ── Tab strip ── */
.stTabs [data-baseweb="tab-list"] {
    background: var(--surface) !important;
    border-radius: 12px !important;
    border: 1px solid var(--border) !important;
    padding: 6px !important;
    gap: 4px !important;
}
.stTabs [data-baseweb="tab"] {
    font-family: 'Orbitron', monospace !important;
    font-size: 11px !important;
    font-weight: 700 !important;
    letter-spacing: 1.5px !important;
    color: var(--muted) !important;
    background: transparent !important;
    border-radius: 8px !important;
    padding: 10px 18px !important;
    border: none !important;
    transition: all .25s !important;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, rgba(0,212,255,.2), rgba(0,212,255,.08)) !important;
    color: var(--accent) !important;
    box-shadow: 0 0 12px rgba(0,212,255,.25) !important;
    border: 1px solid rgba(0,212,255,.3) !important;
}

/* ── Cards ── */
.conv-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 24px;
    margin-bottom: 18px;
    position: relative;
    transition: border-color .3s;
}
.conv-card:hover { border-color: rgba(0,212,255,.4); }
.conv-card .card-label {
    font-family: 'Orbitron', monospace;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    color: var(--accent);
    text-transform: uppercase;
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 8px;
}
.card-label::before {
    content: '';
    width: 3px; height: 16px;
    background: var(--accent);
    border-radius: 2px;
    box-shadow: 0 0 8px var(--accent);
    display: inline-block;
}

/* ── Result box ── */
.result-box {
    background: linear-gradient(135deg, rgba(0,212,255,.08), rgba(0,212,255,.03));
    border: 1px solid rgba(0,212,255,.4);
    border-radius: 12px;
    padding: 20px 24px;
    text-align: center;
    box-shadow: 0 0 24px rgba(0,212,255,.1);
}
.result-value {
    font-family: 'Orbitron', monospace;
    font-size: clamp(22px, 4vw, 38px);
    font-weight: 900;
    color: var(--accent);
    text-shadow: var(--glow);
    word-break: break-all;
}
.result-unit {
    font-family: 'Share Tech Mono', monospace;
    font-size: 14px;
    color: var(--muted);
    margin-top: 4px;
}
.result-formula {
    font-family: 'Share Tech Mono', monospace;
    font-size: 12px;
    color: var(--green);
    margin-top: 8px;
    opacity: .8;
}

/* ── Density table ── */
.density-table { width: 100%; border-collapse: collapse; margin-top: 8px; }
.density-table th {
    background: rgba(0,212,255,.1);
    color: var(--accent);
    font-family: 'Orbitron', monospace;
    font-size: 10px;
    letter-spacing: 1.5px;
    padding: 10px 14px;
    text-align: left;
    border-bottom: 1px solid var(--border);
}
.density-table td {
    padding: 10px 14px;
    font-family: 'Share Tech Mono', monospace;
    font-size: 13px;
    color: var(--text);
    border-bottom: 1px solid rgba(30,58,95,.5);
    transition: background .2s;
}
.density-table tr:hover td { background: rgba(0,212,255,.05); }
.density-table .highlight td { color: var(--green); background: rgba(0,255,157,.04); }

/* ── Streamlit widgets ── */
div[data-testid="stNumberInput"] input,
div[data-testid="stTextInput"] input,
div[data-testid="stSelectbox"] select,
.stSelectbox > div > div {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    color: var(--text) !important;
    font-family: 'Share Tech Mono', monospace !important;
}
div[data-testid="stNumberInput"] input:focus,
div[data-testid="stSelectbox"] > div:focus-within {
    border-color: var(--accent) !important;
    box-shadow: 0 0 0 2px rgba(0,212,255,.15) !important;
}

label, .stSelectbox label {
    font-family: 'Exo 2', sans-serif !important;
    font-size: 13px !important;
    color: var(--muted) !important;
    font-weight: 600 !important;
    letter-spacing: .5px !important;
}

/* ── Buttons ── */
.stButton > button {
    background: linear-gradient(135deg, #0050a0, #003070) !important;
    color: var(--accent) !important;
    border: 1px solid rgba(0,212,255,.4) !important;
    border-radius: 10px !important;
    font-family: 'Orbitron', monospace !important;
    font-size: 11px !important;
    font-weight: 700 !important;
    letter-spacing: 2px !important;
    padding: 12px 28px !important;
    width: 100% !important;
    transition: all .25s !important;
    box-shadow: 0 4px 20px rgba(0,0,0,.4) !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #0060c0, #004090) !important;
    box-shadow: 0 0 20px rgba(0,212,255,.3) !important;
    transform: translateY(-1px) !important;
}

/* ── Horizontal rule ── */
hr { border-color: var(--border) !important; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }

/* ── Metric ── */
div[data-testid="stMetric"] {
    background: var(--card) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    padding: 16px !important;
}
div[data-testid="stMetric"] label {
    font-family: 'Orbitron', monospace !important;
    font-size: 10px !important;
    letter-spacing: 1.5px !important;
    color: var(--muted) !important;
}
div[data-testid="stMetricValue"] {
    font-family: 'Orbitron', monospace !important;
    color: var(--accent) !important;
}

/* ── Footer ── */
.footer {
    text-align: center;
    padding: 20px;
    font-family: 'Share Tech Mono', monospace;
    font-size: 11px;
    color: var(--muted);
    border-top: 1px solid var(--border);
    margin-top: 40px;
    letter-spacing: 1px;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  DATA
# ─────────────────────────────────────────────
MATERIALS = {
    # Metals
    "Steel (Carbon)":          7850,
    "Steel (Stainless 304)":   8000,
    "Aluminum (Pure)":         2700,
    "Aluminum Alloy (6061)":   2700,
    "Copper":                  8960,
    "Brass":                   8500,
    "Cast Iron (Gray)":        7200,
    "Titanium (Grade 5)":      4430,
    "Nickel":                  8908,
    "Lead":                   11340,
    "Zinc":                    7133,
    "Magnesium":               1738,
    "Gold":                   19300,
    "Silver":                 10490,
    "Tungsten":               19250,
    "Chromium":                7190,
    "Molybdenum":             10220,
    # Polymers
    "ABS Plastic":             1050,
    "Nylon (PA6)":             1140,
    "Polycarbonate (PC)":      1200,
    "HDPE":                     950,
    "PTFE (Teflon)":           2200,
    "PVC (Rigid)":             1400,
    "Epoxy Resin":             1250,
    "Polypropylene (PP)":       905,
    # Composites / Ceramics
    "Carbon Fiber Composite":  1600,
    "Fiberglass (GFRP)":       1900,
    "Concrete":                2400,
    "Granite":                 2700,
    "Glass (Borosilicate)":    2230,
    "Silicon Carbide (SiC)":   3210,
    "Alumina (Al₂O₃)":        3960,
    # Natural
    "Oak Wood":                 700,
    "Balsa Wood":               120,
    "Rubber (Natural)":         920,
    "Cork":                     120,
    "Ice":                      917,
    "Water":                   1000,
    "Air (at STP)":           1.225,
}

CATEGORIES = {
    "⚖️  Force":          ("N",   ["N","kN","MN","lbf","kgf","dyn"]),
    "📏  Length":         ("m",   ["m","cm","mm","km","in","ft","yd","mi","μm"]),
    "⚡  Pressure":       ("Pa",  ["Pa","kPa","MPa","GPa","bar","atm","psi","ksi","torr","mmHg"]),
    "🔁  Torque":         ("N·m", ["N·m","kN·m","N·cm","lbf·ft","lbf·in","kgf·m"]),
    "🏎️  Velocity":       ("m/s", ["m/s","km/h","ft/s","mph","knot"]),
    "🔥  Temperature":    ("°C",  ["°C","°F","K","°R"]),
    "⚡  Power":          ("W",   ["W","kW","MW","hp","BTU/hr","cal/s"]),
    "🔩  Stress/Strength":("Pa",  ["Pa","kPa","MPa","GPa","psi","ksi"]),
    "📦  Mass":           ("kg",  ["kg","g","mg","t","lb","oz","slug"]),
    "🌀  Angular Velocity":("rad/s",["rad/s","rpm","deg/s","rev/s"]),
    "💧  Viscosity (Dyn)":("Pa·s",["Pa·s","cP","mPa·s","lbf·s/ft²"]),
    "⚡  Energy":         ("J",   ["J","kJ","MJ","cal","kcal","BTU","kWh","eV","ft·lbf"]),
}

# Conversion factors to SI base unit
FACTORS = {
    # Force → N
    "N":1, "kN":1e3, "MN":1e6, "lbf":4.44822, "kgf":9.80665, "dyn":1e-5,
    # Length → m
    "m":1, "cm":0.01, "mm":0.001, "km":1000, "in":0.0254,
    "ft":0.3048, "yd":0.9144, "mi":1609.344, "μm":1e-6,
    # Pressure → Pa
    "Pa":1, "kPa":1e3, "MPa":1e6, "GPa":1e9, "bar":1e5,
    "atm":101325, "psi":6894.757, "ksi":6.894757e6,
    "torr":133.322, "mmHg":133.322,
    # Torque → N·m
    "N·m":1, "kN·m":1e3, "N·cm":0.01, "lbf·ft":1.35582, "lbf·in":0.112985, "kgf·m":9.80665,
    # Velocity → m/s
    "m/s":1, "km/h":1/3.6, "ft/s":0.3048, "mph":0.44704, "knot":0.514444,
    # Power → W
    "W":1, "kW":1e3, "MW":1e6, "hp":745.7, "BTU/hr":0.29307, "cal/s":4.18400,
    # Mass → kg
    "kg":1, "g":0.001, "mg":1e-6, "t":1000, "lb":0.453592, "oz":0.0283495, "slug":14.5939,
    # Angular velocity → rad/s
    "rad/s":1, "rpm":math.pi/30, "deg/s":math.pi/180, "rev/s":2*math.pi,
    # Viscosity → Pa·s
    "Pa·s":1, "cP":0.001, "mPa·s":0.001, "lbf·s/ft²":47.8803,
    # Energy → J
    "J":1, "kJ":1e3, "MJ":1e6, "cal":4.184, "kcal":4184,
    "BTU":1055.06, "kWh":3.6e6, "eV":1.60218e-19, "ft·lbf":1.35582,
    # Stress (same as Pressure factors above, already added)
}

def convert_temp(val, frm, to):
    # → Celsius first
    if frm == "°C":   c = val
    elif frm == "°F": c = (val - 32) * 5/9
    elif frm == "K":  c = val - 273.15
    elif frm == "°R": c = (val - 491.67) * 5/9
    # Celsius → target
    if to == "°C":   return c
    if to == "°F":   return c * 9/5 + 32
    if to == "K":    return c + 273.15
    if to == "°R":   return (c + 273.15) * 9/5

def do_convert(val, frm, to):
    if frm == to:
        return val
    si = val * FACTORS[frm]
    return si / FACTORS[to]

# ─────────────────────────────────────────────
#  HEADER
# ─────────────────────────────────────────────
st.markdown("""
<div class="hero-banner">
    <div class="hero-title">⚙ Mechanical Unit Converter & Material Density Checker</div>
    <div class="hero-sub">PRECISION ENGINEERING TOOLKIT — STREAMLIT EDITION</div>
    <div class="badge-row">
        <span class="badge">👤 Muhammad Bin Akrma</span>
        <span class="badge gold">🎓 Roll No: 25-ME-59</span>
        <span class="badge">🏛 Mechanical Engineering</span>
        <span class="badge">📐 12 Unit Categories</span>
        <span class="badge">🧱 40+ Materials</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  TABS
# ─────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs([
    "⚙️  UNIT CONVERTER",
    "🧱  MATERIAL DENSITY",
    "📊  QUICK REFERENCE",
])

# ══════════════════════════════════════════════
#  TAB 1 – UNIT CONVERTER
# ══════════════════════════════════════════════
with tab1:
    st.markdown("### Select a Category & Convert")

    cat_name = st.selectbox(
        "📂 Unit Category",
        list(CATEGORIES.keys()),
        index=0,
    )

    base_unit, units = CATEGORIES[cat_name]
    is_temp = "Temperature" in cat_name

    col1, col2 = st.columns([1, 1], gap="large")
    with col1:
        st.markdown('<div class="conv-card"><div class="card-label">INPUT</div>', unsafe_allow_html=True)
        value_in = st.number_input("Enter Value", value=1.0, format="%.6g", key="val_in")
        unit_from = st.selectbox("From Unit", units, key="uf")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="conv-card"><div class="card-label">OUTPUT</div>', unsafe_allow_html=True)
        unit_to = st.selectbox("To Unit", units,
                                index=min(1, len(units)-1), key="ut")
        st.markdown("<br>", unsafe_allow_html=True)
        convert_btn = st.button("⚡ CONVERT", key="conv_btn")
        st.markdown("</div>", unsafe_allow_html=True)

    # Perform conversion
    try:
        if is_temp:
            result = convert_temp(value_in, unit_from, unit_to)
            formula = f"{value_in} {unit_from} → {unit_to}"
        else:
            result = do_convert(value_in, unit_from, unit_to)
            if unit_from in FACTORS and unit_to in FACTORS:
                f_from = FACTORS[unit_from]
                f_to   = FACTORS[unit_to]
                ratio  = f_from / f_to
                formula = f"× {ratio:.6g}"
            else:
                formula = ""

        fmt = f"{result:.6g}" if abs(result) < 1e10 else f"{result:.4e}"

        st.markdown(f"""
        <div class="result-box">
            <div class="result-value">{fmt}</div>
            <div class="result-unit">{unit_to}</div>
            <div class="result-formula">
                {value_in} {unit_from} = {fmt} {unit_to} &nbsp;|&nbsp; {formula}
            </div>
        </div>
        """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Conversion error: {e}")

    # Batch conversion table
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("#### 🔢 All Unit Equivalents")
    if is_temp:
        rows = ""
        for u in units:
            try:
                v = convert_temp(value_in, unit_from, u)
                highlight = "highlight" if u == unit_to else ""
                rows += f'<tr class="{highlight}"><td>{u}</td><td>{v:.6g}</td></tr>'
            except:
                pass
    else:
        rows = ""
        try:
            si_val = value_in * FACTORS.get(unit_from, 1)
            for u in units:
                v = si_val / FACTORS.get(u, 1)
                highlight = "highlight" if u == unit_to else ""
                rows += f'<tr class="{highlight}"><td>{u}</td><td>{v:.6g}</td></tr>'
        except:
            rows = "<tr><td colspan='2'>Error</td></tr>"

    st.markdown(f"""
    <table class="density-table">
      <thead><tr><th>UNIT</th><th>VALUE</th></tr></thead>
      <tbody>{rows}</tbody>
    </table>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════
#  TAB 2 – MATERIAL DENSITY
# ══════════════════════════════════════════════
with tab2:
    st.markdown("### Material Density Lookup & Volume → Mass Calculator")

    col_a, col_b = st.columns([1, 1], gap="large")

    with col_a:
        st.markdown('<div class="conv-card"><div class="card-label">SELECT MATERIAL</div>', unsafe_allow_html=True)
        search = st.text_input("🔍 Filter materials", placeholder="e.g. steel, aluminum…")
        filtered = {k: v for k, v in MATERIALS.items()
                    if search.lower() in k.lower()} if search else MATERIALS
        mat = st.selectbox("Material", list(filtered.keys()))
        density = MATERIALS[mat]
        st.markdown(f"""
        <div class="result-box" style="margin-top:16px">
            <div class="result-value">{density:,}</div>
            <div class="result-unit">kg/m³</div>
            <div class="result-formula">{density/1000:.4f} g/cm³ &nbsp;|&nbsp; {density*0.062428:.4f} lb/ft³</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col_b:
        st.markdown('<div class="conv-card"><div class="card-label">MASS / VOLUME CALCULATOR</div>', unsafe_allow_html=True)
        calc_mode = st.radio("Calculate", ["Mass from Volume", "Volume from Mass"], horizontal=True)
        shape = st.selectbox("Shape", ["Custom Volume (m³)", "Rectangular Block", "Cylinder", "Sphere", "Hollow Cylinder"])

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
            H = c2.number_input("Height (m)", value=0.2, format="%.4f", min_value=0.0)
            vol_m3 = math.pi * R**2 * H

        elif shape == "Sphere":
            R = st.number_input("Radius (m)", value=0.05, format="%.4f", min_value=0.0)
            vol_m3 = (4/3) * math.pi * R**3

        elif shape == "Hollow Cylinder":
            c1, c2, c3 = st.columns(3)
            Ro = c1.number_input("Outer R (m)", value=0.06, format="%.4f", min_value=0.0)
            Ri = c2.number_input("Inner R (m)", value=0.04, format="%.4f", min_value=0.0)
            H  = c3.number_input("Height (m)",  value=0.2,  format="%.4f", min_value=0.0)
            vol_m3 = math.pi * (Ro**2 - Ri**2) * H

        if calc_mode == "Mass from Volume":
            mass_kg = density * vol_m3
            st.markdown(f"""
            <div class="result-box" style="margin-top:16px">
                <div style="font-family:'Share Tech Mono';font-size:12px;color:#5a7a9a;margin-bottom:4px">CALCULATED MASS</div>
                <div class="result-value">{mass_kg:.4f} kg</div>
                <div class="result-unit">{mass_kg*1000:.2f} g &nbsp;|&nbsp; {mass_kg*2.20462:.4f} lb</div>
                <div class="result-formula">V = {vol_m3:.6f} m³ &nbsp;×&nbsp; ρ = {density} kg/m³</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            mass_in = st.number_input("Mass (kg)", value=1.0, format="%.4f", min_value=0.0)
            vol_calc = mass_in / density if density else 0
            st.markdown(f"""
            <div class="result-box" style="margin-top:8px">
                <div style="font-family:'Share Tech Mono';font-size:12px;color:#5a7a9a;margin-bottom:4px">CALCULATED VOLUME</div>
                <div class="result-value">{vol_calc:.6f} m³</div>
                <div class="result-unit">{vol_calc*1e6:.4f} cm³ &nbsp;|&nbsp; {vol_calc*1e9:.4f} mm³</div>
                <div class="result-formula">m = {mass_in} kg &nbsp;÷&nbsp; ρ = {density} kg/m³</div>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Full density table
    st.markdown("<br>#### 📋 Full Material Database")
    cat_filter = st.multiselect("Show categories", ["Metals", "Polymers", "Composites/Ceramics", "Natural"],
                                 default=["Metals", "Polymers", "Composites/Ceramics", "Natural"])

    metal_keys    = list(MATERIALS.keys())[:18]
    polymer_keys  = list(MATERIALS.keys())[18:26]
    comp_keys     = list(MATERIALS.keys())[26:33]
    natural_keys  = list(MATERIALS.keys())[33:]

    show = []
    if "Metals"               in cat_filter: show += metal_keys
    if "Polymers"             in cat_filter: show += polymer_keys
    if "Composites/Ceramics"  in cat_filter: show += comp_keys
    if "Natural"              in cat_filter: show += natural_keys

    rows = ""
    for k in show:
        v = MATERIALS[k]
        hl = "highlight" if k == mat else ""
        rows += f'<tr class="{hl}"><td>{k}</td><td>{v:,.3f}</td><td>{v/1000:.4f}</td><td>{v*0.062428:.4f}</td></tr>'

    st.markdown(f"""
    <table class="density-table">
      <thead><tr>
        <th>MATERIAL</th><th>kg/m³</th><th>g/cm³</th><th>lb/ft³</th>
      </tr></thead>
      <tbody>{rows}</tbody>
    </table>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════
#  TAB 3 – QUICK REFERENCE
# ══════════════════════════════════════════════
with tab3:
    st.markdown("### 📐 Engineering Quick Reference")

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("#### ⚡ Key Constants")
        constants = {
            "g (Gravity)":           "9.80665 m/s²",
            "R (Gas constant)":      "8.314 J/(mol·K)",
            "σ (Stefan-Boltzmann)":  "5.67×10⁻⁸ W/(m²·K⁴)",
            "E_steel (Young's)":     "200 GPa",
            "E_aluminum (Young's)":  "69 GPa",
            "ν_steel (Poisson)":     "0.30",
            "ν_aluminum (Poisson)":  "0.33",
            "1 atm":                 "101,325 Pa",
            "1 cal":                 "4.184 J",
            "1 hp":                  "745.7 W",
        }
        rows = "".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in constants.items())
        st.markdown(f"""<table class="density-table">
          <thead><tr><th>CONSTANT</th><th>VALUE</th></tr></thead>
          <tbody>{rows}</tbody></table>""", unsafe_allow_html=True)

    with col2:
        st.markdown("#### 🔩 Stress & Strength Reference")
        strengths = {
            "Steel (Mild) UTS":     "400–550 MPa",
            "Steel (High) UTS":     "800–2000 MPa",
            "Aluminum 6061 UTS":    "310 MPa",
            "Titanium Ti-6Al-4V":   "950 MPa",
            "CFRP (Composite)":     "600–1500 MPa",
            "Concrete (Compress)":  "20–50 MPa",
            "Copper UTS":           "210–400 MPa",
            "Nylon 6 UTS":          "75–85 MPa",
            "ABS Plastic UTS":      "40–55 MPa",
            "Cast Iron UTS":        "150–400 MPa",
        }
        rows = "".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k, v in strengths.items())
        st.markdown(f"""<table class="density-table">
          <thead><tr><th>MATERIAL</th><th>STRENGTH</th></tr></thead>
          <tbody>{rows}</tbody></table>""", unsafe_allow_html=True)

    st.markdown("<br>#### 🧮 Useful Mechanical Formulas")
    formulas = [
        ("Stress",             "σ = F / A",             "Pa = N / m²"),
        ("Strain",             "ε = ΔL / L₀",           "dimensionless"),
        ("Young's Modulus",    "E = σ / ε",              "Pa"),
        ("Torque",             "T = F × r",              "N·m"),
        ("Power",              "P = T × ω",              "W"),
        ("Pressure",           "p = F / A",              "Pa"),
        ("Bernoulli",          "p + ½ρv² + ρgh = const","Pa"),
        ("Reynolds Number",    "Re = ρvD / μ",           "dimensionless"),
        ("Thermal Stress",     "σ = E × α × ΔT",         "Pa"),
        ("Shear Stress",       "τ = T × r / J",          "Pa"),
    ]
    rows = "".join(f"<tr><td>{n}</td><td>{f}</td><td>{u}</td></tr>"
                   for n, f, u in formulas)
    st.markdown(f"""<table class="density-table">
      <thead><tr><th>FORMULA</th><th>EXPRESSION</th><th>UNIT</th></tr></thead>
      <tbody>{rows}</tbody></table>""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  FOOTER
# ─────────────────────────────────────────────
st.markdown("""
<div class="footer">
    ⚙ Mechanical Unit Converter & Material Density Checker &nbsp;|&nbsp;
    Muhammad Bin Akrma &nbsp;|&nbsp; Roll No: 25-ME-59 &nbsp;|&nbsp;
    Built with Streamlit &amp; Python
</div>
""", unsafe_allow_html=True)
