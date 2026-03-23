import joblib
import pandas as pd
from scapy.all import sniff, IP, conf, L3RawSocket

# 1. FORCE MAC TO USE L3 SOCKET GLOBALLY
conf.L3socket = L3RawSocket

# Load the trained AI
try:
    model = joblib.load('sniffer_model.pkl')
    print("--- AI Model Loaded Successfully ---")
except:
    print("Error: Run train_ai.py first!")
    exit()

def analyze_packet(packet):
    # This print is our 'heartbeat' - if you see this, the sniffer IS working
    print("Analyzing live packet...") 
    
    if packet.haslayer(IP):
        pkt_size = len(packet)
        pkt_proto = packet[IP].proto
        current_data = pd.DataFrame([[pkt_size, pkt_proto]], columns=['len', 'proto'])
        prediction = model.predict(current_data)
        
        if prediction[0] == -1:
            print(f"[!!! AI ALERT !!!] Anomaly: {packet[IP].src} | Size: {pkt_size}")
        else:
            print(f"[OK] Traffic from {packet[IP].src}")

if __name__ == "__main__":
    print("--- Capturing Live Traffic ---")
    # Cleanest possible sniff call for macOS
    sniff(prn=analyze_packet, store=0)