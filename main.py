#xt2640_data_logger.py
#Use: Run this script on a raspberry pi connected via LAN to Xitron xt2640 power analyzer
#extends the capabilities of the built in logging system

#imports
import time
import socket

#user variables
xitron_ip_list = ["192.168.99.245"]
xitron_port_list = [10733]


def send_scpi_command(ip_address, port, command):

    # debug prints
    #print(f"Making connection to {ip_address} at port {port} with command {command}")
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Connect to the specified IP address and port
        s.connect((ip_address, port))
        s.settimeout(10)
        
        # Send the SCPI command
        s.sendall(command.encode())
        
        # Receive the response (assuming it's not too large)
        response = s.recv(1024).decode()
        
        # Print and return the response
        #print("Response:", response)
        return response

        
    finally:
        # Close the socket
        s.close()

        # let the socket actually close
        time.sleep(0.05)

#function for getting pa data via serial comms
def log_pa_response(xitron_ip,xitron_port,measurement_number,query_string,log_file):
    #get measurement date
    date_string = send_scpi_command(xitron_ip, xitron_port, "DATE?\n").removesuffix('\r\n')

    #get measurement time
    time_string = send_scpi_command(xitron_ip,xitron_port,"TIME?\n").removesuffix('\r\n')

    #get measurement values
    measurement_string = send_scpi_command(xitron_ip, xitron_port, query_string)


    #build log string
    log_string=str(measurement_number)+','+date_string+','+time_string+','+measurement_string
    f=open(log_file,"a")
    f.write(log_string)
    f.close()

#get inputs from user
duration_int=int(input("Enter test duration in seconds: "))
delay_int=int(input("Enter delay period before test start in seconds: "))
log_file_name=input("Enter name of log file: ")


#get query string from file
f=open('query-string.txt','r')
query_string=f.readline()
f.close()
print(f'Found query string {query_string}')

#set up log file
f=open(log_file_name,'w')
f.write("SAMPLE NUM,DATE,TIME,")
f.write(query_string.removeprefix('READ?,'))
f.close()

#wait for delay time
for x in range(delay_int):
    print(str(delay_int-x)+" seconds till test start")
    time.sleep(1)

#main logging loop
for x in range(duration_int):

    #log time before getting data and writing file
    start_time=time.time()

    #write data to log
    for analyzer_num in range(len(xitron_ip_list)):
        log_pa_response(xitron_ip_list[analyzer_num],xitron_port_list[analyzer_num],x+1,query_string,log_file_name)
        print(f'logged point {x+1} out of {duration_int} from analyzer at {xitron_ip_list[analyzer_num]}')
    

    #wait till 1 second elapses before getting next measurement
    while(time.time()-start_time<1):
        pass