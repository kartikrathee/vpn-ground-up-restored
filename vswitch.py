#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import sys

# parse parameters
server_port = None
if len(sys.argv) != 2:
  print("Usage: python3 vswitch.py {VSWITCH_PORT}")
  sys.exit(1)
else:
  server_port = int(sys.argv[1])
server_addr = ("0.0.0.0", server_port)

# 0. create UDP socket, bind to service port
vserver_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
vserver_sock.bind(server_addr)
print(f"[VSwitch] Started at {server_addr[0]}:{server_addr[1]}")

mac_table = {}

while True:
  # 1. read ethernet frame from VPort
  data, vport_addr = vserver_sock.recvfrom(1518)

  # 2. parse ethernet frame
  eth_header = data[:14]
  #    ethernet destination hardware address (MAC)
