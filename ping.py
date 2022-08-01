from mcstatus import JavaServer
import sys

try:
  HOST = sys.argv[sys.argv.index('-h') + 1]
except:
  HOST = '127.0.0.1'

try:
  PORT = int(sys.argv[sys.argv.index('-p') + 1])
except:
  PORT = 25565

print('Pinging server {}:{}'.format(HOST, PORT))
server = JavaServer(HOST, PORT)

# 'status' is supported by all Minecraft servers that are version 1.7 or higher.
status = server.status()
print("Players: {}".format(status.players.online))

if status.players.online > 0:
  exit(1)
