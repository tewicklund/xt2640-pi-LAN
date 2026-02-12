import socket

HOST = "192.168.99.245"
PORT = 10733

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(3)

try:
    s.connect((HOST, PORT))
    print("OPEN: connection succeeded")
except ConnectionRefusedError:
    print("CLOSED: host reachable but nothing listening on that port")
except socket.timeout:
    print("FILTERED: timed out (firewall or wrong IP)")
except Exception as e:
    print("ERROR:", e)
finally:
    s.close()
