import os, sys
import argparse
from subprocess import Popen, PIPE
import bluetooth
from PyOBEX.client import Client
from PyQt5.QtWidgets import QFileDialog, QApplication
from PyQt5 import QtWidgets


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

	parser.add_argument("-s", "--set", type = str, nargs = 1,
						metavar = "address", default = None,
						help = "Set default Bluetooth address.")
	
	parser.add_argument("-d", "--default", action='store_true',
						help = "Shows the default bluetooth address.")

	parser.add_argument("-l", "--list", action='store_true',
						help = "Shows all the added bluetooth devices identified by your device.")
	  
	args = parser.parse_args()

	# my default bluetooth MAC address
	try:
		with open(os.path.join(os.path.dirname(__file__), 'default_addr'), "r") as f:
			default_addr = f.read()
	except FileNotFoundError:
		default_addr = ''

	if args.list:
		p = Popen(["bt-device", "-l"], stdout=PIPE)
		print(str(p.stdout.read(), encoding="utf8"))
	elif args.default:
		print("Default bluetooth address: {}".format(default_addr))
	elif args.set != None:
		print("Default bluetooth address was changed to {}".format(args.set[0]))
		with open(os.path.join(os.path.dirname(__file__), 'default_addr'), "w") as f:
			f.write(args.set[0])
	elif args.addr != None:
		sharer(args.addr[0])
	else:
		sharer(default_addr)


if __name__=="__main__":
	main()