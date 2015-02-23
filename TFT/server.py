from twisted.internet import protocol
from twisted.internet import reactor
from kivy.app import App


class FileProtocol(protocol.Protocol):
    def dataReceived(self, data):
        # get the file and call fileReceived
        pass

    def fileReceived(self, file):
        pass

    def sendFile(self, file):
        # use file object to create a transport object
        pass

class FileFactory(protocol.Factory):
    pass


class Server(App):
    def __init__(self, port=8000):
        self.factory = FileFactory()
        self.factory.protocol = FileProtocol
        self.port = port

    def listen(self):
        reactor.listenTCP(self.port, self.factory)

