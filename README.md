# spacecraft-separation-dynamics

![Phase drift sweep](figures/phase-drift.svg)

Dependency-free, first-order calculations for separation impulse, host recoil, tip-off,
and a symmetric internal mass move. Each function exposes its narrow physical boundary.

```python
from separation_dynamics import host_recoil, tangential_impulse
print(host_recoil(10, 2, 1000))
print(tangential_impulse(500_000, 10))
```

Regenerate the chart with `python tools/generate_figure.py`; run tests with
`python -m unittest discover -s tests -v`.
This focused library complements the broader [VOLLEY](https://github.com/aaaaaaaaaaaavm/VOLLEY)
programme without duplicating its architecture.

## Separation convention

`host_recoil` accepts signed payload-to-host relative separation speed and returns a
non-negative recoil magnitude. `host_mass_kg` is the remaining host, excluding the payload.
For payload m and host M, recoil is `m * abs(u) / (M + m)`; payload inertial delta-v is
`M * u / (M + m)`. Their momentum changes cancel. Zero release speed gives zero recoil.
The original denominator M was an approximation when u was interpreted as relative speed.
These are instantaneous rigid-body screens without external impulse, flexible response or
controller dynamics; they do not establish safe separation.

[Scientific figures and documentation conventions](docs/FIGURE_STANDARD.md) · [Released figure sources](docs/SCIENTIFIC_FIGURES.json)

The overview figures are regenerated with `python tools/generate_figure.py`. Quantitative plots retain their committed model inputs; diagrams describe relationships and do not add validation evidence.
