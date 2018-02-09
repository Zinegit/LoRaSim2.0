from network import LoRa
import socket
import time
from machine import SD
from L76GNSS import L76GNSS
from pytrack import Pytrack
import time
import pycom
from machine import Pin

# receive packet from Lopy card, write current GPS coords and LoRa stats in a file, send back a packet containing GPS coords to Lopy card and switch RGB Led color
def lora_cb(lora) :
	global fileOpen
	global toggle
	if (fileOpen) :
		recept = s.recv(64)
		stat = lora.stats()
		coord = l76.coordinates()
		
		f.write("{} ; {} ; {}\n".format(coord, stat.rssi, stat.snr))
		print("{} - {} - {}".format(coord, stat.rssi, stat.snr))
		
		# Convert GPS coords from tuple to string then send it by socket
		coordStr = str(coord)
		s.send(coordStr)

		if toggle:
			pycom.rgbled(0x007f00)
			toggle = False
		else:
			pycom.rgbled(0x7f0000)
			toggle = True

# Close file			
def pin_handler(arg):
	global fileOpen
	if (fileOpen) :
		f.close()		
		print('File closed')
		fileOpen = False
		
	
# Init LoRa and socket
lora = LoRa(mode=LoRa.LORA, tx_power = 2, sf = 7, bandwidth=LoRa.BW_500KHZ, coding_rate=LoRa.CODING_4_8, preamble=8, frequency=868000000)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)

# Init Pytrack card and GPS receiver
time.sleep(2)
py = Pytrack()
l76 = L76GNSS(py, timeout=3)

# Mount SD card and open a file on it
sd = SD()
os.mount(sd, '/sd')
f = open('/sd/gps-record.txt', 'w')
f.write('LoRa test with: tx_power = 2, sf = 7, bandwidth=LoRa.BW_500KHZ, coding_rate=LoRa.CODING_4_8, preamble=8, frequency=868000000\n')

# Send first packet to init comm on the other side
s.send('Pong')
print('Send Pong')

# Init RGB Led and global variables
pycom.heartbeat(False)
pycom.rgbled(0x7f0000)
toggle = True
fileOpen = True

# Init button for closing file purpose
p_in = Pin('P14', mode=Pin.IN, pull = Pin.PULL_UP)

# Call lora_cb function when a packet is received
lora.callback(trigger = LoRa.RX_PACKET_EVENT,  handler = lora_cb)

# Call pin_handler function when button is pressed
p_in.callback(Pin.IRQ_FALLING, pin_handler)	