'''
Created on Sep 30, 2013

@author: Ankit Kumar Honey
Gossip Protocol Implemented With ZeroMq 
Connect REP socket to tcp://<IP-Address>:<Port>
'''

import sys
from GossipSend import *
from GossipRecive import *

def main():
	
	# Get the GossipSend & GossipRecive objects
	sendMsg = GossipSend()
	recvMsg = GossipRecive()

	# Start sendMsg & recvMsg processes.
	sendMsg.start()
	recvMsg.start()

	sendMsg.join()
	recvMsg.join()


# Staring Of The Main Function
if __name__ == '__main__':
	sys.exit(main())