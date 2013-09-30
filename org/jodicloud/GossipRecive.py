'''
Created on Sep 23, 2013

@author: Ankit Kumar Honey
Gossip Protocol Implemented With ZeroMq 
Bind ROUTER socket to tcp://*:<Port>

'''

import zmq
#import ConfigParser
from multiprocessing import Process
from GossipConnection import *

class GossipRecive(Process):

	
	# Create a Req Socket With The given IPAddress, Perform The Send 
	# Operation And Close The Req Socket.
	def run(self):
		
		# Create a Context
		context = zmq.Context()
	
		# Create a Reply Socket
		rep = context.socket(zmq.ROUTER)

		recvConnect = GossipConnection()
		recvConnection = recvConnect.getConnection(False)
		rep.bind(recvConnection)
		
		try:
			while True:
				
				# Receive The Output.
				outputMsg = rep.recv()
				print outputMsg

				# rep.send("ACK From GAMMA")

		except TypeError as err:
			print (str(err))
			
		finally:
			rep.close()
