# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 14:10:40 2017

@author: liuning11
"""
from pack.goods import Goods
from pack.load import load
from functools import reduce
from pack.box import Box


class ppack:
    __cost = 2000
    __width = 2
    __depth = 2
    __height = 3
    __volume = __width * __depth * __height

    def __init__(self, file):
        l = load(file)
        goods = l.load()
        self.boxRoot = \
            Box.create(width=self.__width, depth=self.__depth, height=self.__height, cost=self.__cost,
                       volume=self.__volume, goodsCollect=goods)
        self.packing()

    # boxed
    def packing(self):
        print('\nPacking...')
        print("Box ID=%d" % (self.boxRoot.id))

        self.__pack(self.boxRoot)

    def __pack(self, box):
        idx = box.isSplit()

        print("\tSpliting Box...From IDX Of Goods=%d" % (idx))
        Goods.printCollect(box.goodsCollect)

        if (idx >= 0):
            box.splitBox(idx)
            self.__packChild(box, idx)

    def __packChild(self, box, idx):
        idx_left = box.boxLeft.isSplit()
        if (idx_left >= 0):
            self.__pack(box.boxLeft)
        idx_right = box.boxRight.isSplit()
        if (idx_right >= 0):
            self.__pack(box.boxRight)
