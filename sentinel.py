from scapy.all import sniff, IP, TCP, UDP, ICMP

def packet_callback(packet):
    # Check if the packet has an IP layer
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto

        # Identify Protocol Name
        proto_name = "Other"
        if proto == 6: proto_name = "TCP"
        elif proto == 17: proto_name = "UDP"
        elif proto == 1: proto_name = "ICMP"

        print(f"[{proto_name}] {src_ip} -> {dst_ip}")

        # Basic Security Logic: Detect potential "Ping Sweep"
        if packet.haslayer(ICMP):
            print(f"  [!] ALERT: ICMP (Ping) detected from {src_ip}")

def main():
    print("--- Sentinel Network Sniffer Active ---")
    print("Press Ctrl+C to stop...")
    # sniff() runs a loop capturing packets. 
    # store=0 means we don't keep them in RAM (prevents crashes).
    sniff(prn=packet_callback, store=0)

if __name__ == "__main__":
    main()