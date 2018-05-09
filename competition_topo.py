# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mininet.topo import Topo

class CompetitionTopo(Topo):
    
    def __init__(self):
        
        Topo.__init__(self)
        
        switch_num = 3
        
        host_num = 4
        
        switchs = []
        hosts = []
        
        for s_index in range(switch_num):
            switch = self.addSwitch('S{}'.format(s_index + 1))
            switchs.append(switch)
            
        for s_link_index in range(switch_num):
            self.addLink(switchs[s_link_index],switchs[s_link_index + 1
                         if s_link_index + 1 < switch_num else 0 ])
    
        for h_index in range(host_num):
            host = self.addHost('H{}'.format(h_index + 1))
            hosts.append(host)
        self.addLink(switchs[0],hosts[0])
        self.addLink(switchs[1],hosts[1])
        self.addLink(switchs[2],hosts[2])
        self.addLink(switchs[2],hosts[3])

topos = {'competition':(lambda:CompetitionTopo())}