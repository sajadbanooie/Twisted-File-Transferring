from TFT.client import Client
from kivy.support import install_twisted_reactor
c = Client(port=8080)
c.connect()
c.run()
