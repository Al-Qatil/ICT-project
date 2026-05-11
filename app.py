import streamlit as st
import math

st.set_page_config(
    page_title="Mech Toolkit | UET Taxila | 25-ME-59",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ══════════════════════════════════════════════
#  FULL CSS
# ══════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Poppins:wght@400;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root {
    --bg:           #f5f7fa;
    --surface:      #ffffff;
    --border:       #e2e8f0;
    --accent:       #1e40af;
    --accent2:      #3b82f6;
    --accent-light: #dbeafe;
    --accent-ultra: #eff6ff;
    --gold:         #b45309;
    --gold-bg:      #fef3c7;
    --green:        #065f46;
    --green-bg:     #d1fae5;
    --red:          #991b1b;
    --red-bg:       #fee2e2;
    --purple:       #5b21b6;
    --purple-bg:    #ede9fe;
    --text:         #0f172a;
    --text2:        #334155;
    --muted:        #64748b;
    --muted2:       #94a3b8;
    --sh1:          0 1px 3px rgba(0,0,0,.07), 0 1px 2px rgba(0,0,0,.04);
    --sh2:          0 4px 20px rgba(0,0,0,.07), 0 2px 6px rgba(0,0,0,.04);
    --sh3:          0 10px 40px rgba(0,0,0,.09), 0 4px 12px rgba(0,0,0,.05);
    --r:            16px;
    --r-sm:         10px;
}

html, body, .stApp {
    background: var(--bg) !important;
    font-family: 'Inter', sans-serif !important;
    color: var(--text) !important;
}
.stApp {
    background-image:
        radial-gradient(ellipse 60% 40% at 10% 0%, rgba(30,64,175,.08) 0%, transparent 60%),
        radial-gradient(ellipse 50% 40% at 90% 100%, rgba(59,130,246,.06) 0%, transparent 55%) !important;
    background-color: #f5f7fa !important;
}

