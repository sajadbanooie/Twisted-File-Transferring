from TFT.client import Client

c = Client(port=8080)
c.connect()
c.sendFile(8080)
