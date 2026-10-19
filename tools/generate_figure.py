from pathlib import Path
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"src"))
plt.style.use(ROOT/"tools/scientific.mplstyle")
(ROOT/"figures").mkdir(exist_ok=True)
from separation_dynamics import tangential_impulse
points=[(dv,tangential_impulse(500_000,dv)["phase_drift_deg_day"]) for dv in range(-20,21)]
fig,ax=plt.subplots(figsize=(7.1,4.1))
ax.plot([x for x,y in points],[y for x,y in points],color="#0072b2",marker="o",markevery=5,ms=3)
ax.axhline(0,color=".65",lw=.7);ax.axvline(0,color=".65",lw=.7)
ax.set_xlabel("Tangential inertial velocity increment [m/s]")
ax.set_ylabel("Phase-drift magnitude [deg/day]")
ax.set_title("Separation impulse and phase-drift magnitude",loc="left")
ax.grid(alpha=.35)
fig.text(.02,.015,"Source: separation_dynamics.tangential_impulse; circular 500 km reference.\nTwo-body orbital screen; no actual release accuracy or host recovery is established.",fontsize=8)
fig.subplots_adjust(left=.13,right=.98,bottom=.28,top=.88)
STEM="phase-drift"

for ext in ("svg","pdf","png"):
    target=ROOT/"figures"/(STEM+"."+ext)
    fig.savefig(target,bbox_inches="tight",metadata={"Creator":"Committed analytical source"} if ext!="png" else None)
    if ext=="svg": target.write_text("\n".join(line.rstrip() for line in target.read_text().splitlines())+"\n")
plt.close(fig)
