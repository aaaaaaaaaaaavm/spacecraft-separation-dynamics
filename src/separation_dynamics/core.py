"""Transparent first-order screens; not a flight dynamics or conjunction product."""
import math

MU_EARTH = 3.986004418e14
R_EARTH = 6_378_137.0


def _positive(**values: float) -> None:
    if any(not math.isfinite(v) or v <= 0 for v in values.values()):
        raise ValueError("inputs must be finite and positive")


def host_recoil(payload_mass_kg: float, separation_speed_m_s: float, host_mass_kg: float) -> float:
    _positive(payload_mass_kg=payload_mass_kg, separation_speed_m_s=separation_speed_m_s, host_mass_kg=host_mass_kg)
    return payload_mass_kg * separation_speed_m_s / host_mass_kg


def tipoff(angular_impulse_n_m_s: float, inertia_kg_m2: float) -> float:
    _positive(angular_impulse_n_m_s=angular_impulse_n_m_s, inertia_kg_m2=inertia_kg_m2)
    return math.degrees(angular_impulse_n_m_s / inertia_kg_m2)


def tangential_impulse(altitude_m: float, delta_v_m_s: float) -> dict[str, float]:
    _positive(altitude_m=altitude_m)
    if not math.isfinite(delta_v_m_s):
        raise ValueError("delta-v must be finite")
    r = R_EARTH + altitude_m
    v0 = math.sqrt(MU_EARTH / r)
    energy = 0.5 * (v0 + delta_v_m_s) ** 2 - MU_EARTH / r
    if energy >= 0:
        raise ValueError("post-impulse path is unbound")
    a = -MU_EARTH / (2 * energy)
    other = 2 * a - r
    if other <= R_EARTH:
        raise ValueError("post-impulse path intersects Earth")
    perigee, apogee = sorted((r, other))
    drift = abs(math.sqrt(MU_EARTH / a**3) - math.sqrt(MU_EARTH / r**3)) * 86400 * 180 / math.pi
    return {"perigee_altitude_m": perigee-R_EARTH, "apogee_altitude_m": apogee-R_EARTH, "phase_drift_deg_day": drift}


def internal_move(mass_kg: float, distance_m: float, duration_s: float, lever_arm_m: float, inertia_kg_m2: float) -> dict[str, float]:
    _positive(mass_kg=mass_kg, distance_m=distance_m, duration_s=duration_s, lever_arm_m=lever_arm_m, inertia_kg_m2=inertia_kg_m2)
    peak_velocity = 2 * distance_m / duration_s
    peak_rate = mass_kg * peak_velocity * lever_arm_m / inertia_kg_m2
    offset = -mass_kg * lever_arm_m * distance_m / inertia_kg_m2
    return {"peak_body_rate_deg_s": math.degrees(peak_rate), "attitude_offset_deg": math.degrees(offset), "residual_body_rate_deg_s": 0.0}
