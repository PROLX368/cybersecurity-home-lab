import unittest
from pathlib import Path
from scapy.all import IP, TCP, wrpcap
import subprocess
import sys
import json


class TestTrafficAnalyzer(unittest.TestCase):

    def setUp(self):
        self.test_file = Path("tests/test_traffic.pcap")
        self.report_file = Path("reports/analysis-results.json")
        self.alert_file = Path("reports/security-alerts.json")

    def run_analyzer(self, packets):
        wrpcap(str(self.test_file), packets)

        result = subprocess.run(
            [
                sys.executable,
                "scripts/traffic_analyzer.py",
                "-f",
                str(self.test_file)
            ],
            capture_output=True,
            text=True
        )

        self.assertEqual(result.returncode, 0, result.stderr)

        with open(self.report_file) as file:
            return json.load(file)

    def test_port_scan_detection(self):
        packets = [
            IP(src="192.168.56.10", dst="192.168.56.20")
            / TCP(sport=45000, dport=port, flags="S")
            for port in range(20, 35)
        ]

        report = self.run_analyzer(packets)

        alert_types = [
            alert["type"] for alert in report["alerts"]
        ]

        self.assertIn("POSSIBLE_PORT_SCAN", alert_types)

    def test_normal_traffic(self):
        packets = [
            IP(src="127.0.0.1", dst="127.0.0.1")
            / TCP(sport=45000, dport=8000, flags="PA")
        ]

        report = self.run_analyzer(packets)

        self.assertEqual(report["total_packets"], 1)
        self.assertEqual(report["alerts"], [])

    def tearDown(self):
        if self.test_file.exists():
            self.test_file.unlink()


if __name__ == "__main__":
    unittest.main(verbosity=2)
