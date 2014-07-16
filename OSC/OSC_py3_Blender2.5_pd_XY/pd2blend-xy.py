import GameLogic
import socket, OSC

# Get controller and owner
controller = GameLogic.getCurrentController()
owner = controller.owner

ip_dump = 'localhost'
host_dump = 12000

x = owner['x']
z = owner['z']

if not owner['connected']:
		
	owner['connected'] = True
	print("Blender Connected")
	
	GameLogic.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	GameLogic.socket.bind((ip_dump, host_dump))
	GameLogic.socket.setblocking(0)
	GameLogic.socket.settimeout(0.01)


else:
	try:
		msg = OSC.decodeOSC(GameLogic.socket.recv(1024))
		
		if msg[0] == '/back':
			x = owner.localPosition[0] - msg[2]
			owner.localPosition = [x, 0.0, 0.0]
		if msg[0] == '/forward':
			x = owner.localPosition[0] + msg[2]
			owner.localPosition = [x, 0.0, 0.0]

		if msg[0] == '/pos-X':
			x = msg[2]
			
		if msg[0] == '/pos-Y':
			z = msg[2]

		owner['x'] = x
		owner['z'] = z

		owner.localPosition = [x, 0.0, z]

	except socket.error:
		pass
