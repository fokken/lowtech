#!/usr/bin/python
# arma3 weridness
from scapy.all import *
import sys

interface = str(sys.argv[1])
target = str(sys.argv[2])

conf.iface=interface

for n in range(0,100):
	strangeness = Ether()/IP(dst=target)/UDP(dport=2302)/fuzz(Raw())
	sendp(strangeness)

