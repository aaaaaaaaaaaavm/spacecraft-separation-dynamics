from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"src"))
from separation_dynamics import tangential_impulse
points=[(dv,tangential_impulse(500_000,dv)["phase_drift_deg_day"]) for dv in range(-20,21,2)]
w,h=900,380; left,base=70,315; ymax=max(y for _,y in points)
poly=" ".join(f"{left+(dv+20)*19:.1f},{base-y/ymax*230:.1f}" for dv,y in points)
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><rect width="100%" height="100%" fill="#07111f"/><text x="45" y="40" fill="#f7fafc" font-family="sans-serif" font-size="23" font-weight="700">Separation impulse → phase drift</text><text x="45" y="65" fill="#8ca3bd" font-family="sans-serif" font-size="13">500 km circular reference · two-body screening only</text><line x1="70" y1="315" x2="850" y2="315" stroke="#496078"/><line x1="450" y1="80" x2="450" y2="315" stroke="#496078"/><polyline points="{poly}" fill="none" stroke="#60a5fa" stroke-width="4"/><text x="720" y="350" fill="#b8c7d9" font-family="sans-serif" font-size="13">Δv (−20 to +20 m/s)</text><text x="75" y="95" fill="#b8c7d9" font-family="sans-serif" font-size="13">phase drift (deg/day)</text></svg>'''
(ROOT/"figures").mkdir(exist_ok=True)
(ROOT/"figures/phase-drift.svg").write_text(svg,encoding="utf-8")
