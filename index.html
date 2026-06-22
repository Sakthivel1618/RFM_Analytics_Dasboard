<!DOCTYPE html>
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
/* ── COHORT HEATMAP ── */
.cohort-wrap{overflow-x:auto;margin-top:8px}
.cohort-table{border-collapse:collapse;font-size:11px;min-width:600px}
.cohort-table th{padding:5px 8px;font-size:10px;color:#666;border:none;white-space:nowrap;background:transparent;font-weight:500}
.cohort-table td{padding:4px 6px;text-align:center;border:1px solid #111;font-size:10px;min-width:60px}
.c-label{text-align:left!important;color:#999;font-weight:500;min-width:80px;white-space:nowrap}
.c-base{background:#1a3a5c;color:#90caff;font-weight:700}
.c-100{background:#1a3a5c;color:#90caff}
.c-hi{background:#1a3a1a;color:#66cc66}
.c-mid{background:#2a2a10;color:#bbbb44}
.c-lo{background:#2a1010;color:#cc6666}
.c-empty{background:#111;color:#333}
/* category month table */
.cat-month-tbl th{text-align:right}
.cat-month-tbl th:first-child{text-align:left}
.cat-month-tbl td:first-child{text-align:left;font-weight:600;color:#e8e8e8}
@media(max-width:700px){.g2,.g3{grid-template-columns:1fr}}
</style>
</head>
<body>
<div class="wrap">
<h1>📊 RFM Deep Analysis Dashboard</h1>
<div class="subtitle">Chennai &nbsp;|&nbsp; Apr 2024 – Jun 2026 &nbsp;|&nbsp; 5 cluster managers &nbsp;|&nbsp; 27 months</div>

<div class="tabs">
  <button class="tab active" onclick="switchTab('month')">📅 Monthly</button>
  <button class="tab" onclick="switchTab('week')">📆 Weekly</button>
  <button class="tab" onclick="switchTab('cm')">👥 Managers</button>
  <button class="tab" onclick="switchTab('cat')">📦 Category (month)</button>
  <button class="tab" onclick="switchTab('cohort')">🔁 Cohort analysis</button>
</div>

<!-- ═══ MONTHLY ═══ -->
<div id="tab-month" class="section active">
  <div class="card">
    <div class="filter-row">
      <label>Manager:</label><select id="m-cm" onchange="renderMonth()"><option value="all">All managers</option></select>
      <label>Year:</label><select id="m-yr" onchange="renderMonth()">
        <option value="all">All (Apr 2024–Jun 2026)</option>
        <option value="2024">2024</option><option value="2025">2025</option><option value="2026">2026</option>
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
    <div class="card">
      <div class="ch">Retention &amp; reactivation rate (%)</div>
      <div class="cw" style="height:175px"><canvas id="mc3"></canvas></div>
    </div>
    <div class="card">
      <div class="ch">Avg ₹ / customer — by segment</div>
      <div class="legend"><span><span class="ls" style="background:#1a73e8"></span>New</span><span><span class="ls" style="background:#1a8a4a"></span>Retained</span><span><span class="ls" style="background:#c0392b"></span>Reactivated</span></div>
      <div class="cw" style="height:175px"><canvas id="mc4"></canvas></div>
    </div>
  </div>
  <div class="card">
    <div class="ch">Customer volume — new / retained / reactivated</div>
    <div class="legend"><span><span class="ls" style="background:#1a73e8"></span>New</span><span><span class="ls" style="background:#1a8a4a"></span>Retained</span><span><span class="ls" style="background:#c0392b"></span>Reactivated</span></div>
    <div class="cw" style="height:200px"><canvas id="mc2"></canvas></div>
  </div>
</div>

<!-- ═══ WEEKLY ═══ -->
<div id="tab-week" class="section">
  <div class="card">
    <div class="filter-row">
      <label>Manager:</label><select id="w-cm" onchange="renderWeek()"><option value="all">All managers</option></select>
      <label>Month:</label><select id="w-mo" onchange="renderWeek()"><option value="all">All months</option></select>
    </div>
    <div class="kpi-row" id="w-kpis"></div>
  </div>
  <div class="card">
    <div class="ch">Weekly customers — new / retained / reactivated</div>
    <div class="legend"><span><span class="ls" style="background:#1a73e8"></span>New</span><span><span class="ls" style="background:#1a8a4a"></span>Retained</span><span><span class="ls" style="background:#c0392b"></span>Reactivated</span></div>
    <div class="cw" style="height:200px"><canvas id="wc1"></canvas></div>
  </div>
  <div class="g2">
    <div class="card">
      <div class="ch">Retention rate % — weekly</div>
      <div class="cw" style="height:175px"><canvas id="wc3"></canvas></div>
    </div>
    <div class="card">
      <div class="ch">Reactivation rate % — weekly</div>
      <div class="cw" style="height:175px"><canvas id="wc5"></canvas></div>
    </div>
  </div>
  <div class="card">
    <div class="ch">Weekly sales stacked — new / retained / reactivated (₹)</div>
    <div class="legend"><span><span class="ls" style="background:#1a73e8"></span>New</span><span><span class="ls" style="background:#1a8a4a"></span>Retained</span><span><span class="ls" style="background:#c0392b"></span>Reactivated</span></div>
    <div class="cw" style="height:200px"><canvas id="wc2"></canvas></div>
  </div>
  <div class="card">
    <div class="ch">Category sales — weekly (₹)</div>
    <div class="legend"><span><span class="ls" style="background:#1a73e8"></span>FMCG</span><span><span class="ls" style="background:#1a8a4a"></span>Fruits</span><span><span class="ls" style="background:#7f77dd"></span>Veg</span><span><span class="ls" style="background:#ba7517"></span>Staples</span><span><span class="ls" style="background:#c0392b"></span>Cons</span></div>
    <div class="cw" style="height:195px"><canvas id="wc4"></canvas></div>
  </div>
</div>

<!-- ═══ MANAGERS ═══ -->
<div id="tab-cm" class="section">
  <div class="card">
    <div class="filter-row">
      <label>Year:</label><select id="cm-yr" onchange="renderCM()">
        <option value="all">All</option><option value="2024">2024</option><option value="2025">2025</option><option value="2026">2026</option>
      </select>
    </div>
    <div class="kpi-row" id="cm-kpis"></div>
  </div>
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

<!-- ═══ CATEGORY MONTH ═══ -->
<div id="tab-cat" class="section">
  <div class="card">
    <div class="filter-row">
      <label>Manager:</label><select id="cat-cm" onchange="renderCat()"><option value="all">All managers</option></select>
      <label>Year:</label><select id="cat-yr" onchange="renderCat()">
        <option value="all">All</option><option value="2024">2024</option><option value="2025">2025</option><option value="2026">2026</option>
      </select>
    </div>
    <div class="ch">Category sales — month-by-month breakdown</div>
    <div class="legend"><span><span class="ls" style="background:#1a73e8"></span>FMCG</span><span><span class="ls" style="background:#c0392b"></span>Fruits</span><span><span class="ls" style="background:#7f77dd"></span>Veg</span><span><span class="ls" style="background:#ba7517"></span>Staples</span><span><span class="ls" style="background:#1a8a4a"></span>Cons</span></div>
    <div class="cw" style="height:220px"><canvas id="catc1"></canvas></div>
  </div>
  <div class="card">
    <div class="ch">Category performance table — month level</div>
    <div id="cat-month-table" style="margin-top:8px;overflow-x:auto"></div>
  </div>
  <div class="card">
    <div class="ch">Category × segment (new / retained / reactivated) — stacked totals</div>
    <div class="legend"><span><span class="ls" style="background:#1a73e8"></span>New</span><span><span class="ls" style="background:#1a8a4a"></span>Retained</span><span><span class="ls" style="background:#c0392b"></span>Reactivated</span></div>
    <div class="cw" style="height:220px"><canvas id="catc2"></canvas></div>
  </div>
</div>

<!-- ═══ COHORT ═══ -->
<div id="tab-cohort" class="section">
  <div class="card">
    <div class="filter-row">
      <label>Manager:</label><select id="coh-cm" onchange="renderCohort()"><option value="all">All managers</option></select>
      <label>Cohort type:</label>
      <select id="coh-type" onchange="renderCohort()">
        <option value="customers">Customer retention</option>
        <option value="sales">Revenue retention</option>
      </select>
      <label>Show:</label>
      <select id="coh-show" onchange="renderCohort()">
        <option value="pct">% of cohort base</option>
        <option value="abs">Absolute count / ₹</option>
      </select>
    </div>
    <p style="font-size:11px;color:#666;margin-bottom:10px">Each row = customers who first transacted in that month. Columns = how many of those customers came back in subsequent months (Month 1 = acquisition month, Month 2 = 1 month later, etc.)</p>
    <div class="cohort-wrap" id="cohort-wrap"></div>
  </div>
  <div class="card">
    <div class="ch">Avg retention % by cohort age (all cohorts blended)</div>
    <div class="cw" style="height:200px"><canvas id="cohc1"></canvas></div>
  </div>
</div>

</div><!-- /wrap -->

<script>
/* ═══════════════════════ DATA ═══════════════════════ */
/* Monthly data is fetched live from Google Sheets; weekly and cohort are derived */
var SHEET_ID='10XNFBfJKW4gs_ra9CNtPUA5GXi9tb6xbnf6PnFgDSLI',GID='1815598507';
var MDATA=[],WDATA=[],WCMDATA=[],allCMs=[];
var activeTab='month', charts={};

/* ── helpers ── */
function fL(v){v=Math.round(v);if(v>=10000000)return'₹'+(v/10000000).toFixed(2)+'Cr';if(v>=100000)return'₹'+(v/100000).toFixed(2)+'L';if(v>=1000)return'₹'+(v/1000).toFixed(1)+'K';return'₹'+v;}
function nL(v){v=Math.round(v);if(v>=10000000)return(v/10000000).toFixed(2)+'Cr';if(v>=100000)return(v/100000).toFixed(2)+'L';if(v>=1000)return(v/1000).toFixed(1)+'K';return v.toLocaleString('en-IN');}
function fmtPct(v,t){return t>0?(v/t*100).toFixed(1)+'%':'—';}
function n(r,f){return parseFloat(r[f])||0;}
function dC(){Object.values(charts).forEach(function(c){try{c.destroy();}catch(e){}});charts={};}

/* ── parse CSV ── */
function parseCSV(txt){
  var rows=[],lines=txt.split('\n');
  for(var i=0;i<lines.length;i++){
    var ln=lines[i];if(!ln.trim())continue;
    var cells=[],cur='',inQ=false;
    for(var j=0;j<ln.length;j++){
      var c=ln[j];
      if(c==='"'){if(inQ&&ln[j+1]==='"'){cur+='"';j++;}else inQ=!inQ;}
      else if(c===','&&!inQ){cells.push(cur);cur='';}else cur+=c;
    }
    cells.push(cur);rows.push(cells);
  }
  return rows;
}

/* ── load sheet ── */
async function loadSheet(){
  var URLS=[
    'https://docs.google.com/spreadsheets/d/'+SHEET_ID+'/export?format=csv&gid='+GID,
    'https://docs.google.com/spreadsheets/d/'+SHEET_ID+'/gviz/tq?tqx=out:csv&gid='+GID
  ];
  var txt=null;
  for(var i=0;i<URLS.length;i++){
    try{
      var r=await fetch(URLS[i]+'&t='+Date.now());
      if(!r.ok)continue;
      var t=await r.text();
      if(t.length>200&&t.indexOf('rolling_period')>-1&&!t.trim().startsWith('<')){txt=t;break;}
    }catch(e){}
  }
  if(!txt){console.warn('Sheet fetch failed');return;}
  var rows=parseCSV(txt);
  var hdrs=rows[0].map(function(h){return h.replace(/"/g,'').trim().toLowerCase();});
  var raw=rows.slice(1).filter(function(r){return r.some(function(c){return c.trim();});})
    .map(function(row){var o={};hdrs.forEach(function(h,i){o[h]=(row[i]||'').replace(/"/g,'').trim();});return o;});

  /* aggregate outlet rows → CM+period level */
  var mGrp={},wGrp={},wCMGrp={};
  raw.forEach(function(r){
    var p=r['rolling_period']||'',cm=r['cluster_manager']||'';
    if(!p)return;
    var isM=p.startsWith('RM_'),isW=p.startsWith('RW_');
    if(!isM&&!isW)return;
    var ym=isM?p.replace('RM_',''):'';

    function agg(grp,key,extra){
      if(!grp[key])grp[key]=Object.assign({new_customers:0,retained_customers:0,reactivated_customers:0,total_customers:0,
        new_overall_nob:0,retained_overall_nob:0,reactivated_overall_nob:0,total_overall_nob:0,
        new_overall_sales:0,retained_overall_sales:0,reactivated_overall_sales:0,total_overall_sales:0,
        total_fmcg_sales:0,new_fmcg_sales:0,retained_fmcg_sales:0,reactivated_fmcg_sales:0,
        total_fruits_sales:0,new_fruits_sales:0,retained_fruits_sales:0,reactivated_fruits_sales:0,
        total_vegetables_sales:0,new_vegetables_sales:0,retained_vegetables_sales:0,reactivated_vegetables_sales:0,
        total_staples_sales:0,new_staples_sales:0,retained_staples_sales:0,reactivated_staples_sales:0,
        total_consumables_sales:0,new_consumables_sales:0,retained_consumables_sales:0,reactivated_consumables_sales:0,
        total_kpn_services_sales:0,total_marketing_scheme_sales:0},extra);
      var g=grp[key];
      ['new_customers','retained_customers','reactivated_customers','total_customers',
       'new_overall_nob','retained_overall_nob','reactivated_overall_nob','total_overall_nob',
       'new_overall_sales','retained_overall_sales','reactivated_overall_sales','total_overall_sales',
       'total_fmcg_sales','new_fmcg_sales','retained_fmcg_sales','reactivated_fmcg_sales',
       'total_fruits_sales','new_fruits_sales','retained_fruits_sales','reactivated_fruits_sales',
       'total_vegetables_sales','new_vegetables_sales','retained_vegetables_sales','reactivated_vegetables_sales',
       'total_staples_sales','new_staples_sales','retained_staples_sales','reactivated_staples_sales',
       'total_consumables_sales','new_consumables_sales','retained_consumables_sales','reactivated_consumables_sales',
       'total_kpn_services_sales','total_marketing_scheme_sales'
      ].forEach(function(f){g[f]+=(parseFloat(r[f])||0);});
    }

    if(isM){
      agg(mGrp,p+'|'+cm,{ym:ym,cluster_manager:cm,period:p});
      /* also aggregate all-CMs for a given ym */
    }
    if(isW){
      agg(wGrp,p,{wk:p,period_start:r['period_start']||''});
      if(cm) agg(wCMGrp,p+'|'+cm,{wk:p,cluster_manager:cm,period_start:r['period_start']||''});
    }
  });

  MDATA=Object.values(mGrp);
  WDATA=Object.values(wGrp).sort(function(a,b){return a.wk>b.wk?1:-1;});
  WCMDATA=Object.values(wCMGrp).sort(function(a,b){return a.wk>b.wk?1:-1;});

  allCMs=[...new Set(MDATA.map(function(r){return r.cluster_manager;}))].filter(Boolean).sort();
  populateSelects();
  renderMonth();
}

function populateSelects(){
  var selIds=['m-cm','w-cm','cm-not','cat-cm','coh-cm'];
  /* weekly month filter */
  var wMonths=[...new Set(WDATA.map(function(r){return r.wk.substring(0,7);}))].sort();
  var wMoSel=document.getElementById('w-mo');
  wMonths.forEach(function(m){var o=document.createElement('option');o.value=m;o.textContent=m;wMoSel.appendChild(o);});

  ['m-cm','w-cm','cat-cm','coh-cm'].forEach(function(id){
    var sel=document.getElementById(id);
    allCMs.forEach(function(cm){var o=document.createElement('option');o.value=cm;o.textContent=cm;sel.appendChild(o);});
  });
}

/* ── Switch tab ── */
function switchTab(t){
  activeTab=t;
  document.querySelectorAll('.tab').forEach(function(el,i){
    el.classList.toggle('active',el.getAttribute('onclick').includes("'"+t+"'"));
  });
  document.querySelectorAll('.section').forEach(function(el){el.classList.remove('active');});
  document.getElementById('tab-'+t).classList.add('active');
  dC();
  if(t==='month')renderMonth();
  else if(t==='week')renderWeek();
  else if(t==='cm')renderCM();
  else if(t==='cat')renderCat();
  else if(t==='cohort')renderCohort();
}

/* ── chart helpers ── */
var DARK_OPTS={responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},
  scales:{x:{ticks:{color:'#555',font:{size:9},autoSkip:true,maxRotation:45},grid:{color:'#1e1e1e'}},
         y:{ticks:{color:'#555',font:{size:9}},grid:{color:'#1e1e1e'}}}};
function mkChart(id,type,data,opts){
  var el=document.getElementById(id);if(!el)return;
  if(charts[id])charts[id].destroy();
  charts[id]=new Chart(el,{type:type,data:data,options:opts||DARK_OPTS});
}
function yFmt(fn){return function(v){return fn(v);};}

/* ══════════ MONTHLY ══════════ */
function mFilter(){
  var cm=document.getElementById('m-cm').value;
  var yr=document.getElementById('m-yr').value;
  return MDATA.filter(function(r){
    if(cm!=='all'&&r.cluster_manager!==cm)return false;
    if(yr!=='all'&&r.ym.indexOf(yr)!==0)return false;
    return true;
  });
}

function renderMonth(){
  dC();
  var rows=mFilter();
  /* aggregate by ym */
  var ymMap={};
  rows.forEach(function(r){
    if(!ymMap[r.ym])ymMap[r.ym]={ym:r.ym,N:0,R:0,X:0,sales:0,nN:0,nR:0,nX:0,sN:0,sR:0,sX:0,nob:0};
    var m=ymMap[r.ym];
    m.N+=n(r,'new_customers');m.R+=n(r,'retained_customers');m.X+=n(r,'reactivated_customers');
    m.sales+=n(r,'total_overall_sales');m.nob+=n(r,'total_overall_nob');
    m.sN+=n(r,'new_overall_sales');m.sR+=n(r,'retained_overall_sales');m.sX+=n(r,'reactivated_overall_sales');
  });
  var yms=Object.keys(ymMap).sort();
  var totN=0,totR=0,totX=0,totS=0,totNob=0;
  yms.forEach(function(y){totN+=ymMap[y].N;totR+=ymMap[y].R;totX+=ymMap[y].X;totS+=ymMap[y].sales;totNob+=ymMap[y].nob;});
  var totC=totN+totR+totX;
  /* last vs prev period */
  var lym=yms[yms.length-1],pym=yms[yms.length-2];
  var lm=ymMap[lym]||{},pm=ymMap[pym]||{},lmC=(lm.N||0)+(lm.R||0)+(lm.X||0),pmC=(pm.N||0)+(pm.R||0)+(pm.X||0);
  var sChg=pm.sales>0?((lm.sales-pm.sales)/pm.sales*100):0;
  /* KPIs */
  var kEl=document.getElementById('m-kpis');
  kEl.innerHTML='';
  function kpi(l,v,s,delta){var d='';if(delta!==undefined&&delta!==0)d='<div class="kpi-delta '+(delta>0?'up':'dn')+'">'+(delta>0?'▲':'▼')+Math.abs(delta).toFixed(1)+'% vs prev</div>';return'<div class="kpi"><div class="kpi-label">'+l+'</div><div class="kpi-val">'+v+'</div><div class="kpi-sub">'+s+'</div>'+d+'</div>';}
  var kpis=[
    kpi('Total customers',nL(totC),'all segments',0),
    kpi('Total sales',fL(totS),'all periods',sChg),
    kpi('Orders (NOB)',nL(totNob),'bills',0),
    kpi('New customers',nL(totN),fmtPct(totN,totC)+' share',0),
    kpi('Retained',nL(totR),fmtPct(totR,totC)+' retention',0),
    kpi('Reactivated',nL(totX),fmtPct(totX,totC)+' share',0),
    kpi('Avg ₹/customer',fL(totC>0?totS/totC:0),'blended',0),
    kpi('Latest period',lym?fL(lm.sales||0):'—',lym||'',0),
  ];
  kEl.innerHTML=kpis.join('');
  /* charts */
  var lbls=yms;
  mkChart('mc1','bar',{labels:lbls,datasets:[
    {label:'New',data:yms.map(function(y){return Math.round(ymMap[y].sN);}),backgroundColor:'rgba(26,115,232,.85)',stack:'s'},
    {label:'Retained',data:yms.map(function(y){return Math.round(ymMap[y].sR);}),backgroundColor:'rgba(26,138,74,.85)',stack:'s'},
    {label:'Reactivated',data:yms.map(function(y){return Math.round(ymMap[y].sX);}),backgroundColor:'rgba(192,57,43,.85)',stack:'s'},
  ]},Object.assign({},DARK_OPTS,{scales:{x:DARK_OPTS.scales.x,y:{ticks:{callback:function(v){return fL(v);},color:'#555',font:{size:9}},grid:{color:'#1e1e1e'}}}}));

  mkChart('mc2','bar',{labels:lbls,datasets:[
    {label:'New',data:yms.map(function(y){return Math.round(ymMap[y].N);}),backgroundColor:'rgba(26,115,232,.85)',stack:'s'},
    {label:'Retained',data:yms.map(function(y){return Math.round(ymMap[y].R);}),backgroundColor:'rgba(26,138,74,.85)',stack:'s'},
    {label:'Reactivated',data:yms.map(function(y){return Math.round(ymMap[y].X);}),backgroundColor:'rgba(192,57,43,.85)',stack:'s'},
  ]},Object.assign({},DARK_OPTS,{scales:{x:DARK_OPTS.scales.x,y:{ticks:{callback:function(v){return nL(v);},color:'#555',font:{size:9}},grid:{color:'#1e1e1e'}}}}));

  var retPcts=yms.map(function(y){var m=ymMap[y],t=m.N+m.R+m.X;return t>0?+(m.R/t*100).toFixed(1):0;});
  var reaPcts=yms.map(function(y){var m=ymMap[y],t=m.N+m.R+m.X;return t>0?+(m.X/t*100).toFixed(1):0;});
  mkChart('mc3','line',{labels:lbls,datasets:[
    {label:'Retention%',data:retPcts,borderColor:'#1a8a4a',backgroundColor:'rgba(26,138,74,.1)',fill:true,tension:.35,borderWidth:2,pointRadius:2},
    {label:'Reactivation%',data:reaPcts,borderColor:'#c0392b',fill:false,tension:.35,borderDash:[4,3],borderWidth:1.5,pointRadius:1.5}
  ]},{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:DARK_OPTS.scales.x,y:{min:0,ticks:{callback:function(v){return v+'%';},color:'#555',font:{size:9}},grid:{color:'#1e1e1e'}}}});

  mkChart('mc4','line',{labels:lbls,datasets:[
    {label:'New',data:yms.map(function(y){var m=ymMap[y];return m.N>0?Math.round(m.sN/m.N):0;}),borderColor:'#1a73e8',fill:false,tension:.35,borderWidth:2,pointRadius:2},
    {label:'Retained',data:yms.map(function(y){var m=ymMap[y];return m.R>0?Math.round(m.sR/m.R):0;}),borderColor:'#1a8a4a',fill:false,tension:.35,borderWidth:2,pointRadius:2},
    {label:'Reactivated',data:yms.map(function(y){var m=ymMap[y];return m.X>0?Math.round(m.sX/m.X):0;}),borderColor:'#c0392b',fill:false,tension:.35,borderWidth:2,pointRadius:2},
  ]},{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:DARK_OPTS.scales.x,y:{ticks:{callback:function(v){return fL(v);},color:'#555',font:{size:9}},grid:{color:'#1e1e1e'}}}});
}

/* ══════════ WEEKLY ══════════ */
function renderWeek(){
  dC();
  var cm=document.getElementById('w-cm').value;
  var mo=document.getElementById('w-mo').value;
  var src=cm==='all'?WDATA:WCMDATA.filter(function(r){return r.cluster_manager===cm;});
  /* aggregate by wk if CM filtered (WCMDATA has per-CM rows) */
  var wkMap={};
  src.forEach(function(r){
    var wk=r.wk;
    if(mo!=='all'&&wk.substring(0,7)!==mo)return;
    if(!wkMap[wk])wkMap[wk]={wk:wk,period_start:r.period_start||'',N:0,R:0,X:0,sN:0,sR:0,sX:0,sales:0,fmcg:0,fruits:0,veg:0,staples:0,cons:0};
    var m=wkMap[wk];
    m.N+=n(r,'new_customers');m.R+=n(r,'retained_customers');m.X+=n(r,'reactivated_customers');
    m.sN+=n(r,'new_overall_sales');m.sR+=n(r,'retained_overall_sales');m.sX+=n(r,'reactivated_overall_sales');
    m.sales+=n(r,'total_overall_sales');
    m.fmcg+=n(r,'total_fmcg_sales');m.fruits+=n(r,'total_fruits_sales');m.veg+=n(r,'total_vegetables_sales');
    m.staples+=n(r,'total_staples_sales');m.cons+=n(r,'total_consumables_sales');
  });
  var wks=Object.keys(wkMap).sort();
  var totN=0,totR=0,totX=0,totS=0;
  wks.forEach(function(w){totN+=wkMap[w].N;totR+=wkMap[w].R;totX+=wkMap[w].X;totS+=wkMap[w].sales;});
  var totC=totN+totR+totX;
  var kEl=document.getElementById('w-kpis');
  function kpi(l,v,s){return'<div class="kpi"><div class="kpi-label">'+l+'</div><div class="kpi-val">'+v+'</div><div class="kpi-sub">'+s+'</div></div>';}
  kEl.innerHTML=[kpi('Total customers',nL(totC),'all weeks'),kpi('Total sales',fL(totS),'all weeks'),kpi('New',nL(totN),fmtPct(totN,totC)),kpi('Retained',nL(totR),fmtPct(totR,totC)),kpi('Reactivated',nL(totX),fmtPct(totX,totC))].join('');
  var lbls=wks.map(function(w){return w.replace('RW_','');});
  mkChart('wc1','bar',{labels:lbls,datasets:[
    {label:'New',data:wks.map(function(w){return wkMap[w].N;}),backgroundColor:'rgba(26,115,232,.85)',stack:'s'},
    {label:'Retained',data:wks.map(function(w){return wkMap[w].R;}),backgroundColor:'rgba(26,138,74,.85)',stack:'s'},
    {label:'Reactivated',data:wks.map(function(w){return wkMap[w].X;}),backgroundColor:'rgba(192,57,43,.85)',stack:'s'},
  ]},Object.assign({},DARK_OPTS,{scales:{x:DARK_OPTS.scales.x,y:{ticks:{callback:function(v){return nL(v);},color:'#555',font:{size:9}},grid:{color:'#1e1e1e'}}}}));
  mkChart('wc2','bar',{labels:lbls,datasets:[
    {label:'New',data:wks.map(function(w){return Math.round(wkMap[w].sN);}),backgroundColor:'rgba(26,115,232,.85)',stack:'s'},
    {label:'Retained',data:wks.map(function(w){return Math.round(wkMap[w].sR);}),backgroundColor:'rgba(26,138,74,.85)',stack:'s'},
    {label:'Reactivated',data:wks.map(function(w){return Math.round(wkMap[w].sX);}),backgroundColor:'rgba(192,57,43,.85)',stack:'s'},
  ]},Object.assign({},DARK_OPTS,{scales:{x:DARK_OPTS.scales.x,y:{ticks:{callback:function(v){return fL(v);},color:'#555',font:{size:9}},grid:{color:'#1e1e1e'}}}}));
  mkChart('wc3','line',{labels:lbls,datasets:[{label:'Ret%',data:wks.map(function(w){var m=wkMap[w],t=m.N+m.R+m.X;return t>0?+(m.R/t*100).toFixed(1):0;}),borderColor:'#1a8a4a',backgroundColor:'rgba(26,138,74,.1)',fill:true,tension:.35,borderWidth:2,pointRadius:1.5}]},{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:DARK_OPTS.scales.x,y:{min:0,ticks:{callback:function(v){return v+'%';},color:'#555',font:{size:9}},grid:{color:'#1e1e1e'}}}});
  mkChart('wc5','line',{labels:lbls,datasets:[{label:'Rea%',data:wks.map(function(w){var m=wkMap[w],t=m.N+m.R+m.X;return t>0?+(m.X/t*100).toFixed(1):0;}),borderColor:'#c0392b',backgroundColor:'rgba(192,57,43,.1)',fill:true,tension:.35,borderWidth:2,pointRadius:1.5}]},{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:DARK_OPTS.scales.x,y:{min:0,ticks:{callback:function(v){return v+'%';},color:'#555',font:{size:9}},grid:{color:'#1e1e1e'}}}});
  mkChart('wc4','line',{labels:lbls,datasets:[
    {label:'FMCG',data:wks.map(function(w){return Math.round(wkMap[w].fmcg);}),borderColor:'#1a73e8',fill:false,tension:.35,borderWidth:1.5,pointRadius:1},
    {label:'Fruits',data:wks.map(function(w){return Math.round(wkMap[w].fruits);}),borderColor:'#c0392b',fill:false,tension:.35,borderWidth:1.5,pointRadius:1},
    {label:'Veg',data:wks.map(function(w){return Math.round(wkMap[w].veg);}),borderColor:'#7f77dd',fill:false,tension:.35,borderWidth:1.5,pointRadius:1},
    {label:'Staples',data:wks.map(function(w){return Math.round(wkMap[w].staples);}),borderColor:'#ba7517',fill:false,tension:.35,borderWidth:1.5,pointRadius:1},
    {label:'Cons',data:wks.map(function(w){return Math.round(wkMap[w].cons);}),borderColor:'#1a8a4a',fill:false,tension:.35,borderWidth:1.5,pointRadius:1},
  ]},{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:DARK_OPTS.scales.x,y:{ticks:{callback:function(v){return fL(v);},color:'#555',font:{size:9}},grid:{color:'#1e1e1e'}}}});
}

/* ══════════ MANAGERS ══════════ */
function renderCM(){
  dC();
  var yr=document.getElementById('cm-yr').value;
  var rows=MDATA.filter(function(r){return yr==='all'||r.ym.indexOf(yr)===0;});
  var cmMap={};
  rows.forEach(function(r){
    var cm=r.cluster_manager;
    if(!cmMap[cm])cmMap[cm]={N:0,R:0,X:0,tot:0,sales:0,nob:0,sN:0,sR:0,sX:0};
    var m=cmMap[cm];
    m.N+=n(r,'new_customers');m.R+=n(r,'retained_customers');m.X+=n(r,'reactivated_customers');m.tot+=n(r,'total_customers');
    m.sales+=n(r,'total_overall_sales');m.nob+=n(r,'total_overall_nob');
    m.sN+=n(r,'new_overall_sales');m.sR+=n(r,'retained_overall_sales');m.sX+=n(r,'reactivated_overall_sales');
  });
  var cms=Object.keys(cmMap).sort(function(a,b){return cmMap[b].sales-cmMap[a].sales;});
  var totS=cms.reduce(function(s,c){return s+cmMap[c].sales;},0);
  var totC=cms.reduce(function(s,c){return s+cmMap[c].tot;},0);
  var kEl=document.getElementById('cm-kpis');
  function kpi(l,v,s){return'<div class="kpi"><div class="kpi-label">'+l+'</div><div class="kpi-val">'+v+'</div><div class="kpi-sub">'+s+'</div></div>';}
  kEl.innerHTML=kpi('Total sales',fL(totS),'all managers')+kpi('Total customers',nL(totC),'all segments')+kpi('Managers',cms.length+'','active')+kpi('Top manager',cms[0]||'—',fL(cmMap[cms[0]]?cmMap[cms[0]].sales:0));
  var clrs=['#1a73e8','#1a8a4a','#c0392b','#7f77dd','#ba7517'];
  mkChart('cmc1','bar',{labels:cms,datasets:[{label:'Sales',data:cms.map(function(c){return Math.round(cmMap[c].sales);}),backgroundColor:clrs}]},{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:DARK_OPTS.scales.x,y:{ticks:{callback:function(v){return fL(v);},color:'#555',font:{size:9}},grid:{color:'#1e1e1e'}}}});
  mkChart('cmc2','bar',{labels:cms,datasets:[{label:'Customers',data:cms.map(function(c){return Math.round(cmMap[c].tot);}),backgroundColor:clrs}]},{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:DARK_OPTS.scales.x,y:{ticks:{callback:function(v){return nL(v);},color:'#555',font:{size:9}},grid:{color:'#1e1e1e'}}}});
  mkChart('cmc3','bar',{labels:cms,datasets:[{label:'Ret%',data:cms.map(function(c){var m=cmMap[c];return m.tot>0?+(m.R/m.tot*100).toFixed(1):0;}),backgroundColor:clrs}]},{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:DARK_OPTS.scales.x,y:{min:0,ticks:{callback:function(v){return v+'%';},color:'#555',font:{size:9}},grid:{color:'#1e1e1e'}}}});
  mkChart('cmc4','bar',{labels:cms,datasets:[{label:'₹/cust',data:cms.map(function(c){var m=cmMap[c];return m.tot>0?Math.round(m.sales/m.tot):0;}),backgroundColor:clrs}]},{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:DARK_OPTS.scales.x,y:{ticks:{callback:function(v){return fL(v);},color:'#555',font:{size:9}},grid:{color:'#1e1e1e'}}}});
  /* table */
  var tbl='<table><thead><tr><th>Manager</th><th class="num">New</th><th class="num">Retained</th><th class="num">Reactivated</th><th class="num">Total</th><th class="num">Ret%</th><th class="num">Sales</th><th class="num">New Sales</th><th class="num">Ret Sales</th><th class="num">NOB</th><th class="num">₹/Cust</th><th class="num">₹/Bill</th></tr></thead><tbody>';
  cms.forEach(function(c){var m=cmMap[c];var rr=m.tot>0?(m.R/m.tot*100).toFixed(1):0;var rc=rr>50?'#3ddc84':rr>35?'#ddaa44':'#ff5c5c';
    tbl+='<tr><td>'+c+'</td><td class="num"><span class="badge badge-b">'+nL(m.N)+'</span></td><td class="num"><span class="badge badge-g">'+nL(m.R)+'</span></td><td class="num"><span class="badge badge-a">'+nL(m.X)+'</span></td><td class="num">'+nL(m.tot)+'</td><td class="num" style="color:'+rc+'">'+rr+'%</td><td class="num">'+fL(m.sales)+'</td><td class="num">'+fL(m.sN)+'</td><td class="num">'+fL(m.sR)+'</td><td class="num">'+nL(m.nob)+'</td><td class="num">'+(m.tot>0?fL(m.sales/m.tot):'—')+'</td><td class="num">'+(m.nob>0?fL(m.sales/m.nob):'—')+'</td></tr>';
  });
  tbl+='</tbody></table>';
  document.getElementById('cm-table').innerHTML=tbl;
}

/* ══════════ CATEGORY MONTHLY ══════════ */
function renderCat(){
  dC();
  var cm=document.getElementById('cat-cm').value;
  var yr=document.getElementById('cat-yr').value;
  var rows=MDATA.filter(function(r){
    if(cm!=='all'&&r.cluster_manager!==cm)return false;
    if(yr!=='all'&&r.ym.indexOf(yr)!==0)return false;
    return true;
  });
  /* aggregate by ym */
  var ymMap={};
  rows.forEach(function(r){
    var y=r.ym;
    if(!ymMap[y])ymMap[y]={ym:y,fmcg:0,fruits:0,veg:0,staples:0,cons:0,kpn:0,mkt:0,
      nFmcg:0,rFmcg:0,xFmcg:0,nFruits:0,rFruits:0,xFruits:0,
      nVeg:0,rVeg:0,xVeg:0,nStaples:0,rStaples:0,xStaples:0,totSales:0};
    var m=ymMap[y];
    m.fmcg+=n(r,'total_fmcg_sales');m.fruits+=n(r,'total_fruits_sales');m.veg+=n(r,'total_vegetables_sales');
    m.staples+=n(r,'total_staples_sales');m.cons+=n(r,'total_consumables_sales');
    m.kpn+=n(r,'total_kpn_services_sales');m.mkt+=n(r,'total_marketing_scheme_sales');
    m.nFmcg+=n(r,'new_fmcg_sales');m.rFmcg+=n(r,'retained_fmcg_sales');m.xFmcg+=n(r,'reactivated_fmcg_sales');
    m.nFruits+=n(r,'new_fruits_sales');m.rFruits+=n(r,'retained_fruits_sales');m.xFruits+=n(r,'reactivated_fruits_sales');
    m.nVeg+=n(r,'new_vegetables_sales');m.rVeg+=n(r,'retained_vegetables_sales');m.xVeg+=n(r,'reactivated_vegetables_sales');
    m.nStaples+=n(r,'new_staples_sales');m.rStaples+=n(r,'retained_staples_sales');m.xStaples+=n(r,'reactivated_staples_sales');
    m.totSales+=n(r,'total_overall_sales');
  });
  var yms=Object.keys(ymMap).sort();
  mkChart('catc1','bar',{labels:yms,datasets:[
    {label:'FMCG',data:yms.map(function(y){return Math.round(ymMap[y].fmcg);}),backgroundColor:'rgba(26,115,232,.85)',stack:'s'},
    {label:'Fruits',data:yms.map(function(y){return Math.round(ymMap[y].fruits);}),backgroundColor:'rgba(192,57,43,.85)',stack:'s'},
    {label:'Veg',data:yms.map(function(y){return Math.round(ymMap[y].veg);}),backgroundColor:'rgba(127,119,221,.85)',stack:'s'},
    {label:'Staples',data:yms.map(function(y){return Math.round(ymMap[y].staples);}),backgroundColor:'rgba(186,117,23,.85)',stack:'s'},
    {label:'Cons',data:yms.map(function(y){return Math.round(ymMap[y].cons);}),backgroundColor:'rgba(26,138,74,.85)',stack:'s'},
  ]},Object.assign({},DARK_OPTS,{scales:{x:DARK_OPTS.scales.x,y:{ticks:{callback:function(v){return fL(v);},color:'#555',font:{size:9}},grid:{color:'#1e1e1e'}}}}));

  /* category × segment bar */
  var cats=['FMCG','Fruits','Vegetables','Staples'];
  var totFmcg={n:0,r:0,x:0},totFruits={n:0,r:0,x:0},totVeg={n:0,r:0,x:0},totStaples={n:0,r:0,x:0};
  yms.forEach(function(y){var m=ymMap[y];totFmcg.n+=m.nFmcg;totFmcg.r+=m.rFmcg;totFmcg.x+=m.xFmcg;totFruits.n+=m.nFruits;totFruits.r+=m.rFruits;totFruits.x+=m.xFruits;totVeg.n+=m.nVeg;totVeg.r+=m.rVeg;totVeg.x+=m.xVeg;totStaples.n+=m.nStaples;totStaples.r+=m.rStaples;totStaples.x+=m.xStaples;});
  mkChart('catc2','bar',{labels:cats,datasets:[
    {label:'New',data:[totFmcg.n,totFruits.n,totVeg.n,totStaples.n].map(Math.round),backgroundColor:'rgba(26,115,232,.85)',stack:'s'},
    {label:'Retained',data:[totFmcg.r,totFruits.r,totVeg.r,totStaples.r].map(Math.round),backgroundColor:'rgba(26,138,74,.85)',stack:'s'},
    {label:'Reactivated',data:[totFmcg.x,totFruits.x,totVeg.x,totStaples.x].map(Math.round),backgroundColor:'rgba(192,57,43,.85)',stack:'s'},
  ]},Object.assign({},DARK_OPTS,{scales:{x:DARK_OPTS.scales.x,y:{ticks:{callback:function(v){return fL(v);},color:'#555',font:{size:9}},grid:{color:'#1e1e1e'}}}}));

  /* month-level category table */
  var tbl='<table class="cat-month-tbl"><thead><tr><th>Month</th><th class="num">FMCG</th><th class="num">Fruits</th><th class="num">Veg</th><th class="num">Staples</th><th class="num">Cons</th><th class="num">KPN</th><th class="num">Mkt Scheme</th><th class="num">Total Sales</th><th class="num">FMCG share</th><th class="num">Fruits share</th><th class="num">Veg share</th><th class="num">Staples share</th></tr></thead><tbody>';
  yms.forEach(function(y){var m=ymMap[y];var ts=m.totSales||1;
    tbl+='<tr><td>'+y+'</td><td class="num">'+fL(m.fmcg)+'</td><td class="num">'+fL(m.fruits)+'</td><td class="num">'+fL(m.veg)+'</td><td class="num">'+fL(m.staples)+'</td><td class="num">'+fL(m.cons)+'</td><td class="num">'+fL(m.kpn)+'</td><td class="num">'+fL(m.mkt)+'</td><td class="num" style="color:#aaa">'+fL(m.totSales)+'</td><td class="num">'+fmtPct(m.fmcg,ts)+'</td><td class="num">'+fmtPct(m.fruits,ts)+'</td><td class="num">'+fmtPct(m.veg,ts)+'</td><td class="num">'+fmtPct(m.staples,ts)+'</td></tr>';
  });
  tbl+='</tbody></table>';
  document.getElementById('cat-month-table').innerHTML=tbl;
}

/* ══════════ COHORT ══════════ */
function renderCohort(){
  dC();
  var cm=document.getElementById('coh-cm').value;
  var type=document.getElementById('coh-type').value; /* customers | sales */
  var show=document.getElementById('coh-show').value; /* pct | abs */

  /* Build cohort from monthly data:
     Each month's "new_customers" is a cohort.
     In subsequent months, "retained_customers" from that cohort = we approximate
     using the fact that MDATA has total retained per CM per month.
     
     REAL COHORT LOGIC:
     - Cohort N = new customers acquired in month M
     - Month+1 for that cohort = how many of those N customers transacted again
     
     We don't have exact cohort tracking in the sheet, BUT we can build a
     PSEUDO-COHORT using the retained customer counts:
     - Month 1 = new_customers (100%)
     - Month 2+ = retained_customers in that period for that cohort origin month
     
     Since the sheet tracks retained/new/reactivated at roll-up level (not individual),
     we use a standard approach:
     COHORT retention[i][j] = retained_customers[j] / new_customers[i]  (for j>i, approx)
     
     Better approach: use RM_ data. Each RM_ period tells us:
     - new customers that period = new cohort
     - retained customers that period = came back from a previous period
     
     We approximate cohort survival as:
     cohort_size[i] = new_customers in period i
     surviving[i][j] = retained * (cohort_i_share) — but we don't know cohort share
     
     SIMPLEST VALID APPROACH:
     For each acquisition month i, cohort base = N_i (new customers)
     For month i+k: survivors = retained customers in month i+k × (N_i / total_prev_customers)
     Where total_prev_customers = sum of new customers from all prior months still "active"
  */

  var rows=MDATA.filter(function(r){return cm==='all'||r.cluster_manager===cm;});
  /* aggregate by ym */
  var ymMap={};
  rows.forEach(function(r){
    var y=r.ym;if(!ymMap[y])ymMap[y]={N:0,R:0,X:0,sN:0,sR:0};
    ymMap[y].N+=n(r,'new_customers');ymMap[y].R+=n(r,'retained_customers');ymMap[y].X+=n(r,'reactivated_customers');
    ymMap[y].sN+=n(r,'new_overall_sales');ymMap[y].sR+=n(r,'retained_overall_sales');
  });
  var yms=Object.keys(ymMap).sort();
  if(yms.length<2){document.getElementById('cohort-wrap').innerHTML='<p style="color:#555;padding:20px">Not enough data for cohort analysis.</p>';return;}

  /* Build cohort matrix — approximation:
     cohort row i acquired N[i] customers.
     In period j>i, the retained pool is R[j].
     We allocate R[j] to cohorts proportionally by N[i] / sum(N[0..j-1])
     This gives a reasonable approximation of per-cohort retention. */

  var N=yms.length;
  /* matrix[i][j] = estimated customers from cohort i still active in period j (j>=i) */
  var matrix=[];
  for(var i=0;i<N;i++){
    matrix.push(new Array(N).fill(null));
    matrix[i][i]=type==='customers'?ymMap[yms[i]].N:ymMap[yms[i]].sN;
  }
  for(var j=1;j<N;j++){
    var totalPrior=0;
    for(var k=0;k<j;k++)totalPrior+=ymMap[yms[k]].N;
    var Rj=type==='customers'?ymMap[yms[j]].R:ymMap[yms[j]].sR;
    for(var i=0;i<j;i++){
      var share=totalPrior>0?ymMap[yms[i]].N/totalPrior:0;
      matrix[i][j]=Math.round(Rj*share);
    }
  }

  /* Build HTML heatmap */
  var MAX_COLS=Math.min(N,13); /* show up to 12 follow-on months */
  var html='<table class="cohort-table"><thead><tr><th class="c-label">Cohort</th><th>Base</th>';
  for(var j=1;j<MAX_COLS;j++)html+='<th>M+'+j+'</th>';
  html+='</tr></thead><tbody>';

  var avgByAge=new Array(MAX_COLS).fill(0),cntByAge=new Array(MAX_COLS).fill(0);

  for(var i=0;i<N;i++){
    html+='<tr>';
    html+='<td class="c-label">'+yms[i]+'</td>';
    var base=matrix[i][i];
    for(var j=0;j<MAX_COLS;j++){
      var col=i+j;
      if(col>=N){html+='<td class="c-empty">—</td>';continue;}
      var val=matrix[i][col];
      if(j===0){html+='<td class="c-base">'+(show==='pct'?'100%':(type==='customers'?nL(val):fL(val)))+'</td>';continue;}
      if(val===null){html+='<td class="c-empty">—</td>';continue;}
      var pctVal=base>0?(val/base*100):0;
      avgByAge[j]+=pctVal;cntByAge[j]++;
      var cls=pctVal>30?'c-hi':pctVal>15?'c-mid':'c-lo';
      var disp=show==='pct'?pctVal.toFixed(1)+'%':(type==='customers'?nL(val):fL(val));
      html+='<td class="'+cls+'" title="'+pctVal.toFixed(1)+'%">'+disp+'</td>';
    }
    html+='</tr>';
  }
  html+='</tbody></table>';
  document.getElementById('cohort-wrap').innerHTML=html;

  /* avg retention by age */
  var ages=[],avgs=[];
  for(var j=1;j<MAX_COLS;j++){if(cntByAge[j]>0){ages.push('M+'+j);avgs.push(+(avgByAge[j]/cntByAge[j]).toFixed(1));}}
  mkChart('cohc1','bar',{labels:ages,datasets:[{label:'Avg ret%',data:avgs,backgroundColor:'rgba(26,138,74,.75)',borderRadius:3}]},{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false},tooltip:{callbacks:{label:function(c){return c.raw+'%';}}}},scales:{x:DARK_OPTS.scales.x,y:{min:0,ticks:{callback:function(v){return v+'%';},color:'#555',font:{size:9}},grid:{color:'#1e1e1e'}}}});
}

/* ══ INIT ══ */
loadSheet();
</script>
</body>
</html>
