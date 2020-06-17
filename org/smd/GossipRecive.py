'''
Created on Sep 23, 2013

@author: Dilip
Gossip Protocol Implemented With ZeroMq 
Bind ROUTER socket to tcp://*:<Port>
'''

from multiprocessing import Process

import zmq

PORT = ":5556"


class GossipRecive(Process):

    # Create a Req Socket With The given IPAddress, Perform The Send
    # Operation And Close The Req Socket.
    def run(self):

        # Create a Context
        context = zmq.Context()

        # Create a Reply Socket
        reply = context.socket(zmq.ROUTER)

        receive_connection = "tcp://*"
        receive_connection = receive_connection + PORT
        reply.bind(receive_connection)

        try:
            while True:
                # Receive The Output.
                output_msg = reply.recv()
                print
                output_msg

            # reply.send("ACK From GAMMA")

        except TypeError as err:
            print(str(err))

        finally:
            reply.close()
