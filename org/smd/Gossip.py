'''
Created on Sep 23, 2013

@author: Dilip
Gossip Protocol Implemented With ZeroMq
Connect REP socket to tcp://<IP-Address>:<Port>
'''

import zmq
import sys
import time
import random
from multiprocessing import Process
from grecv import *


class Gsend(Process):

    # Create a Req Socket With The given IPAddress, Perform The Send
    # Operation And Close The Req Socket.
    def run(self):

        # Create a Context
        context = zmq.Context()

        while True:
            # Create a Request Socket
            req = context.socket(zmq.REQ)
            ip_address = get_ip_address()
            request_connection = get_connection(ip_address)
            req.connect(request_connection)

            cmd = 'GAMMA'

            try:
                # Send a Request To Execute a Command.
                req.send(cmd)

                # Receive The Output.
                # outputMsg = req.recv()
                # print outputMsg
                time.sleep(7)

            except TypeError as err:
                print(str(err))

            finally:
                req.close()


# This function randomly selects the ipaddress from the list.
def get_ip_address():
    ip_address_list = ["192.168.14.148", "192.168.14.127"]
    ip_address = random.choice(ip_address_list)
    return ip_address


def get_connection(ip_address):
    cmd_str = "tcp://"
    cmd_str = cmd_str + ip_address
    cmd_str = cmd_str + ":5556"
    return cmd_str


def grecv():
    return 


def main():
    # Get the Gsend & grecv objects
    send_msg = Gsend()
    recv_msg = grecv()

    # Start send_msg & recv_msg processes.
    send_msg.start()
    recv_msg.start()

    send_msg.join()
    recv_msg.join()


# Staring Of The Main Function
if __name__ == '__main__':
    sys.exit(main())
