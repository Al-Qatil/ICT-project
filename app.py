import streamlit as st
import math

st.set_page_config(
    page_title="Mech Toolkit | UET Taxila | 25-ME-59",
    page_icon="⚙️",
    layout="centered",          # ← narrow / centered layout
    initial_sidebar_state="collapsed",
)

# ══════════════════════════════════════════════════════════════
#  CSS — Teal / Emerald professional palette, narrow & clean
# ══════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Poppins:wght@600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

/* ─── Palette ─── */
:root{
  --bg:       #f0faf8;
  --surface:  #ffffff;
  --border:   #ccebe5;
  --bsoft:    #e5f5f2;
  --accent:   #0d7a68;
  --accent2:  #10a58a;
  --alight:   #d0f0ea;
  --aultra:   #edfaf7;
  --gold:     #b45309;
  --goldbg:   #fef3c7;
  --red:      #991b1b;
  --redbg:    #fee2e2;
  --text:     #0d1f1c;
  --text2:    #1f4039;
  --muted:    #4a7a6d;
  --muted2:   #7fb3a8;
  --sh1:      0 1px 4px rgba(13,122,104,.08);
  --sh2:      0 4px 18px rgba(13,122,104,.10);
  --sh3:      0 8px 32px rgba(13,122,104,.13);
  --r:        14px;
  --rsm:      9px;
}

/* ─── Base ─── */
html,body,.stApp{
  background:var(--bg) !important;
  font-family:'Inter',sans-serif !important;
  color:var(--text) !important;
}
.stApp{
  background-image:
    radial-gradient(ellipse 70% 40% at 50% -10%, rgba(13,122,104,.10) 0%, transparent 60%) !important;
  background-color:var(--bg) !important;
}

/* ─── Narrow container ─── */
.block-container{
  max-width: 820px !important;
  padding: 1.5rem 1.5rem 2rem !important;
  margin: 0 auto !important;
}

