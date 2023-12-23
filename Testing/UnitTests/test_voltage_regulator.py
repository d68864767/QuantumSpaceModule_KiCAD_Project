```python
import unittest
from voltage_regulator import read_voltage

class TestVoltageRegulator(unittest.TestCase):
    def setUp(self):
        self.expected_voltage = 5.0  # Expected voltage output
        self.tolerance = 0.1  # Allowable tolerance

    def test_voltage_regulator(self):
        voltage = read_voltage()
        self.assertTrue((self.expected_voltage - self.tolerance) <= voltage <= (self.expected_voltage + self.tolerance),
                        f"Voltage out of range: {voltage}V. Expected around {self.expected_voltage}V.")

if __name__ == '__main__':
    unittest.main()
```
