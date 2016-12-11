import urllib
#import socket

#mySocket = socket.socket()
#mySocket.connect('http://www.pythonlearn.com/code/intro-short.txt')

#mySocket.close()

fileHandler = urllib.urlopen('http://www.pythonlearn.com/code/intro-short.txt')
print fileHandler.info()
#for line in fileHandler:
#    print line.strip()