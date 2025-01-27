# portScanner
A simple port scanner that returns if the requested port on the host is open/closed and which service its running

This python script takes input from the user and will use the input to scan the host and all ports between 2 numbers. The inputs for this script are 
1) Host address to scan
2) What port to start on
3) What port to end on

Functions in the application
1) main - This functions accepts 3 inputs from the user which are the host IP, startport and endPort which are defined in the port_scan function. This function starts the port_Scan function.
2) port_scan - This function accepts 3 parameters, host, startPort, and endPort. This function will start by informating the user that it is scanning from the inputted host from the starting port number given and ending at the last port number given. It will then use a for loop to create a socket connection to each port through the given host. It will then print if the port is open and what the service it is using is if it is open.
   **host** - An IP address for the host that is to be scanned
  **startPort** - The starting port number
   **endPort** - The ending Port number
3) printServiceName - This functions takes 1 parameter which is the port number that is currently being scanned. This function will print the name of the service that is being ran, if it is not using TCP or UDP it will print out that the port does not use TCP or UDP
   **port** - The port that is being scanned
