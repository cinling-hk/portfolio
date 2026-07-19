import socket
import time

def simulate_botnet_probe(target_ip, target_port=25, num_probes=1000):
    print(f"Start {target_ip}:{target_port} Similating Botnet detection...")
    for i in range(num_probes):
        try:
            # Build a basic TCP Socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            # Try to connect
            s.connect((target_ip, target_port))
            # Connection sucess, do not send any L7 data, close connection
            s.close()
            print(f"[{i}] attack package sent!")
        except Exception as e:
            print(f"[{i}] Connection fail (maybe blocked): {e}") 
        # short intervals, simulating high-frequency scanning
        time.sleep(0.1) 

simulate_botnet_probe('16.162.188.119', target_port=25, num_probes=1000)

