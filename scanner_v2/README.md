# 🚀 Simple Python Port Scanner

This repository features a lightweight **TCP port scanner** that uses Python's `socket` module to identify open ports (1–1024) on a target IP. It leverages the `connect_ex` method and a 0.1s timeout for efficient, exception-free scanning.

### Key Features
*  **Targeted Scanning:** Prompts for a specific IP address to audit.
*  **Resource Management:** Uses `with` statements to ensure sockets close properly.
*  **Clean Output:** Clearly identifies open ports versus closed ones.

---
