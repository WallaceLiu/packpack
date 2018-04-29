# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 14:10:40 2017

@author: liuning11
"""
import copy
from base import base, space


class box(base):
    """商品
    """

    def __init__(self, id, width, depth, height):
        """
        
        """
        base.__init__(self, id, width, depth, height)
        self.goods = []
        self.isFull = False
        self.costed = 0
        self.volUsed = 0

    def addGoods(self, g):
        self.goodses.append(g)

    def clone(self):
        return copy.copy(self)


class boxTree:
    """商品
    """

    def __init__(self, width=0, depth=0, height=0, cnt=0, cardinal=1):
        """
        参数
            p   价值
            w   长
            d   宽
            h   高
        """
        self.id = 'ROOT'
        self.cardinal = cardinal
        self.boxes = []
        self.__initBox__(width, depth, height, cnt, self.cardinal)

    def __initBox__(self, width, depth, height, cnt, cardinal):
        for c in range(1, cnt):
            bx = box(id='', width=width, depth=depth, height=height)
            #bx.space.partition(cardinal, width, depth, height)
            bx.id = c
            self.boxes.append(bx)

    def findFstBoxAvailable(self):
        for b in self.boxes:
            if b.isFull == False:
                return b
