#!/usr/bin/env python
# coding: utf-8

# In[1]:


import socket

def port_scan(ip, start_port, end_port):
    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            # Create a socket object
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Set timeout to 1 second
            s.settimeout(1)
            # Attempt to connect to the port
            s.connect((ip, port))
            # If connection successful, mark the port as open
            open_ports.append(port)
            # Close the socket
            s.close()
        except (socket.timeout, ConnectionRefusedError):
            # If connection timed out or refused, port is closed
            pass

    return open_ports

def main():
    ip = input("Enter IP address: ")
    start_port = int(input("Enter starting port: "))
    end_port = int(input("Enter ending port: "))

    open_ports = port_scan(ip, start_port, end_port)

    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(port)
    else:
        print("No open ports found.")

if __name__ == "__main__":
    main()


# In[ ]:




