import sys
import argparse
from subprocess import Popen, PIPE
import bluetooth
from PyOBEX.client import Client
from PyQt5.QtWidgets import QFileDialog, QApplication
from PyQt5 import QtWidgets

# my default bluetooth MAC address
default_addr = 'F4:F5:24:B2:D9:7D'

def select_files():
	# Qt GUI to select files to share
	qtapp = QApplication(sys.argv)
	qtwgt = QtWidgets.QWidget()
	filenames, _ = QFileDialog.getOpenFileNames(qtwgt)
	return filenames


def share_files(filenames, client):
	# share all files with client
	for filename in filenames:
		with open(filename, "rb") as f:
			client.put(filename.split('/')[-1], f.read())


def get_service(addr):
	# find the service and its port which allows file transfer
	service = bluetooth.find_service(name='OBEX Object Push', address=addr)
	if not len(service):
		print("No service found.")
		sys.exit(0)
	return service[0]


def get_client(service):
	# connect to service by making PyOBEX client
	print("Connecting to {} on {}.".format(service['name'], service['host']))
	client = Client(service['host'], service['port'])
	return client


def sharer(addr):
	"""
	bluetooth file sharing activity 
	"""
	service = get_service(addr)
	client = get_client(service)
	client.connect()
	filenames = select_files()
	share_files(filenames, client)
	client.disconnect()


def main():
	parser = argparse.ArgumentParser(description = "A simple bluetooth file sharer!")
 
	parser.add_argument("-a", "--addr", type = str, nargs = 1,
						metavar = "address", default = None,
						help = "Connect to bluetooth device with specified Bluetooth address.")
	 
	parser.add_argument("-l", "--list", action='store_true',
						help = "Shows all the bluetooth devices identified by your device.")
	 
 
	args = parser.parse_args()

	if args.list:
		p = Popen(["bt-device", "-l"], stdout=PIPE)
		print(str(p.stdout.read(), encoding="utf8"))
	elif args.addr != None:
		sharer(args.addr[0])
	else:
		sharer(default_addr)


if __name__=="__main__":
	main()