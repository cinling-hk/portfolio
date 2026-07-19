import joblib
import pandas as pd
import time
import os

# --- Local Com Public IP ---
MY_REAL_ATTACKER_IP = "49.130.132.32" 
# --------------------------------------------

# Load model
try:
    pipeline = joblib.load('RF_spam_filter_350trees.pkl')
    print("Load Pipeline Successful！")
except FileNotFoundError:
    print("Can not find RF_spam_filter_350trees.pkl, please check if it is in the folder.")
    exit()

# Reading testing flow data
try:
    test_data = pd.read_csv('traffic_sample.csv')
except FileNotFoundError:
    print("Can not find traffic_sample.csv。")
    exit()

# Define features for model
features_to_use = [
    'Dst Port', 'Protocol', 'Flow Duration', 'TotLen Fwd Pkts', 
    'Fwd Pkt Len Min', 'Bwd Pkt Len Max', 'Flow Byts/s', 'Flow Pkts/s', 
    'Fwd IAT Tot', 'Fwd PSH Flags', 'Fwd Header Len', 'Bwd Header Len', 
    'Fwd Pkts/s', 'Bwd Pkts/s', 'Pkt Len Max', 'FIN Flag Cnt', 
    'SYN Flag Cnt', 'RST Flag Cnt', 'PSH Flag Cnt', 'ACK Flag Cnt', 
    'URG Flag Cnt', 'ECE Flag Cnt', 'Down/Up Ratio', 'Bwd Seg Size Avg', 
    'Subflow Fwd Byts', 'Init Fwd Win Byts', 'Init Bwd Win Byts', 
    'Fwd Act Data Pkts', 'Fwd Seg Size Min', 'Active Max', 'Idle Max'
]

print("Start simulating real-time flow control...")
print(f"Total rows in CSV: {len(test_data)}")
print("-" * 50)

# Simulating to read every flow and predict
for i in range(len(test_data)):
    # Get feature data
    single_flow_features = test_data[features_to_use].iloc[[i]]

    # Prediction
    prediction = pipeline.predict(single_flow_features)
    
    # Forced trigger
    if i == 10: 
        prediction[0] = 1
    # ----------------------------------------------
    
    # Trigger
    if prediction[0] == 1: # Malignant
        print(f"[!] Warning！Attack detected from IP: {MY_REAL_ATTACKER_IP}！Ready to block...")
        
        # os.system call Linux command, block {MY_REAL_ATTACKER_IP} to blacklist
        block_command = f"sudo ipset add blacklist {MY_REAL_ATTACKER_IP}"
        
        # Run command and hidden system default message
        result = os.system(block_command + " > /dev/null 2>&1")
        
        if result == 0:
            print(f"    -> [Success] IP {MY_REAL_ATTACKER_IP} added to iptable blacklist successfully")
        else:
            print(f"    -> [Info] IP {MY_REAL_ATTACKER_IP} maybe in blacklist already or invalid privileges。")
    else:
        print(f"[O] Normal traffic")
    
    print("-" * 50)
    time.sleep(2) 

