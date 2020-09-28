import socket 

ip = ''
# I have hidden my Ip Address here but you can add your own IP to check your ports.
port_list = [20, 80, 8080, 139, 445, 21 ,22]


for port in port_list:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((ip,port))
	
        if result == 0:
                print ('-' * 60)
                print ('port:',port,'open')
                print ('-' * 60)
		
        else:
                print ('-' * 60)
                print ('port:' , port, 'closed')
                print ('-' * 60)
