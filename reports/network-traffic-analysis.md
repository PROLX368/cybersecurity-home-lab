# Network Traffic Analysis Report

## 1. Objective

Analyze locally generated HTTP traffic using Wireshark and TShark to understand network requests and identify HTTP activity.

## 2. Environment

- Operating System: Kali Linux
- Packet Analyzer: Wireshark
- Command-Line Analyzer: TShark
- HTTP Server: Python HTTP Server
- Interface: Loopback (lo)
- Target: 127.0.0.1:8000

## 3. Methodology

A local HTTP server was started on port 8000. Three HTTP GET requests were generated using curl. The traffic was captured with TShark and subsequently analyzed using Wireshark and command-line filters.

## 4. Observed Requests

| Frame | Source IP | Destination IP | Method | URI |
|---|---|---|---|---|
| 4 | 127.0.0.1 | 127.0.0.1 | GET | / |
| 16 | 127.0.0.1 | 127.0.0.1 | GET | /robots.txt |
| 28 | 127.0.0.1 | 127.0.0.1 | GET | /missing-page |

## 5. Findings

Three HTTP GET requests were identified in the packet capture.

- `/`: Request to the server's root path.
- `/robots.txt`: Request for a conventional website resource.
- `/missing-page`: Request for a path that was expected to be unavailable.

The requests were generated locally. Therefore, they do not represent evidence of an external attack.

## 6. Limitations

This experiment used loopback traffic and a small number of requests. It does not establish whether the observed activity would be malicious in a production environment.

## 7. Conclusion

The experiment demonstrated how to capture HTTP traffic and extract request metadata using Wireshark and TShark. The resulting packet capture provides a foundation for automated traffic analysis in Python.
