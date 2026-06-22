"""
RFM Dashboard Builder
=====================
Fetches data from Google Sheets (RFM - E tab) and generates index.html

Requirements:
    pip install requests pandas

Usage:
    python build_dashboard.py

Output:
    index.html  — open in any browser or upload to GitHub Pages
"""

import requests
import csv
import io
import json
import sys
from collections import defaultdict

# ── CONFIG ─────────────────────────────────────────────────────────────────
SHEET_ID = "10XNFBfJKW4gs_ra9CNtPUA5GXi9tb6xbnf6PnFgDSLI"
GID      = "1815598507"          # RFM - E tab
OUTPUT   = "index.html"

FETCH_URLS = [
    f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv&gid={GID}",
    f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&gid={GID}",
    f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet=RFM+-+E",
]

NUMERIC_FIELDS = [
    "new_customers","retained_customers","reactivated_customers","total_customers",
    "new_overall_nob","retained_overall_nob","reactivated_overall_nob","total_overall_nob",
    "new_overall_sales","retained_overall_sales","reactivated_overall_sales","total_overall_sales",
    "total_fmcg_sales","new_fmcg_sales","retained_fmcg_sales","reactivated_fmcg_sales",
    "total_fruits_sales","new_fruits_sales","retained_fruits_sales","reactivated_fruits_sales",
    "total_vegetables_sales","new_vegetables_sales","retained_vegetables_sales","reactivated_vegetables_sales",
    "total_staples_sales","new_staples_sales","retained_staples_sales","reactivated_staples_sales",
    "total_consumables_sales","new_consumables_sales","retained_consumables_sales","reactivated_consumables_sales",
    "total_kpn_services_sales","new_kpn_services_sales","retained_kpn_services_sales","reactivated_kpn_services_sales",
    "total_marketing_scheme_sales","new_marketing_scheme_sales","retained_marketing_scheme_sales","reactivated_marketing_scheme_sales",
]

# ── FETCH ───────────────────────────────────────────────────────────────────
def fetch_csv():
    for url in FETCH_URLS:
        try:
            print(f"  Trying: {url[:80]}...")
            r = requests.get(url, timeout=40)
            if r.status_code != 200:
                print(f"    HTTP {r.status_code}, skipping")
                continue
            text = r.text
            if len(text) < 200 or text.strip().startswith("<"):
                print("    Response looks like HTML error page, skipping")
                continue
            if "rolling_period" not in text:
                print("    'rolling_period' column not found, skipping")
                continue
            print(f"    ✓ Got {len(text):,} bytes")
            return text
        except Exception as e:
            print(f"    Error: {e}")
    return None

# ── PARSE ───────────────────────────────────────────────────────────────────
def parse_csv(text):
    reader = csv.DictReader(io.StringIO(text))
    rows = []
    for row in reader:
        clean = {k.strip().lower().replace(" ", "_"): v.strip().strip('"') for k, v in row.items()}
        for f in NUMERIC_FIELDS:
            clean[f] = float(clean.get(f, 0) or 0)
        rows.append(clean)
    return rows

# ── AGGREGATE ───────────────────────────────────────────────────────────────
def zero_row():
    return {f: 0.0 for f in NUMERIC_FIELDS}

def add_row(dest, src):
    for f in NUMERIC_FIELDS:
        dest[f] += src.get(f, 0)

def aggregate_monthly(rows):
    """Returns list of dicts aggregated by (ym, cluster_manager)."""
    grp = defaultdict(zero_row)
    meta = {}
    for r in rows:
        p = r.get("rolling_period", "")
        if not p.startswith("RM_"):
            continue
        ym = p.replace("RM_", "")
        cm = r.get("cluster_manager", "")
        key = (ym, cm)
        add_row(grp[key], r)
        if key not in meta:
            meta[key] = {"ym": ym, "cluster_manager": cm, "period": p}
    result = []
    for key, vals in grp.items():
        row = dict(meta[key])
        row.update(vals)
        result.append(row)
    return sorted(result, key=lambda x: (x["ym"], x["cluster_manager"]))

def aggregate_weekly_all(rows):
    """Returns list of dicts aggregated by rolling_period (all CMs combined)."""
    grp = defaultdict(zero_row)
    meta = {}
    for r in rows:
        p = r.get("rolling_period", "")
        if not p.startswith("RW_"):
            continue
        add_row(grp[p], r)
        if p not in meta:
            meta[p] = {"wk": p, "period_start": r.get("period_start", "")}
    result = []
    for key, vals in grp.items():
        row = dict(meta[key])
        row.update(vals)
        result.append(row)
    return sorted(result, key=lambda x: x["wk"])

def aggregate_weekly_cm(rows):
    """Returns list of dicts aggregated by (rolling_period, cluster_manager)."""
    grp = defaultdict(zero_row)
    meta = {}
    for r in rows:
        p = r.get("rolling_period", "")
        if not p.startswith("RW_"):
            continue
        cm = r.get("cluster_manager", "")
        key = (p, cm)
        add_row(grp[key], r)
        if key not in meta:
            meta[key] = {"wk": p, "cluster_manager": cm, "period_start": r.get("period_start", "")}
    result = []
    for key, vals in grp.items():
        row = dict(meta[key])
        row.update(vals)
        result.append(row)
    return sorted(result, key=lambda x: (x["wk"], x["cluster_manager"]))

# ── ROUND ALL NUMERICS ───────────────────────────────────────────────────────
def round_row(row):
    out = {}
    for k, v in row.items():
        out[k] = round(v) if k in NUMERIC_FIELDS else v
    return out

