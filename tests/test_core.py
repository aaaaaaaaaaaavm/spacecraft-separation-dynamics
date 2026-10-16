import unittest
from separation_dynamics import host_recoil, internal_move, tangential_impulse

class CoreTests(unittest.TestCase):
    def test_momentum_recoil(self):
        self.assertAlmostEqual(host_recoil(10, 2, 1000), 20 / 1010)
    def test_closed_internal_move_has_no_ideal_residual_rate(self):
        self.assertEqual(internal_move(2, 1, 2, .5, 10)["residual_body_rate_deg_s"], 0)
    def test_prograde_impulse_raises_apogee(self):
        result=tangential_impulse(500_000,10)
        self.assertGreater(result["apogee_altitude_m"],result["perigee_altitude_m"])

if __name__ == "__main__": unittest.main()

class DirectionReversalRegressionTests(unittest.TestCase):
    def test_reversed_velocity_orders_apses_by_radius(self):
        import math
        from separation_dynamics.core import MU_EARTH,R_EARTH
        speed=math.sqrt(MU_EARTH/(R_EARTH+500_000))
        result=tangential_impulse(500_000,-2*speed-10)
        self.assertAlmostEqual(result["perigee_altitude_m"],500_000)
        self.assertGreater(result["apogee_altitude_m"],result["perigee_altitude_m"])
