# ⚡ Advanced Multi-Threaded Port Scanner

This repository features a high-performance **Python Port Scanner** upgraded with multithreading, progress tracking via `tqdm`, and organized table output using `prettytable`. It includes **banner grabbing** capabilities to identify services running on open ports.

### ✨ Key Features
* **Multithreading:** Uses `ThreadPoolExecutor` with 100 workers for lightning-fast scanning.
* **Visual Progress:** Real-time progress bar powered by `tqdm`.
* **Banner Grabbing:** Attempts to retrieve service information from open ports.
* **Tabular Reports:** Outputs results in a clean, professional table format.

### 🛠️ Prerequisites
Before running the script, ensure you have the required dependencies installed:
```bash
pip install tqdm prettytable
