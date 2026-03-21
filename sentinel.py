import joblib
from scapy.all import sniff, IP

# Load the trained model
try:
    model = joblib.load('sniffer_model.pkl')
    print("AI Model Loaded Successfully.")
except:
    print("No model found. Run training script first.")
    model = None

def packet_callback(packet):
    if packet.haslayer(IP) and model:
        p_len = len(packet)
        p_proto = packet[IP].proto
        
        # Predict: 1 = Normal, -1 = Anomaly
        prediction = model.predict([[p_len, p_proto]])
        
        if prediction[0] == -1:
            print(f"[!!! AI ALERT !!!] Anomaly Detected! IP: {packet[IP].src} | Size: {p_len}")
        else:
            print(f"[Normal] {packet[IP].src} -> {packet[IP].dst}")

sniff(prn=packet_callback, store=0)