from scapy.all import *
import base64, random, time


real_flag = "f{totally_real_flag_123}"

secret_nums = [
    0x51, 0x4C, 0x5A, 0x52, 0x44, 0x44, 0x56, 0x50,
    0x52, 0x68, 0x76, 0x74, 0x7C, 0x59, 0x58, 0x40,
    0x5B, 0x52, 0x53, 0x50, 0x52, 0x53, 0x4A
]

junk1 = [0x10,0x20,0x30]
junk2 = [0x45,0x46,0x47,0x48]

def build_flag(nums):
    return "".join(chr(x ^ 0x37) for x in nums)


flag_plain = build_flag(secret_nums)
flag_b64 = base64.b64encode(flag_plain.encode()).decode()

decoys = [
    "hello from UDP",
    "this is just noise",
    "definitely not the flag",
    "maybe another protocol?",
    "hint: TCP might be useful",
    "still not the right packet"
]

for i in range(25): 
    msg = random.choice(decoys)
    pkt = IP(dst="127.0.0.1")/UDP(dport=12345)/msg
    send(pkt, verbose=False)
    time.sleep(0.05)

tcp_payload = flag_b64.encode()
pkt = IP(dst="127.0.0.1")/TCP(dport=9090, sport=2345, flags="PA")/tcp_payload
send(pkt, verbose=False)

print("Packets sent! Capture with Wireshark (localhost).")
