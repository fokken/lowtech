#!/usr/bin/python
# arma3 weridness
from scapy.all import *

conf.iface='eth0'

for n in range(0,100):
	strangeness = Ether()/IP(dst='46.252.6.180')/UDP(dport=2302)/fuzz(Raw())
	sendp(strangeness)

