import pandas as pd
import os

print("Start Loading Spamhaus Static blacklist (Static Rules)...")

# Reading drop_v4.csv
try:
    df = pd.read_csv('drop_v4.csv')
    
    # Change it to list
    bad_ips = df.iloc[:, 0].dropna().tolist() 
    
    print(f"Read {len(bad_ips)} rows of IP address successfully. Ready to write in Firewall...")
except Exception as e:
    print(f"Fail to read CSV: {e}")
    exit()

# Confirm blacklist is built
os.system("sudo ipset create blacklist hash:net -exist")

#  Add IP to blacklist
count = 0
for ip in bad_ips:
    #  Ignore non IP format data
    if isinstance(ip, str) and ('.' in ip or ':' in ip):
        command = f"sudo ipset add blacklist {ip} -exist"
        os.system(command + " > /dev/null 2>&1")
        count += 1
        if count % 100 == 0:
            print(f"Total: {count} ...")

print(f"Finish！Total {count} static rules in iptables blacklist")
