#import socket

#mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#mysock.connect(('www.pythonlearn.com', 80))
#mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')
#print 5
#while True:
    #data = mysock.recv(512)
    #if ( len(data) < 1 ) :
      #  break
   # print data

#mysock.close()


#import urllib
#fhand = urllib.urlopen("http://www.pythonlearn.com/code/intro-short.txt")

#counts = dict()
#for line in fhand:
   # words = line.split()
   # for word in words:
      #  counts[word] = counts.get(word,0) + 1
#print counts


import socket

mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host='www.pythonlearn.com'
# host='www.google.com'
port=80
host_ip=socket.gethostbyname(host)
print host_ip
mysock.connect((host_ip, port))

# request='GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n'
request="GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\r\n\r\n"

mysock.send(request)

# outd = mysock.recv(1024)
# print outd

while True:
 
     outd = mysock.recv(4096)
 
     if(len(outd)<1):
 
         break
 
     print "data is",outd
 
# mysock.close()

