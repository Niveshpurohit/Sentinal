# Sentinel: AI-Powered Network Intrusion Detection System

A sophisticated network security tool built with **Python** and **Scikit-Learn** that uses **Unsupervised Machine Learning** to detect anomalous traffic patterns in real-time. Unlike traditional sniffers, Sentinel "learns" your normal network behavior and flags deviations that could indicate a security threat.

---

## 🚀 Features

* **AI-Driven Detection:** Implements the **Isolation Forest** algorithm to identify zero-day threats without pre-defined signatures.
* **Live L3 Monitoring:** Optimized for **macOS (Apple Silicon/M2)** using `L3RawSocket` to bypass kernel-level packet restrictions.
* **Data Pipeline:** Automated flow from raw packet capture (`logger.py`) to model training (`train_ai.py`).
* **Visual Analysis:** Generates traffic density heatmaps to visualize network clusters and outliers.
* **Protocol Support:** Decodes and analyzes IP, TCP, UDP, and ICMP layers.

---

## 📂 Project Structure

| File | Description |
| :--- | :--- |
| `logger.py` | Captures raw network traffic and saves it to `network_data.csv`. |
| `train_ai.py` | Processes the CSV and trains the Isolation Forest ML model. |
| `sentinel.py` | The live guard that uses the trained model to flag anomalies. |
| `sniffer_model.pkl` | The serialized "brain" of the AI (generated after training). |

---

## 🛠️ Tech Stack

* **Language:** Python 3.10+
* **Machine Learning:** Scikit-Learn (Isolation Forest)
* **Network Analysis:** Scapy
* **Data Science:** Pandas, NumPy
* **Visualization:** Seaborn, Matplotlib

---

## 📋 How to Use

### 1. Installation
Clone the repository and install the dependencies:
```bash
git clone [https://github.com/Niveshpurohit/sentinel.git](https://github.com/Niveshpurohit/sentinel.git)
cd sentinel
pip3 install scapy pandas scikit-learn joblib matplotlib seaborn