/* ── UET Banner ── */
.uet-top-bar {
    background: linear-gradient(90deg, #1e3a8a 0%, #1e40af 50%, #1d4ed8 100%);
    border-radius: 14px 14px 0 0;
    padding: 10px 28px;
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 0;
}
.uet-logo-svg { flex-shrink: 0; }
.uet-name-block { flex: 1; }
.uet-name {
    font-family: 'Poppins', sans-serif;
    font-size: 15px; font-weight: 700;
    color: #ffffff; letter-spacing: .3px; line-height: 1.2;
}
.uet-name-sub {
    font-size: 11px; color: rgba(255,255,255,.65);
    letter-spacing: .5px; margin-top: 1px;
}
.uet-dept {
    font-size: 11px; font-weight: 600;
    background: rgba(255,255,255,.15);
    border: 1px solid rgba(255,255,255,.25);
    border-radius: 20px; padding: 4px 14px;
    color: rgba(255,255,255,.90); white-space: nowrap;
}

/* ── Hero ── */
.hero-banner {
    background: linear-gradient(135deg, #1e3a8a 0%, #1e40af 40%, #2563eb 75%, #3b82f6 100%);
    border-radius: 0 0 16px 16px;
    padding: 32px 40px 36px;
    margin-bottom: 24px;
    position: relative;
    overflow: hidden;
    box-shadow: var(--sh3);
}
.hero-banner::before {
    content:'⚙'; position:absolute; right:-10px; top:-20px;
    font-size:200px; opacity:.05; color:#fff; line-height:1; pointer-events:none;
}
.hero-banner::after {
    content:''; position:absolute; bottom:-60px; left:-40px;
    width:220px; height:220px; border-radius:50%;
    background:rgba(255,255,255,.04); pointer-events:none;
}
.hero-eyebrow {
    font-size:11px; font-weight:700; letter-spacing:3px;
    text-transform:uppercase; color:rgba(255,255,255,.55); margin-bottom:8px;
}
.hero-title {
    font-family:'Poppins',sans-serif;
    font-size:clamp(20px,3vw,36px); font-weight:800;
    color:#ffffff; line-height:1.2; margin:0 0 8px; letter-spacing:-.3px;
}
.hero-title span { color:rgba(255,255,255,.75); font-weight:500; }
.hero-desc { font-size:13px; color:rgba(255,255,255,.65); margin-bottom:20px; max-width:600px; }
.badge-row { display:flex; gap:9px; flex-wrap:wrap; }
.badge {
    background:rgba(255,255,255,.15); backdrop-filter:blur(6px);
    border:1px solid rgba(255,255,255,.22); border-radius:20px;
    padding:5px 16px; font-size:12px; font-weight:600; color:#fff;
}
.badge.gold  { background:rgba(180,83,9,.3); border-color:rgba(251,191,36,.4); color:#fde68a; }
.badge.green { background:rgba(6,95,70,.3);  border-color:rgba(52,211,153,.4); color:#6ee7b7; }

/* ── Stat chips ── */
.stat-row { display:flex; gap:12px; flex-wrap:wrap; margin-bottom:24px; }
.stat-chip {
    background:var(--surface); border:1px solid var(--border);
    border-radius:14px; padding:14px 18px;
    display:flex; align-items:center; gap:13px;
    box-shadow:var(--sh1); flex:1; min-width:140px;
    transition: box-shadow .2s, transform .15s;
}
.stat-chip:hover { box-shadow:var(--sh2); transform:translateY(-1px); }
.stat-icon {
    width:44px; height:44px; border-radius:11px;
    display:flex; align-items:center; justify-content:center; font-size:20px; flex-shrink:0;
}
.si-b { background:var(--accent-light); }
.si-g { background:var(--green-bg); }
.si-o { background:var(--gold-bg); }
.si-p { background:var(--purple-bg); }
.si-r { background:var(--red-bg); }
.stat-num { font-size:22px; font-weight:800; color:var(--text); line-height:1; font-family:'Poppins',sans-serif; }
.stat-lbl { font-size:11px; color:var(--muted); font-weight:500; margin-top:2px; }

/* ── Section heading ── */
.sh {
    font-family:'Poppins',sans-serif; font-size:14px; font-weight:700;
    color:var(--text); margin:0 0 16px;
    display:flex; align-items:center; gap:10px;
}
.sh::after { content:''; flex:1; height:1px; background:var(--border); }

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    background:var(--surface) !important; border-radius:14px !important;
    border:1px solid var(--border) !important; padding:5px !important;
    gap:3px !important; box-shadow:var(--sh1) !important;
    margin-bottom: 24px !important;
}
.stTabs [data-baseweb="tab"] {
    font-family:'Inter',sans-serif !important; font-size:13px !important;
    font-weight:600 !important; color:var(--muted) !important;
    background:transparent !important; border-radius:10px !important;
    padding:10px 22px !important; border:none !important; transition:all .2s !important;
}
.stTabs [aria-selected="true"] {
    background:var(--accent) !important; color:#fff !important;
    box-shadow:0 3px 12px rgba(30,64,175,.35) !important;
}

/* ── Panel ── */
.panel {
    background:var(--surface); border:1px solid var(--border);
    border-radius:var(--r); padding:24px; margin-bottom:16px;
    box-shadow:var(--sh1); transition:box-shadow .2s, border-color .2s;
}
.panel:hover { box-shadow:var(--sh2); border-color:#c7d7eb; }
.panel-title {
    font-size:10px; font-weight:800; letter-spacing:2px; text-transform:uppercase;
    color:var(--accent2); margin-bottom:18px; display:flex; align-items:center; gap:8px;
}
.pt-dot { width:7px; height:7px; border-radius:50%; background:var(--accent2); flex-shrink:0; }

/* ── Result box ── */
.result-box {
    background:linear-gradient(135deg, #dbeafe 0%, #eff6ff 100%);
    border:1.5px solid rgba(59,130,246,.25); border-radius:14px;
    padding:28px 24px; text-align:center; position:relative; overflow:hidden;
    box-shadow: 0 2px 12px rgba(59,130,246,.1);
}
.result-box::before {
    content:''; position:absolute; top:-50px; right:-50px;
    width:150px; height:150px; border-radius:50%;
    background:rgba(59,130,246,.06); pointer-events:none;
}
.res-label { font-size:10px; font-weight:800; letter-spacing:2.5px; text-transform:uppercase; color:var(--accent2); margin-bottom:8px; }
.res-val { font-family:'JetBrains Mono',monospace; font-size:clamp(26px,4.5vw,48px); font-weight:700; color:var(--accent); line-height:1; word-break:break-all; }
.res-unit { font-size:16px; font-weight:600; color:var(--muted); margin-top:6px; }
.res-formula {
    font-family:'JetBrains Mono',monospace; font-size:11px; color:var(--green);
    margin-top:12px; background:var(--green-bg); display:inline-block;
    padding:4px 14px; border-radius:6px; font-weight:600;
}
.res-secondary {
    font-size:11px; color:var(--muted); margin-top:8px;
    font-family:'JetBrains Mono',monospace;
}

/* ── Density result ── */
.density-result {
    background:linear-gradient(135deg, #fef9c3 0%, #fffde7 100%);
    border:1.5px solid rgba(180,83,9,.2); border-radius:14px;
    padding:22px; text-align:center; margin-top:14px;
    box-shadow: 0 2px 10px rgba(180,83,9,.08);
}
.density-result .res-val   { color:var(--gold); }
.density-result .res-label { color:var(--gold); }
.d-tag {
    font-family:'JetBrains Mono',monospace; font-size:11px; font-weight:600;
    background:#fef3c7; color:#92400e; display:inline-block;
    padding:4px 14px; border-radius:6px; margin-top:10px;
}

/* ── Info cards (quick ref) ── */
.info-card {
    background:var(--surface); border:1px solid var(--border);
    border-radius:var(--r); padding:20px 22px; margin-bottom:14px;
    box-shadow:var(--sh1);
}
.info-card-title {
    font-size:11px; font-weight:800; letter-spacing:1.5px;
    text-transform:uppercase; margin-bottom:14px;
    display:flex; align-items:center; gap:8px;
}

/* ── Tables ── */
.tw { background:var(--surface); border:1px solid var(--border); border-radius:var(--r); overflow:hidden; box-shadow:var(--sh1); overflow-x:auto; }
.dt { width:100%; border-collapse:collapse; font-size:13px; }
.dt thead tr { background:var(--accent); }
.dt th { padding:11px 18px; text-align:left; font-size:10px; font-weight:700; letter-spacing:1.5px; text-transform:uppercase; color:#fff; }
.dt td { padding:10px 18px; color:var(--text2); border-bottom:1px solid #f1f5f9; font-family:'JetBrains Mono',monospace; font-size:12px; }
.dt td:first-child { font-family:'Inter',sans-serif; font-weight:600; color:var(--text); font-size:13px; }
.dt tbody tr:hover td { background:#f8faff; }
.dt .hl td { background:var(--green-bg) !important; color:var(--green) !important; font-weight:700; }
.dt tbody tr:last-child td { border-bottom:none; }

/* ── Arrow ── */
.arrow { display:flex; align-items:center; justify-content:center; height:100%; padding-top:40px; font-size:28px; color:var(--muted2); }

/* ── Widgets ── */
div[data-testid="stNumberInput"] input,
div[data-testid="stTextInput"] input {
    background:#f8fafc !important; border:1.5px solid var(--border) !important;
    border-radius:var(--r-sm) !important; color:var(--text) !important;
    font-family:'JetBrains Mono',monospace !important; font-size:15px !important;
    padding:10px 14px !important; transition:border-color .2s, box-shadow .2s !important;
}
div[data-testid="stNumberInput"] input:focus,
div[data-testid="stTextInput"] input:focus {
    border-color:var(--accent2) !important;
    box-shadow:0 0 0 3px rgba(59,130,246,.15) !important;
    background:#fff !important; outline:none !important;
}
div[data-testid="stSelectbox"] > div > div {
    background:#f8fafc !important; border:1.5px solid var(--border) !important;
    border-radius:var(--r-sm) !important; color:var(--text) !important; font-size:14px !important;
}
label, .stSelectbox label, .stNumberInput label {
    font-family:'Inter',sans-serif !important; font-size:11px !important;
    font-weight:700 !important; color:var(--muted) !important;
    text-transform:uppercase !important; letter-spacing:.8px !important;
}
.stRadio > div { gap:10px !important; }
.stRadio label { text-transform:none !important; letter-spacing:0 !important; font-size:13px !important; font-weight:500 !important; }

/* ── Buttons ── */
.stButton > button {
    background:var(--accent) !important; color:#fff !important;
    border:none !important; border-radius:var(--r-sm) !important;
    font-family:'Inter',sans-serif !important; font-size:13px !important;
    font-weight:700 !important; letter-spacing:.4px !important;
    padding:13px 28px !important; width:100% !important;
    transition:all .2s !important; box-shadow:0 4px 14px rgba(30,64,175,.28) !important;
}
.stButton > button:hover {
    background:#1d4ed8 !important;
    box-shadow:0 6px 22px rgba(30,64,175,.40) !important;
    transform:translateY(-1px) !important;
}

/* ── Formula pill ── */
.formula-pill {
    display:inline-flex; align-items:center; gap:8px;
    background:var(--purple-bg); border:1px solid rgba(91,33,182,.15);
    border-radius:8px; padding:8px 14px; margin:4px;
    font-family:'JetBrains Mono',monospace; font-size:13px; color:var(--purple);
    font-weight:600;
}

/* ── Comparison table colors ── */
.cmp-low  { color:var(--green) !important; font-weight:700 !important; }
.cmp-mid  { color:var(--gold) !important; font-weight:700 !important; }
.cmp-high { color:var(--red) !important; font-weight:700 !important; }

/* ── Footer ── */
.footer {
    background:var(--surface); border:1px solid var(--border); border-radius:var(--r);
    padding:16px 28px; margin-top:36px;
    display:flex; align-items:center; justify-content:center; flex-wrap:wrap;
    gap:8px; font-size:12px; color:var(--muted); font-weight:500;
    box-shadow:var(--sh1);
}
.footer strong { color:var(--accent); }
.footer .s { color:#e2e8f0; margin:0 2px; }

::-webkit-scrollbar { width:6px; height:6px; }
::-webkit-scrollbar-track { background:var(--bg); }
::-webkit-scrollbar-thumb { background:#cbd5e1; border-radius:3px; }
#MainMenu, footer, header { visibility:hidden; }
.block-container { padding-top:1.5rem !important; padding-bottom:1rem !important; }
div[data-testid="stVerticalBlock"] { gap: 0 !important; }
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════
#  DATA
# ══════════════════════════════════════════════
MATERIALS = {
    "Steel (Carbon)": 7850, "Steel (Stainless 304)": 8000, "Steel (Tool)": 7750,
    "Aluminum (Pure)": 2700, "Aluminum Alloy (6061)": 2700, "Aluminum Alloy (7075)": 2810,
    "Copper": 8960, "Brass": 8500, "Bronze": 8800,
    "Cast Iron (Gray)": 7200, "Cast Iron (Ductile)": 7100,
    "Titanium (Grade 5)": 4430, "Nickel": 8908, "Lead": 11340,
    "Zinc": 7133, "Magnesium": 1738, "Gold": 19300, "Silver": 10490,
    "Tungsten": 19250, "Chromium": 7190, "Molybdenum": 10220, "Inconel 718": 8190,
    "ABS Plastic": 1050, "Nylon (PA6)": 1140, "Polycarbonate (PC)": 1200,
    "HDPE": 950, "PTFE (Teflon)": 2200, "PVC (Rigid)": 1400,
    "Epoxy Resin": 1250, "Polypropylene (PP)": 905, "PET": 1380,
    "Carbon Fiber Composite": 1600, "Fiberglass (GFRP)": 1900,
    "Concrete": 2400, "Granite": 2700, "Glass (Borosilicate)": 2230,
    "Silicon Carbide (SiC)": 3210, "Alumina (Al₂O₃)": 3960, "Zirconia": 5680,
    "Oak Wood": 700, "Balsa Wood": 120, "Rubber (Natural)": 920,
    "Cork": 120, "Ice": 917, "Water": 1000, "Air (at STP)": 1.225,
    "Diesel Fuel": 850, "Engine Oil (SAE 30)": 875,
}

CATEGORIES = {
    "⚖️  Force":             ("N",    ["N","kN","MN","lbf","kgf","dyn","ozf"]),
    "📏  Length":            ("m",    ["m","cm","mm","km","in","ft","yd","mi","μm","nm"]),
    "⚡  Pressure":          ("Pa",   ["Pa","kPa","MPa","GPa","bar","mbar","atm","psi","ksi","torr","mmHg"]),
    "🔁  Torque":            ("N·m",  ["N·m","kN·m","N·cm","N·mm","lbf·ft","lbf·in","kgf·m"]),
    "🏎️  Velocity":          ("m/s",  ["m/s","km/h","ft/s","mph","knot","ft/min"]),
    "🌡️  Temperature":       ("°C",   ["°C","°F","K","°R"]),
    "💡  Power":             ("W",    ["W","kW","MW","hp (mech)","hp (elec)","BTU/hr","cal/s","ton (refrig)"]),
    "🔩  Stress / Strength": ("Pa",   ["Pa","kPa","MPa","GPa","psi","ksi"]),
    "📦  Mass":              ("kg",   ["kg","g","mg","t (metric)","lb","oz","slug","grain"]),
    "🌀  Angular Velocity":  ("rad/s",["rad/s","rpm","deg/s","rev/s","rev/min"]),
    "💧  Dynamic Viscosity": ("Pa·s", ["Pa·s","cP","mPa·s","μPa·s","lbf·s/ft²","P"]),
    "🌊  Kinematic Viscosity":("m²/s",["m²/s","mm²/s (cSt)","ft²/s","in²/s"]),
    "⚡  Energy / Work":     ("J",    ["J","kJ","MJ","cal","kcal","BTU","kWh","MWh","eV","ft·lbf"]),
    "🔥  Heat Flux":         ("W/m²", ["W/m²","kW/m²","BTU/(hr·ft²)","cal/(s·cm²)"]),
    "📐  Area":              ("m²",   ["m²","cm²","mm²","km²","in²","ft²","yd²","acre","hectare"]),
    "🧊  Volume":            ("m³",   ["m³","cm³","mm³","L","mL","in³","ft³","gal (US)","gal (UK)","fl oz"]),
}

FACTORS = {
    # Force
    "N":1,"kN":1e3,"MN":1e6,"lbf":4.44822,"kgf":9.80665,"dyn":1e-5,"ozf":0.278014,
    # Length
    "m":1,"cm":0.01,"mm":0.001,"km":1000,"in":0.0254,
    "ft":0.3048,"yd":0.9144,"mi":1609.344,"μm":1e-6,"nm":1e-9,
    # Pressure
    "Pa":1,"kPa":1e3,"MPa":1e6,"GPa":1e9,"bar":1e5,"mbar":100,
    "atm":101325,"psi":6894.757,"ksi":6.894757e6,"torr":133.322,"mmHg":133.322,
    # Torque
    "N·m":1,"kN·m":1e3,"N·cm":0.01,"N·mm":0.001,"lbf·ft":1.35582,"lbf·in":0.112985,"kgf·m":9.80665,
    # Velocity
    "m/s":1,"km/h":1/3.6,"ft/s":0.3048,"mph":0.44704,"knot":0.514444,"ft/min":0.00508,
    # Power
    "W":1,"kW":1e3,"MW":1e6,"hp (mech)":745.7,"hp (elec)":746.0,
    "BTU/hr":0.29307,"cal/s":4.18400,"ton (refrig)":3516.85,
    # Mass
    "kg":1,"g":0.001,"mg":1e-6,"t (metric)":1000,"lb":0.453592,
    "oz":0.0283495,"slug":14.5939,"grain":6.47989e-5,
    # Angular velocity
    "rad/s":1,"rpm":math.pi/30,"deg/s":math.pi/180,"rev/s":2*math.pi,"rev/min":math.pi/30,
    # Dynamic Viscosity
    "Pa·s":1,"cP":0.001,"mPa·s":0.001,"μPa·s":1e-6,"lbf·s/ft²":47.8803,"P":0.1,
    # Kinematic Viscosity
    "m²/s":1,"mm²/s (cSt)":1e-6,"ft²/s":0.0929030,"in²/s":6.4516e-4,
    # Energy
    "J":1,"kJ":1e3,"MJ":1e6,"cal":4.184,"kcal":4184,
    "BTU":1055.06,"kWh":3.6e6,"MWh":3.6e9,"eV":1.60218e-19,"ft·lbf":1.35582,
    # Heat Flux
    "W/m²":1,"kW/m²":1e3,"BTU/(hr·ft²)":3.15459,"cal/(s·cm²)":41840,
    # Area
    "m²":1,"cm²":1e-4,"mm²":1e-6,"km²":1e6,"in²":6.4516e-4,
    "ft²":0.092903,"yd²":0.836127,"acre":4046.86,"hectare":1e4,
    # Volume
    "m³":1,"cm³":1e-6,"mm³":1e-9,"L":0.001,"mL":1e-6,
    "in³":1.6387e-5,"ft³":0.028317,"gal (US)":0.003785,"gal (UK)":0.004546,"fl oz":2.9574e-5,
}

def convert_temp(val, frm, to):
    if frm=="°C":   c=val
    elif frm=="°F": c=(val-32)*5/9
    elif frm=="K":  c=val-273.15
    elif frm=="°R": c=(val-491.67)*5/9
    if to=="°C":   return c
    if to=="°F":   return c*9/5+32
    if to=="K":    return c+273.15
    if to=="°R":   return (c+273.15)*9/5

def do_convert(val, frm, to):
    if frm==to: return val
    return val*FACTORS[frm]/FACTORS[to]

def fmt_num(v):
    if v == 0: return "0"
    if abs(v) >= 1e12 or (abs(v) < 1e-6 and v != 0): return f"{v:.4e}"
    if abs(v) >= 1e6: return f"{v:,.2f}"
    return f"{v:.6g}"

# ══════════════════════════════════════════════
#  UET TOP BAR + HERO
# ══════════════════════════════════════════════
st.markdown("""
<div class="uet-top-bar">
  <!-- SVG Gear / UET Logo placeholder -->
  <svg class="uet-logo-svg" width="52" height="52" viewBox="0 0 52 52" fill="none" xmlns="http://www.w3.org/2000/svg">
    <circle cx="26" cy="26" r="25" fill="rgba(255,255,255,0.12)" stroke="rgba(255,255,255,0.3)" stroke-width="1.5"/>
    <circle cx="26" cy="26" r="8" fill="none" stroke="rgba(255,255,255,0.85)" stroke-width="2.5"/>
    <g stroke="rgba(255,255,255,0.85)" stroke-width="2.5" stroke-linecap="round">
      <line x1="26" y1="6"  x2="26" y2="12"/>
      <line x1="26" y1="40" x2="26" y2="46"/>
      <line x1="6"  y1="26" x2="12" y2="26"/>
      <line x1="40" y1="26" x2="46" y2="26"/>
      <line x1="11.5" y1="11.5" x2="15.7" y2="15.7"/>
      <line x1="36.3" y1="36.3" x2="40.5" y2="40.5"/>
      <line x1="40.5" y1="11.5" x2="36.3" y2="15.7"/>
      <line x1="15.7" y1="36.3" x2="11.5" y2="40.5"/>
    </g>
    <text x="26" y="30" text-anchor="middle" font-size="7" font-weight="700" fill="white" font-family="Arial">UET</text>
  </svg>
  <div class="uet-name-block">
    <div class="uet-name">University of Engineering &amp; Technology, Taxila</div>
    <div class="uet-name-sub">ESTABLISHED 1975 · PAKISTAN</div>
  </div>
  <div class="uet-dept">🔧 Dept. of Mechanical Engineering</div>
</div>

<div class="hero-banner">
    <div class="hero-eyebrow">⚙ Mechanical Engineering Toolkit — Academic Edition</div>
    <div class="hero-title">Unit Converter &amp; <span>Material Density Checker</span></div>
    <div class="hero-desc">A comprehensive precision engineering calculator — 16 unit categories, 45+ materials, shape calculators, and reference charts.</div>
    <div class="badge-row">
        <span class="badge">👤 Muhammad Bin Akrma</span>
        <span class="badge gold">🎓 Roll No: 25-ME-59</span>
        <span class="badge green">✅ Batch 2025</span>
    </div>
</div>
""", unsafe_allow_html=True)

# STATS
st.markdown("""
<div class="stat-row">
  <div class="stat-chip"><div class="stat-icon si-b">📐</div>
    <div><div class="stat-num">16</div><div class="stat-lbl">Unit Categories</div></div></div>
  <div class="stat-chip"><div class="stat-icon si-g">🧱</div>
    <div><div class="stat-num">45+</div><div class="stat-lbl">Materials</div></div></div>
  <div class="stat-chip"><div class="stat-icon si-o">⚡</div>
    <div><div class="stat-num">100+</div><div class="stat-lbl">Unit Pairs</div></div></div>
  <div class="stat-chip"><div class="stat-icon si-p">📐</div>
    <div><div class="stat-num">5</div><div class="stat-lbl">Shape Calcs</div></div></div>
  <div class="stat-chip"><div class="stat-icon si-r">📋</div>
    <div><div class="stat-num">30+</div><div class="stat-lbl">ME Formulas</div></div></div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════
#  TABS
# ══════════════════════════════════════════════
tab1, tab2, tab3, tab4 = st.tabs([
    "⚙️   Unit Converter",
    "🧱   Material Density",
    "📋   Reference & Formulas",
    "🔬   Beam & Stress Calc",
])

# ═══════════════════════
#  TAB 1 — UNIT CONVERTER
# ═══════════════════════
with tab1:
    st.markdown('<p class="sh">⚙️ Select a Category and Convert</p>', unsafe_allow_html=True)

    cat_col, _ = st.columns([3, 1])
    with cat_col:
        cat_name = st.selectbox("Category", list(CATEGORIES.keys()), index=0, label_visibility="collapsed")

    base_unit, units = CATEGORIES[cat_name]
    is_temp = "Temperature" in cat_name

    col1, col2, col3 = st.columns([5, 1, 5], gap="medium")
    with col1:
        st.markdown('<div class="panel"><div class="panel-title"><span class="pt-dot"></span>INPUT</div>', unsafe_allow_html=True)
        value_in  = st.number_input("Value", value=1.0, format="%.6g", key="val_in", label_visibility="collapsed")
        unit_from = st.selectbox("From", units, key="uf")
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="arrow">→</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="panel"><div class="panel-title"><span class="pt-dot"></span>OUTPUT</div>', unsafe_allow_html=True)
        unit_to = st.selectbox("To", units, index=min(1, len(units)-1), key="ut")
        st.button("⚡  Convert", key="conv_btn")
        st.markdown("</div>", unsafe_allow_html=True)

    # Compute & display
    try:
        if is_temp:
            result = convert_temp(value_in, unit_from, unit_to)
            formula_str = f"{fmt_num(value_in)} {unit_from}  →  {fmt_num(result)} {unit_to}"
            secondary = ""
        else:
            result = do_convert(value_in, unit_from, unit_to)
            ratio  = FACTORS.get(unit_from, 1) / FACTORS.get(unit_to, 1)
            formula_str = f"1 {unit_from} = {fmt_num(ratio)} {unit_to}"
            secondary   = f"{fmt_num(value_in)} × {fmt_num(ratio)} = {fmt_num(result)}"

        st.markdown(f"""
        <div class="result-box" style="margin:18px 0 28px">
            <div class="res-label">Converted Result</div>
            <div class="res-val">{fmt_num(result)}</div>
            <div class="res-unit">{unit_to}</div>
            <div class="res-formula">{formula_str}</div>
            <div class="res-secondary">{secondary}</div>
        </div>""", unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Conversion error: {e}")

    # Equivalents table
    st.markdown('<p class="sh">🔢 All Equivalent Values</p>', unsafe_allow_html=True)
    rows = ""
    if is_temp:
        for u in units:
            try:
                v = convert_temp(value_in, unit_from, u)
                hl = "hl" if u == unit_to else ""
                tick = "✓" if u == unit_to else ""
                rows += f'<tr class="{hl}"><td>{u}</td><td>{fmt_num(v)}</td><td style="color:#059669;font-weight:700">{tick}</td></tr>'
            except: pass
    else:
        try:
            si_val = value_in * FACTORS.get(unit_from, 1)
            for u in units:
                v = si_val / FACTORS.get(u, 1)
                hl = "hl" if u == unit_to else ""
                tick = "✓" if u == unit_to else ""
                rows += f'<tr class="{hl}"><td>{u}</td><td>{fmt_num(v)}</td><td style="color:#059669;font-weight:700">{tick}</td></tr>'
        except:
            rows = "<tr><td colspan='3'>Error</td></tr>"

    st.markdown(f"""<div class="tw"><table class="dt">
      <thead><tr><th>Unit</th><th>Value</th><th>Selected</th></tr></thead>
      <tbody>{rows}</tbody></table></div>""", unsafe_allow_html=True)

# ═══════════════════════
#  TAB 2 — DENSITY
# ═══════════════════════
with tab2:
    st.markdown('<p class="sh">🧱 Material Lookup &amp; Mass / Volume Calculator</p>', unsafe_allow_html=True)

    col_a, col_b = st.columns(2, gap="large")

    with col_a:
        st.markdown('<div class="panel"><div class="panel-title"><span class="pt-dot"></span>SELECT MATERIAL</div>', unsafe_allow_html=True)
        search   = st.text_input("🔍 Search", placeholder="e.g. steel, aluminum, copper…", label_visibility="collapsed")
        filtered = {k:v for k,v in MATERIALS.items() if search.lower() in k.lower()} if search else MATERIALS
        if not filtered:
            st.warning("No match — showing all.")
            filtered = MATERIALS
        mat     = st.selectbox("Material", list(filtered.keys()))
        density = MATERIALS[mat]

        # Density category chip
        if density < 500:      d_cat, d_col = "Ultra-Light",  "#059669"
        elif density < 2000:   d_cat, d_col = "Light",        "#0284c7"
        elif density < 5000:   d_cat, d_col = "Medium",       "#d97706"
        elif density < 10000:  d_cat, d_col = "Heavy",        "#b45309"
        else:                  d_cat, d_col = "Very Heavy",   "#991b1b"

        st.markdown(f"""
        <div class="density-result">
            <div class="res-label">Density</div>
            <div class="res-val">{density:,}</div>
            <div class="res-unit">kg / m³</div>
            <div class="d-tag">{density/1000:.4f} g/cm³ &nbsp;·&nbsp; {density*0.062428:.4f} lb/ft³</div>
            <div style="margin-top:10px;font-size:12px;font-weight:700;color:{d_col}">{d_cat} Material</div>
        </div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col_b:
        st.markdown('<div class="panel"><div class="panel-title"><span class="pt-dot"></span>MASS / VOLUME CALCULATOR</div>', unsafe_allow_html=True)
        calc_mode = st.radio("Mode", ["Mass from Volume", "Volume from Mass"], horizontal=True)
        shape     = st.selectbox("Geometry", ["Custom Volume (m³)", "Rectangular Block",
                                               "Cylinder", "Sphere", "Hollow Cylinder",
                                               "Hollow Sphere", "Triangular Prism"])
        vol_m3 = 0.0
        if shape == "Custom Volume (m³)":
            vol_m3 = st.number_input("Volume (m³)", value=0.001, format="%.8f", min_value=0.0)
        elif shape == "Rectangular Block":
            c1, c2, c3 = st.columns(3)
            L=c1.number_input("L (m)",value=0.1,format="%.4f",min_value=0.0)
            W=c2.number_input("W (m)",value=0.1,format="%.4f",min_value=0.0)
            H=c3.number_input("H (m)",value=0.1,format="%.4f",min_value=0.0)
            vol_m3 = L*W*H
        elif shape == "Cylinder":
            c1,c2=st.columns(2)
            R=c1.number_input("Radius (m)",value=0.05,format="%.4f",min_value=0.0)
            H=c2.number_input("Height (m)",value=0.20,format="%.4f",min_value=0.0)
            vol_m3=math.pi*R**2*H
        elif shape == "Sphere":
            R=st.number_input("Radius (m)",value=0.05,format="%.4f",min_value=0.0)
            vol_m3=(4/3)*math.pi*R**3
        elif shape == "Hollow Cylinder":
            c1,c2,c3=st.columns(3)
            Ro=c1.number_input("Outer R (m)",value=0.06,format="%.4f",min_value=0.0)
            Ri=c2.number_input("Inner R (m)",value=0.04,format="%.4f",min_value=0.0)
            H =c3.number_input("Height (m)", value=0.20,format="%.4f",min_value=0.0)
            vol_m3=math.pi*(Ro**2-Ri**2)*H
        elif shape == "Hollow Sphere":
            c1,c2=st.columns(2)
            Ro=c1.number_input("Outer R (m)",value=0.06,format="%.4f",min_value=0.0)
            Ri=c2.number_input("Inner R (m)",value=0.04,format="%.4f",min_value=0.0)
            vol_m3=(4/3)*math.pi*(Ro**3-Ri**3)
        elif shape == "Triangular Prism":
            c1,c2,c3=st.columns(3)
            b=c1.number_input("Base (m)", value=0.1,format="%.4f",min_value=0.0)
            h=c2.number_input("Height (m)",value=0.1,format="%.4f",min_value=0.0)
            l=c3.number_input("Length (m)",value=0.2,format="%.4f",min_value=0.0)
            vol_m3=0.5*b*h*l

        if calc_mode == "Mass from Volume":
            mass_kg = density * vol_m3
            st.markdown(f"""
            <div class="result-box" style="margin-top:16px">
                <div class="res-label">Calculated Mass</div>
                <div class="res-val">{mass_kg:.4f}</div>
                <div class="res-unit">kg</div>
                <div class="res-formula">{mass_kg*1000:.3f} g &nbsp;·&nbsp; {mass_kg*2.20462:.4f} lb &nbsp;·&nbsp; {mass_kg*1000/1000:.4f} t</div>
                <div class="res-secondary">V = {vol_m3:.6f} m³ × ρ = {density:,} kg/m³</div>
            </div>""", unsafe_allow_html=True)
        else:
            mass_in  = st.number_input("Mass (kg)", value=1.0, format="%.4f", min_value=0.0)
            vol_calc = mass_in / density if density else 0
            st.markdown(f"""
            <div class="result-box" style="margin-top:10px">
                <div class="res-label">Calculated Volume</div>
                <div class="res-val">{vol_calc:.6f}</div>
                <div class="res-unit">m³</div>
                <div class="res-formula">{vol_calc*1e6:.4f} cm³ &nbsp;·&nbsp; {vol_calc*1e9:.4f} mm³ &nbsp;·&nbsp; {vol_calc*1000:.5f} L</div>
                <div class="res-secondary">m = {mass_in} kg ÷ ρ = {density:,} kg/m³</div>
            </div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Material comparison
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<p class="sh">🔍 Compare Materials Side-by-Side</p>', unsafe_allow_html=True)
    cmp_cols = st.columns(3)
    cmp_mats = []
    for i, col in enumerate(cmp_cols):
        with col:
            m = col.selectbox(f"Material {i+1}", list(MATERIALS.keys()),
                              index=i*5, key=f"cmp{i}")
            cmp_mats.append(m)

    if len(cmp_mats) == 3:
        rows = ""
        props = [
            ("Density", lambda m: f"{MATERIALS[m]:,} kg/m³"),
            ("g/cm³",   lambda m: f"{MATERIALS[m]/1000:.4f}"),
            ("lb/ft³",  lambda m: f"{MATERIALS[m]*0.062428:.3f}"),
        ]
        for label, fn in props:
            vals = [MATERIALS[m] for m in cmp_mats]
            mn, mx = min(vals), max(vals)
            def cls(v):
                if v == mn: return "cmp-low"
                if v == mx: return "cmp-high"
                return "cmp-mid"
            cells = "".join(f'<td class="{cls(MATERIALS[m])}">{fn(m)}</td>' for m in cmp_mats)
            rows += f"<tr><td>{label}</td>{cells}</tr>"

        hdrs = "".join(f"<th>{m}</th>" for m in cmp_mats)
        st.markdown(f"""<div class="tw"><table class="dt">
          <thead><tr><th>Property</th>{hdrs}</tr></thead>
          <tbody>{rows}</tbody></table></div>""", unsafe_allow_html=True)

    # Full DB
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<p class="sh">📋 Full Material Database</p>', unsafe_allow_html=True)
    cats = st.multiselect("Filter", ["Metals","Polymers","Composites & Ceramics","Natural & Other"],
                          default=["Metals","Polymers","Composites & Ceramics","Natural & Other"])
    mk = list(MATERIALS.keys())
    km = {"Metals":mk[:22],"Polymers":mk[22:31],"Composites & Ceramics":mk[31:39],"Natural & Other":mk[39:]}
    show = []
    for c in cats: show += km.get(c, [])
    rows = "".join(
        f'<tr class="{"hl" if k==mat else ""}"><td>{k}</td><td>{v:,.3f}</td><td>{v/1000:.4f}</td><td>{v*0.062428:.4f}</td></tr>'
        for k in show for v in [MATERIALS[k]]
    )
    st.markdown(f"""<div class="tw"><table class="dt">
      <thead><tr><th>Material</th><th>kg/m³</th><th>g/cm³</th><th>lb/ft³</th></tr></thead>
      <tbody>{rows}</tbody></table></div>""", unsafe_allow_html=True)

# ═══════════════════════
#  TAB 3 — REFERENCE
# ═══════════════════════
with tab3:
    c1, c2 = st.columns(2, gap="large")

    with c1:
        st.markdown('<p class="sh">⚡ Key Engineering Constants</p>', unsafe_allow_html=True)
        consts = {
            "g — Standard Gravity":       "9.80665 m/s²",
            "G — Gravitational Const.":   "6.674×10⁻¹¹ N·m²/kg²",
            "R — Universal Gas Const.":   "8.314 J/(mol·K)",
            "NA — Avogadro's Number":     "6.022×10²³ mol⁻¹",
            "σ — Stefan-Boltzmann":       "5.67×10⁻⁸ W/(m²·K⁴)",
            "k — Boltzmann Const.":       "1.381×10⁻²³ J/K",
            "E_steel (Young's Mod.)":     "200 GPa",
            "E_aluminum (Young's Mod.)":  "69 GPa",
            "E_titanium (Young's Mod.)":  "116 GPa",
            "ν_steel (Poisson)":          "0.30",
            "ν_aluminum (Poisson)":       "0.33",
            "1 atm":                      "101,325 Pa",
            "1 hp (mechanical)":          "745.7 W",
            "1 BTU":                      "1,055.06 J",
            "0 °C (in Kelvin)":           "273.15 K",
        }
        rows = "".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k,v in consts.items())
        st.markdown(f"""<div class="tw"><table class="dt">
          <thead><tr><th>Constant</th><th>Value</th></tr></thead>
          <tbody>{rows}</tbody></table></div>""", unsafe_allow_html=True)

    with c2:
        st.markdown('<p class="sh">🔩 Material Strength Reference</p>', unsafe_allow_html=True)
        strengths = {
            "Steel (Mild) — UTS":       "400–550 MPa",
            "Steel (High-Strength)":    "800–2000 MPa",
            "Aluminum 6061-T6":         "310 MPa",
            "Aluminum 7075-T6":         "572 MPa",
            "Titanium Ti-6Al-4V":       "950 MPa",
            "Inconel 718":              "1240 MPa",
            "CFRP (Carbon Composite)":  "600–1500 MPa",
            "Fiberglass (GFRP)":        "300–400 MPa",
            "Concrete (Compression)":   "20–50 MPa",
            "Copper":                   "210–400 MPa",
            "Brass (70/30)":            "370–500 MPa",
            "Nylon 6 UTS":              "75–85 MPa",
            "ABS Plastic UTS":          "40–55 MPa",
            "Cast Iron (Gray)":         "150–400 MPa",
        }
        rows = "".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k,v in strengths.items())
        st.markdown(f"""<div class="tw"><table class="dt">
          <thead><tr><th>Material</th><th>UTS / Strength</th></tr></thead>
          <tbody>{rows}</tbody></table></div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<p class="sh">🧮 Core Mechanical Engineering Formulas</p>', unsafe_allow_html=True)

    formulas = [
        ("Stress",           "σ = F / A",                   "Pa",             "F=Force(N), A=Area(m²)"),
        ("Strain",           "ε = ΔL / L₀",                 "dimensionless",  "ΔL=deformation, L₀=original length"),
        ("Young's Modulus",  "E = σ / ε",                   "Pa",             "Ratio of stress to strain"),
        ("Shear Stress",     "τ = F / A",                    "Pa",             "F=shear force, A=cross-section"),
        ("Torque",           "T = F × r",                    "N·m",            "r=radius from axis"),
        ("Power",            "P = T × ω = F × v",            "W",              "ω=angular velocity (rad/s)"),
        ("Pressure",         "p = F / A",                    "Pa",             "Perpendicular force per unit area"),
        ("Bernoulli",        "p + ½ρv² + ρgh = constant",   "Pa",             "For ideal incompressible flow"),
        ("Reynolds Number",  "Re = ρvL / μ",                 "dimensionless",  "L=char. length, μ=dynamic viscosity"),
        ("Thermal Stress",   "σ = E·α·ΔT",                   "Pa",             "α=thermal expansion coefficient"),
        ("Shear in Shaft",   "τ = T·r / J",                  "Pa",             "J=polar moment of inertia"),
        ("Beam Bending",     "σ = M·y / I",                  "Pa",             "M=moment, y=dist. from NA, I=2nd moment"),
        ("Euler Buckling",   "Pcr = π²EI / (KL)²",          "N",              "K=end condition factor"),
        ("Heat Conduction",  "Q = kA·ΔT / L",                "W",              "k=thermal conductivity"),
        ("Hoop Stress",      "σ_h = p·r / t",                "Pa",             "Thin-walled pressure vessel"),
    ]
    rows = "".join(
        f"<tr><td>{n}</td><td>{f}</td><td>{u}</td><td style='font-size:11px;color:#64748b'>{d}</td></tr>"
        for n,f,u,d in formulas
    )
    st.markdown(f"""<div class="tw"><table class="dt">
      <thead><tr><th>Formula</th><th>Expression</th><th>Unit</th><th>Notes</th></tr></thead>
      <tbody>{rows}</tbody></table></div>""", unsafe_allow_html=True)

    # Thermal conductivity table
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<p class="sh">🌡️ Thermal Properties of Common Materials</p>', unsafe_allow_html=True)
    thermal = {
        "Copper":            ("385", "17×10⁻⁶",  "390"),
        "Aluminum 6061":     ("167", "23.6×10⁻⁶","897"),
        "Steel (Carbon)":    ("50",  "12×10⁻⁶",  "502"),
        "Stainless Steel":   ("16",  "17.2×10⁻⁶","500"),
        "Titanium":          ("22",  "8.6×10⁻⁶", "520"),
        "Cast Iron":         ("55",  "10.8×10⁻⁶","460"),
        "Concrete":          ("1.4", "10×10⁻⁶",  "840"),
        "Glass":             ("1.05","9×10⁻⁶",   "720"),
        "ABS Plastic":       ("0.17","90×10⁻⁶",  "1400"),
        "Carbon Fiber":      ("5–7", "0.5×10⁻⁶", "800"),
    }
    rows = "".join(
        f"<tr><td>{k}</td><td>{v[0]}</td><td>{v[1]}</td><td>{v[2]}</td></tr>"
        for k,v in thermal.items()
    )
    st.markdown(f"""<div class="tw"><table class="dt">
      <thead><tr><th>Material</th><th>k (W/m·K)</th><th>α CTE (1/°C)</th><th>cp (J/kg·K)</th></tr></thead>
      <tbody>{rows}</tbody></table></div>""", unsafe_allow_html=True)

# ═══════════════════════
#  TAB 4 — BEAM & STRESS
# ═══════════════════════
with tab4:
    st.markdown('<p class="sh">🔬 Beam Bending & Stress Calculator</p>', unsafe_allow_html=True)

    c1, c2 = st.columns(2, gap="large")

    with c1:
        st.markdown('<div class="panel"><div class="panel-title"><span class="pt-dot"></span>SIMPLY SUPPORTED BEAM</div>', unsafe_allow_html=True)
        st.markdown("**Point load at centre: max bending moment & deflection**")
        b_L  = st.number_input("Span L (m)",        value=2.0, min_value=0.001, format="%.3f")
        b_W  = st.number_input("Point Load W (kN)", value=10.0, format="%.3f") * 1000  # → N
        b_E  = st.number_input("Young's Mod E (GPa)",value=200.0, format="%.1f") * 1e9
        b_cs = st.selectbox("Cross-section", ["Rectangle","Circle (solid)","I-Beam (approx)","Hollow Circle"])

        if b_cs == "Rectangle":
            bc1,bc2=st.columns(2)
            b_b=bc1.number_input("Width b (mm)",value=50.0,format="%.1f")*0.001
            b_h=bc2.number_input("Depth h (mm)",value=100.0,format="%.1f")*0.001
            b_I=b_b*b_h**3/12; b_y=b_h/2; b_A=b_b*b_h
        elif b_cs == "Circle (solid)":
            b_d=st.number_input("Diameter (mm)",value=80.0,format="%.1f")*0.001
            b_I=math.pi*b_d**4/64; b_y=b_d/2; b_A=math.pi*b_d**2/4
        elif b_cs == "I-Beam (approx)":
            bc1,bc2,bc3=st.columns(3)
            b_b =bc1.number_input("Flange w (mm)",value=100.0,format="%.1f")*0.001
            b_h =bc2.number_input("Total h (mm)", value=200.0,format="%.1f")*0.001
            b_tw=bc3.number_input("Web t (mm)",   value=8.0,  format="%.1f")*0.001
            b_tf=st.number_input("Flange t (mm)", value=12.0, format="%.1f")*0.001
            Iflange=2*(b_b*b_tf**3/12 + b_b*b_tf*((b_h/2-b_tf/2)**2))
            Iweb   =(b_tw*(b_h-2*b_tf)**3)/12
            b_I=Iflange+Iweb; b_y=b_h/2; b_A=2*b_b*b_tf+b_tw*(b_h-2*b_tf)
        else:
            bc1,bc2=st.columns(2)
            Do=bc1.number_input("Outer D (mm)",value=100.0,format="%.1f")*0.001
            Di=bc2.number_input("Inner D (mm)", value=80.0, format="%.1f")*0.001
            b_I=math.pi*(Do**4-Di**4)/64; b_y=Do/2; b_A=math.pi*(Do**2-Di**2)/4

        M_max  = b_W * b_L / 4          # N·m
        delta  = b_W * b_L**3 / (48*b_E*b_I) * 1000  # mm
        sigma  = M_max * b_y / b_I / 1e6   # MPa
        shear  = b_W / (2 * b_A) / 1e6     # MPa

        st.markdown(f"""
        <div class="result-box" style="margin-top:16px">
            <div class="res-label">Max Bending Moment</div>
            <div class="res-val">{M_max/1000:.4f}</div>
            <div class="res-unit">kN·m</div>
            <div class="res-formula">σ_max = {sigma:.4f} MPa &nbsp;·&nbsp; τ_avg = {shear:.4f} MPa</div>
            <div class="res-secondary">Max Deflection = {delta:.4f} mm &nbsp;·&nbsp; I = {b_I*1e8:.4f} ×10⁻⁸ m⁴</div>
        </div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="panel"><div class="panel-title"><span class="pt-dot"></span>THIN-WALLED PRESSURE VESSEL</div>', unsafe_allow_html=True)
        pv_p  = st.number_input("Internal Pressure (MPa)", value=5.0, format="%.3f")
        pv_r  = st.number_input("Inner Radius r (mm)",     value=500.0, format="%.1f") * 0.001
        pv_t  = st.number_input("Wall Thickness t (mm)",   value=10.0, format="%.1f") * 0.001
        pv_shape = st.radio("Vessel Type", ["Cylinder","Sphere"], horizontal=True)

        if pv_shape == "Cylinder":
            hoop    = pv_p * pv_r / pv_t
            axial   = pv_p * pv_r / (2 * pv_t)
            vol_pv  = math.pi * pv_r**2
            label2  = f"Axial Stress: {axial:.4f} MPa"
        else:
            hoop  = pv_p * pv_r / (2 * pv_t)
            axial = hoop
            vol_pv = (4/3)*math.pi*pv_r**3
            label2 = "Uniform stress (sphere)"

        safety = 250 / hoop if hoop > 0 else 999  # vs 250 MPa mild steel

        st.markdown(f"""
        <div class="result-box" style="margin-top:16px">
            <div class="res-label">Hoop (Circumferential) Stress</div>
            <div class="res-val">{hoop:.4f}</div>
            <div class="res-unit">MPa</div>
            <div class="res-formula">{label2}</div>
            <div class="res-secondary">
                Safety Factor vs Mild Steel: {safety:.2f} &nbsp;·&nbsp;
                r/t ratio: {pv_r/pv_t:.1f}
            </div>
        </div>""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div class="panel"><div class="panel-title"><span class="pt-dot"></span>SHAFT TORSION CALCULATOR</div>', unsafe_allow_html=True)
        sh_T = st.number_input("Torque T (N·m)", value=500.0, format="%.2f")
        sh_d = st.number_input("Shaft Diameter (mm)", value=50.0, format="%.1f") * 0.001
        sh_L = st.number_input("Shaft Length (mm)", value=500.0, format="%.1f") * 0.001
        sh_G = st.number_input("Shear Mod G (GPa)", value=80.0, format="%.1f") * 1e9

        sh_J   = math.pi * sh_d**4 / 32
        sh_tau = sh_T * (sh_d/2) / sh_J / 1e6
        sh_phi = (sh_T * sh_L / (sh_G * sh_J)) * (180/math.pi)

        st.markdown(f"""
        <div class="result-box" style="margin-top:12px">
            <div class="res-label">Max Shear Stress</div>
            <div class="res-val">{sh_tau:.4f}</div>
            <div class="res-unit">MPa</div>
            <div class="res-formula">Angle of Twist = {sh_phi:.4f} °</div>
            <div class="res-secondary">J = {sh_J*1e8:.4f} ×10⁻⁸ m⁴</div>
        </div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════
#  FOOTER
# ══════════════════════════════════════════════
st.markdown("""
<div class="footer">
    ⚙️
    <strong>Mechanical Unit Converter &amp; Material Density Checker</strong>
    <span class="s">|</span> Muhammad Bin Akrma
    <span class="s">|</span> Roll No: 25-ME-59
    <span class="s">|</span> UET Taxila — Dept. of Mechanical Engineering
    <span class="s">|</span> Built with Python &amp; Streamlit
</div>
""", unsafe_allow_html=True)
