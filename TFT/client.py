from twisted.internet import protocol
from twisted.internet import reactor


class FileClient(protocol.Protocol):
    def connectionMade(self):
        print "connected"

    def dataReceived(self, data):
        # get the file and call fileReceived
        pass

    def fileReceived(self, file):
        pass

    def sendFile(self, file):
        # use file object to create a transport object
        print file


class FileFactory(protocol.ClientFactory):
    pass


class Client:
    def __init__(self, port=8000, host="localhost"):
        self.factory = FileFactory()
        self.factory.protocol = FileClient
        self.port = port
        self.host = host

    def connect(self):
        reactor.connectTCP(self.host, self.port, self.factory)
        self.on_connect()
        reactor.run()