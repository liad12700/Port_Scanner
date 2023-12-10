import socket

def port_scanner(target, start, end):
    for i in range(start, end):
        client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        res= client.connect_ex((target, i))
        if res==0:
            print(str(i)+" OPEN")
        else:
            print(str(i)+"Is Close")



port_scanner(input("Write the target "),int(input("Write the start port ")),int(input("Write the end port ")))        