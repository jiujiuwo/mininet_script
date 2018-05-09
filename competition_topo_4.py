# -*- coding: utf-8 -*-
from mininet.topo import Topo
from mininet.node import Host

class CompetitionTopo4(Topo):

	def __init__(self):
		
		Topo.__init__(self)

		switch_num = 5

		host_num = 6

		switchs = []
		hosts = []

		for s_index in range(switch_num):
			switch = self.addSwitch('S{}'.format(s_index + 1))
			switchs.append(switch)

		for h_index in range(host_num):
			host = self.addHost('H{}'.format(h_index + 1))
                        hosts.append(host)
 
		#add switchs links
		self.addLink(switchs[0],switchs[1])
		self.addLink(switchs[0],switchs[2])
		self.addLink(switchs[0],switchs[3])
		self.addLink(switchs[1],switchs[4])
		self.addLink(switchs[2],switchs[4])
		self.addLink(switchs[3],switchs[4])

		#add switch host links
		for h_index in range(host_num):
			if h_index < host_num / 2:
				self.addLink(switchs[0],hosts[h_index])
			else:
				self.addLink(switchs[4],hosts[h_index])
				
topos = {'CompetitionTopo4':(lambda:CompetitionTopo4())}
