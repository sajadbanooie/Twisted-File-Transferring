from TFT.server import Server
from kivy.support import install_twisted_reactor
install_twisted_reactor()
s = Server(8080)
s.listen()
s.run()