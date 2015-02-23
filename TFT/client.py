from twisted.internet import protocol
from twisted.internet import reactor
from kivy.app import App

class FileClient(protocol.Protocol):
    def connectionMade(self):
        print "connected"
        self.factory.sender = self

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


class Client(App):
    def __init__(self, port=8000, host="localhost"):
        self.factory = FileFactory()
        self.factory.protocol = FileClient
        self.port = port
        self.host = host
        self.connection = None

    def connect(self):
        reactor.connectTCP(self.host, self.port, self.factory)

    def sendFile(self, file):
        self.connection.sendFile(file)

    def on_connection(self, connection):
        self.connection = connection