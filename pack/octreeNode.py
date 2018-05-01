# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 15:48:18 2017

@author: liuning11
"""
from pack.box import Box
from pack.base import Space


class OctreeNode:
    def __init__(self,
                 data=None,
                 blf=None,
                 blb=None,
                 brb=None,
                 brf=None,
                 tlf=None,
                 tlb=None,
                 trb=None,
                 trf=None,
                 parent=None,
                 direct=-1,
                 tag=-1):
        self.data = data  #节点数据 width, depth, height
        #self.isSeparated = False

        self.space = None  #self.__initSize()

        self.tag = tag

        # 八叉树和方向
        self.dir = direct

        self.bottom_left_front = blf
        self.bottom_left_back = blb
        self.bottom_right_back = brb
        self.bottom_right_front = brf

        self.top_left_front = tlf
        self.top_left_back = tlb
        self.top_right_back = trb
        self.top_right_front = trf

        self.parent = parent

    def getvertex(self):
        v = []
        v.append({
            "name": 'bottom_left_front',
            "x": self.xmin,
            "y": self.ymin,
            "z": self.zmin
        })
        v.append({
            "name": 'bottom_left_back',
            "x": self.xmin,
            "y": self.ymax,
            "z": self.zmin
        })
        v.append({
            "name": 'bottom_right_back',
            "x": self.xmax,
            "y": self.ymax,
            "z": self.zmin
        })
        v.append({
            "name": 'bottom_right_front',
            "x": self.xmax,
            "y": self.ymin,
            "z": self.zmin
        })
        v.append({
            "name": 'top_left_front',
            "x": self.xmin,
            "y": self.ymin,
            "z": self.zmax
        })
        v.append({
            "name": 'top_left_back',
            "x": self.xmin,
            "y": self.ymax,
            "z": self.zmax
        })
        v.append({
            "name": 'top_right_front',
            "x": self.xmax,
            "y": self.ymax,
            "z": self.zmax
        })
        v.append({
            "name": 'top_right_back',
            "x": self.xmax,
            "y": self.ymin,
            "z": self.zmax
        })

        return v
