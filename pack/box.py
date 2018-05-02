# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 14:10:40 2017

@author: liuning800202@gmail.com
"""
from pack.base import Base
from pack.goods import Goods


class Box(Base):
    """
    Box class
    """

    def __init__(self, id, width, depth, height, cost, volume, goodsCollect):
        """

        :param id:
        :param width:
        :param depth:
        :param height:
        :param cost:
        :param volume:
        :param goodsCollect:
        """
        Base.__init__(self, id, width, depth, height)

        self.cost = cost
        self.volume = volume
        self.parent = None
        self.boxLeft = None
        self.boxRight = None
        self.goodsCollect = [g for g in goodsCollect]

    def isSplit(self):
        """
        if or not need split
        :return:
        """
        cost = 0
        vol = 0
        idx = 0
        for g in self.goodsCollect:
            if (cost + g.price > self.cost or vol + g.space.volume > self.volume):
                return idx
            else:
                cost += g.price
                vol += g.space.volume

            idx += 1

        return -1 if (idx >= len(self.goodsCollect)) else idx

    def splitBox(self, idx):
        """
        split box, from one to two
        :return:
        :param idx:
        :return:
        """
        bx_left = Box(self.id - 1, self.space.wdh[0], self.space.wdh[1], self.space.wdh[2], self.cost, self.volume,
                      self.goodsCollect[:idx])
        bx_left.parent = self

        bx_right = Box(self.id + 1, self.space.wdh[0], self.space.wdh[1], self.space.wdh[2], self.cost, self.volume,
                       self.goodsCollect[-1 * (len(self.goodsCollect) - idx):])
        bx_right.parent = self

        self.boxLeft = bx_left
        self.boxRight = bx_right

        self.goodsCollect = []

        print('\t\tCreate New Box...ID=%d' % (bx_left.id))
        Goods.printCollect(bx_left.goodsCollect)
        print('\t\tCreate New Box...ID=%d' % (bx_right.id))
        Goods.printCollect(bx_right.goodsCollect)

    def print(self):
        def __print(box):
            if (box.boxLeft == None and box.boxRight == None):
                print('ID=%d' % (box.id))
                Goods.printCollect(box.goodsCollect)

            if (box.boxLeft != None):
                __print(box.boxLeft)
            if (box.boxRight != None):
                __print(box.boxRight)

        print('\n=============================================================')
        print('Box INFO:')
        print('-------------------------------------------------------------')
        if (self.boxLeft == None and self.boxRight == None):
            print('ID=%d\tWDH=%s\tCOST=%d\tVOL=%d' % (self.id, self.space.wdh, self.cost, self.volume))
            Goods.printCollect(self.goodsCollect)

        if (self.boxLeft != None):
            __print(self.boxLeft)
        if (self.boxRight != None):
            __print(self.boxRight)

        print('=============================================================')

    @staticmethod
    def create(width, depth, height, cost, volume, goodsCollect):
        """
        init create the root of box
        :param width:
        :param depth:
        :param height:
        :param cost:
        :param volume:
        :param goodsCollect:
        :return:
        """
        root = Box(1000, width, depth, height, cost, volume, goodsCollect)
        return root
