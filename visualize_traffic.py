import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def create_heatmap(csv_file):
    # 1. Load the data
    try:
        df = pd.read_csv(csv_file)
    except FileNotFoundError:
        print("Error: network_data.csv not found. Run the logger first!")
        return

    # 2. Set the visual style
    sns.set_theme(style="white")
    plt.figure(figsize=(10, 6))

    # 3. Create a Kernel Density Estimate (KDE) Plot
    # This acts like a heatmap for data points
    plot = sns.kdeplot(
        data=df, 
        x="len", 
        y="proto", 
        fill=True, 
        thresh=0, 
        levels=100, 
        cmap="mako"
    )

    plt.title("Network Traffic Density (AI Training Base)")
    plt.xlabel("Packet Length (Bytes)")
    plt.ylabel("Protocol Number (1=ICMP, 6=TCP, 17=UDP)")
    
    # 4. Save the plot for your GitHub README
    plt.savefig("traffic_heatmap.png")
    print("Heatmap saved as 'traffic_heatmap.png'. Open it to see your traffic patterns!")
    plt.show()

if __name__ == "__main__":
    create_heatmap('network_data.csv')