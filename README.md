# 💻 Windows API & Memory Management PoC (Python)

## 📖 Overview
This repository contains two Proof-of-Concept (PoC) scripts demonstrating how a high-level language like Python can bypass its standard limitations to interact directly with the low-level Windows Operating System (C/C++ API). 

By utilizing Python's built-in `ctypes` library, these scripts act as a "translator," allowing direct execution of native Windows DLL functions. Understanding these mechanisms is crucial for malware analysis, endpoint detection and response (EDR) engineering, and advanced penetration testing.

## 🧠 Core Concepts Explored
* **The Language Barrier:** Bridging the gap between high-level Python and low-level C machine instructions.
* **Dynamic Link Libraries (DLLs):** Interacting directly with core Windows rulebooks, specifically `user32.dll` (User Interface) and `kernel32.dll` (Core OS/Memory).
* **Memory Allocation:** Understanding how programs request memory space from the Windows Kernel.

## 📂 Included Scripts

### 1. `win_alert.py` (User Interface Interaction)
This script demonstrates direct interaction with `user32.dll`. Instead of using a Python GUI library like Tkinter, it sends a command directly to the Windows API to execute the C-level `MessageBoxW` function, generating a native OS-level alert box.

### 2. `stealth_mem.py` (Kernel-Level Memory Allocation)
This script demonstrates how advanced software (including malware and advanced persistent threats) requests highly-privileged memory space. It interacts with `kernel32.dll` to execute the `VirtualAlloc` command. 
* It requests a block of RAM completely separated from standard application memory.
* It requests `0x40` (`PAGE_EXECUTE_READWRITE`) permissions, an advanced allocation state that allows code to be simultaneously written and executed in memory—a primary indicator monitored by modern Antivirus/EDR solutions.

## 🚀 Usage
Ensure you are running these scripts on a Windows machine, as they specifically target the Windows OS architecture. No external pip libraries are required.

Run the scripts via your terminal:
```bash
python win_alert.py
python stealth_mem.py
```

---

## ⚠️ Legal Disclaimer
> **FOR EDUCATIONAL PURPOSES ONLY.**
> 
> These scripts are designed strictly for educational environments and to demonstrate operating system architecture and memory management concepts. They do not contain weaponized code, malicious payloads, or exploit capabilities. The developer assumes no liability and is not responsible for any misuse of this information or code.
