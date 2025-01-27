import socket, time
#A port scanning function that accepts 3 parameters, the host that is going to be scanned and the start/ending ports 
#The function creates a socket and a for loop that will loop the connection attempts at each port until it reaches the ending port
def port_scan(host, startPort, endPort):
    print(f"Scanning {host} from port {startPort} to {endPort}")
    start_time = time.time()

    for port in range(startPort, endPort+1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = s.connect_ex((host, port))
        if result == 0:
            print(f"Port {port}: Open - ", printSerivceName(port))
        else: 
            print(f"Port {port}: Closed - ", printSerivceName(port))
        s.close()

    end_time = time.time()
    total_time = end_time - start_time
    print(f"Scanning completed in: {total_time}")

#A function to check if the port is running via tcp/udp and if so print the name of the service that is running on that port.
def printSerivceName(port):
    try:
        print(socket.getservbyport(port, 'tcp'))
    except:
            try:
                print(socket.getservbyport(port, 'udp'))
            except:
                print(f"Port: {port} does not use TCP/UDP")

#Main function that asks for the host, starting and ending ports that the user wants scanned
def main():
    host = (input("What host do you want to scan? "))
    startPort = input("What port do you want to start with? ")
    endPort = input("What port do you want to end with? ")

    port_scan(host, int(startPort), int(endPort))

if __name__ == '__main__':
    main()
