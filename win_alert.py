import ctypes

print("[*] Sending command to the Windows API...")

# The CEO (Python) tells the Translator (ctypes) to open the UI Rulebook (user32.dll)
# We ask it to run the C-level "MessageBoxW" function
ctypes.windll.user32.MessageBoxW(0, "You just executed a native C command from Python!", "Level 5 Unlocked", 0x40)

print("[*] Command executed successfully!")