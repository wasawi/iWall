import GameLogic
import socket, OSC

# Get controller and owner
controller = GameLogic.getCurrentController()
owner = controller.owner

ip_send = 'localhost'
host_send = 11000

client = OSC.OSCClient()
msg = OSC.OSCMessage()

## Example
#Get Cube location
x = owner.worldPosition[0]

msg.setAddress("/blender/x")
msg.append(x)
print msg

client.sendto(msg, (ip_send, host_send))
