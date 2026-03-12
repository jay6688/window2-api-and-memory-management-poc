import ctypes

# 1. We hire the Translator again
kernel32 = ctypes.windll.kernel32

# 2. We set our instructions for the Hotel Manager
size = 4000              # We want a room that holds 4000 bytes
allocation_type = 0x3000 # "Reserve the room and give me the keys"
protection = 0x40        # "PAGE_EXECUTE_READWRITE" (Full invisible admin access)

print("[*] Approaching the Front Desk (kernel32.dll)...")
print("[*] Requesting a highly-privileged, invisible sector of RAM...")

# 3. The CEO orders the Manager to run the C-level VirtualAlloc command
# The '0' at the start means "We don't care which room, just pick an empty one."
memory_address = kernel32.VirtualAlloc(0, size, allocation_type, protection)

# 4. The Manager hands us back the exact Room Number (Memory Address)
print(f"[+] Success! The Manager gave us Room Number (Memory Address): {hex(memory_address)}")