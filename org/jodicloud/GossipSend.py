'''
Created on Sep 23, 2013

@author: Ankit Kumar Honey
Gossip Protocol Implemented With ZeroMq 
Connect REP socket to tcp://<IP-Address>:<Port>
'''

import zmq
import time
import random	
from multiprocessing import Process
from GossipConnection import *

class GossipSend(Process):
	
	# Create a Req Socket With The given IPAddress, Perform The Send 
	# Operation And Close The Req Socket.
	def run(self):
		
	   	# Create a Context
	   	context = zmq.Context()

		reqConnect  = GossipConnection()
		port = reqConnect.getPort()
				   	
		while True:
			# Create a Request Socket
			req = context.socket(zmq.REQ)
			ipAddress = getIPAddress()
			
			reqConnection = reqConnect.getConnection(ipAddress)	
			req.connect(reqConnection)

			cmd = 'GAMMA'

			try:
				# Send a Request To Execute a Command.
				req.send(cmd)

                # Receive The Output.
                # outputMsg = req.recv()
                # print outputMsg
				time.sleep(7)

			except TypeError as err:
				print (str(err))

	  		finally:
	  			req.close()


# This function randomaly selects the ipaddress from the list.
def getIPAddress():
	ipAddressList = ["192.168.14.148", "192.168.14.127"]
	ipAddress = random.choice(ipAddressList)
	return ipAddress