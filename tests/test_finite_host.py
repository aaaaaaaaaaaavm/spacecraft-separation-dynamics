import math
import unittest
from separation_dynamics import host_recoil


class FiniteHostTests(unittest.TestCase):
    def test_equal_masses_split_relative_velocity(self):
        self.assertEqual(host_recoil(10, 2, 10), 1)

    def test_momentum_and_relative_velocity_across_mass_ratios(self):
        for payload in (1, 4, 100):
            for host in (1, 500, 10000):
                for relative in (-16, 0, 3):
                    recoil = math.copysign(host_recoil(payload, relative, host), relative)
                    payload_dv = relative - recoil
                    self.assertAlmostEqual(payload * payload_dv - host * recoil, 0, places=9)
                    self.assertAlmostEqual(payload_dv + recoil, relative)

    def test_invalid_inputs(self):
        for args in ((0, 2, 10), (1, 2, 0), (1, math.nan, 10)):
            with self.assertRaises(ValueError):
                host_recoil(*args)
