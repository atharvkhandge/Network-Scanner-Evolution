# Network Scanner Project

A three-tier evolution of a network reconnaissance tool built with Python, moving from basic connectivity checks to professional-grade scanning.

### 📜 Versions Overview

* **Version 1 (Basic Scanner):** Focuses on core socket programming using a single-threaded loop to identify open ports via TCP handshakes.
* **Version 2 (Optimization & Banners):** Enhances performance using `ThreadPoolExecutor` for multithreading and implements banner grabbing to identify running services.
* **Version 3 (Professional Tool):** Features a polished CLI with structured table outputs, custom port ranges, and robust error handling.

---

### 🚀 Getting Started

1. **Prerequisites**: Python 3.x installed. 
2. **Installation**: Clone this repository.
3. **Execution**: Run the script from your terminal:
   ```bash
   python scanner_v1.py
