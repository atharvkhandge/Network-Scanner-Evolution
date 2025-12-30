# Network Scanner V1: Basic Connectivity

This initial version demonstrates the fundamentals of network reconnaissance by using Python's `socket` library to perform a simple TCP port scan.
It iterates sequentially through ports, attempting a connection to each to determine if it is open based on the TCP three-way handshake.

### Features
* **Core Socket Logic:** Uses `socket.AF_INET` and `socket.SOCK_STREAM` to initiate standard TCP connections.
* **Efficient Checks:** Employs `connect_ex` to return error codes instead of raising exceptions, making the loop cleaner.
* **Timeout Control:** Includes a 0.1-second timeout per port to balance scanning speed with accuracy.
