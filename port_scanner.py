import socket   #Import the socket library to establish network connections.

def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #Create a TCP socket.
    s.settimeout(1) #Set timeout to 1 second for each connection attempt.


    try:
        s.connect((ip, port))   #Try to connect to the IP address and port.
        return True #If connection is successful, the port is open.
    except:
        return False #If connection fails, the port is closed.
    finally:
        s.close()   #Close the socket.

# Main function to scan a few ports
if __name__ == "__main__":
    ip = input("Enter IP address to scan: ")    # Get the target IP from user
    for port in range(20, 26):  # Scan ports 20 to 25
        if scan_port(ip, port):  # Call the scan_port function
            print(f"Port {port} is OPEN")   # If open, print that the port is open
        else:
            print(f"Port {port} is CLOSED") # If closed, print that the port is closed