/* ─── UET bar ─── */
.uet-bar{
  background:linear-gradient(135deg,#064e3b 0%,#0d7a68 55%,#10a58a 100%);
  border-radius:14px 14px 0 0;
  padding:12px 22px;
  display:flex; align-items:center; gap:14px;
  margin-bottom:0;
}
.uet-name{font-family:'Poppins',sans-serif;font-size:14px;font-weight:700;color:#fff;line-height:1.25;}
.uet-sub{font-size:10px;color:rgba(255,255,255,.60);letter-spacing:.6px;margin-top:1px;}
.uet-pill{
  margin-left:auto; white-space:nowrap;
  background:rgba(255,255,255,.15); border:1px solid rgba(255,255,255,.25);
  border-radius:20px; padding:4px 14px;
  font-size:11px; font-weight:600; color:#fff;
}

/* ─── Hero ─── */
.hero{
  background:linear-gradient(140deg,#064e3b 0%,#0d7a68 45%,#059669 80%,#10b981 100%);
  border-radius:0 0 14px 14px;
  padding:28px 28px 32px;
  margin-bottom:20px;
  position:relative; overflow:hidden;
  box-shadow:var(--sh3);
}
.hero::before{
  content:'⚙'; position:absolute; right:-8px; top:-16px;
  font-size:160px; opacity:.05; color:#fff; line-height:1; pointer-events:none;
}
.hero-eye{font-size:10px;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:rgba(255,255,255,.50);margin-bottom:6px;}
.hero-title{
  font-family:'Poppins',sans-serif;
  font-size:clamp(18px,3.5vw,28px); font-weight:800;
  color:#fff; line-height:1.25; margin:0 0 6px; letter-spacing:-.2px;
}
.hero-title span{color:rgba(255,255,255,.72); font-weight:500;}
.hero-desc{font-size:12px;color:rgba(255,255,255,.62);margin-bottom:18px;line-height:1.5;}
.brow{display:flex;gap:8px;flex-wrap:wrap;}
.bx{
  background:rgba(255,255,255,.15); border:1px solid rgba(255,255,255,.22);
  border-radius:20px; padding:4px 14px; font-size:11px; font-weight:600; color:#fff;
}
.bx.g{background:rgba(180,83,9,.28);border-color:rgba(251,191,36,.40);color:#fde68a;}

/* ─── Stat strip ─── */
.srow{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:20px;}
.schip{
  background:var(--surface); border:1px solid var(--border);
  border-radius:12px; padding:12px 14px;
  display:flex;align-items:center;gap:11px;
  box-shadow:var(--sh1); flex:1; min-width:120px;
  transition:box-shadow .2s,transform .15s;
}
.schip:hover{box-shadow:var(--sh2);transform:translateY(-2px);}
.sico{width:38px;height:38px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:17px;flex-shrink:0;}
.sb{background:var(--alight);}
.sg{background:#d1fae5;}
.so{background:#fef3c7;}
.sp{background:#ede9fe;}
.sr{background:#fee2e2;}
.snum{font-size:19px;font-weight:800;color:var(--text);line-height:1;font-family:'Poppins',sans-serif;}
.slbl{font-size:10px;color:var(--muted);font-weight:500;margin-top:2px;}

/* ─── Section head ─── */
.sh{
  font-family:'Poppins',sans-serif; font-size:13px; font-weight:700;
  color:var(--text); margin:0 0 14px;
  display:flex; align-items:center; gap:9px;
}
.sh::after{content:'';flex:1;height:1px;background:var(--border);}

/* ─── Tabs ─── */
.stTabs [data-baseweb="tab-list"]{
  background:var(--surface) !important; border-radius:12px !important;
  border:1px solid var(--border) !important; padding:4px !important;
  gap:3px !important; box-shadow:var(--sh1) !important; margin-bottom:22px !important;
}
.stTabs [data-baseweb="tab"]{
  font-family:'Inter',sans-serif !important; font-size:12px !important;
  font-weight:600 !important; color:var(--muted) !important;
  background:transparent !important; border-radius:9px !important;
  padding:9px 16px !important; border:none !important; transition:all .2s !important;
}
.stTabs [aria-selected="true"]{
  background:var(--accent) !important; color:#fff !important;
  box-shadow:0 2px 10px rgba(13,122,104,.35) !important;
}

/* ─── Panel ─── */
.panel{
  background:var(--surface); border:1px solid var(--border);
  border-radius:var(--r); padding:20px; margin-bottom:14px;
  box-shadow:var(--sh1); transition:box-shadow .2s,border-color .2s;
}
.panel:hover{box-shadow:var(--sh2); border-color:#aad8d0;}
.ptitle{
  font-size:9px; font-weight:800; letter-spacing:2px; text-transform:uppercase;
  color:var(--accent2); margin-bottom:16px; display:flex; align-items:center; gap:7px;
}
.pdot{width:6px;height:6px;border-radius:50%;background:var(--accent2);flex-shrink:0;}

/* ─── Result box ─── */
.rbox{
  background:linear-gradient(135deg,var(--alight) 0%,var(--aultra) 100%);
  border:1.5px solid rgba(13,122,104,.22); border-radius:14px;
  padding:24px 20px; text-align:center; position:relative; overflow:hidden;
  box-shadow:0 2px 14px rgba(13,122,104,.10);
  margin: 16px 0 20px;
}
.rbox::before{
  content:''; position:absolute; top:-40px; right:-40px;
  width:130px; height:130px; border-radius:50%;
  background:rgba(13,122,104,.05); pointer-events:none;
}
.rlbl{font-size:9px;font-weight:800;letter-spacing:2.5px;text-transform:uppercase;color:var(--accent2);margin-bottom:7px;}
.rval{font-family:'JetBrains Mono',monospace;font-size:clamp(24px,5vw,44px);font-weight:700;color:var(--accent);line-height:1;word-break:break-all;}
.runit{font-size:14px;font-weight:600;color:var(--muted);margin-top:5px;}
.rform{
  font-family:'JetBrains Mono',monospace; font-size:11px; color:var(--accent);
  margin-top:11px; background:var(--alight); display:inline-block;
  padding:4px 12px; border-radius:6px; font-weight:600; border:1px solid var(--border);
}
.rsec{font-size:11px;color:var(--muted);margin-top:7px;font-family:'JetBrains Mono',monospace;}

/* ─── Density result ─── */
.dbox{
  background:linear-gradient(135deg,#fef9c3 0%,#fffde7 100%);
  border:1.5px solid rgba(180,83,9,.18); border-radius:14px;
  padding:20px; text-align:center; margin-top:12px;
  box-shadow:0 2px 10px rgba(180,83,9,.07);
}
.dbox .rval{color:var(--gold);}
.dbox .rlbl{color:var(--gold);}
.dtag{
  font-family:'JetBrains Mono',monospace; font-size:11px; font-weight:600;
  background:#fef3c7; color:#92400e; display:inline-block;
  padding:3px 12px; border-radius:6px; margin-top:9px;
}

/* ─── Tables ─── */
.tw{background:var(--surface);border:1px solid var(--border);border-radius:var(--r);overflow:hidden;box-shadow:var(--sh1);overflow-x:auto;}
.dt{width:100%;border-collapse:collapse;font-size:12.5px;}
.dt thead tr{background:var(--accent);}
.dt th{padding:10px 16px;text-align:left;font-size:9px;font-weight:700;letter-spacing:1.5px;text-transform:uppercase;color:#fff;}
.dt td{padding:9px 16px;color:var(--text2);border-bottom:1px solid var(--bsoft);font-family:'JetBrains Mono',monospace;font-size:12px;}
.dt td:first-child{font-family:'Inter',sans-serif;font-weight:600;color:var(--text);}
.dt tbody tr:hover td{background:var(--aultra);}
.dt .hl td{background:#d1fae5 !important;color:#065f46 !important;font-weight:700;}
.dt tbody tr:last-child td{border-bottom:none;}
.clow{color:#065f46 !important;font-weight:700 !important;}
.cmid{color:#b45309 !important;font-weight:700 !important;}
.chigh{color:#991b1b !important;font-weight:700 !important;}

/* ─── Arrow ─── */
.arrow{display:flex;align-items:center;justify-content:center;height:100%;padding-top:36px;font-size:24px;color:var(--muted2);}

/* ─── Widgets ─── */
div[data-testid="stNumberInput"] input,
div[data-testid="stTextInput"] input{
  background:#f6fdfb !important; border:1.5px solid var(--border) !important;
  border-radius:var(--rsm) !important; color:var(--text) !important;
  font-family:'JetBrains Mono',monospace !important; font-size:14px !important;
  padding:9px 13px !important; transition:border-color .2s,box-shadow .2s !important;
}
div[data-testid="stNumberInput"] input:focus,
div[data-testid="stTextInput"] input:focus{
  border-color:var(--accent2) !important;
  box-shadow:0 0 0 3px rgba(16,165,138,.14) !important;
  background:#fff !important; outline:none !important;
}
div[data-testid="stSelectbox"] > div > div{
  background:#f6fdfb !important; border:1.5px solid var(--border) !important;
  border-radius:var(--rsm) !important; color:var(--text) !important; font-size:13px !important;
}
label,.stSelectbox label,.stNumberInput label{
  font-family:'Inter',sans-serif !important; font-size:10px !important;
  font-weight:700 !important; color:var(--muted) !important;
  text-transform:uppercase !important; letter-spacing:.8px !important;
}
.stRadio > div{gap:8px !important;}
.stRadio label{text-transform:none !important;letter-spacing:0 !important;font-size:13px !important;font-weight:500 !important;}

/* ─── Button ─── */
.stButton > button{
  background:var(--accent) !important; color:#fff !important;
  border:none !important; border-radius:var(--rsm) !important;
  font-family:'Inter',sans-serif !important; font-size:12px !important;
  font-weight:700 !important; letter-spacing:.4px !important;
  padding:12px 24px !important; width:100% !important;
  transition:all .2s !important; box-shadow:0 3px 12px rgba(13,122,104,.28) !important;
}
.stButton > button:hover{
  background:#0a6357 !important;
  box-shadow:0 5px 18px rgba(13,122,104,.40) !important;
  transform:translateY(-1px) !important;
}

/* ─── Footer ─── */
.footer{
  background:var(--surface); border:1px solid var(--border); border-radius:var(--r);
  padding:14px 22px; margin-top:32px;
  display:flex; align-items:center; justify-content:center; flex-wrap:wrap;
  gap:6px; font-size:11px; color:var(--muted); font-weight:500;
  box-shadow:var(--sh1);
}
.footer strong{color:var(--accent);}
.footer .s{color:var(--border);margin:0 1px;}

::-webkit-scrollbar{width:5px;height:5px;}
::-webkit-scrollbar-track{background:var(--bg);}
::-webkit-scrollbar-thumb{background:#9fd4cc;border-radius:3px;}
#MainMenu,footer,header{visibility:hidden;}
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════
#  DATA
# ══════════════════════════════════════════════
MATERIALS = {
    "Steel (Carbon)":7850,"Steel (Stainless 304)":8000,"Steel (Tool)":7750,
    "Aluminum (Pure)":2700,"Aluminum Alloy (6061)":2700,"Aluminum Alloy (7075)":2810,
    "Copper":8960,"Brass":8500,"Bronze":8800,
    "Cast Iron (Gray)":7200,"Cast Iron (Ductile)":7100,
    "Titanium (Grade 5)":4430,"Nickel":8908,"Lead":11340,
    "Zinc":7133,"Magnesium":1738,"Gold":19300,"Silver":10490,
    "Tungsten":19250,"Chromium":7190,"Molybdenum":10220,"Inconel 718":8190,
    "ABS Plastic":1050,"Nylon (PA6)":1140,"Polycarbonate (PC)":1200,
    "HDPE":950,"PTFE (Teflon)":2200,"PVC (Rigid)":1400,
    "Epoxy Resin":1250,"Polypropylene (PP)":905,"PET":1380,
    "Carbon Fiber Composite":1600,"Fiberglass (GFRP)":1900,
    "Concrete":2400,"Granite":2700,"Glass (Borosilicate)":2230,
    "Silicon Carbide (SiC)":3210,"Alumina (Al₂O₃)":3960,
    "Oak Wood":700,"Balsa Wood":120,"Rubber (Natural)":920,
    "Cork":120,"Ice":917,"Water":1000,"Air (at STP)":1.225,
}

CATEGORIES = {
    "⚖️  Force":             ("N",    ["N","kN","MN","lbf","kgf","dyn"]),
    "📏  Length":            ("m",    ["m","cm","mm","km","in","ft","yd","mi","μm","nm"]),
    "⚡  Pressure":          ("Pa",   ["Pa","kPa","MPa","GPa","bar","atm","psi","ksi","torr","mmHg"]),
    "🔁  Torque":            ("N·m",  ["N·m","kN·m","N·cm","N·mm","lbf·ft","lbf·in","kgf·m"]),
    "🏎️  Velocity":          ("m/s",  ["m/s","km/h","ft/s","mph","knot","ft/min"]),
    "🌡️  Temperature":       ("°C",   ["°C","°F","K","°R"]),
    "💡  Power":             ("W",    ["W","kW","MW","hp","BTU/hr","cal/s"]),
    "🔩  Stress / Strength": ("Pa",   ["Pa","kPa","MPa","GPa","psi","ksi"]),
    "📦  Mass":              ("kg",   ["kg","g","mg","t","lb","oz","slug"]),
    "🌀  Angular Velocity":  ("rad/s",["rad/s","rpm","deg/s","rev/s"]),
    "💧  Viscosity":         ("Pa·s", ["Pa·s","cP","mPa·s","lbf·s/ft²"]),
    "⚡  Energy":            ("J",    ["J","kJ","MJ","cal","kcal","BTU","kWh","eV","ft·lbf"]),
    "📐  Area":              ("m²",   ["m²","cm²","mm²","in²","ft²","acre","hectare"]),
    "🧊  Volume":            ("m³",   ["m³","cm³","mm³","L","mL","in³","ft³","gal (US)"]),
}

FACTORS = {
    "N":1,"kN":1e3,"MN":1e6,"lbf":4.44822,"kgf":9.80665,"dyn":1e-5,
    "m":1,"cm":0.01,"mm":0.001,"km":1000,"in":0.0254,
    "ft":0.3048,"yd":0.9144,"mi":1609.344,"μm":1e-6,"nm":1e-9,
    "Pa":1,"kPa":1e3,"MPa":1e6,"GPa":1e9,"bar":1e5,
    "atm":101325,"psi":6894.757,"ksi":6.894757e6,"torr":133.322,"mmHg":133.322,
    "N·m":1,"kN·m":1e3,"N·cm":0.01,"N·mm":0.001,"lbf·ft":1.35582,"lbf·in":0.112985,"kgf·m":9.80665,
    "m/s":1,"km/h":1/3.6,"ft/s":0.3048,"mph":0.44704,"knot":0.514444,"ft/min":0.00508,
    "W":1,"kW":1e3,"MW":1e6,"hp":745.7,"BTU/hr":0.29307,"cal/s":4.18400,
    "kg":1,"g":0.001,"mg":1e-6,"t":1000,"lb":0.453592,"oz":0.0283495,"slug":14.5939,
    "rad/s":1,"rpm":math.pi/30,"deg/s":math.pi/180,"rev/s":2*math.pi,
    "Pa·s":1,"cP":0.001,"mPa·s":0.001,"lbf·s/ft²":47.8803,
    "J":1,"kJ":1e3,"MJ":1e6,"cal":4.184,"kcal":4184,
    "BTU":1055.06,"kWh":3.6e6,"eV":1.60218e-19,"ft·lbf":1.35582,
    "m²":1,"cm²":1e-4,"mm²":1e-6,"in²":6.4516e-4,"ft²":0.092903,"acre":4046.86,"hectare":1e4,
    "m³":1,"cm³":1e-6,"mm³":1e-9,"L":0.001,"mL":1e-6,
    "in³":1.6387e-5,"ft³":0.028317,"gal (US)":0.003785,
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

def fn(v):
    if v==0: return "0"
    if abs(v)>=1e12 or (abs(v)<1e-6 and v!=0): return f"{v:.4e}"
    if abs(v)>=1e6: return f"{v:,.2f}"
    return f"{v:.6g}"

# ══════════════════════════════════════════════
#  UET BAR + HERO
# ══════════════════════════════════════════════
st.markdown("""
<div class="uet-bar">
  <svg width="44" height="44" viewBox="0 0 44 44" fill="none" xmlns="http://www.w3.org/2000/svg">
    <circle cx="22" cy="22" r="21" fill="rgba(255,255,255,0.10)" stroke="rgba(255,255,255,0.28)" stroke-width="1.2"/>
    <circle cx="22" cy="22" r="7" fill="none" stroke="rgba(255,255,255,.85)" stroke-width="2"/>
    <g stroke="rgba(255,255,255,.85)" stroke-width="2" stroke-linecap="round">
      <line x1="22" y1="4"  x2="22" y2="10"/>
      <line x1="22" y1="34" x2="22" y2="40"/>
      <line x1="4"  y1="22" x2="10" y2="22"/>
      <line x1="34" y1="22" x2="40" y2="22"/>
      <line x1="8"  y1="8"  x2="12.5" y2="12.5"/>
      <line x1="31.5" y1="31.5" x2="36" y2="36"/>
      <line x1="36" y1="8"  x2="31.5" y2="12.5"/>
      <line x1="12.5" y1="31.5" x2="8" y2="36"/>
    </g>
  </svg>
  <div>
    <div class="uet-name">University of Engineering &amp; Technology, Taxila</div>
    <div class="uet-sub">ESTABLISHED 1975 &nbsp;·&nbsp; PAKISTAN</div>
  </div>
  <div class="uet-pill">🔧 Mechanical Eng.</div>
</div>

<div class="hero">
  <div class="hero-eye">⚙ Mechanical Engineering Toolkit</div>
  <div class="hero-title">Unit Converter &amp; <span>Material Density Checker</span></div>
  <div class="hero-desc">Precision engineering calculations — 14 categories, 45+ materials, shape calculators &amp; reference tables.</div>
  <div class="brow">
    <span class="bx">👤 Muhammad Bin Akrma</span>
    <span class="bx g">🎓 Roll No: 25-ME-59</span>
    <span class="bx">✅ Batch 2025</span>
  </div>
</div>
""", unsafe_allow_html=True)

# STAT STRIP
st.markdown("""
<div class="srow">
  <div class="schip"><div class="sico sb">📐</div><div><div class="snum">14</div><div class="slbl">Categories</div></div></div>
  <div class="schip"><div class="sico sg">🧱</div><div><div class="snum">45+</div><div class="slbl">Materials</div></div></div>
  <div class="schip"><div class="sico so">⚡</div><div><div class="snum">100+</div><div class="slbl">Unit Pairs</div></div></div>
  <div class="schip"><div class="sico sp">📋</div><div><div class="snum">30+</div><div class="slbl">Formulas</div></div></div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════
#  TABS
# ══════════════════════════════════════════════
tab1, tab2, tab3, tab4 = st.tabs([
    "⚙️  Unit Converter",
    "🧱  Material Density",
    "📋  Reference",
    "🔬  Stress Calc",
])

# ─── TAB 1 ───
with tab1:
    st.markdown('<p class="sh">⚙️ Select Category &amp; Convert</p>', unsafe_allow_html=True)
    cat_name = st.selectbox("Category", list(CATEGORIES.keys()), index=0, label_visibility="collapsed")
    base_unit, units = CATEGORIES[cat_name]
    is_temp = "Temperature" in cat_name

    col1, col2, col3 = st.columns([5,1,5], gap="small")
    with col1:
        st.markdown('<div class="panel"><div class="ptitle"><span class="pdot"></span>INPUT</div>', unsafe_allow_html=True)
        value_in  = st.number_input("Value", value=1.0, format="%.6g", key="vi", label_visibility="collapsed")
        unit_from = st.selectbox("From", units, key="uf")
        st.markdown("</div>", unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="arrow">→</div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="panel"><div class="ptitle"><span class="pdot"></span>OUTPUT</div>', unsafe_allow_html=True)
        unit_to = st.selectbox("To", units, index=min(1,len(units)-1), key="ut")
        st.button("⚡  Convert", key="cb")
        st.markdown("</div>", unsafe_allow_html=True)

    try:
        if is_temp:
            result = convert_temp(value_in, unit_from, unit_to)
            fstr   = f"{fn(value_in)} {unit_from}  →  {fn(result)} {unit_to}"
            sec    = ""
        else:
            result = do_convert(value_in, unit_from, unit_to)
            ratio  = FACTORS.get(unit_from,1)/FACTORS.get(unit_to,1)
            fstr   = f"1 {unit_from} = {fn(ratio)} {unit_to}"
            sec    = f"{fn(value_in)} × {fn(ratio)} = {fn(result)}"

        st.markdown(f"""
        <div class="rbox">
          <div class="rlbl">Result</div>
          <div class="rval">{fn(result)}</div>
          <div class="runit">{unit_to}</div>
          <div class="rform">{fstr}</div>
          <div class="rsec">{sec}</div>
        </div>""", unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error: {e}")

    st.markdown('<p class="sh">🔢 All Equivalent Values</p>', unsafe_allow_html=True)
    rows=""
    if is_temp:
        for u in units:
            try:
                v=convert_temp(value_in,unit_from,u)
                hl="hl" if u==unit_to else ""
                rows+=f'<tr class="{hl}"><td>{u}</td><td>{fn(v)}</td><td>{"✓" if u==unit_to else ""}</td></tr>'
            except: pass
    else:
        try:
            sv=value_in*FACTORS.get(unit_from,1)
            for u in units:
                v=sv/FACTORS.get(u,1)
                hl="hl" if u==unit_to else ""
                rows+=f'<tr class="{hl}"><td>{u}</td><td>{fn(v)}</td><td style="color:#0d7a68;font-weight:700">{"✓" if u==unit_to else ""}</td></tr>'
        except:
            rows="<tr><td colspan='3'>Error</td></tr>"

    st.markdown(f"""<div class="tw"><table class="dt">
      <thead><tr><th>Unit</th><th>Value</th><th>Active</th></tr></thead>
      <tbody>{rows}</tbody></table></div>""", unsafe_allow_html=True)

# ─── TAB 2 ───
with tab2:
    st.markdown('<p class="sh">🧱 Material Lookup</p>', unsafe_allow_html=True)

    search = st.text_input("🔍 Search material", placeholder="e.g. steel, copper…", label_visibility="collapsed")
    filtered = {k:v for k,v in MATERIALS.items() if search.lower() in k.lower()} if search else MATERIALS
    if not filtered: filtered = MATERIALS
    mat = st.selectbox("Material", list(filtered.keys()))
    density = MATERIALS[mat]

    if density<500: dcat,dcol="Ultra-Light","#059669"
    elif density<2000: dcat,dcol="Light","#0d7a68"
    elif density<5000: dcat,dcol="Medium","#b45309"
    elif density<10000: dcat,dcol="Heavy","#92400e"
    else: dcat,dcol="Very Heavy","#991b1b"

    st.markdown(f"""
    <div class="dbox">
      <div class="rlbl">Density of {mat}</div>
      <div class="rval">{density:,}</div>
      <div class="runit">kg / m³</div>
      <div class="dtag">{density/1000:.4f} g/cm³ &nbsp;·&nbsp; {density*0.062428:.4f} lb/ft³</div>
      <div style="margin-top:9px;font-size:12px;font-weight:700;color:{dcol}">● {dcat} Material</div>
    </div>""", unsafe_allow_html=True)

    st.markdown('<p class="sh" style="margin-top:20px">🧮 Mass / Volume Calculator</p>', unsafe_allow_html=True)
    st.markdown('<div class="panel"><div class="ptitle"><span class="pdot"></span>GEOMETRY CALCULATOR</div>', unsafe_allow_html=True)
    calc_mode = st.radio("Mode", ["Mass from Volume","Volume from Mass"], horizontal=True)
    shape = st.selectbox("Shape", ["Custom Volume (m³)","Rectangular Block","Cylinder","Sphere","Hollow Cylinder","Hollow Sphere"])

    vol_m3=0.0
    if shape=="Custom Volume (m³)":
        vol_m3=st.number_input("Volume (m³)",value=0.001,format="%.8f",min_value=0.0)
    elif shape=="Rectangular Block":
        c1,c2,c3=st.columns(3)
        L=c1.number_input("L (m)",value=0.1,format="%.4f",min_value=0.0)
        W=c2.number_input("W (m)",value=0.1,format="%.4f",min_value=0.0)
        H=c3.number_input("H (m)",value=0.1,format="%.4f",min_value=0.0)
        vol_m3=L*W*H
    elif shape=="Cylinder":
        c1,c2=st.columns(2)
        R=c1.number_input("Radius (m)",value=0.05,format="%.4f",min_value=0.0)
        H=c2.number_input("Height (m)",value=0.20,format="%.4f",min_value=0.0)
        vol_m3=math.pi*R**2*H
    elif shape=="Sphere":
        R=st.number_input("Radius (m)",value=0.05,format="%.4f",min_value=0.0)
        vol_m3=(4/3)*math.pi*R**3
    elif shape=="Hollow Cylinder":
        c1,c2,c3=st.columns(3)
        Ro=c1.number_input("Outer R (m)",value=0.06,format="%.4f",min_value=0.0)
        Ri=c2.number_input("Inner R (m)",value=0.04,format="%.4f",min_value=0.0)
        H=c3.number_input("Height (m)",value=0.20,format="%.4f",min_value=0.0)
        vol_m3=math.pi*(Ro**2-Ri**2)*H
    elif shape=="Hollow Sphere":
        c1,c2=st.columns(2)
        Ro=c1.number_input("Outer R (m)",value=0.06,format="%.4f",min_value=0.0)
        Ri=c2.number_input("Inner R (m)",value=0.04,format="%.4f",min_value=0.0)
        vol_m3=(4/3)*math.pi*(Ro**3-Ri**3)

    if calc_mode=="Mass from Volume":
        mass_kg=density*vol_m3
        st.markdown(f"""
        <div class="rbox">
          <div class="rlbl">Calculated Mass</div>
          <div class="rval">{mass_kg:.4f}</div>
          <div class="runit">kg</div>
          <div class="rform">{mass_kg*1000:.3f} g &nbsp;·&nbsp; {mass_kg*2.20462:.4f} lb</div>
          <div class="rsec">V = {vol_m3:.6f} m³ × ρ = {density:,} kg/m³</div>
        </div>""", unsafe_allow_html=True)
    else:
        mass_in=st.number_input("Mass (kg)",value=1.0,format="%.4f",min_value=0.0)
        vc=mass_in/density if density else 0
        st.markdown(f"""
        <div class="rbox">
          <div class="rlbl">Calculated Volume</div>
          <div class="rval">{vc:.6f}</div>
          <div class="runit">m³</div>
          <div class="rform">{vc*1e6:.4f} cm³ &nbsp;·&nbsp; {vc*1000:.5f} L</div>
          <div class="rsec">m = {mass_in} kg ÷ ρ = {density:,} kg/m³</div>
        </div>""", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Compare
    st.markdown('<p class="sh">🔍 Compare Materials</p>', unsafe_allow_html=True)
    cc=st.columns(3)
    cms=[]
    for i,col in enumerate(cc):
        with col: cms.append(col.selectbox(f"Mat {i+1}",list(MATERIALS.keys()),index=i*5,key=f"cm{i}"))
    vals=[MATERIALS[m] for m in cms]; mn,mx=min(vals),max(vals)
    def cls(v): return "clow" if v==mn else ("chigh" if v==mx else "cmid")
    rows=""
    for lbl,fn2 in [("kg/m³",lambda m:f"{MATERIALS[m]:,}"),("g/cm³",lambda m:f"{MATERIALS[m]/1000:.4f}"),("lb/ft³",lambda m:f"{MATERIALS[m]*0.062428:.3f}")]:
        cells="".join(f'<td class="{cls(MATERIALS[m])}">{fn2(m)}</td>' for m in cms)
        rows+=f"<tr><td>{lbl}</td>{cells}</tr>"
    hdrs="".join(f"<th>{m.split('(')[0].strip()}</th>" for m in cms)
    st.markdown(f"""<div class="tw"><table class="dt">
      <thead><tr><th>Property</th>{hdrs}</tr></thead><tbody>{rows}</tbody></table></div>""", unsafe_allow_html=True)

    # Full DB
    st.markdown('<p class="sh" style="margin-top:20px">📋 Full Database</p>', unsafe_allow_html=True)
    cats=st.multiselect("Filter",["Metals","Polymers","Composites & Ceramics","Natural"],
                        default=["Metals","Polymers","Composites & Ceramics","Natural"])
    mk=list(MATERIALS.keys())
    km={"Metals":mk[:22],"Polymers":mk[22:31],"Composites & Ceramics":mk[31:38],"Natural":mk[38:]}
    show=[]
    for c in cats: show+=km.get(c,[])
    rows="".join(
        f'<tr class="{"hl" if k==mat else ""}"><td>{k}</td><td>{v:,.3f}</td><td>{v/1000:.4f}</td><td>{v*0.062428:.4f}</td></tr>'
        for k in show for v in [MATERIALS[k]]
    )
    st.markdown(f"""<div class="tw"><table class="dt">
      <thead><tr><th>Material</th><th>kg/m³</th><th>g/cm³</th><th>lb/ft³</th></tr></thead>
      <tbody>{rows}</tbody></table></div>""", unsafe_allow_html=True)

# ─── TAB 3 ───
with tab3:
    st.markdown('<p class="sh">⚡ Engineering Constants</p>', unsafe_allow_html=True)
    consts={
        "g — Standard Gravity":"9.80665 m/s²","R — Gas Constant":"8.314 J/(mol·K)",
        "σ — Stefan-Boltzmann":"5.67×10⁻⁸ W/(m²·K⁴)","E — Steel (Young's)":"200 GPa",
        "E — Aluminum (Young's)":"69 GPa","E — Titanium (Young's)":"116 GPa",
        "ν — Steel (Poisson)":"0.30","ν — Aluminum (Poisson)":"0.33",
        "1 atm":"101,325 Pa","1 hp":"745.7 W","1 BTU":"1,055.06 J","0°C in Kelvin":"273.15 K",
    }
    rows="".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k,v in consts.items())
    st.markdown(f"""<div class="tw"><table class="dt">
      <thead><tr><th>Constant</th><th>Value</th></tr></thead><tbody>{rows}</tbody></table></div>""", unsafe_allow_html=True)

    st.markdown('<p class="sh" style="margin-top:20px">🔩 Material Strength (UTS)</p>', unsafe_allow_html=True)
    strengths={
        "Steel (Mild)":"400–550 MPa","Steel (High-Strength)":"800–2000 MPa",
        "Aluminum 6061-T6":"310 MPa","Aluminum 7075-T6":"572 MPa",
        "Titanium Ti-6Al-4V":"950 MPa","CFRP Composite":"600–1500 MPa",
        "Fiberglass (GFRP)":"300–400 MPa","Concrete (Compressive)":"20–50 MPa",
        "Copper":"210–400 MPa","Nylon 6":"75–85 MPa","ABS Plastic":"40–55 MPa","Cast Iron":"150–400 MPa",
    }
    rows="".join(f"<tr><td>{k}</td><td>{v}</td></tr>" for k,v in strengths.items())
    st.markdown(f"""<div class="tw"><table class="dt">
      <thead><tr><th>Material</th><th>UTS</th></tr></thead><tbody>{rows}</tbody></table></div>""", unsafe_allow_html=True)

    st.markdown('<p class="sh" style="margin-top:20px">🧮 Mechanical Formulas</p>', unsafe_allow_html=True)
    formulas=[
        ("Stress","σ = F / A","Pa","F=Force, A=Area"),
        ("Strain","ε = ΔL / L₀","—","ΔL=deformation"),
        ("Young's Modulus","E = σ / ε","Pa","Elastic modulus"),
        ("Torque","T = F × r","N·m","r=radius from axis"),
        ("Power","P = T × ω","W","ω in rad/s"),
        ("Pressure","p = F / A","Pa","Perp. force per area"),
        ("Bernoulli","p + ½ρv² + ρgh = C","Pa","Ideal incompressible"),
        ("Reynolds No.","Re = ρvL / μ","—","Laminar Re < 2300"),
        ("Thermal Stress","σ = E·α·ΔT","Pa","α=CTE"),
        ("Beam Bending","σ = M·y / I","Pa","I=2nd moment of area"),
        ("Hoop Stress","σ_h = p·r / t","Pa","Thin-walled vessel"),
        ("Euler Buckling","Pcr = π²EI/(KL)²","N","K=end cond. factor"),
        ("Shear in Shaft","τ = T·r / J","Pa","J=polar 2nd moment"),
        ("Heat Conduction","Q = kA·ΔT / L","W","k=thermal cond."),
    ]
    rows="".join(
        f"<tr><td>{n}</td><td>{f}</td><td>{u}</td><td style='font-size:11px;color:#4a7a6d'>{d}</td></tr>"
        for n,f,u,d in formulas
    )
    st.markdown(f"""<div class="tw"><table class="dt">
      <thead><tr><th>Name</th><th>Formula</th><th>Unit</th><th>Notes</th></tr></thead>
      <tbody>{rows}</tbody></table></div>""", unsafe_allow_html=True)

    st.markdown('<p class="sh" style="margin-top:20px">🌡️ Thermal Properties</p>', unsafe_allow_html=True)
    thermal={
        "Copper":("385","17×10⁻⁶","390"),"Aluminum 6061":("167","23.6×10⁻⁶","897"),
        "Steel (Carbon)":("50","12×10⁻⁶","502"),"Stainless Steel":("16","17.2×10⁻⁶","500"),
        "Titanium":("22","8.6×10⁻⁶","520"),"Cast Iron":("55","10.8×10⁻⁶","460"),
        "Concrete":("1.4","10×10⁻⁶","840"),"ABS Plastic":("0.17","90×10⁻⁶","1400"),
    }
    rows="".join(f"<tr><td>{k}</td><td>{v[0]}</td><td>{v[1]}</td><td>{v[2]}</td></tr>" for k,v in thermal.items())
    st.markdown(f"""<div class="tw"><table class="dt">
      <thead><tr><th>Material</th><th>k (W/m·K)</th><th>α (1/°C)</th><th>cp (J/kg·K)</th></tr></thead>
      <tbody>{rows}</tbody></table></div>""", unsafe_allow_html=True)

# ─── TAB 4 ───
with tab4:
    st.markdown('<p class="sh">🔬 Beam Bending Calculator</p>', unsafe_allow_html=True)
    st.markdown('<div class="panel"><div class="ptitle"><span class="pdot"></span>SIMPLY SUPPORTED BEAM — CENTRAL POINT LOAD</div>', unsafe_allow_html=True)

    c1,c2=st.columns(2)
    b_L=c1.number_input("Span L (m)",value=2.0,min_value=0.001,format="%.3f")
    b_W=c2.number_input("Load W (kN)",value=10.0,format="%.3f")*1000
    c1,c2=st.columns(2)
    b_E=c1.number_input("E (GPa)",value=200.0,format="%.1f")*1e9
    b_cs=c2.selectbox("Cross-Section",["Rectangle","Circle","Hollow Circle","I-Beam"])

    if b_cs=="Rectangle":
        c1,c2=st.columns(2)
        b_b=c1.number_input("Width (mm)",value=50.0,format="%.1f")*0.001
        b_h=c2.number_input("Depth (mm)",value=100.0,format="%.1f")*0.001
        b_I=b_b*b_h**3/12; b_y=b_h/2; b_A=b_b*b_h
    elif b_cs=="Circle":
        b_d=st.number_input("Diameter (mm)",value=80.0,format="%.1f")*0.001
        b_I=math.pi*b_d**4/64; b_y=b_d/2; b_A=math.pi*b_d**2/4
    elif b_cs=="Hollow Circle":
        c1,c2=st.columns(2)
        Do=c1.number_input("Outer D (mm)",value=100.0,format="%.1f")*0.001
        Di=c2.number_input("Inner D (mm)",value=80.0,format="%.1f")*0.001
        b_I=math.pi*(Do**4-Di**4)/64; b_y=Do/2; b_A=math.pi*(Do**2-Di**2)/4
    else:
        c1,c2=st.columns(2)
        b_b=c1.number_input("Flange W (mm)",value=100.0,format="%.1f")*0.001
        b_h=c2.number_input("Total H (mm)",value=200.0,format="%.1f")*0.001
        c1,c2=st.columns(2)
        b_tw=c1.number_input("Web t (mm)",value=8.0,format="%.1f")*0.001
        b_tf=c2.number_input("Flange t (mm)",value=12.0,format="%.1f")*0.001
        Ifl=2*(b_b*b_tf**3/12+b_b*b_tf*((b_h/2-b_tf/2)**2))
        Iw=(b_tw*(b_h-2*b_tf)**3)/12
        b_I=Ifl+Iw; b_y=b_h/2; b_A=2*b_b*b_tf+b_tw*(b_h-2*b_tf)

    Mm=b_W*b_L/4
    delta=b_W*b_L**3/(48*b_E*b_I)*1000
    sigma=Mm*b_y/b_I/1e6
    shear=b_W/(2*b_A)/1e6

    st.markdown(f"""
    <div class="rbox">
      <div class="rlbl">Max Bending Moment</div>
      <div class="rval">{Mm/1000:.4f} kN·m</div>
      <div class="runit"></div>
      <div class="rform">σ_max = {sigma:.4f} MPa &nbsp;·&nbsp; τ_avg = {shear:.4f} MPa</div>
      <div class="rsec">Max Deflection = {delta:.4f} mm &nbsp;·&nbsp; I = {b_I*1e8:.4f} ×10⁻⁸ m⁴</div>
    </div>""", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<p class="sh" style="margin-top:4px">💊 Pressure Vessel & Shaft</p>', unsafe_allow_html=True)
    vc1,vc2=st.columns(2)
    with vc1:
        st.markdown('<div class="panel"><div class="ptitle"><span class="pdot"></span>PRESSURE VESSEL</div>', unsafe_allow_html=True)
        pv_p=st.number_input("Pressure (MPa)",value=5.0,format="%.3f")
        pv_r=st.number_input("Inner R (mm)",value=500.0,format="%.1f")*0.001
        pv_t=st.number_input("Wall t (mm)",value=10.0,format="%.1f")*0.001
        pv_s=st.radio("Type",["Cylinder","Sphere"],horizontal=True,key="pvt")
        hoop=pv_p*pv_r/pv_t if pv_s=="Cylinder" else pv_p*pv_r/(2*pv_t)
        axial=pv_p*pv_r/(2*pv_t)
        sf=250/hoop if hoop>0 else 999
        st.markdown(f"""
        <div class="rbox">
          <div class="rlbl">Hoop Stress</div>
          <div class="rval">{hoop:.3f}</div>
          <div class="runit">MPa</div>
          <div class="rform">Axial = {axial:.3f} MPa</div>
          <div class="rsec">Safety Factor ≈ {sf:.2f}</div>
        </div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with vc2:
        st.markdown('<div class="panel"><div class="ptitle"><span class="pdot"></span>SHAFT TORSION</div>', unsafe_allow_html=True)
        sh_T=st.number_input("Torque (N·m)",value=500.0,format="%.2f")
        sh_d=st.number_input("Diameter (mm)",value=50.0,format="%.1f",key="shd")*0.001
        sh_L=st.number_input("Length (mm)",value=500.0,format="%.1f",key="shl")*0.001
        sh_G=st.number_input("G (GPa)",value=80.0,format="%.1f")*1e9
        sh_J=math.pi*sh_d**4/32
        sh_tau=sh_T*(sh_d/2)/sh_J/1e6
        sh_phi=(sh_T*sh_L/(sh_G*sh_J))*(180/math.pi)
        st.markdown(f"""
        <div class="rbox">
          <div class="rlbl">Max Shear Stress</div>
          <div class="rval">{sh_tau:.4f}</div>
          <div class="runit">MPa</div>
          <div class="rform">Angle of Twist = {sh_phi:.4f} °</div>
          <div class="rsec">J = {sh_J*1e8:.4f} ×10⁻⁸ m⁴</div>
        </div>""", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════
#  FOOTER
# ══════════════════════════════════════════════
st.markdown("""
<div class="footer">
  ⚙️ <strong>Mechanical Unit Converter &amp; Material Density Checker</strong>
  <span class="s">|</span> Muhammad Bin Akrma
  <span class="s">|</span> Roll No: 25-ME-59
  <span class="s">|</span> UET Taxila — Mechanical Engineering
</div>
""", unsafe_allow_html=True)
