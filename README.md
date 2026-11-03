<<<<<<< HEAD
# Cybersecurity Home Lab

A hands-on cybersecurity laboratory built with Kali Linux, Wireshark, TShark, and Python.

## Project Overview

This project focuses on network traffic analysis, packet inspection, and the development of automated security analysis tools.

The goal is to build practical cybersecurity skills through controlled experiments and documented investigations.
=======
# Cybersecurity Home Lab — Network Traffic Analysis

## Overview

A hands-on cybersecurity project focused on network traffic capture and analysis using Kali Linux, Wireshark, and TShark in a controlled local laboratory.

## Objectives

- Capture network traffic in a Linux environment.
- Analyze TCP and HTTP packets.
- Investigate network connections using Wireshark display filters.
- Document findings and technical observations.
- Build a foundation for Python-based threat detection.
>>>>>>> d7df62133da0f2ca05b212cc0cacd537222a35e6

## Environment

- Operating System: Kali Linux
- Virtualization: Oracle VirtualBox
<<<<<<< HEAD
- Network Analysis: Wireshark
- Packet Capture: TShark
- Programming: Python
- Version Control: Git and GitHub

## Project Structure

```text
cybersecurity-home-lab/
├── evidence/
├── reports/
├── scripts/
├── tests/
├── screenshots/
├── .gitignore
└── README.md
```

## Completed Activities

- Configured a Kali Linux cybersecurity environment.
- Captured local network traffic using TShark.
- Inspected HTTP packets using Wireshark.
- Extracted HTTP request metadata.
- Documented network traffic analysis findings.

## Planned Activities

- Develop automated traffic analysis scripts using Python.
- Identify suspicious network activity.
- Implement detection rules.
- Create automated security reports.
- Perform controlled security experiments.

## Disclaimer

All experiments are performed in a controlled laboratory environment for educational purposes.
=======
- Packet Analysis: Wireshark
- Command-Line Analysis: TShark
- Test Traffic: Local HTTP server

## Work Completed

- Created a local packet capture using TShark.
- Generated HTTP requests to a test server running on localhost.
- Saved the network capture in PCAPNG format.
- Prepared the environment for packet inspection and security analysis.

## Next Steps

- Analyze TCP and HTTP traffic.
- Export packet fields to CSV.
- Develop a Python-based detection script.
- Create automated tests and an investigation report.

## Disclaimer

All traffic is generated in a controlled laboratory environment for educational and defensive cybersecurity purposes.
>>>>>>> d7df62133da0f2ca05b212cc0cacd537222a35e6
## Automated Testing

The project includes automated tests to validate traffic analysis and security alert detection.

Current test cases:

- Port scan detection using simulated TCP SYN packets.
- Normal traffic analysis without false security alerts.

Run tests with:

```bash
python3 -m unittest discover -s tests -p "test_*.py" -v
