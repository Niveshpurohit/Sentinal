import csv
import os
from scapy.all import sniff, IP

# Define the file name
FILE_NAME = 'network_data.csv'

# Create the file and add headers if it doesn't exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['len', 'proto'])

def log_packet(packet):
    if packet.haslayer(IP):
        len = len(packet)
        proto = packet[IP].proto
        
        # Save to CSV
        with open(FILE_NAME, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([len, proto])
        
        print(f"Logged: Len={len}, Proto={proto}")

def main():
    print(f"--- Data Logger Started: Saving to {FILE_NAME} ---")
    print("Go browse some websites to generate data...")
    # store=0 is important so your Mac's RAM doesn't fill up
    sniff(prn=log_packet, store=0)

if __name__ == "__main__":
    main()