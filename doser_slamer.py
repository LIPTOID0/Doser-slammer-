import os
import socket
import time

# ANSI escape sequences for green color
GREEN = "\033[92m"
RESET_COLOR = "\033[0m"

def send_packets(target_ip, target_port):
    # File name for the packet file
    file_name = "poko.txt"

    while True:
        try:
            # Create a socket object inside the loop
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Connect to the target IP and port
            s.connect((target_ip, target_port))
            print(f"Connected to {target_ip}:{target_port}")

            # Read packets from the file and send them
            with open(file_name, 'r') as file:
                packets = file.readlines()
                for packet in packets:
                    try:
                        # Send the packet
                        s.sendall(packet.encode())
                        print(f"Sent: {packet.strip()}")
                        time.sleep(0.1)  # Adjust this delay as needed to meet the desired rate
                    except Exception as e:
                        print(f"An error occurred while sending packet: {e}")
                        break  # Stop sending packets if an error occurs

            # Close the connection
            s.close()

            # Pause until the connection is closed
            while True:
                try:
                    # Try to connect to check if the connection is closed
                    s.connect((target_ip, target_port))
                    s.close()
                except Exception as e:
                    print(GREEN + "No contacting maybe down" + RESET_COLOR)
                    print("Waiting to reconnect...")
                    break
                time.sleep(1)  # Check every second if the connection is still closed

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    target_ip = input("Enter target IP address: ")
    target_port = int(input("Enter target port: "))
    
    send_packets(target_ip, target_port)