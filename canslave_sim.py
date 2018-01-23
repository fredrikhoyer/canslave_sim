#!/usr/bin/env python
"""
Simple canopen slave/instrument simulator.

It takes an EDS file as argument and will answer with the
default values from this EDS file. If no default value exist
then 060A 0023 abort code (Resource not available) is returned.

The script assumes that the can interface is a linux socketCan
interface.

This scripts depends on the github project fredrikhoyer/canopen
branch canopenslave (or at least until these changes are pulled
into the canopen main project)
"""

from __future__ import print_function
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
import canopen
import time
import logging


def get_options():
    parser = ArgumentParser(description="Simple Canopen instrument simulator",
                            formatter_class=ArgumentDefaultsHelpFormatter)

    parser.add_argument("-e", "--edsFile", required=True,
                        help="The EDS file for the instrument")
    parser.add_argument("-i", "--interface", required=True,
                        help="The name of the canbus interface")
    parser.add_argument("-n", "--nodeId", type=int, required=True,
                        help="The canopen node id")

    return parser.parse_args()


def main():
    args = get_options()

    logging.basicConfig(level=logging.INFO)

    network = canopen.Network()
    network.connect(bustype='socketcan', channel=args.interface)
    can_slave = network.create_node(args.nodeId, args.edsFile)

    # Finished with initialization so set to pre-opertaional state
    can_slave.nmt.state = 'PRE-OPERATIONAL'

    print("Canopen Slave with id %s has started and is connected to %s" %
          (can_slave.id, args.interface))
    print("-----Terminate by pressing ctrl+c-----")

    try:
        while True:
            time.sleep(50.0/1000.0)
            pass

    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
