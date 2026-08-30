import unittest
from separation_dynamics import host_recoil, internal_move, tangential_impulse

class CoreTests(unittest.TestCase):
    def test_momentum_recoil(self):
        self.assertAlmostEqual(host_recoil(10, 2, 1000), 0.02)
    def test_closed_internal_move_has_no_ideal_residual_rate(self):
        self.assertEqual(internal_move(2, 1, 2, .5, 10)["residual_body_rate_deg_s"], 0)
    def test_prograde_impulse_raises_apogee(self):
        result=tangential_impulse(500_000,10)
        self.assertGreater(result["apogee_altitude_m"],result["perigee_altitude_m"])

if __name__ == "__main__": unittest.main()
