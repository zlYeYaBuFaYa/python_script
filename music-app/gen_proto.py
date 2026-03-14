
# -*- coding: utf-8 -*-
import os

OUT = '/Users/zlyybfy/workspace/python/python_script/music-app/prototype.html'

# ─── CSS ────────────────────────────────────────────────────────────────────
CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,"PingFang SC","Helvetica Neue",Arial,sans-serif;background:#f0f0f5;padding:24px;color:#1d1d1f}
.page-hdr{text-align:center;padding:28px 20px;background:linear-gradient(135deg,#667eea,#764ba2);border-radius:16px;color:white;margin-bottom:28px}
.page-hdr h1{font-size:24px;margin-bottom:6px}
.page-hdr p{opacity:.8;font-size:13px}
.sec-title{font-size:12px;font-weight:700;color:#86868b;text-transform:uppercase;letter-spacing:1px;padding:6px 4px;margin:28px 0 10px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(310px,1fr));gap:20px;max-width:1900px;margin:0 auto}
.phone{background:white;border-radius:18px;overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,.1);transition:.2s}
.phone:hover{box-shadow:0 8px 32px rgba(0,0,0,.16);transform:translateY(-2px)}
.plbl{background:linear-gradient(135deg,#667eea,#764ba2);color:white;padding:9px 14px;font-size:12px;font-weight:600;display:flex;justify-content:space-between;align-items:center}
.plbl .tag{background:rgba(255,255,255,.25);padding:2px 7px;border-radius:10px;font-size:11px}
.sbody{min-height:500px}
.nav{display:flex;justify-content:space-between;align-items:center;padding:12px 14px;border-bottom:1px solid #f0f0f0;background:#fafafa}
.ntitle{font-size:16px;font-weight:600}
.nic{font-size:18px;cursor:pointer;color:#555}
.nback{color:#667eea;font-size:14px;cursor:pointer;display:flex;align-items:center;gap:3px}
.tabs{display:flex;border-bottom:1px solid #e5e5e7;background:white;padding:0 6px}
.tab{padding:11px 11px;font-size:13px;color:#86868b;cursor:pointer;border-bottom:2.5px solid transparent;white-space:nowrap}
.tab.on{color:#667eea;border-bottom-color:#667eea;font-weight:600}
.sbar{padding:9px 14px;background:#f5f5f7;border-bottom:1px solid #eee}
.sinp{width:100%;padding:8px 12px 8px 32px;border:none;border-radius:10px;background:white;font-size:14px;outline:none}
.sbar-wrap{position:relative}
.sbar-wrap::before{content:"🔍";position:absolute;left:22px;top:50%;transform:translateY(-50%);font-size:13px}
.fbar{display:flex;gap:8px;padding:8px 14px;border-bottom:1px solid #eee;background:#fafafa}
.fbtn{padding:5px 10px;font-size:12px;border:1px solid #d1d1d6;border-radius:7px;background:white;cursor:pointer}
.song{display:flex;align-items:center;padding:11px 14px;border-bottom:1px solid #f2f2f2;cursor:pointer}
.song:hover,.song.sel{background:#f0f0ff}
.cov{width:40px;height:40px;border-radius:8px;background:linear-gradient(135deg,#667eea,#764ba2);display:flex;align-items:center;justify-content:center;font-size:18px;margin-right:11px;flex-shrink:0}
.cov.sm{width:34px;height:34px;border-radius:6px;font-size:14px}
.cov.g2{background:linear-gradient(135deg,#f093fb,#f5576c)}
.cov.g3{background:linear-gradient(135deg,#43e97b,#38f9d7)}
.cov.g4{background:linear-gradient(135deg,#fa709a,#fee140)}
.sinf{flex:1;min-width:0}
.sname{font-size:14px;font-weight:500;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.smeta{font-size:12px;color:#86868b;margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sright{display:flex;align-items:center;gap:8px;flex-shrink:0}
.heart{font-size:16px}
.more{color:#c8c8c8;font-size:16px}
.lrow{display:flex;align-items:center;padding:12px 14px;border-bottom:1px solid #f2f2f2;cursor:pointer}
.lrow:hover{background:#f8f8f8}
.lic{width:44px;height:44px;border-radius:10px;background:#f0f0f5;display:flex;align-items:center;justify-content:center;font-size:22px;margin-right:12px;flex-shrink:0}
.linf{flex:1}
.lname{font-size:14px;font-weight:500}
.lsub{font-size:12px;color:#86868b;margin-top:2px}
.arr{color:#c8c8c8;font-size:13px}
.player-bg{background:linear-gradient(160deg,#1a1a2e,#2c2c3e);padding:18px;color:white;text-align:center}
.alb{width:170px;height:170px;border-radius:14px;background:linear-gradient(135deg,#667eea,#764ba2);display:flex;align-items:center;justify-content:center;font-size:60px;margin:0 auto 16px;box-shadow:0 10px 40px rgba(0,0,0,.4)}
.pname{font-size:17px;font-weight:600;margin-bottom:4px}
.partist{font-size:13px;opacity:.7}
.prog{margin:14px 0}
.ptrack{height:4px;background:rgba(255,255,255,.2);border-radius:2px}
.pfill{height:100%;width:38%;background:white;border-radius:2px}
.ptime{display:flex;justify-content:space-between;font-size:11px;opacity:.6;margin-top:5px}
.ctrl-row{display:flex;justify-content:center;align-items:center;gap:22px;margin:14px 0}
.ctrl{font-size:26px;cursor:pointer;opacity:.75}
.ctrl.main{font-size:44px;opacity:1}
.pextras{display:flex;justify-content:space-around;padding:10px 0;border-top:1px solid rgba(255,255,255,.1);margin-top:6px}
.pext{font-size:22px;opacity:.65;cursor:pointer}
.pl-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;padding:12px}
.plcard{border-radius:12px;overflow:hidden;cursor:pointer}
.plcard:hover{opacity:.85}
.plcov{height:90px;background:linear-gradient(135deg,#667eea,#764ba2);display:flex;align-items:center;justify-content:center;font-size:28px}
.plcov-4{display:grid;grid-template-columns:1fr 1fr;height:90px}
.plcov-4 span{display:flex;align-items:center;justify-content:center;font-size:18px;background:linear-gradient(135deg,#667eea,#764ba2)}
.plcov-4 span:nth-child(2){background:linear-gradient(135deg,#f093fb,#f5576c)}
.plcov-4 span:nth-child(3){background:linear-gradient(135deg,#43e97b,#38f9d7)}
.plcov-4 span:nth-child(4){background:linear-gradient(135deg,#fa709a,#fee140)}
.pltitle{padding:7px 10px;font-size:13px;font-weight:500;background:#f5f5f7}
.plsub{padding:0 10px 8px;font-size:11px;color:#86868b;background:#f5f5f7}
.sec-hdr{padding:10px 14px 6px;font-size:12px;font-weight:600;color:#86868b;background:#f8f8f8;border-bottom:1px solid #f0f0f0;text-transform:uppercase;letter-spacing:.5px}
.toggle-row{display:flex;justify-content:space-between;align-items:center;padding:12px 14px;border-bottom:1px solid #f2f2f2}
.toggle-info{flex:1}
.tlabel{font-size:14px}
.tsub{font-size:12px;color:#86868b;margin-top:1px}
.tog{width:46px;height:26px;border-radius:13px;background:#e5e5ea;position:relative;cursor:pointer;flex-shrink:0}
.tog.on{background:#34c759}
.tog::after{content:'';position:absolute;width:22px;height:22px;background:white;border-radius:50%;top:2px;left:2px;transition:.2s;box-shadow:0 1px 3px rgba(0,0,0,.25)}
.tog.on::after{transform:translateX(20px)}
.set-row{display:flex;justify-content:space-between;align-items:center;padding:12px 14px;border-bottom:1px solid #f2f2f2;cursor:pointer}
.set-row:hover{background:#fafafa}
.sval{font-size:13px;color:#86868b;display:flex;align-items:center;gap:6px}
.empty{text-align:center;padding:48px 20px}
.eic{font-size:52px;margin-bottom:14px}
.etxt{font-size:15px;color:#333;margin-bottom:6px;font-weight:500}
.esub{font-size:13px;color:#86868b;margin-bottom:20px}
.btn-row{display:flex;gap:10px;justify-content:center;flex-wrap:wrap}
.btn{padding:10px 18px;border:none;border-radius:10px;font-size:14px;cursor:pointer;font-weight:500}
.btnp{background:#667eea;color:white}
.btns{background:#e5e5ea;color:#333}
.btnd{background:#ff3b30;color:white}
.modal-wrap{padding:14px}
.mbox{background:white;border-radius:14px;overflow:hidden;box-shadow:0 4px 20px rgba(0,0,0,.12)}
.mtitle{padding:16px 16px 0;font-size:16px;font-weight:600}
.msub{padding:8px 16px 14px;font-size:13px;color:#86868b}
.mdiv{height:1px;background:#f0f0f0}
.mbtns{display:flex}
.mbtn{flex:1;padding:14px;text-align:center;font-size:14px;cursor:pointer;color:#667eea;border:none;background:none}
.mbtn.danger{color:#ff3b30}
.mbtn+.mbtn{border-left:1px solid #f0f0f0}
.snackbar{margin:10px 14px;padding:11px 14px;background:#1d1d1f;color:white;border-radius:10px;font-size:13px;display:flex;justify-content:space-between;align-items:center}
.snk-action{color:#667eea;font-weight:600;cursor:pointer}
.alert{margin:0;padding:10px 14px;font-size:13px;display:flex;gap:8px;align-items:flex-start;border-bottom:1px solid rgba(0,0,0,.06)}
.alert-w{background:#fff8e6;color:#7c5c00}
.alert-e{background:#fff0f0;color:#c00}
.wifi-box{background:#f5f5f7;margin:10px 14px;padding:14px;border-radius:12px}
.waddr{font-family:monospace;font-size:15px;text-align:center;background:white;padding:10px;border-radius:8px;margin-bottom:10px;letter-spacing:.5px}
.wpwd{display:flex;gap:6px;justify-content:center;margin:10px 0}
.wdig{width:34px;height:42px;background:white;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:20px;font-weight:700;color:#667eea;border:2px solid #667eea}
.qr{width:80px;height:80px;background:white;border-radius:8px;margin:10px auto;display:flex;align-items:center;justify-content:center;font-size:38px;border:1px solid #e5e5e7}
.imp-prog{padding:14px}
.pbar-wrap{background:#f0f0f0;border-radius:6px;height:8px;margin:10px 0}
.pbar-fill{height:100%;background:linear-gradient(90deg,#667eea,#764ba2);border-radius:6px}
.imp-stats{display:flex;flex-direction:column;gap:6px;margin:12px 0;padding:12px;background:#f8f8f8;border-radius:10px}
.istat{display:flex;align-items:center;gap:8px;font-size:13px}
.q-item{display:flex;align-items:center;padding:10px 14px;border-bottom:1px solid #f2f2f2}
.q-item.playing{background:#f0f0ff}
.qnum{width:26px;text-align:center;font-size:12px;color:#86868b;flex-shrink:0}
.qdrag{font-size:16px;color:#c8c8c8;margin-left:8px;cursor:grab}
.lyric-wrap{padding:16px 14px;text-align:center}
.lyric-line{font-size:14px;color:#bbb;padding:9px 0;line-height:1.5}
.lyric-line.act{font-size:17px;color:#1d1d1f;font-weight:600}
.lyric-line.near{font-size:15px;color:#666}
.det-cov{display:flex;justify-content:center;padding:20px;background:linear-gradient(180deg,#f0f0ff,white)}
.det-alb{width:150px;height:150px;border-radius:12px;background:linear-gradient(135deg,#667eea,#764ba2);display:flex;align-items:center;justify-content:center;font-size:54px;box-shadow:0 8px 24px rgba(102,126,234,.28)}
.det-inf{padding:12px 14px;border-bottom:1px solid #f0f0f0}
.det-name{font-size:17px;font-weight:600;margin-bottom:3px}
.det-artist{font-size:13px;color:#86868b}
.det-acts{display:flex;justify-content:space-around;padding:12px;border-bottom:1px solid #f0f0f0}
.dact{text-align:center;cursor:pointer}
.dact-ic{font-size:22px;margin-bottom:3px}
.dact-lbl{font-size:11px;color:#86868b}
.irow{display:flex;justify-content:space-between;padding:11px 14px;border-bottom:1px solid #f2f2f2;font-size:13px}
.ikey{color:#86868b}
.ival{font-weight:500}
.alb-head{padding:16px 14px;background:linear-gradient(180deg,#f0f0ff,white);text-align:center}
.alb-cov{width:140px;height:140px;border-radius:12px;background:linear-gradient(135deg,#667eea,#764ba2);display:flex;align-items:center;justify-content:center;font-size:52px;margin:0 auto 12px;box-shadow:0 6px 20px rgba(102,126,234,.28)}
.alb-meta{font-size:13px;color:#86868b;margin-top:3px}
.alb-btns{display:flex;justify-content:center;gap:10px;margin-top:12px}
.ablbtn{padding:8px 18px;border-radius:20px;font-size:13px;font-weight:600;border:none;cursor:pointer}
.ablbtn.m{background:#667eea;color:white}
.ablbtn.s{background:#f0f0f5;color:#333}
.tnum{width:24px;text-align:center;font-size:12px;color:#86868b;flex-shrink:0;margin-right:6px}
.steps{display:flex;justify-content:center;gap:8px;padding:10px}
.sdot{width:8px;height:8px;border-radius:50%;background:#e5e5e7}
.sdot.on{background:#667eea;width:20px;border-radius:4px}
.time-opt{display:flex;justify-content:space-between;align-items:center;padding:13px 14px;border-bottom:1px solid #f2f2f2;cursor:pointer;font-size:14px}
.time-opt:hover{background:#f8f8f8}
.time-opt .ck{color:#667eea}
.timer-active{background:#f0f0ff;margin:12px 14px;padding:14px;border-radius:12px;text-align:center}
.timer-cd{font-size:36px;font-weight:700;color:#667eea;margin:8px 0}
.speed-opt{display:flex;justify-content:space-between;align-items:center;padding:12px 14px;border-bottom:1px solid #f2f2f2;cursor:pointer;font-size:14px}
.speed-opt:hover{background:#f8f8f8}
.speed-opt .ck{color:#667eea}
.bulk-bar{display:flex;justify-content:space-between;align-items:center;padding:10px 14px;background:#eeeeff;border-bottom:1px solid #d0d0ee}
.bcount{font-size:14px;font-weight:600;color:#667eea}
.bcancel{font-size:14px;color:#667eea;cursor:pointer}
.bulk-acts{display:flex;gap:8px;padding:8px 14px;background:#f8f8f8;border-bottom:1px solid #eee;flex-wrap:wrap}
.bbtn{padding:5px 11px;font-size:12px;font-weight:600;border:none;border-radius:7px;cursor:pointer}
.bbtn.a{background:#667eea;color:white}
.bbtn.p{background:#34c759;color:white}
.bbtn.pl{background:#f0f0f5;color:#333}
.bbtn.d{background:#ff3b30;color:white}
.cb{width:22px;height:22px;border-radius:50%;border:2px solid #667eea;display:flex;align-items:center;justify-content:center;margin-right:10px;flex-shrink:0;font-size:12px}
.cb.on{background:#667eea;color:white}
.hist-item{display:flex;justify-content:space-between;align-items:center;padding:11px 14px;border-bottom:1px solid #f2f2f2;cursor:pointer}
.hist-item:hover{background:#f8f8f8}
.hkw{font-size:14px}
.htime{font-size:12px;color:#86868b}
.hdel{color:#c8c8c8}
.clear-all{padding:11px 14px;text-align:center;font-size:13px;color:#ff3b30;cursor:pointer;border-bottom:1px solid #f2f2f2}
.grp-row{display:flex;align-items:center;padding:12px 14px;border-bottom:1px solid #f2f2f2;cursor:pointer}
.grp-row:hover{background:#f8f8f8}
.gic{font-size:28px;margin-right:12px}
.ginf{flex:1}
.gname{font-size:14px;font-weight:500}
.gsub{font-size:12px;color:#86868b;margin-top:2px}
.frow{display:flex;align-items:center;padding:10px 14px;border-bottom:1px solid #f2f2f2}
.fic{font-size:22px;margin-right:10px}
.finf{flex:1}
.fname{font-size:13px;font-weight:500;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:150px}
.fsize{font-size:12px;color:#86868b;margin-top:2px}
.ftag{font-size:11px;padding:2px 7px;border-radius:8px;margin-left:8px}
.fok{background:#dcfce7;color:#166534}
.forp{background:#fee2e2;color:#991b1b}
.stbar{margin:10px 14px;padding:12px;background:#f5f5f7;border-radius:10px}
.sttrack{height:8px;background:#e5e5e7;border-radius:4px;margin:8px 0}
.stfill{height:100%;width:62%;background:linear-gradient(90deg,#667eea,#764ba2);border-radius:4px}
.stlbls{display:flex;justify-content:space-between;font-size:12px;color:#86868b}
.bs{background:white;border-radius:16px 16px 0 0;border-top:1px solid #e5e5e7}
.bs-handle{width:36px;height:4px;background:#e5e5e7;border-radius:2px;margin:10px auto 12px}
.bs-title{font-size:15px;font-weight:600;padding:0 14px 12px;text-align:center}
.bs-opt{display:flex;align-items:center;gap:12px;padding:14px;border-top:1px solid #f2f2f2;cursor:pointer;font-size:14px}
.bs-opt:hover{background:#f8f8f8}
.bsic{font-size:20px;width:28px;text-align:center}
.radio-opt{display:flex;align-items:flex-start;padding:12px 14px;border-bottom:1px solid #f2f2f2;cursor:pointer;gap:10px}
.radio-opt:hover{background:#f8f8f8}
.rdot{width:20px;height:20px;border-radius:50%;border:2px solid #d1d1d6;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:2px}
.rdot.on{border-color:#667eea;background:#667eea}
.rdot.on::after{content:'';width:8px;height:8px;background:white;border-radius:50%}
.rtxt{flex:1}
.rlbl{font-size:14px;font-weight:500}
.rdesc{font-size:12px;color:#86868b;margin-top:2px}
.mini-player{display:flex;align-items:center;padding:10px 14px;background:white;border-top:1px solid #f0f0f0;box-shadow:0 -2px 8px rgba(0,0,0,.05)}
.mcov{width:36px;height:36px;border-radius:6px;background:linear-gradient(135deg,#667eea,#764ba2);display:flex;align-items:center;justify-content:center;font-size:15px;margin-right:10px;flex-shrink:0}
.minf{flex:1;min-width:0}
.mname{font-size:13px;font-weight:500;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.martist{font-size:11px;color:#86868b}
.mbtns{display:flex;gap:12px;align-items:center}
.mbtn2{font-size:20px;cursor:pointer;color:#555}
.tab-bar{display:flex;border-top:1px solid #f0f0f0;background:white;padding:6px 0}
.tb{flex:1;text-align:center;cursor:pointer;padding:4px 0}
.tbic{font-size:22px}
.tblbl{font-size:10px;color:#86868b;margin-top:1px}
.tb.on .tbic,.tb.on .tblbl{color:#667eea}
.onb-body{padding:24px;display:flex;flex-direction:column;align-items:center;justify-content:center;min-height:460px;text-align:center}
.onb-ic{font-size:70px;margin-bottom:18px}
.onb-title{font-size:21px;font-weight:700;margin-bottom:10px}
.onb-desc{font-size:13px;color:#86868b;line-height:1.7;margin-bottom:22px}
.onb-feat{font-size:13px;color:#555;padding:5px 0;text-align:left;width:100%;max-width:230px}
.divider{height:1px;background:#f0f0f0}
.thick-div{height:8px;background:#f5f5f7}
.chip{display:inline-block;padding:2px 8px;border-radius:10px;font-size:11px;font-weight:600;margin:2px}
.chip0{background:#fee2e2;color:#991b1b}
.chip1{background:#fef3c7;color:#92400e}
.chip2{background:#dbeafe;color:#1e40af}
.chip3{background:#e5e7eb;color:#374151}
.flex-btw{display:flex;justify-content:space-between;align-items:center}
.flex-ctr{display:flex;justify-content:center;align-items:center}
.p14{padding:14px}
.text-sm{font-size:12px;color:#86868b}
.text-ctr{text-align:center}
.fw6{font-weight:600}
.cp{color:#667eea}
.cred{color:#ff3b30}
.storage-row{display:flex;justify-content:space-around;padding:14px;background:#f5f5f7;margin:10px 14px;border-radius:10px}
.stor-item{text-align:center}
.stor-val{font-size:20px;font-weight:700;color:#667eea}
.stor-lbl{font-size:11px;color:#86868b;margin-top:3px}
"""

# ─── HTML BODY ───────────────────────────────────────────────────────────────
def phone(label, tag, content):
    return f"""<div class="phone">
  <div class="plbl"><span>{label}</span><span class="tag">{tag}</span></div>
  <div class="sbody">{content}</div>
</div>"""

def nav(title, left="☰", right="⚙️"):
    return f"""<div class="nav"><span class="nic">{left}</span><span class="ntitle">{title}</span><span class="nic">{right}</span></div>"""

def nav_back(title, right="···"):
    return f"""<div class="nav"><span class="nback">← 返回</span><span class="ntitle">{title}</span><span class="nic">{right}</span></div>"""

def tabs(items, active=0):
    t = ""
    for i, it in enumerate(items):
        cls = " on" if i == active else ""
        t += f'<div class="tab{cls}">{it}</div>'
    return f'<div class="tabs">{t}</div>'

def search_bar(placeholder="搜索歌曲、艺术家、专辑"):
    return f"""<div class="sbar"><div class="sbar-wrap"><input class="sinp" placeholder="🔍 {placeholder}" type="text"></div></div>"""

def filter_bar():
    return '<div class="fbar"><button class="fbtn">排序: 文件名 ▼</button><button class="fbtn">筛选 ▼</button></div>'

def song(name, meta, fav="🤍", cov_class=""):
    return f"""<div class="song"><div class="cov {cov_class}">🎵</div><div class="sinf"><div class="sname">{name}</div><div class="smeta">{meta}</div></div><div class="sright"><span class="heart">{fav}</span><span class="more">›</span></div></div>"""

def song_cb(name, meta, checked=False, playing=False):
    cb = '<div class="cb on">✓</div>' if checked else '<div class="cb"></div>'
    sel = " sel" if checked else ""
    play_ic = "🎵" if playing else ""
    return f"""<div class="song{sel}">{cb}<div class="cov sm">🎵</div><div class="sinf"><div class="sname">{play_ic} {name}</div><div class="smeta">{meta}</div></div></div>"""

def lrow(icon, name, sub, arrow=True):
    arr = '<span class="arr">›</span>' if arrow else ""
    return f"""<div class="lrow"><div class="lic">{icon}</div><div class="linf"><div class="lname">{name}</div><div class="lsub">{sub}</div></div>{arr}</div>"""

def set_row(label, val="", sub="", arrow=True):
    sub_html = f'<div class="tsub">{sub}</div>' if sub else ""
    arr = '<span class="arr">›</span>' if arrow else ""
    return f"""<div class="set-row"><div><div class="tlabel">{label}</div>{sub_html}</div><div class="sval">{val}{arr}</div></div>"""

def toggle_row(label, on=False, sub=""):
    state = " on" if on else ""
    sub_html = f'<div class="tsub">{sub}</div>' if sub else ""
    return f"""<div class="toggle-row"><div class="toggle-info"><div class="tlabel">{label}</div>{sub_html}</div><div class="tog{state}"></div></div>"""

def mini_player():
    return """<div class="mini-player"><div class="mcov">🎵</div><div class="minf"><div class="mname">夜曲</div><div class="martist">周杰伦</div></div><div class="mbtns"><span class="mbtn2">⏮</span><span class="mbtn2">⏸</span><span class="mbtn2">⏭</span></div></div>"""

def tab_bar(active=0):
    items = [("🎵", "音乐"), ("📋", "歌单"), ("📥", "导入"), ("⚙️", "设置")]
    html = ""
    for i, (ic, lbl) in enumerate(items):
        cls = " on" if i == active else ""
        html += f'<div class="tb{cls}"><div class="tbic">{ic}</div><div class="tblbl">{lbl}</div></div>'
    return f'<div class="tab-bar">{html}</div>'

def sec_hdr(text):
    return f'<div class="sec-hdr">{text}</div>'

def thick_div():
    return '<div class="thick-div"></div>'

# ─── PAGE CONTENT ────────────────────────────────────────────────────────────

pages = []

# ── 1. 欢迎引导 Step 1 ──
pages.append(phone("1. 欢迎引导 — 第1步", "P2",
    f"""<div class="onb-body">
      <div class="onb-ic">🎵</div>
      <div class="onb-title">欢迎使用本地音乐播放器</div>
      <div class="onb-desc">完全本地，无需网络<br>简洁优雅的设计<br>强大的音乐管理功能</div>
      <div class="onb-feat">✓ 完全本地播放，保护隐私</div>
      <div class="onb-feat">✓ 支持 MP3 / FLAC / WAV 等格式</div>
      <div class="onb-feat">✓ 歌单 / 艺术家 / 专辑分类管理</div>
      <div style="margin-top:28px" class="btn-row">
        <button class="btn btnp">开始使用</button>
        <button class="btn btns">跳过</button>
      </div>
    </div>
    <div class="steps"><div class="sdot on"></div><div class="sdot"></div><div class="sdot"></div></div>"""))

# ── 2. 引导 Step 2 ──
pages.append(phone("2. 欢迎引导 — 第2步 导入", "P2",
    f"""<div class="onb-body">
      <div class="onb-ic">📥</div>
      <div class="onb-title">导入你的音乐</div>
      <div class="onb-desc">选择一种方式导入音乐到应用</div>
      <div style="width:100%;max-width:260px">
        <div style="background:#f5f5f7;border-radius:12px;padding:14px;margin-bottom:12px;cursor:pointer;text-align:left">
          <div style="font-weight:600;font-size:14px;margin-bottom:4px">📂 从文件应用导入</div>
          <div class="text-sm">从 iPhone 文件中选择音频文件</div>
        </div>
        <div style="background:#f5f5f7;border-radius:12px;padding:14px;margin-bottom:12px;cursor:pointer;text-align:left">
          <div style="font-weight:600;font-size:14px;margin-bottom:4px">📡 WiFi 传输</div>
          <div class="text-sm">从电脑无线传输，支持批量导入</div>
        </div>
        <div style="color:#86868b;font-size:13px;text-align:center;cursor:pointer;padding:8px">稍后导入</div>
      </div>
    </div>
    <div class="steps"><div class="sdot"></div><div class="sdot on"></div><div class="sdot"></div></div>"""))

# ── 3. 引导 Step 3 ──
pages.append(phone("3. 欢迎引导 — 第3步 开始", "P2",
    f"""<div class="onb-body">
      <div class="onb-ic">▶️</div>
      <div class="onb-title">开始播放音乐</div>
      <div class="onb-desc">点击任意歌曲立即开始播放<br>或先创建你的第一个歌单</div>
      <div style="margin-top:24px" class="btn-row">
        <button class="btn btnp">开始播放</button>
        <button class="btn btns">创建歌单</button>
      </div>
    </div>
    <div class="steps"><div class="sdot"></div><div class="sdot"></div><div class="sdot on"></div></div>"""))

# ── 4. 音乐库 全部音乐 ──
pages.append(phone("4. 音乐库 — 全部音乐", "P0",
    nav("音乐库", "☰", "⚙️") +
    tabs(["全部", "艺术家", "专辑", "歌单分组"], 0) +
    search_bar() + filter_bar() +
    song("夜曲", "周杰伦 · 十一月的萧邦 · 3:45 · 8.2MB", "❤️") +
    song("晴天", "周杰伦 · 叶惠美 · 4:29 · 7.5MB") +
    song("稻香", "周杰伦 · 魔杰座 · 3:43 · 6.8MB") +
    song("七里香", "周杰伦 · 七里香 · 4:59 · 9.1MB", "❤️", "g2") +
    song("告白气球", "周杰伦 · 周杰伦的床边故事 · 3:31 · 6.2MB") +
    song("青花瓷", "周杰伦 · 我很忙 · 4:00 · 7.3MB", "❤️", "g3") +
    mini_player() + tab_bar(0)))

# ── 5. 艺术家列表 ──
pages.append(phone("5. 艺术家视图", "P0",
    nav("音乐库", "☰", "⚙️") +
    tabs(["全部", "艺术家", "专辑", "歌单分组"], 1) +
    search_bar("搜索艺术家") +
    lrow("👤", "周杰伦", "42首歌曲") +
    lrow("👤", "林俊杰", "28首歌曲") +
    lrow("👤", "邓紫棋", "19首歌曲") +
    lrow("👤", "陈奕迅", "35首歌曲") +
    lrow("👤", "五月天", "22首歌曲") +
    lrow("👤", "未知艺术家", "8首歌曲") +
    mini_player() + tab_bar(0)))

# ── 6. 艺术家详情 ──
pages.append(phone("6. 艺术家详情页", "P0",
    nav_back("周杰伦", "···") +
    f"""<div style="padding:16px 14px;text-align:center;background:#f0f0ff">
      <div style="width:80px;height:80px;border-radius:50%;background:linear-gradient(135deg,#667eea,#764ba2);display:flex;align-items:center;justify-content:center;font-size:36px;margin:0 auto 10px">👤</div>
      <div style="font-size:18px;font-weight:700;margin-bottom:4px">周杰伦</div>
      <div class="text-sm">42首歌曲 · 12张专辑</div>
      <div style="display:flex;justify-content:center;gap:10px;margin-top:12px">
        <button class="ablbtn m">▶ 播放全部</button>
        <button class="ablbtn s">🔀 随机播放</button>
      </div>
    </div>""" +
    sec_hdr("歌曲") +
    song("夜曲", "十一月的萧邦 · 3:45", "❤️") +
    song("晴天", "叶惠美 · 4:29") +
    song("稻香", "魔杰座 · 3:43") +
    song("七里香", "七里香 · 4:59", "❤️", "g2") +
    mini_player() + tab_bar(0)))

# ── 7. 专辑视图 ──
pages.append(phone("7. 专辑视图", "P0",
    nav("音乐库", "☰", "⚙️") +
    tabs(["全部", "艺术家", "专辑", "歌单分组"], 2) +
    search_bar("搜索专辑") +
    lrow("💿", "十一月的萧邦", "周杰伦 · 2005 · 10首") +
    lrow("💿", "叶惠美", "周杰伦 · 2003 · 10首") +
    lrow("💿", "七里香", "周杰伦 · 2004 · 10首") +
    lrow("💿", "魔杰座", "周杰伦 · 2008 · 10首") +
    lrow("💿", "我很忙", "周杰伦 · 2007 · 10首") +
    mini_player() + tab_bar(0)))

# ── 8. 专辑详情 ──
pages.append(phone("8. 专辑详情页", "P0",
    nav_back("七里香", "···") +
    f"""<div class="alb-head">
      <div class="alb-cov">🎵</div>
      <div style="font-size:17px;font-weight:700">七里香</div>
      <div class="alb-meta">周杰伦 · 2004 · 10首歌曲</div>
      <div class="alb-btns">
        <button class="ablbtn m">▶ 播放全部</button>
        <button class="ablbtn s">🔀 随机</button>
        <button class="ablbtn s">❤️</button>
      </div>
    </div>""" +
    f"""<div class="song"><div class="tnum">1</div><div class="sinf"><div class="sname">我的地盘</div><div class="smeta">4:02</div></div><span class="more">›</span></div>
    <div class="song"><div class="tnum">2</div><div class="sinf"><div class="sname">七里香</div><div class="smeta">4:59</div></div><span class="more">›</span></div>
    <div class="song"><div class="tnum">3</div><div class="sinf"><div class="sname">借口</div><div class="smeta">3:31</div></div><span class="more">›</span></div>
    <div class="song"><div class="tnum">4</div><div class="sinf"><div class="sname">外婆</div><div class="smeta">3:26</div></div><span class="more">›</span></div>
    <div class="song"><div class="tnum">5</div><div class="sinf"><div class="sname">将军</div><div class="smeta">4:26</div></div><span class="more">›</span></div>""" +
    mini_player() + tab_bar(0)))

# ── 9. 歌单分组视图 ──
pages.append(phone("9. 歌单分组视图", "P2",
    nav("音乐库", "☰", "⚙️") +
    tabs(["全部", "艺术家", "专辑", "歌单分组"], 3) +
    search_bar("搜索分组") +
    f"""<div class="grp-row"><span class="gic">📁</span><div class="ginf"><div class="gname">通勤</div><div class="gsub">3个歌单</div></div><span class="arr">›</span></div>
    <div class="grp-row"><span class="gic">📁</span><div class="ginf"><div class="gname">运动健身</div><div class="gsub">2个歌单</div></div><span class="arr">›</span></div>
    <div class="grp-row"><span class="gic">📁</span><div class="ginf"><div class="gname">睡前放松</div><div class="gsub">4个歌单</div></div><span class="arr">›</span></div>
    <div class="grp-row"><span class="gic">📁</span><div class="ginf"><div class="gname">工作专注</div><div class="gsub">5个歌单</div></div><span class="arr">›</span></div>
    <div class="grp-row"><span class="gic">📁</span><div class="ginf"><div class="gname">未分组</div><div class="gsub">8个歌单</div></div><span class="arr">›</span></div>""" +
    f'<div style="padding:14px"><button class="btn btnp" style="width:100%">＋ 新建分组</button></div>' +
    mini_player() + tab_bar(0)))

# ── 10. 歌曲详情页 ──
pages.append(phone("10. 歌曲详情页", "P0",
    nav_back("歌曲详情") +
    f"""<div class="det-cov"><div class="det-alb">🎵</div></div>
    <div class="det-inf">
      <div class="det-name">夜曲</div>
      <div class="det-artist">周杰伦 · 十一月的萧邦</div>
    </div>
    <div class="det-acts">
      <div class="dact"><div class="dact-ic">❤️</div><div class="dact-lbl">收藏</div></div>
      <div class="dact"><div class="dact-ic">▶️</div><div class="dact-lbl">播放</div></div>
      <div class="dact"><div class="dact-ic">➕</div><div class="dact-lbl">加入歌单</div></div>
      <div class="dact"><div class="dact-ic">⋯</div><div class="dact-lbl">更多</div></div>
    </div>""" +
    sec_hdr("文件信息") +
    f"""<div class="irow"><span class="ikey">格式</span><span class="ival">MP3</span></div>
    <div class="irow"><span class="ikey">采样率</span><span class="ival">44100 Hz</span></div>
    <div class="irow"><span class="ikey">比特率</span><span class="ival">320 kbps</span></div>
    <div class="irow"><span class="ikey">声道</span><span class="ival">立体声</span></div>
    <div class="irow"><span class="ikey">时长</span><span class="ival">3:45</span></div>
    <div class="irow"><span class="ikey">文件大小</span><span class="ival">8.2 MB</span></div>""" +
    sec_hdr("导入信息") +
    f"""<div class="irow"><span class="ikey">导入时间</span><span class="ival">2026-03-14</span></div>
    <div class="irow"><span class="ikey">播放次数</span><span class="ival">12</span></div>
    <div class="irow"><span class="ikey">最后播放</span><span class="ival">2小时前</span></div>
    <div class="irow"><span class="ikey">文件路径</span><span class="ival" style="font-size:11px">Music/夜曲.mp3</span></div>"""))

# ── 11. 播放器主页 ──
pages.append(phone("11. 播放器 — 主界面", "P0",
    nav_back("正在播放", "⋯") +
    f"""<div class="player-bg">
      <div class="alb">🎵</div>
      <div class="pname">夜曲</div>
      <div class="partist">周杰伦 · 十一月的萧邦</div>
      <div style="display:flex;justify-content:space-between;align-items:center;margin-top:10px">
        <span style="font-size:20px;cursor:pointer;opacity:.7">🤍</span>
        <span style="font-size:13px;opacity:.6">FLAC · 44100 Hz</span>
        <span style="font-size:20px;cursor:pointer;opacity:.7">➕</span>
      </div>
      <div class="prog">
        <div class="ptrack"><div class="pfill"></div></div>
        <div class="ptime"><span>1:23</span><span>3:45</span></div>
      </div>
      <div class="ctrl-row">
        <span class="ctrl">🔀</span>
        <span class="ctrl">⏮</span>
        <span class="ctrl main">⏸</span>
        <span class="ctrl">⏭</span>
        <span class="ctrl">🔁</span>
      </div>
      <div class="pextras">
        <span class="pext">📃</span>
        <span class="pext">⏱</span>
        <span class="pext">🎛</span>
        <span class="pext">📋</span>
        <span class="pext">1.0x</span>
      </div>
    </div>"""))

# ── 12. 歌词页 ──
pages.append(phone("12. 歌词显示页", "P2",
    nav_back("歌词", "⋯") +
    f"""<div style="padding:10px 14px;background:#f0f0ff;display:flex;align-items:center;gap:10px">
      <div class="mcov">🎵</div>
      <div><div class="mname fw6">夜曲</div><div class="text-sm">周杰伦</div></div>
      <div style="margin-left:auto;font-size:13px;color:#86868b">同步歌词</div>
    </div>
    <div class="lyric-wrap">
      <div class="lyric-line">半岛铁盒</div>
      <div class="lyric-line near">等一下再出发</div>
      <div class="lyric-line act">夜曲 弹一首</div>
      <div class="lyric-line near">献给你的爱</div>
      <div class="lyric-line">想要再靠近你一些</div>
      <div class="lyric-line">怕你跟我说再见</div>
      <div class="lyric-line">如果 你已爱上了别人</div>
      <div class="lyric-line">就不应该再奢望拥有我的心</div>
    </div>
    <div style="text-align:center;padding:14px">
      <button class="btn btns" style="font-size:12px">✏️ 编辑歌词 (P3)</button>
    </div>""" +
    mini_player()))

# ── 13. 播放队列 ──
pages.append(phone("13. 播放队列", "P1",
    nav_back("播放队列", "⋯") +
    f"""<div style="padding:8px 14px;display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #f0f0f0">
      <span class="text-sm">共8首 · 已播放2首</span>
      <span style="font-size:13px;color:#ff3b30;cursor:pointer">清空</span>
    </div>""" +
    f"""<div class="q-item playing"><span class="qnum">▶</span><div class="cov sm">🎵</div><div class="sinf"><div class="sname cp fw6">夜曲</div><div class="smeta">周杰伦 · 正在播放</div></div><span class="qdrag">⋮⋮</span></div>
    <div class="q-item"><span class="qnum">2</span><div class="cov sm">🎵</div><div class="sinf"><div class="sname">晴天</div><div class="smeta">周杰伦</div></div><span class="qdrag">⋮⋮</span></div>
    <div class="q-item"><span class="qnum">3</span><div class="cov sm">🎵</div><div class="sinf"><div class="sname">稻香</div><div class="smeta">周杰伦</div></div><span class="qdrag">⋮⋮</span></div>
    <div class="q-item"><span class="qnum">4</span><div class="cov sm">🎵</div><div class="sinf"><div class="sname">七里香</div><div class="smeta">周杰伦</div></div><span class="qdrag">⋮⋮</span></div>
    <div class="q-item" style="opacity:.5"><span class="qnum">✓</span><div class="cov sm">🎵</div><div class="sinf"><div class="sname" style="text-decoration:line-through">青花瓷</div><div class="smeta">已播放</div></div></div>""" +
    f'<div style="padding:12px 14px"><button class="btn btnp" style="width:100%;font-size:13px">💾 保存为歌单</button></div>'))

# ── 14. 歌单列表 ──
pages.append(phone("14. 歌单列表", "P0",
    nav("歌单", "☰", "＋") +
    lrow("❤️", "我喜欢", "24首 · 按收藏时间排序") +
    lrow("🕐", "最近播放", "50首 · 最近7天") +
    thick_div() +
    f"""<div class="pl-grid">
      <div class="plcard"><div class="plcov-4"><span>🎵</span><span>🎵</span><span>🎵</span><span>🎵</span></div><div class="pltitle">通勤必备</div><div class="plsub">18首</div></div>
      <div class="plcard"><div class="plcov g2">🎵</div><div class="pltitle">运动电音</div><div class="plsub">12首</div></div>
      <div class="plcard"><div class="plcov g3">🎵</div><div class="pltitle">睡前轻音乐</div><div class="plsub">8首</div></div>
      <div class="plcard"><div class="plcov g4">🎵</div><div class="pltitle">周杰伦精选</div><div class="plsub">30首</div></div>
    </div>""" +
    mini_player() + tab_bar(1)))

# ── 15. 我喜欢歌单 ──
pages.append(phone("15. 我喜欢 歌单", "P0",
    nav_back("我喜欢", "⋯") +
    f"""<div style="padding:14px;background:#fff5f5;border-bottom:1px solid #fecaca;display:flex;justify-content:space-between;align-items:center">
      <span style="font-size:24px;font-weight:600">24首收藏</span>
      <span style="font-size:13px;color:#86868b">按收藏时间排序</span>
    </div>""" +
    song("夜曲", "周杰伦 · 3:45 · 收藏于1小时前", "❤️") +
    song("七里香", "周杰伦 · 4:59 · 收藏于昨天", "❤️", "g2") +
    song("青花瓷", "周杰伦 · 4:00 · 收藏于3天前", "❤️", "g3") +
    song("告白气球", "周杰伦 · 3:31 · 收藏于上周", "❤️", "g4") +
    f"""<div style="padding:10px 14px;text-align:center;color:#86868b;font-size:12px">不可删除 · 不可重命名</div>""" +
    mini_player()))

# ── 16. 最近播放 ──
pages.append(phone("16. 最近播放 歌单", "P1",
    nav_back("最近播放", "⋯") +
    f"""<div style="padding:10px 14px;background:#f8f8f8;border-bottom:1px solid #eee">
      <div style="display:flex;gap:6px;font-size:12px;flex-wrap:wrap">
        <span style="padding:4px 10px;border-radius:12px;background:#667eea;color:white;cursor:pointer">7天</span>
        <span style="padding:4px 10px;border-radius:12px;background:#f0f0f0;cursor:pointer">3天</span>
        <span style="padding:4px 10px;border-radius:12px;background:#f0f0f0;cursor:pointer">14天</span>
        <span style="padding:4px 10px;border-radius:12px;background:#f0f0f0;cursor:pointer">30天</span>
        <span style="padding:4px 10px;border-radius:12px;background:#f0f0f0;cursor:pointer">全部</span>
      </div>
    </div>""" +
    song("夜曲", "周杰伦 · 最后播放：2分钟前", "❤️") +
    song("晴天", "周杰伦 · 最后播放：1小时前") +
    song("告白气球", "周杰伦 · 最后播放：昨天", "❤️", "g2") +
    song("稻香", "周杰伦 · 最后播放：昨天") +
    f'<div style="text-align:center;padding:10px;font-size:12px;color:#86868b">已加载 4 / 38 首</div>' +
    mini_player()))

# ── 17. 创建歌单 ──
pages.append(phone("17. 创建歌单", "P0",
    nav_back("新建歌单", "完成") +
    f"""<div style="padding:20px 14px;text-align:center">
      <div style="width:100px;height:100px;border-radius:16px;background:linear-gradient(135deg,#667eea,#764ba2);display:flex;align-items:center;justify-content:center;font-size:40px;margin:0 auto 10px;cursor:pointer">🎵</div>
      <div style="font-size:12px;color:#86868b;cursor:pointer">点击设置封面</div>
    </div>
    <div class="thick-div"></div>
    <div style="padding:12px 14px">
      <div style="margin-bottom:14px">
        <div style="font-size:12px;color:#86868b;margin-bottom:6px">歌单名称</div>
        <input type="text" style="width:100%;padding:10px;border:1px solid #e5e5e7;border-radius:10px;font-size:14px;outline:none" placeholder="输入歌单名称（最多50字）" value="我的歌单">
      </div>
      <div>
        <div style="font-size:12px;color:#86868b;margin-bottom:6px">描述（可选）</div>
        <textarea style="width:100%;padding:10px;border:1px solid #e5e5e7;border-radius:10px;font-size:14px;outline:none;resize:none;height:70px" placeholder="添加描述（最多200字）"></textarea>
      </div>
    </div>
    <div style="padding:0 14px 14px">
      <button class="btn btnp" style="width:100%">创建歌单</button>
    </div>"""))

# ── 18. 导入进度 ──
pages.append(phone("18. 导入音乐 — 进度", "P0",
    nav("正在导入音乐", "✕", "") +
    f"""<div class="imp-prog">
      <div class="pbar-wrap"><div class="pbar-fill" style="width:60%"></div></div>
      <div class="text-sm" style="margin-top:4px">正在导入：周杰伦 - 夜曲.mp3</div>
      <div class="flex-btw" style="margin-top:6px">
        <span class="text-sm">已完成：6 / 10</span>
        <span class="text-sm">预计剩余：30秒</span>
      </div>
      <div class="imp-stats">
        <div class="istat"><span>✅</span><span style="color:#166534">成功：6首</span></div>
        <div class="istat"><span>⚠️</span><span style="color:#92400e">跳过：2首（格式不支持）</span></div>
        <div class="istat"><span>❌</span><span style="color:#991b1b">失败：1首</span></div>
        <div class="istat"><span>ℹ️</span><span style="color:#1e40af">元数据不完整：1首（已用默认）</span></div>
      </div>
      <button class="btn btns" style="width:100%;margin-top:8px">取消（已导入的保留）</button>
    </div>"""))

# ── 19. 导入完成 ──
pages.append(phone("19. 导入完成", "P0",
    nav("导入完成", "✕", "") +
    f"""<div class="empty" style="padding-top:32px">
      <div class="eic">✅</div>
      <div class="etxt">导入完成</div>
      <div class="esub">成功导入 8 首，跳过 2 首</div>
    </div>
    <div class="imp-stats" style="margin:0 14px">
      <div class="istat"><span>✅</span><span style="color:#166534">成功：8首</span></div>
      <div class="istat"><span>⚠️</span><span style="color:#92400e">跳过：2首（格式不支持）</span></div>
    </div>
    <div style="padding:14px">
      <button class="btn btnp" style="width:100%;margin-bottom:10px">查看导入的音乐</button>
      <button class="btn btns" style="width:100%">关闭</button>
    </div>"""))

# ── 20. WiFi 传输 ──
pages.append(phone("20. WiFi 传输", "P1",
    nav_back("WiFi 传输", "⋯") +
    f"""<div class="alert alert-w">⚠️ 仅在可信WiFi网络中使用，HTTP传输可能被监听</div>
    <div class="wifi-box">
      <div style="font-size:12px;color:#86868b;margin-bottom:6px;text-align:center">在浏览器中打开以下地址</div>
      <div class="waddr">http://192.168.1.100:8080</div>
      <div class="qr">📱</div>
      <div style="font-size:12px;color:#86868b;text-align:center;margin-bottom:8px">访问密码</div>
      <div class="wpwd">
        <div class="wdig">8</div><div class="wdig">5</div><div class="wdig">2</div>
        <div class="wdig">7</div><div class="wdig">3</div><div class="wdig">9</div>
      </div>
    </div>""" +
    sec_hdr("状态") +
    f"""<div class="irow"><span class="ikey">连接状态</span><span class="ival" style="color:#34c759">已连接 · 192.168.1.50</span></div>
    <div class="irow"><span class="ikey">传输状态</span><span class="ival cp">传输中 · 2.3 MB/s</span></div>""" +
    toggle_row("访问密码保护", True, "关闭后任何人可访问") +
    f'<div style="padding:14px"><button class="btn btnd" style="width:100%">停止 WiFi 传输</button></div>'))

# ── 21. 搜索历史 ──
pages.append(phone("21. 搜索 — 历史记录", "P1",
    nav("音乐库", "☰", "⚙️") +
    tabs(["全部", "艺术家", "专辑", "歌单分组"], 0) +
    search_bar() +
    f"""<div class="search-stats">🔍 周杰伦 · 搜索到42首歌曲，1个艺术家，12个专辑</div>""" +
    sec_hdr("最近搜索") +
    f"""<div class="clear-all">清除所有历史</div>
    <div class="hist-item"><span class="hkw">🕐 周杰伦</span><span class="htime">2分钟前</span><span class="hdel">✕</span></div>
    <div class="hist-item"><span class="hkw">🕐 稻香</span><span class="htime">1小时前</span><span class="hdel">✕</span></div>
    <div class="hist-item"><span class="hkw">🕐 七里香</span><span class="htime">昨天</span><span class="hdel">✕</span></div>
    <div class="hist-item"><span class="hkw">🕐 林俊杰</span><span class="htime">2天前</span><span class="hdel">✕</span></div>""" +
    f"""<div class="empty" style="padding:24px 20px">
      <div style="font-size:13px;color:#86868b">输入关键词开始搜索歌曲、艺术家、专辑</div>
    </div>"""))

# ── 22. 搜索结果 ──
pages.append(phone("22. 搜索结果", "P1",
    nav("音乐库", "☰", "⚙️") +
    tabs(["全部", "艺术家", "专辑", "歌单分组"], 0) +
    f"""<div class="sbar"><div class="sbar-wrap"><input class="sinp" type="text" value="周杰伦" style="background:#f0f0ff"></div></div>""" +
    f"""<div class="search-stats">搜索到 42首歌曲，1个艺术家，12个专辑</div>""" +
    sec_hdr("歌曲") +
    f"""<div class="song"><div class="cov">🎵</div><div class="sinf"><div class="sname"><b>周杰伦</b> — 夜曲</div><div class="smeta" style="color:#667eea">十一月的萧邦 · 3:45</div></div></div>
    <div class="song"><div class="cov g2">🎵</div><div class="sinf"><div class="sname"><b>周杰伦</b> — 晴天</div><div class="smeta" style="color:#667eea">叶惠美 · 4:29</div></div></div>""" +
    sec_hdr("艺术家") +
    lrow("👤", "周杰伦", "42首歌曲") +
    sec_hdr("专辑") +
    lrow("💿", "七里香", "周杰伦 · 2004")))

# ── 23. 批量操作 ──
pages.append(phone("23. 批量操作", "P2",
    f"""<div class="bulk-bar"><span class="bcancel">取消</span><span class="bcount">已选 3 首</span></div>
    <div class="bulk-acts">
      <button class="bbtn a">全选</button>
      <button class="bbtn p">▶ 播放</button>
      <button class="bbtn pl">＋ 歌单</button>
      <button class="bbtn d">🗑 删除</button>
    </div>""" +
    song_cb("夜曲", "周杰伦 · 3:45", True, True) +
    song_cb("晴天", "周杰伦 · 4:29", True) +
    song_cb("稻香", "周杰伦 · 3:43", False) +
    song_cb("七里香", "周杰伦 · 4:59", True) +
    song_cb("告白气球", "周杰伦 · 3:31", False) +
    mini_player()))

# ── 24. 定时播放 ──
pages.append(phone("24. 定时播放", "P2",
    nav_back("定时播放") +
    f"""<div class="timer-active">
      <div style="font-size:13px;color:#86868b">距离停止播放</div>
      <div class="timer-cd">28:43</div>
      <div style="font-size:12px;color:#86868b">后台受系统调度影响，可能存在少许延迟</div>
      <button class="btn btnd" style="margin-top:10px;font-size:13px">取消定时</button>
    </div>""" +
    sec_hdr("设置定时") +
    f"""<div class="time-opt"><span>关闭定时器</span><span></span></div>
    <div class="time-opt"><span>15 分钟后停止</span><span></span></div>
    <div class="time-opt" style="background:#f0f0ff"><span class="cp fw6">30 分钟后停止</span><span class="ck">✓</span></div>
    <div class="time-opt"><span>45 分钟后停止</span><span></span></div>
    <div class="time-opt"><span>60 分钟后停止</span><span></span></div>""" +
    f"""<div class="alert alert-w" style="margin:10px 14px;border-radius:8px">⚠️ 结束前1分钟将发送通知提醒（需授权）</div>"""))

# ── 25. 播放速度 ──
pages.append(phone("25. 播放速度", "P2",
    nav_back("播放速度") +
    f"""<div class="speed-opt"><span>0.5x <span class="text-sm">学习/听清歌词</span></span><span></span></div>
    <div class="speed-opt"><span>0.75x <span class="text-sm">慢速欣赏</span></span><span></span></div>
    <div class="speed-opt" style="background:#f0f0ff"><span class="cp fw6">1.0x <span style="color:#86868b;font-weight:400">正常播放（默认）</span></span><span class="ck">✓</span></div>
    <div class="speed-opt"><span>1.25x <span class="text-sm">快速浏览</span></span><span></span></div>
    <div class="speed-opt"><span>1.5x <span class="text-sm">运动/快速听</span></span><span></span></div>
    <div class="speed-opt"><span>2.0x <span class="text-sm">快速查找</span></span><span></span></div>""" +
    toggle_row("全局记忆速度", True, "所有歌曲使用相同速度") +
    f"""<div style="padding:10px 14px;font-size:12px;color:#86868b">当前：1.0x · 速度调整时保持音调不变</div>"""))

# ── 26. 设置主页 ──
pages.append(phone("26. 设置主页", "P0",
    nav("设置", "←", "") +
    f"""<div class="storage-row">
      <div class="stor-item"><div class="stor-val">128</div><div class="stor-lbl">首歌曲</div></div>
      <div class="stor-item"><div class="stor-val">2.4GB</div><div class="stor-lbl">占用空间</div></div>
      <div class="stor-item"><div class="stor-val">89MB</div><div class="stor-lbl">缓存</div></div>
    </div>""" +
    sec_hdr("导入") +
    set_row("从文件应用导入", "›") +
    set_row("WiFi 传输", "›") +
    set_row("文件管理", "›") +
    sec_hdr("播放") +
    set_row("播放设置", "›") +
    set_row("均衡器", "P3 ›") +
    sec_hdr("显示") +
    set_row("主题", "跟随系统 ›") +
    sec_hdr("数据") +
    set_row("清理缓存", "89 MB ›") +
    set_row("数据备份恢复", "P3 ›") +
    sec_hdr("其他") +
    set_row("隐私政策", "›") +
    set_row("帮助与反馈", "›") +
    tab_bar(3)))

# ── 27. 播放设置 ──
pages.append(phone("27. 播放设置", "P1",
    nav_back("播放设置") +
    sec_hdr("播放模式") +
    toggle_row("随机播放", False) +
    toggle_row("列表循环", False) +
    sec_hdr("音频") +
    set_row("播放速度", "1.0x ›") +
    set_row("均衡器", "关闭 · P3 ›") +
    sec_hdr("行为") +
    toggle_row("后台播放", True) +
    toggle_row("来电时暂停", True) +
    toggle_row("中断后自动恢复", True) +
    sec_hdr("定时播放") +
    set_row("定时停止", "关闭 ›") +
    sec_hdr("耳机控制说明") +
    f"""<div class="p14">
      <div class="text-sm" style="line-height:1.9">
        单击中键：播放/暂停<br>
        双击中键：下一曲<br>
        三击中键：上一曲<br>
        <span style="color:#ff9500">不同品牌耳机可能存在差异，请以说明书为准</span>
      </div>
    </div>"""))

# ── 28. 主题设置 ──
pages.append(phone("28. 主题设置", "P1",
    nav_back("主题") +
    f"""<div class="radio-opt">
      <div class="rdot on"></div>
      <div class="rtxt"><div class="rlbl">跟随系统（默认）</div><div class="rdesc">自动跟随 iOS 深色/浅色模式</div></div>
    </div>
    <div class="radio-opt">
      <div class="rdot"></div>
      <div class="rtxt"><div class="rlbl">日间模式</div><div class="rdesc">强制使用浅色主题</div></div>
    </div>
    <div class="radio-opt">
      <div class="rdot"></div>
      <div class="rtxt"><div class="rlbl">夜间模式</div><div class="rdesc">强制使用深色主题</div></div>
    </div>""" +
    f"""<div class="p14 text-sm" style="margin-top:8px">当前：跟随系统 · 已启用浅色模式</div>"""))

# ── 29. 文件管理 ──
pages.append(phone("29. 文件管理", "P0",
    nav_back("文件管理", "⋯") +
    f"""<div class="stbar">
      <div class="flex-btw" style="font-size:13px"><span>已用空间</span><span class="fw6">2.4 GB</span></div>
      <div class="sttrack"><div class="stfill"></div></div>
      <div class="stlbls"><span>0</span><span>可用 12.6 GB</span></div>
    </div>""" +
    sec_hdr("音乐文件") +
    f"""<div class="frow"><span class="fic">🎵</span><div class="finf"><div class="fname">夜曲.mp3</div><div class="fsize">8.2 MB · 2026-03-14</div></div><span class="ftag fok">正常</span></div>
    <div class="frow"><span class="fic">🎵</span><div class="finf"><div class="fname">晴天.flac</div><div class="fsize">32.4 MB · 2026-03-12</div></div><span class="ftag fok">正常</span></div>
    <div class="frow"><span class="fic">🎵</span><div class="finf"><div class="fname">orphan_file.mp3</div><div class="fsize">5.1 MB · 无引用</div></div><span class="ftag forp">无引用</span></div>""" +
    f"""<div style="padding:12px 14px"><button class="btn" style="width:100%;background:#fee2e2;color:#991b1b;font-size:13px">清理无引用文件（5.1 MB）</button></div>"""))

# ── 30. 空状态 无音乐 ──
pages.append(phone("30. 空状态 — 无音乐", "P2",
    nav("音乐库", "☰", "⚙️") +
    tabs(["全部", "艺术家", "专辑", "歌单分组"], 0) +
    f"""<div class="empty">
      <div class="eic">🎵</div>
      <div class="etxt">还没有音乐文件</div>
      <div class="esub">点击下方按钮导入音乐到应用</div>
      <div class="btn-row">
        <button class="btn btnp">📂 从文件导入</button>
        <button class="btn btns">📡 WiFi 传输</button>
      </div>
    </div>""" +
    tab_bar(0)))

# ── 31. 空状态 无收藏 ──
pages.append(phone("31. 空状态 — 无收藏", "P2",
    nav_back("我喜欢") +
    f"""<div class="empty">
      <div class="eic">🤍</div>
      <div class="etxt">还没有收藏的歌曲</div>
      <div class="esub">在歌曲列表中点击爱心<br>或左滑选择"添加到我喜欢"</div>
    </div>"""))

# ── 32. 空状态 歌单为空 ──
pages.append(phone("32. 空状态 — 歌单为空", "P2",
    nav_back("我的歌单", "⋯") +
    f"""<div class="empty">
      <div class="eic">📋</div>
      <div class="etxt">这个歌单还没有歌曲</div>
      <div class="esub">去音乐库中添加歌曲到此歌单</div>
      <button class="btn btnp">去添加歌曲</button>
    </div>"""))

# ── 33. 空状态 无搜索结果 ──
pages.append(phone("33. 空状态 — 无搜索结果", "P2",
    nav("音乐库", "☰", "⚙️") +
    tabs(["全部", "艺术家", "专辑", "歌单分组"], 0) +
    f"""<div class="sbar"><div class="sbar-wrap"><input class="sinp" type="text" value="xyz123"></div></div>""" +
    f"""<div class="empty">
      <div class="eic">🔍</div>
      <div class="etxt">未找到相关音乐</div>
      <div class="esub">"xyz123" 没有匹配结果</div>
      <div class="btn-row">
        <button class="btn btns">清除搜索</button>
        <button class="btn btnp">浏览全部音乐</button>
      </div>
    </div>"""))

# ── 34. 删除确认弹窗 ──
pages.append(phone("34. 删除确认 — 弹窗", "P0",
    nav_back("全部音乐") +
    song("夜曲", "周杰伦 · 3:45", "❤️") +
    song("晴天", "周杰伦 · 4:29") +
    f"""<div class="modal-wrap" style="padding:0;margin:0">
      <div style="background:rgba(0,0,0,.35);padding:20px 14px">
        <div class="mbox">
          <div class="mtitle">从音乐库删除</div>
          <div class="msub">确定要从音乐库删除"夜曲"吗？<br>文件将被永久删除（30秒内可撤销）</div>
          <div class="mdiv"></div>
          <div class="mbtns">
            <button class="mbtn">取消</button>
            <button class="mbtn danger">删除</button>
          </div>
        </div>
      </div>
    </div>""" +
    f"""<div class="snackbar">已删除"夜曲" <span class="snk-action">撤销</span></div>"""))

# ── 35. 队列已满弹窗 ──
pages.append(phone("35. 播放队列已满", "P1",
    nav_back("正在播放") +
    f"""<div style="padding:20px 14px">
      <div class="mbox">
        <div class="mtitle">播放队列已满（999首）</div>
        <div class="msub">继续添加歌曲，请选择操作方式：</div>
        <div class="mdiv"></div>
        <div class="radio-opt"><div class="rdot"></div><div class="rtxt"><div class="rlbl">清空后添加</div><div class="rdesc">清空当前队列并添加新歌曲</div></div></div>
        <div class="radio-opt"><div class="rdot on"></div><div class="rtxt"><div class="rlbl cp">仅播放不入队（推荐）</div><div class="rdesc">立即播放，不改变队列</div></div></div>
        <div class="mdiv"></div>
        <div class="mbtns">
          <button class="mbtn">取消</button>
          <button class="mbtn cp fw6">确认</button>
        </div>
      </div>
    </div>"""))

# ── 36. 错误：播放失败 ──
pages.append(phone("36. 错误 — 播放失败", "P0",
    nav_back("全部音乐") +
    f"""<div style="padding:20px 14px">
      <div class="mbox">
        <div style="text-align:center;padding:20px 14px 0">
          <div style="font-size:44px;margin-bottom:12px">❌</div>
          <div style="font-size:16px;font-weight:600;margin-bottom:6px">无法播放歌曲</div>
          <div style="font-size:13px;color:#86868b;line-height:1.6">文件不存在或已被移动<br>该文件可能已被删除</div>
        </div>
        <div class="mdiv" style="margin-top:16px"></div>
        <div class="mbtns">
          <button class="mbtn">重试</button>
          <button class="mbtn">播放下一首</button>
          <button class="mbtn danger">移除歌曲</button>
        </div>
      </div>
    </div>"""))

# ── 37. 错误：权限 ──
pages.append(phone("37. 错误 — 权限/通知授权", "P0",
    nav_back("定时播放") +
    f"""<div style="padding:16px 14px">
      <div class="mbox">
        <div style="text-align:center;padding:16px 14px 0">
          <div style="font-size:44px;margin-bottom:12px">🔔</div>
          <div style="font-size:16px;font-weight:600;margin-bottom:6px">开启通知提醒？</div>
          <div style="font-size:13px;color:#86868b;line-height:1.6">定时播放结束前1分钟<br>发送提醒通知（需授权）<br>选择"暂不"仍可使用定时功能</div>
        </div>
        <div class="mdiv" style="margin-top:14px"></div>
        <div class="mbtns">
          <button class="mbtn">暂不开启</button>
          <button class="mbtn cp fw6">去设置中开启</button>
        </div>
      </div>
    </div>
    <div class="time-opt" style="margin-top:8px"><span>30 分钟后停止</span><span class="ck">✓</span></div>
    <div class="alert alert-w" style="margin:10px 14px;border-radius:8px">ℹ️ 通知已关闭，定时结束时将直接暂停播放</div>"""))

# ── 38. 批量删除选项 ──
pages.append(phone("38. 批量删除 — 选项", "P2",
    f"""<div class="bulk-bar"><span class="bcancel">取消</span><span class="bcount">已选 3 首</span></div>""" +
    song_cb("夜曲", "周杰伦 · 3:45", True) +
    song_cb("晴天", "周杰伦 · 4:29", True) +
    song_cb("稻香", "周杰伦 · 3:43", True) +
    f"""<div style="padding:14px">
      <div class="mbox">
        <div class="mtitle">选择删除方式</div>
        <div class="mdiv" style="margin-top:12px"></div>
        <div class="radio-opt"><div class="rdot on"></div><div class="rtxt"><div class="rlbl">从歌单移除</div><div class="rdesc">从所有歌单中移除，不删除文件</div></div></div>
        <div class="radio-opt"><div class="rdot"></div><div class="rtxt"><div class="rlbl cred">从音乐库删除</div><div class="rdesc">删除文件，需二次确认，30秒内可撤销</div></div></div>
        <div class="mdiv"></div>
        <div class="mbtns">
          <button class="mbtn">取消</button>
          <button class="mbtn cp fw6">确认</button>
        </div>
      </div>
    </div>"""))

# ── 39. 左滑操作 Bottom Sheet ──
pages.append(phone("39. 歌曲操作 — 左滑菜单", "P0",
    nav_back("全部音乐") +
    song("夜曲", "周杰伦 · 十一月的萧邦 · 3:45", "❤️") +
    song("晴天", "周杰伦 · 叶惠美 · 4:29") +
    f"""<div class="bs">
      <div class="bs-handle"></div>
      <div class="bs-title">夜曲 — 周杰伦</div>
      <div class="bs-opt"><span class="bsic">▶️</span>播放</div>
      <div class="bs-opt"><span class="bsic">⏭</span>下一首播放</div>
      <div class="bs-opt"><span class="bsic">➕</span>添加到播放队列</div>
      <div class="bs-opt"><span class="bsic">📋</span>添加到歌单</div>
      <div class="bs-opt"><span class="bsic">❤️</span>添加到我喜欢</div>
      <div class="bs-opt"><span class="bsic">ℹ️</span>查看详细信息</div>
      <div class="bs-opt" style="color:#ff3b30"><span class="bsic">🗑</span>从音乐库删除</div>
    </div>"""))

# ── 40. WiFi 传输断连确认 ──
pages.append(phone("40. WiFi传输 — 断连保护", "P1",
    nav_back("WiFi 传输") +
    f"""<div class="alert alert-w">⚠️ 仅在可信WiFi网络中使用，HTTP传输可能被监听</div>
    <div class="wifi-box">
      <div class="waddr">http://192.168.1.100:8080</div>
      <div class="irow" style="margin:0"><span class="ikey">状态</span><span class="ival" style="color:#ff9500">⚠️ 传输中 · 78%</span></div>
    </div>
    <div style="padding:0 14px">
      <div class="mbox">
        <div class="mtitle">⚠️ 有设备正在传输文件</div>
        <div class="msub">192.168.1.50 正在上传"夜曲合集.zip"（已上传78%）<br>断开将中止传输，不完整文件将被自动清理</div>
        <div class="mdiv"></div>
        <div class="mbtns">
          <button class="mbtn">取消</button>
          <button class="mbtn danger">确认断开</button>
        </div>
      </div>
    </div>"""))

# ── 41. 隐私政策页 ──
pages.append(phone("41. 隐私政策", "P1",
    nav_back("隐私政策") +
    f"""<div class="privacy-section">
      <div class="privacy-title">数据收集</div>
      <div class="privacy-item">✅ 我们不收集任何用户数据</div>
      <div class="privacy-item">✅ 所有数据仅存储在您的设备上</div>
      <div class="privacy-item">✅ 不使用任何第三方分析工具</div>
    </div>
    <div class="thick-div"></div>
    <div class="privacy-section">
      <div class="privacy-title">本地存储说明</div>
      <div class="privacy-item">🎵 音乐文件 → Documents/Music/</div>
      <div class="privacy-item">🖼 封面图片 → Caches/</div>
      <div class="privacy-item">📃 歌词文件 → Documents/Lyrics/</div>
      <div class="privacy-item">📊 播放记录 → CoreData 数据库</div>
      <div class="privacy-item">⚙️ 设置偏好 → UserDefaults</div>
    </div>
    <div class="thick-div"></div>
    <div class="privacy-section">
      <div class="privacy-title">数据安全</div>
      <div class="privacy-item">🔒 使用 iOS 沙盒机制保护数据</div>
      <div class="privacy-item">🔒 您的数据完全受您控制</div>
    </div>
    <div style="padding:14px"><button class="btn btns" style="width:100%">查看完整隐私政策</button></div>"""))

# ─── ASSEMBLE ─────────────────────────────────────────────────────────────────

SECTIONS = [
    ("🚀 引导与启动", pages[0:3]),
    ("🎵 音乐库", pages[3:10]),
    ("▶️ 播放器", pages[10:13]),
    ("📋 歌单管理", pages[13:17]),
    ("📥 导入与传输", pages[17:20]),
    ("🔍 搜索", pages[20:22]),
    ("⚙️ 批量与操作", pages[22:24]),
    ("⏱ 定时与速度", pages[24:26]),
    ("⚙️ 设置", pages[26:29]),
    ("📭 空状态", pages[29:33]),
    ("💬 弹窗与错误", pages[33:41]),
]

body_parts = []
for title, phones in SECTIONS:
    body_parts.append(f'<div class="sec-title">{title}</div>')
    body_parts.append('<div class="grid">')
    body_parts.extend(phones)
    body_parts.append('</div>')

full_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>本地音乐播放器 - 产品原型 v1.0</title>
<style>{CSS}</style>
</head>
<body>
<div class="page-hdr">
  <h1>🎵 本地音乐播放器 — 产品原型骨架</h1>
  <p>v1.0 · iOS · 共 41 个页面全部平铺 · 基于需求文档 v4.4</p>
</div>
{''.join(body_parts)}
</body>
</html>"""

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(full_html)

print(f"Done! Written to {OUT}")
print(f"File size: {len(full_html)} bytes")
