#!/usr/bin/env python
# encoding: utf-8
"""
nodes.py

Created by Henry Herman on 2011-05-25.
Copyright (c) 2011 UCLA. All rights reserved.
"""

import sys
import os
import unittest
import numpy as np
from utils.units import meter2cm

class Nodes(object):
    def __init__(self, nodes =[]):
        self.nodes=dict()
        for node in nodes:
            self.nodes[node.id] = node
        
    def add(self, node):
        if node.id in self.nodes.keys():
            return
        self.nodes[node.id] = node
        
    def __getitem__(self, key):
        key =int(key)
        return self.nodes[key]

    def get(self,key, d=None):
        key =int(key)
        return self.nodes.get(key,d)
    def __repr__(self):
        return "<Nodes(count=%d)>" % len(self.nodes)

    def __str__(self):
        return self.__repr__()    

    def getExtents(self):
        xs = np.array([n.xpos_cm for n in self.nodes.values()])
        ys = np.array([n.ypos_cm for n in self.nodes.values()])
        zs = np.array([n.zpos_cm for n in self.nodes.values()])
        
        xmax = np.max(xs)
        ymax = np.max(ys)
        zmax = np.max(zs)
        xmin = np.min(xs)
        ymin = np.min(ys)
        zmin = np.min(zs)
        
        return ((xmax,xmin),(ymax,ymin),(zmax,zmin))
            
    extents = property(getExtents)

        

class Node(object):
    ID = 0
    def __init__(self, nodeid, xpos=0, ypos=0, zpos=0):
        self.xpos =float(xpos)
        self.ypos =float(ypos)
        self.zpos =float(zpos)
        self.id = int(nodeid)
        
    def setPos(x,y,z):
        self.xpos = x
        self.ypos = y
        self.zpos = z    
        
    def getxpos_cm(self):
        return meter2cm(self.xpos)

    def getypos_cm(self):
        return meter2cm(self.ypos)

    def getzpos_cm(self):
        return meter2cm(self.zpos)

    def getPos(self):
        return (self.xpos_cm, self.ypos_cm, self.zpos_cm)


    def distanceFromPos(self,xpos, ypos, zpos, incm=True):
        if incm is True:
            myxpos = self.xpos_cm
            myypos = self.ypos_cm
            myzpos = self.zpos_cm
        else:
            myxpos = self.xpos
            myypos = self.ypos
            myzpos = self.zpos

        return np.sqrt( np.square(myxpos-xpos) + 
                        np.square(myypos-ypos) + 
                        np.square(myzpos-zpos) )    
        
    
    def distanceFromNode(self, node):
        return self.distanceFromPos(node.xpos_cm, node.ypos_cm, node.zpos_cm)

    def __repr__(self):
        return "<Node(id=%d)>" % self.id

    def __str__(self):
        return self.__repr__()
        
    xpos_cm = property(getxpos_cm)
    ypos_cm = property(getypos_cm)
    zpos_cm = property(getzpos_cm)
    pos = property(getPos)

class NodesTests(unittest.TestCase):
    def setUp(self):
        node = Node(1)
        nodes = Nodes([node])

if __name__ == '__main__':
    unittest.main()