# ── BUILD HTML ───────────────────────────────────────────────────────────────
HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>RFM Deep Analysis — Chennai</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:system-ui,sans-serif;background:#0a0a0a;color:#e8e8e8;font-size:13px}
::-webkit-scrollbar{width:5px;height:5px}::-webkit-scrollbar-track{background:#0a0a0a}::-webkit-scrollbar-thumb{background:#2a2a2a;border-radius:3px}
.wrap{max-width:1400px;margin:0 auto;padding:14px}
h1{font-size:17px;font-weight:600;color:#f5f5f5}
.subtitle{font-size:11px;color:#666;margin-top:3px;margin-bottom:14px}
.tabs{display:flex;gap:0;border-bottom:1px solid #222;margin-bottom:16px;background:#111;border-radius:8px 8px 0 0;padding:0 6px;overflow-x:auto}
.tab{padding:9px 16px;font-size:12px;font-weight:500;cursor:pointer;color:#666;border:none;background:none;border-bottom:2px solid transparent;white-space:nowrap;transition:all .15s}
.tab.active{color:#4d9bff;border-bottom-color:#4d9bff}
.section{display:none}.section.active{display:block}
.card{background:#141414;border-radius:8px;padding:14px;margin-bottom:12px;border:1px solid #222}
.kpi-row{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:8px;margin-bottom:12px}
.kpi{background:#1a1a1a;border-radius:6px;padding:10px 12px;border:1px solid #222}
.kpi-label{font-size:10px;color:#888;margin-bottom:2px}
.kpi-val{font-size:19px;font-weight:700;color:#f5f5f5}
.kpi-sub{font-size:10px;color:#666;margin-top:2px}
.kpi-delta{font-size:10px;margin-top:2px}
.up{color:#3ddc84}.dn{color:#ff5c5c}
.filter-row{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin-bottom:10px}
.filter-row label{font-size:11px;color:#888}
.filter-row select{font-size:11px;padding:4px 8px;border-radius:5px;border:1px solid #2a2a2a;background:#1a1a1a;color:#e8e8e8;cursor:pointer;outline:none}
.ch{font-size:12px;font-weight:600;color:#ccc;margin-bottom:6px;margin-top:14px}
.legend{display:flex;flex-wrap:wrap;gap:8px;font-size:10px;color:#777;margin-bottom:5px}
.legend span{display:flex;align-items:center;gap:4px}
.ls{width:8px;height:8px;border-radius:2px;flex-shrink:0}
.cw{position:relative;width:100%;margin-bottom:6px}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.g3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px}
table{width:100%;border-collapse:collapse;font-size:11px}
th{text-align:left;padding:6px 8px;font-size:10px;font-weight:600;color:#888;background:#111;border-bottom:1px solid #222;white-space:nowrap}
th.num{text-align:right}
td{padding:5px 8px;border-bottom:1px solid #1a1a1a;color:#ccc;white-space:nowrap}
td.num{text-align:right}
tr:last-child td{border-bottom:none}
tr:hover td{background:#181818}
.badge{display:inline-block;font-size:9px;padding:1px 6px;border-radius:8px;font-weight:600}
.badge-b{background:#16304d;color:#5aadff}
.badge-g{background:#123a22;color:#4dde8a}
.badge-a{background:#3a2410;color:#f0a050}
.cohort-wrap{overflow-x:auto;margin-top:8px}
.cohort-table{border-collapse:collapse;font-size:11px;min-width:600px}
.cohort-table th{padding:5px 8px;font-size:10px;color:#666;border:none;white-space:nowrap;background:transparent;font-weight:500}
.cohort-table td{padding:4px 6px;text-align:center;border:1px solid #111;font-size:10px;min-width:60px}
.c-label{text-align:left!important;color:#999;font-weight:500;min-width:80px;white-space:nowrap}
.c-base{background:#1a3a5c;color:#90caff;font-weight:700}
.c-hi{background:#1a3a1a;color:#66cc66}
.c-mid{background:#2a2a10;color:#bbbb44}
.c-lo{background:#2a1010;color:#cc6666}
.c-empty{background:#111;color:#333}
.cat-month-tbl th{text-align:right}
.cat-month-tbl th:first-child{text-align:left}
.cat-month-tbl td:first-child{text-align:left;font-weight:600;color:#e8e8e8}
@media(max-width:700px){.g2,.g3{grid-template-columns:1fr}}
</style>
</head>
<body>
<div class="wrap">
<h1>📊 RFM Deep Analysis Dashboard</h1>
<div class="subtitle">Chennai &nbsp;|&nbsp; Apr 2024 – Jun 2026 &nbsp;|&nbsp; 5 cluster managers &nbsp;|&nbsp; 27 months &nbsp;|&nbsp; Built: __BUILD_DATE__</div>

<div class="tabs">
  <button class="tab active" onclick="switchTab('month')">📅 Monthly</button>
  <button class="tab" onclick="switchTab('week')">📆 Weekly</button>
  <button class="tab" onclick="switchTab('cm')">👥 Managers</button>
  <button class="tab" onclick="switchTab('cat')">📦 Category (month)</button>
  <button class="tab" onclick="switchTab('cohort')">🔁 Cohort analysis</button>
</div>

<!-- MONTHLY -->
<div id="tab-month" class="section active">
  <div class="card">
    <div class="filter-row">
      <label>Manager:</label><select id="m-cm" onchange="renderMonth()">__CM_OPTIONS__</select>
      <label>Year:</label><select id="m-yr" onchange="renderMonth()">
        <option value="all">All</option><option value="2024">2024</option><option value="2025">2025</option><option value="2026">2026</option>
      </select>
    </div>
    <div class="kpi-row" id="m-kpis"></div>
  </div>
  <div class="card">
    <div class="ch">Sales trend (₹) — by segment</div>
    <div class="legend"><span><span class="ls" style="background:#1a73e8"></span>New</span><span><span class="ls" style="background:#1a8a4a"></span>Retained</span><span><span class="ls" style="background:#c0392b"></span>Reactivated</span></div>
    <div class="cw" style="height:210px"><canvas id="mc1"></canvas></div>
  </div>
  <div class="g2">
    <div class="card"><div class="ch">Retention &amp; reactivation rate (%)</div><div class="cw" style="height:175px"><canvas id="mc3"></canvas></div></div>
    <div class="card"><div class="ch">Avg ₹/customer — by segment</div><div class="legend"><span><span class="ls" style="background:#1a73e8"></span>New</span><span><span class="ls" style="background:#1a8a4a"></span>Retained</span><span><span class="ls" style="background:#c0392b"></span>Reactivated</span></div><div class="cw" style="height:175px"><canvas id="mc4"></canvas></div></div>
  </div>
  <div class="card">
    <div class="ch">Customer volume — new / retained / reactivated</div>
    <div class="legend"><span><span class="ls" style="background:#1a73e8"></span>New</span><span><span class="ls" style="background:#1a8a4a"></span>Retained</span><span><span class="ls" style="background:#c0392b"></span>Reactivated</span></div>
    <div class="cw" style="height:200px"><canvas id="mc2"></canvas></div>
  </div>
</div>

<!-- WEEKLY -->
<div id="tab-week" class="section">
  <div class="card">
    <div class="filter-row">
      <label>Manager:</label><select id="w-cm" onchange="renderWeek()">__CM_OPTIONS__</select>
      <label>Month:</label><select id="w-mo" onchange="renderWeek()">__WEEK_MONTH_OPTIONS__</select>
    </div>
    <div class="kpi-row" id="w-kpis"></div>
  </div>
  <div class="card"><div class="ch">Weekly customers — new / retained / reactivated</div><div class="legend"><span><span class="ls" style="background:#1a73e8"></span>New</span><span><span class="ls" style="background:#1a8a4a"></span>Retained</span><span><span class="ls" style="background:#c0392b"></span>Reactivated</span></div><div class="cw" style="height:200px"><canvas id="wc1"></canvas></div></div>
  <div class="g2">
    <div class="card"><div class="ch">Retention rate % — weekly</div><div class="cw" style="height:175px"><canvas id="wc3"></canvas></div></div>
    <div class="card"><div class="ch">Reactivation rate % — weekly</div><div class="cw" style="height:175px"><canvas id="wc5"></canvas></div></div>
  </div>
  <div class="card"><div class="ch">Weekly sales stacked (₹)</div><div class="legend"><span><span class="ls" style="background:#1a73e8"></span>New</span><span><span class="ls" style="background:#1a8a4a"></span>Retained</span><span><span class="ls" style="background:#c0392b"></span>Reactivated</span></div><div class="cw" style="height:200px"><canvas id="wc2"></canvas></div></div>
  <div class="card"><div class="ch">Category sales — weekly (₹)</div><div class="legend"><span><span class="ls" style="background:#1a73e8"></span>FMCG</span><span><span class="ls" style="background:#c0392b"></span>Fruits</span><span><span class="ls" style="background:#7f77dd"></span>Veg</span><span><span class="ls" style="background:#ba7517"></span>Staples</span><span><span class="ls" style="background:#1a8a4a"></span>Cons</span></div><div class="cw" style="height:195px"><canvas id="wc4"></canvas></div></div>
</div>

<!-- MANAGERS -->
<div id="tab-cm" class="section">
  <div class="card"><div class="filter-row"><label>Year:</label><select id="cm-yr" onchange="renderCM()"><option value="all">All</option><option value="2024">2024</option><option value="2025">2025</option><option value="2026">2026</option></select></div><div class="kpi-row" id="cm-kpis"></div></div>
  <div class="g2">
    <div class="card"><div class="ch">Total sales by manager (₹)</div><div class="cw" style="height:210px"><canvas id="cmc1"></canvas></div></div>
    <div class="card"><div class="ch">Customer count by manager</div><div class="cw" style="height:210px"><canvas id="cmc2"></canvas></div></div>
  </div>
  <div class="g2">
    <div class="card"><div class="ch">Retention rate by manager (%)</div><div class="cw" style="height:200px"><canvas id="cmc3"></canvas></div></div>
    <div class="card"><div class="ch">Avg ₹/customer by manager</div><div class="cw" style="height:200px"><canvas id="cmc4"></canvas></div></div>
  </div>
  <div class="card"><div class="ch">Manager detail table</div><div id="cm-table" style="margin-top:8px;overflow-x:auto"></div></div>
</div>

<!-- CATEGORY MONTH -->
<div id="tab-cat" class="section">
  <div class="card">
    <div class="filter-row">
      <label>Manager:</label><select id="cat-cm" onchange="renderCat()">__CM_OPTIONS__</select>
      <label>Year:</label><select id="cat-yr" onchange="renderCat()"><option value="all">All</option><option value="2024">2024</option><option value="2025">2025</option><option value="2026">2026</option></select>
    </div>
    <div class="ch">Category sales — month-by-month</div>
    <div class="legend"><span><span class="ls" style="background:#1a73e8"></span>FMCG</span><span><span class="ls" style="background:#c0392b"></span>Fruits</span><span><span class="ls" style="background:#7f77dd"></span>Veg</span><span><span class="ls" style="background:#ba7517"></span>Staples</span><span><span class="ls" style="background:#1a8a4a"></span>Cons</span></div>
    <div class="cw" style="height:220px"><canvas id="catc1"></canvas></div>
  </div>
  <div class="card"><div class="ch">Category performance table — month level</div><div id="cat-month-table" style="margin-top:8px;overflow-x:auto"></div></div>
  <div class="card"><div class="ch">Category × segment (new / retained / reactivated)</div><div class="legend"><span><span class="ls" style="background:#1a73e8"></span>New</span><span><span class="ls" style="background:#1a8a4a"></span>Retained</span><span><span class="ls" style="background:#c0392b"></span>Reactivated</span></div><div class="cw" style="height:220px"><canvas id="catc2"></canvas></div></div>
</div>

<!-- COHORT -->
<div id="tab-cohort" class="section">
  <div class="card">
    <div class="filter-row">
      <label>Manager:</label><select id="coh-cm" onchange="renderCohort()">__CM_OPTIONS__</select>
      <label>Type:</label><select id="coh-type" onchange="renderCohort()"><option value="customers">Customer retention</option><option value="sales">Revenue retention</option></select>
      <label>Show:</label><select id="coh-show" onchange="renderCohort()"><option value="pct">% of base</option><option value="abs">Absolute</option></select>
    </div>
    <p style="font-size:11px;color:#666;margin-bottom:10px">Each row = customers first acquired in that month. Columns = M+1, M+2… M+12 return rate.</p>
    <div class="cohort-wrap" id="cohort-wrap"></div>
  </div>
  <div class="card"><div class="ch">Avg retention % by cohort age (all cohorts blended)</div><div class="cw" style="height:200px"><canvas id="cohc1"></canvas></div></div>
</div>

</div>
<script>
var MDATA=__MDATA__;
var WDATA=__WDATA__;
var WCMDATA=__WCMDATA__;
var charts={};

function fL(v){v=Math.round(v);if(v>=10000000)return'₹'+(v/10000000).toFixed(2)+'Cr';if(v>=100000)return'₹'+(v/100000).toFixed(2)+'L';if(v>=1000)return'₹'+(v/1000).toFixed(1)+'K';return'₹'+v;}
function nL(v){v=Math.round(v);if(v>=10000000)return(v/10000000).toFixed(2)+'Cr';if(v>=100000)return(v/100000).toFixed(2)+'L';if(v>=1000)return(v/1000).toFixed(1)+'K';return v.toLocaleString('en-IN');}
function fmtPct(a,b){return b>0?(a/b*100).toFixed(1)+'%':'—';}
function n(r,f){return parseFloat(r[f])||0;}
function dC(){Object.values(charts).forEach(function(c){try{c.destroy();}catch(e){}});charts={};}
var DARK={responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:{ticks:{color:'#555',font:{size:9},autoSkip:true,maxRotation:45},grid:{color:'#1e1e1e'}},y:{ticks:{color:'#555',font:{size:9}},grid:{color:'#1e1e1e'}}}};
function mkC(id,type,data,opts){var el=document.getElementById(id);if(!el)return;if(charts[id])charts[id].destroy();charts[id]=new Chart(el,{type:type,data:data,options:opts||DARK});}

function switchTab(t){
  document.querySelectorAll('.tab').forEach(function(el){el.classList.toggle('active',el.getAttribute('onclick').includes("'"+t+"'"));});
  document.querySelectorAll('.section').forEach(function(el){el.classList.remove('active');});
  document.getElementById('tab-'+t).classList.add('active');
  dC();
  if(t==='month')renderMonth();else if(t==='week')renderWeek();else if(t==='cm')renderCM();else if(t==='cat')renderCat();else if(t==='cohort')renderCohort();
}

function renderMonth(){
  dC();
  var cm=document.getElementById('m-cm').value,yr=document.getElementById('m-yr').value;
  var rows=MDATA.filter(function(r){return(cm==='all'||r.cluster_manager===cm)&&(yr==='all'||r.ym.indexOf(yr)===0);});
  var ymMap={};
  rows.forEach(function(r){if(!ymMap[r.ym])ymMap[r.ym]={N:0,R:0,X:0,sN:0,sR:0,sX:0,nob:0};var m=ymMap[r.ym];m.N+=n(r,'new_customers');m.R+=n(r,'retained_customers');m.X+=n(r,'reactivated_customers');m.sN+=n(r,'new_overall_sales');m.sR+=n(r,'retained_overall_sales');m.sX+=n(r,'reactivated_overall_sales');m.nob+=n(r,'total_overall_nob');});
  var yms=Object.keys(ymMap).sort();
  var tN=0,tR=0,tX=0,tS=0,tNob=0;yms.forEach(function(y){tN+=ymMap[y].N;tR+=ymMap[y].R;tX+=ymMap[y].X;tS+=ymMap[y].sN+ymMap[y].sR+ymMap[y].sX;tNob+=ymMap[y].nob;});
  var tC=tN+tR+tX;var lym=yms[yms.length-1],pym=yms[yms.length-2];var lm=ymMap[lym]||{},pm=ymMap[pym]||{};
  var lmS=(lm.sN||0)+(lm.sR||0)+(lm.sX||0),pmS=(pm.sN||0)+(pm.sR||0)+(pm.sX||0);
  var sChg=pmS>0?((lmS-pmS)/pmS*100):0;
  function kpi(l,v,s,d){var dd='';if(d)dd='<div class="kpi-delta '+(d>0?'up':'dn')+'">'+(d>0?'▲':'▼')+Math.abs(d).toFixed(1)+'% vs prev</div>';return'<div class="kpi"><div class="kpi-label">'+l+'</div><div class="kpi-val">'+v+'</div><div class="kpi-sub">'+s+'</div>'+dd+'</div>';}
  document.getElementById('m-kpis').innerHTML=[kpi('Customers',nL(tC),'all',0),kpi('Sales',fL(tS),'all',sChg),kpi('NOB',nL(tNob),'bills',0),kpi('New',nL(tN),fmtPct(tN,tC),0),kpi('Retained',nL(tR),fmtPct(tR,tC),0),kpi('Reactivated',nL(tX),fmtPct(tX,tC),0),kpi('₹/cust',fL(tC>0?tS/tC:0),'blended',0),kpi('Latest',lym?fL(lmS):'—',lym||'',0)].join('');
  var SO=Object.assign({},DARK,{scales:{x:DARK.scales.x,y:{ticks:{callback:function(v){return fL(v);},color:'#555',font:{size:9}},grid:{color:'#1e1e1e'}}}});
  mkC('mc1','bar',{labels:yms,datasets:[{label:'New',data:yms.map(function(y){return Math.round(ymMap[y].sN);}),backgroundColor:'rgba(26,115,232,.85)',stack:'s'},{label:'Retained',data:yms.map(function(y){return Math.round(ymMap[y].sR);}),backgroundColor:'rgba(26,138,74,.85)',stack:'s'},{label:'Reactivated',data:yms.map(function(y){return Math.round(ymMap[y].sX);}),backgroundColor:'rgba(192,57,43,.85)',stack:'s'}]},SO);
  var CO=Object.assign({},DARK,{scales:{x:DARK.scales.x,y:{ticks:{callback:function(v){return nL(v);},color:'#555',font:{size:9}},grid:{color:'#1e1e1e'}}}});
  mkC('mc2','bar',{labels:yms,datasets:[{label:'New',data:yms.map(function(y){return Math.round(ymMap[y].N);}),backgroundColor:'rgba(26,115,232,.85)',stack:'s'},{label:'Retained',data:yms.map(function(y){return Math.round(ymMap[y].R);}),backgroundColor:'rgba(26,138,74,.85)',stack:'s'},{label:'Reactivated',data:yms.map(function(y){return Math.round(ymMap[y].X);}),backgroundColor:'rgba(192,57,43,.85)',stack:'s'}]},CO);
  mkC('mc3','line',{labels:yms,datasets:[{label:'Ret%',data:yms.map(function(y){var m=ymMap[y],t=m.N+m.R+m.X;return t>0?+(m.R/t*100).toFixed(1):0;}),borderColor:'#1a8a4a',backgroundColor:'rgba(26,138,74,.1)',fill:true,tension:.35,borderWidth:2,pointRadius:2},{label:'Rea%',data:yms.map(function(y){var m=ymMap[y],t=m.N+m.R+m.X;return t>0?+(m.X/t*100).toFixed(1):0;}),borderColor:'#c0392b',fill:false,tension:.35,borderDash:[4,3],borderWidth:1.5,pointRadius:1.5}]},{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:DARK.scales.x,y:{min:0,ticks:{callback:function(v){return v+'%';},color:'#555',font:{size:9}},grid:{color:'#1e1e1e'}}}});
  mkC('mc4','line',{labels:yms,datasets:[{label:'New',data:yms.map(function(y){var m=ymMap[y];return m.N>0?Math.round(m.sN/m.N):0;}),borderColor:'#1a73e8',fill:false,tension:.35,borderWidth:2,pointRadius:2},{label:'Retained',data:yms.map(function(y){var m=ymMap[y];return m.R>0?Math.round(m.sR/m.R):0;}),borderColor:'#1a8a4a',fill:false,tension:.35,borderWidth:2,pointRadius:2},{label:'Reactivated',data:yms.map(function(y){var m=ymMap[y];return m.X>0?Math.round(m.sX/m.X):0;}),borderColor:'#c0392b',fill:false,tension:.35,borderWidth:2,pointRadius:2}]},{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:DARK.scales.x,y:{ticks:{callback:function(v){return fL(v);},color:'#555',font:{size:9}},grid:{color:'#1e1e1e'}}}});
}

function renderWeek(){
  dC();
  var cm=document.getElementById('w-cm').value,mo=document.getElementById('w-mo').value;
  var src=cm==='all'?WDATA:WCMDATA.filter(function(r){return r.cluster_manager===cm;});
  var wkMap={};
  src.forEach(function(r){var wk=r.wk;if(mo!=='all'&&wk.substring(0,7)!==mo)return;if(!wkMap[wk])wkMap[wk]={wk:wk,N:0,R:0,X:0,sN:0,sR:0,sX:0,fmcg:0,fruits:0,veg:0,staples:0,cons:0};var m=wkMap[wk];m.N+=n(r,'new_customers');m.R+=n(r,'retained_customers');m.X+=n(r,'reactivated_customers');m.sN+=n(r,'new_overall_sales');m.sR+=n(r,'retained_overall_sales');m.sX+=n(r,'reactivated_overall_sales');m.fmcg+=n(r,'total_fmcg_sales');m.fruits+=n(r,'total_fruits_sales');m.veg+=n(r,'total_vegetables_sales');m.staples+=n(r,'total_staples_sales');m.cons+=n(r,'total_consumables_sales');});
  var wks=Object.keys(wkMap).sort();
  var tN=0,tR=0,tX=0,tS=0;wks.forEach(function(w){tN+=wkMap[w].N;tR+=wkMap[w].R;tX+=wkMap[w].X;tS+=wkMap[w].sN+wkMap[w].sR+wkMap[w].sX;});
  var tC=tN+tR+tX;
  function kpi(l,v,s){return'<div class="kpi"><div class="kpi-label">'+l+'</div><div class="kpi-val">'+v+'</div><div class="kpi-sub">'+s+'</div></div>';}
  document.getElementById('w-kpis').innerHTML=[kpi('Customers',nL(tC),'all weeks'),kpi('Sales',fL(tS),'all weeks'),kpi('New',nL(tN),fmtPct(tN,tC)),kpi('Retained',nL(tR),fmtPct(tR,tC)),kpi('Reactivated',nL(tX),fmtPct(tX,tC))].join('');
  var lbls=wks.map(function(w){return w.replace('RW_','');});
  var SO=Object.assign({},DARK,{scales:{x:DARK.scales.x,y:{ticks:{callback:function(v){return nL(v);},color:'#555',font:{size:9}},grid:{color:'#1e1e1e'}}}});
  mkC('wc1','bar',{labels:lbls,datasets:[{label:'New',data:wks.map(function(w){return wkMap[w].N;}),backgroundColor:'rgba(26,115,232,.85)',stack:'s'},{label:'Retained',data:wks.map(function(w){return wkMap[w].R;}),backgroundColor:'rgba(26,138,74,.85)',stack:'s'},{label:'Reactivated',data:wks.map(function(w){return wkMap[w].X;}),backgroundColor:'rgba(192,57,43,.85)',stack:'s'}]},SO);
  var SS=Object.assign({},DARK,{scales:{x:DARK.scales.x,y:{ticks:{callback:function(v){return fL(v);},color:'#555',font:{size:9}},grid:{color:'#1e1e1e'}}}});
  mkC('wc2','bar',{labels:lbls,datasets:[{label:'New',data:wks.map(function(w){return Math.round(wkMap[w].sN);}),backgroundColor:'rgba(26,115,232,.85)',stack:'s'},{label:'Retained',data:wks.map(function(w){return Math.round(wkMap[w].sR);}),backgroundColor:'rgba(26,138,74,.85)',stack:'s'},{label:'Reactivated',data:wks.map(function(w){return Math.round(wkMap[w].sX);}),backgroundColor:'rgba(192,57,43,.85)',stack:'s'}]},SS);
  var RP={responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:DARK.scales.x,y:{min:0,ticks:{callback:function(v){return v+'%';},color:'#555',font:{size:9}},grid:{color:'#1e1e1e'}}}};
  mkC('wc3','line',{labels:lbls,datasets:[{label:'Ret%',data:wks.map(function(w){var m=wkMap[w],t=m.N+m.R+m.X;return t>0?+(m.R/t*100).toFixed(1):0;}),borderColor:'#1a8a4a',backgroundColor:'rgba(26,138,74,.1)',fill:true,tension:.35,borderWidth:2,pointRadius:1.5}]},RP);
  mkC('wc5','line',{labels:lbls,datasets:[{label:'Rea%',data:wks.map(function(w){var m=wkMap[w],t=m.N+m.R+m.X;return t>0?+(m.X/t*100).toFixed(1):0;}),borderColor:'#c0392b',backgroundColor:'rgba(192,57,43,.1)',fill:true,tension:.35,borderWidth:2,pointRadius:1.5}]},RP);
  mkC('wc4','line',{labels:lbls,datasets:[{label:'FMCG',data:wks.map(function(w){return Math.round(wkMap[w].fmcg);}),borderColor:'#1a73e8',fill:false,tension:.35,borderWidth:1.5,pointRadius:1},{label:'Fruits',data:wks.map(function(w){return Math.round(wkMap[w].fruits);}),borderColor:'#c0392b',fill:false,tension:.35,borderWidth:1.5,pointRadius:1},{label:'Veg',data:wks.map(function(w){return Math.round(wkMap[w].veg);}),borderColor:'#7f77dd',fill:false,tension:.35,borderWidth:1.5,pointRadius:1},{label:'Staples',data:wks.map(function(w){return Math.round(wkMap[w].staples);}),borderColor:'#ba7517',fill:false,tension:.35,borderWidth:1.5,pointRadius:1},{label:'Cons',data:wks.map(function(w){return Math.round(wkMap[w].cons);}),borderColor:'#1a8a4a',fill:false,tension:.35,borderWidth:1.5,pointRadius:1}]},SS);
}

function renderCM(){
  dC();
  var yr=document.getElementById('cm-yr').value;
  var rows=MDATA.filter(function(r){return yr==='all'||r.ym.indexOf(yr)===0;});
  var cmMap={};
  rows.forEach(function(r){var cm=r.cluster_manager;if(!cmMap[cm])cmMap[cm]={N:0,R:0,X:0,tot:0,sales:0,nob:0,sN:0,sR:0,sX:0};var m=cmMap[cm];m.N+=n(r,'new_customers');m.R+=n(r,'retained_customers');m.X+=n(r,'reactivated_customers');m.tot+=n(r,'total_customers');m.sales+=n(r,'total_overall_sales');m.nob+=n(r,'total_overall_nob');m.sN+=n(r,'new_overall_sales');m.sR+=n(r,'retained_overall_sales');m.sX+=n(r,'reactivated_overall_sales');});
  var cms=Object.keys(cmMap).sort(function(a,b){return cmMap[b].sales-cmMap[a].sales;});
  var tS=cms.reduce(function(s,c){return s+cmMap[c].sales;},0),tC=cms.reduce(function(s,c){return s+cmMap[c].tot;},0);
  function kpi(l,v,s){return'<div class="kpi"><div class="kpi-label">'+l+'</div><div class="kpi-val">'+v+'</div><div class="kpi-sub">'+s+'</div></div>';}
  document.getElementById('cm-kpis').innerHTML=[kpi('Total sales',fL(tS),'all managers'),kpi('Total customers',nL(tC),'all segments'),kpi('Managers',cms.length+'','active'),kpi('Top manager',cms[0]||'—',fL(cmMap[cms[0]]?cmMap[cms[0]].sales:0))].join('');
  var clrs=['#1a73e8','#1a8a4a','#c0392b','#7f77dd','#ba7517'];
  mkC('cmc1','bar',{labels:cms,datasets:[{data:cms.map(function(c){return Math.round(cmMap[c].sales);}),backgroundColor:clrs}]},{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:DARK.scales.x,y:{ticks:{callback:function(v){return fL(v);},color:'#555',font:{size:9}},grid:{color:'#1e1e1e'}}}});
  mkC('cmc2','bar',{labels:cms,datasets:[{data:cms.map(function(c){return Math.round(cmMap[c].tot);}),backgroundColor:clrs}]},{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:DARK.scales.x,y:{ticks:{callback:function(v){return nL(v);},color:'#555',font:{size:9}},grid:{color:'#1e1e1e'}}}});
  mkC('cmc3','bar',{labels:cms,datasets:[{data:cms.map(function(c){var m=cmMap[c];return m.tot>0?+(m.R/m.tot*100).toFixed(1):0;}),backgroundColor:clrs}]},{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:DARK.scales.x,y:{min:0,ticks:{callback:function(v){return v+'%';},color:'#555',font:{size:9}},grid:{color:'#1e1e1e'}}}});
  mkC('cmc4','bar',{labels:cms,datasets:[{data:cms.map(function(c){var m=cmMap[c];return m.tot>0?Math.round(m.sales/m.tot):0;}),backgroundColor:clrs}]},{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:DARK.scales.x,y:{ticks:{callback:function(v){return fL(v);},color:'#555',font:{size:9}},grid:{color:'#1e1e1e'}}}});
  var tbl='<table><thead><tr><th>Manager</th><th class="num">New</th><th class="num">Retained</th><th class="num">Reactivated</th><th class="num">Total</th><th class="num">Ret%</th><th class="num">Sales</th><th class="num">New Sales</th><th class="num">Ret Sales</th><th class="num">NOB</th><th class="num">₹/Cust</th><th class="num">₹/Bill</th></tr></thead><tbody>';
  cms.forEach(function(c){var m=cmMap[c];var rr=m.tot>0?(m.R/m.tot*100).toFixed(1):0;var rc=rr>50?'#3ddc84':rr>35?'#ddaa44':'#ff5c5c';tbl+='<tr><td>'+c+'</td><td class="num"><span class="badge badge-b">'+nL(m.N)+'</span></td><td class="num"><span class="badge badge-g">'+nL(m.R)+'</span></td><td class="num"><span class="badge badge-a">'+nL(m.X)+'</span></td><td class="num">'+nL(m.tot)+'</td><td class="num" style="color:'+rc+'">'+rr+'%</td><td class="num">'+fL(m.sales)+'</td><td class="num">'+fL(m.sN)+'</td><td class="num">'+fL(m.sR)+'</td><td class="num">'+nL(m.nob)+'</td><td class="num">'+(m.tot>0?fL(m.sales/m.tot):'—')+'</td><td class="num">'+(m.nob>0?fL(m.sales/m.nob):'—')+'</td></tr>';});
  tbl+='</tbody></table>';document.getElementById('cm-table').innerHTML=tbl;
}

function renderCat(){
  dC();
  var cm=document.getElementById('cat-cm').value,yr=document.getElementById('cat-yr').value;
  var rows=MDATA.filter(function(r){return(cm==='all'||r.cluster_manager===cm)&&(yr==='all'||r.ym.indexOf(yr)===0);});
  var ymMap={};
  rows.forEach(function(r){var y=r.ym;if(!ymMap[y])ymMap[y]={fmcg:0,fruits:0,veg:0,staples:0,cons:0,kpn:0,mkt:0,nF:0,rF:0,xF:0,nFr:0,rFr:0,xFr:0,nV:0,rV:0,xV:0,nS:0,rS:0,xS:0,totS:0};var m=ymMap[y];m.fmcg+=n(r,'total_fmcg_sales');m.fruits+=n(r,'total_fruits_sales');m.veg+=n(r,'total_vegetables_sales');m.staples+=n(r,'total_staples_sales');m.cons+=n(r,'total_consumables_sales');m.kpn+=n(r,'total_kpn_services_sales');m.mkt+=n(r,'total_marketing_scheme_sales');m.nF+=n(r,'new_fmcg_sales');m.rF+=n(r,'retained_fmcg_sales');m.xF+=n(r,'reactivated_fmcg_sales');m.nFr+=n(r,'new_fruits_sales');m.rFr+=n(r,'retained_fruits_sales');m.xFr+=n(r,'reactivated_fruits_sales');m.nV+=n(r,'new_vegetables_sales');m.rV+=n(r,'retained_vegetables_sales');m.xV+=n(r,'reactivated_vegetables_sales');m.nS+=n(r,'new_staples_sales');m.rS+=n(r,'retained_staples_sales');m.xS+=n(r,'reactivated_staples_sales');m.totS+=n(r,'total_overall_sales');});
  var yms=Object.keys(ymMap).sort();
  var SS=Object.assign({},DARK,{scales:{x:DARK.scales.x,y:{ticks:{callback:function(v){return fL(v);},color:'#555',font:{size:9}},grid:{color:'#1e1e1e'}}}});
  mkC('catc1','bar',{labels:yms,datasets:[{label:'FMCG',data:yms.map(function(y){return Math.round(ymMap[y].fmcg);}),backgroundColor:'rgba(26,115,232,.85)',stack:'s'},{label:'Fruits',data:yms.map(function(y){return Math.round(ymMap[y].fruits);}),backgroundColor:'rgba(192,57,43,.85)',stack:'s'},{label:'Veg',data:yms.map(function(y){return Math.round(ymMap[y].veg);}),backgroundColor:'rgba(127,119,221,.85)',stack:'s'},{label:'Staples',data:yms.map(function(y){return Math.round(ymMap[y].staples);}),backgroundColor:'rgba(186,117,23,.85)',stack:'s'},{label:'Cons',data:yms.map(function(y){return Math.round(ymMap[y].cons);}),backgroundColor:'rgba(26,138,74,.85)',stack:'s'}]},SS);
  var cats=['FMCG','Fruits','Veg','Staples'];
  var totF={n:0,r:0,x:0},totFr={n:0,r:0,x:0},totV={n:0,r:0,x:0},totS={n:0,r:0,x:0};
  yms.forEach(function(y){var m=ymMap[y];totF.n+=m.nF;totF.r+=m.rF;totF.x+=m.xF;totFr.n+=m.nFr;totFr.r+=m.rFr;totFr.x+=m.xFr;totV.n+=m.nV;totV.r+=m.rV;totV.x+=m.xV;totS.n+=m.nS;totS.r+=m.rS;totS.x+=m.xS;});
  mkC('catc2','bar',{labels:cats,datasets:[{label:'New',data:[totF.n,totFr.n,totV.n,totS.n].map(Math.round),backgroundColor:'rgba(26,115,232,.85)',stack:'s'},{label:'Retained',data:[totF.r,totFr.r,totV.r,totS.r].map(Math.round),backgroundColor:'rgba(26,138,74,.85)',stack:'s'},{label:'Reactivated',data:[totF.x,totFr.x,totV.x,totS.x].map(Math.round),backgroundColor:'rgba(192,57,43,.85)',stack:'s'}]},SS);
  var tbl='<table class="cat-month-tbl"><thead><tr><th>Month</th><th class="num">FMCG</th><th class="num">Fruits</th><th class="num">Veg</th><th class="num">Staples</th><th class="num">Cons</th><th class="num">KPN</th><th class="num">Mkt Scheme</th><th class="num">Total Sales</th><th class="num">FMCG%</th><th class="num">Fruits%</th><th class="num">Veg%</th><th class="num">Staples%</th></tr></thead><tbody>';
  yms.forEach(function(y){var m=ymMap[y];var ts=m.totS||1;tbl+='<tr><td>'+y+'</td><td class="num">'+fL(m.fmcg)+'</td><td class="num">'+fL(m.fruits)+'</td><td class="num">'+fL(m.veg)+'</td><td class="num">'+fL(m.staples)+'</td><td class="num">'+fL(m.cons)+'</td><td class="num">'+fL(m.kpn)+'</td><td class="num">'+fL(m.mkt)+'</td><td class="num" style="color:#aaa">'+fL(m.totS)+'</td><td class="num">'+fmtPct(m.fmcg,ts)+'</td><td class="num">'+fmtPct(m.fruits,ts)+'</td><td class="num">'+fmtPct(m.veg,ts)+'</td><td class="num">'+fmtPct(m.staples,ts)+'</td></tr>';});
  tbl+='</tbody></table>';document.getElementById('cat-month-table').innerHTML=tbl;
}

function renderCohort(){
  dC();
  var cm=document.getElementById('coh-cm').value,type=document.getElementById('coh-type').value,show=document.getElementById('coh-show').value;
  var rows=MDATA.filter(function(r){return cm==='all'||r.cluster_manager===cm;});
  var ymMap={};
  rows.forEach(function(r){var y=r.ym;if(!ymMap[y])ymMap[y]={N:0,R:0,sN:0,sR:0};var m=ymMap[y];m.N+=n(r,'new_customers');m.R+=n(r,'retained_customers');m.sN+=n(r,'new_overall_sales');m.sR+=n(r,'retained_overall_sales');});
  var yms=Object.keys(ymMap).sort();
  if(yms.length<2){document.getElementById('cohort-wrap').innerHTML='<p style="color:#555;padding:20px">Not enough data.</p>';return;}
  var N=yms.length,MAX=Math.min(N,13),matrix=[];
  for(var i=0;i<N;i++){matrix.push(new Array(N).fill(null));matrix[i][i]=type==='customers'?ymMap[yms[i]].N:ymMap[yms[i]].sN;}
  for(var j=1;j<N;j++){var tot=0;for(var k=0;k<j;k++)tot+=ymMap[yms[k]].N;var Rj=type==='customers'?ymMap[yms[j]].R:ymMap[yms[j]].sR;for(var i=0;i<j;i++){var sh=tot>0?ymMap[yms[i]].N/tot:0;matrix[i][j]=Math.round(Rj*sh);}}
  var html='<table class="cohort-table"><thead><tr><th class="c-label">Cohort</th><th>Base</th>';
  for(var j=1;j<MAX;j++)html+='<th>M+'+j+'</th>';html+='</tr></thead><tbody>';
  var avgA=new Array(MAX).fill(0),cntA=new Array(MAX).fill(0);
  for(var i=0;i<N;i++){html+='<tr><td class="c-label">'+yms[i]+'</td>';var base=matrix[i][i];
    for(var j=0;j<MAX;j++){var col=i+j;if(col>=N){html+='<td class="c-empty">—</td>';continue;}var val=matrix[i][col];if(j===0){html+='<td class="c-base">'+(show==='pct'?'100%':(type==='customers'?nL(val):fL(val)))+'</td>';continue;}if(val===null){html+='<td class="c-empty">—</td>';continue;}var pv=base>0?(val/base*100):0;avgA[j]+=pv;cntA[j]++;var cls=pv>30?'c-hi':pv>15?'c-mid':'c-lo';html+='<td class="'+cls+'" title="'+pv.toFixed(1)+'%">'+(show==='pct'?pv.toFixed(1)+'%':(type==='customers'?nL(val):fL(val)))+'</td>';}html+='</tr>';}
  html+='</tbody></table>';document.getElementById('cohort-wrap').innerHTML=html;
  var ages=[],avgs=[];for(var j=1;j<MAX;j++){if(cntA[j]>0){ages.push('M+'+j);avgs.push(+(avgA[j]/cntA[j]).toFixed(1));}}
  mkC('cohc1','bar',{labels:ages,datasets:[{data:avgs,backgroundColor:'rgba(26,138,74,.75)',borderRadius:3}]},{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false},tooltip:{callbacks:{label:function(c){return c.raw+'%';}}}},scales:{x:DARK.scales.x,y:{min:0,ticks:{callback:function(v){return v+'%';},color:'#555',font:{size:9}},grid:{color:'#1e1e1e'}}}});
}

renderMonth();
</script>
</body>
</html>
"""

def build_html(mdata, wdata, wcmdata, build_date):
    all_cms = sorted(set(r["cluster_manager"] for r in mdata if r.get("cluster_manager")))
    cm_opts = '<option value="all">All managers</option>' + "".join(f'<option value="{cm}">{cm}</option>' for cm in all_cms)

    week_months = sorted(set(r["wk"][:7] for r in wdata))
    wm_opts = '<option value="all">All months</option>' + "".join(f'<option value="{m}">{m}</option>' for m in week_months)

    html = HTML_TEMPLATE
    html = html.replace("__BUILD_DATE__", build_date)
    html = html.replace("__CM_OPTIONS__", cm_opts)
    html = html.replace("__WEEK_MONTH_OPTIONS__", wm_opts)
    html = html.replace("__MDATA__", json.dumps([round_row(r) for r in mdata], separators=(",", ":")))
    html = html.replace("__WDATA__", json.dumps([round_row(r) for r in wdata], separators=(",", ":")))
    html = html.replace("__WCMDATA__", json.dumps([round_row(r) for r in wcmdata], separators=(",", ":")))
    return html

# ── MAIN ────────────────────────────────────────────────────────────────────
def main():
    from datetime import datetime

    print("RFM Dashboard Builder")
    print("=" * 50)
    print(f"Sheet ID : {SHEET_ID}")
    print(f"Tab GID  : {GID}")
    print()

    print("Step 1 — Fetching data from Google Sheets...")
    text = fetch_csv()
    if not text:
        print("\n❌ Could not fetch data. Check that the sheet is shared (Anyone with link → Viewer).")
        sys.exit(1)

    print("Step 2 — Parsing CSV...")
    rows = parse_csv(text)
    print(f"  Parsed {len(rows):,} outlet-level rows")

    print("Step 3 — Aggregating...")
    mdata   = aggregate_monthly(rows)
    wdata   = aggregate_weekly_all(rows)
    wcmdata = aggregate_weekly_cm(rows)
    print(f"  Monthly rows (CM×period): {len(mdata)}")
    print(f"  Weekly rows (all CMs):    {len(wdata)}")
    print(f"  Weekly rows (per CM):     {len(wcmdata)}")

    print("Step 4 — Building HTML...")
    build_date = datetime.now().strftime("%d %b %Y %H:%M")
    html = build_html(mdata, wdata, wcmdata, build_date)

    print(f"Step 5 — Writing {OUTPUT}...")
    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write(html)

    size_kb = len(html) // 1024
    print(f"\n✅ Done!  →  {OUTPUT}  ({size_kb} KB)")
    print(f"   Built at: {build_date}")
    print()
    print("Next steps:")
    print("  1. Open index.html in your browser to preview locally")
    print("  2. Upload to GitHub Pages for a shareable live URL")
    print("     → https://sakthivel1618.github.io/index.html/")
    print()
    print("To auto-run every morning at 8 AM (Windows Task Scheduler):")
    print("  Program : python")
    print("  Args    : build_dashboard.py")
    print("  Start in: <folder where this script lives>")

if __name__ == "__main__":
    main()
