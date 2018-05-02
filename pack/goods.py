# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 14:10:40 2017

@author: liuning800202@gmail.com
"""
from pack.base import Base


class Goods(Base):
    """商品
    """

    def __init__(self, id, pseudoId, price, width, depth, height):
        """

        :param id:
        :param pseudoId:
        :param price:
        :param width:
        :param depth:
        :param height:
        """
        Base.__init__(self, id, width, depth, height)
        self.pseudoId = pseudoId
        self.price = price
        self.gs = []

    def print(self):
        print('\tID=%d\tPRI=%d\tWDH=%s\tVOL=%d' % (self.id, self.price, self.space.wdh, self.space.volume))

    def printDetail(self):
        print('\t%s\t%s\t%d\t%s\t%d\t%d\t%d\t%d' %
              (self.id, self.pseudoId, self.price, self.space.wdh, self.space.volume,
               self.space.area, self.space.diagonal, self.space.angle))

    @staticmethod
    def printCollect(goodsCollect):
        print('\n\tgoods INFO:')
        print('\t=============================================================')
        for g in goodsCollect:
            if (isinstance(g, Goods)):
                g.print()
        print('\t=============================================================')

    @staticmethod
    def sort(goodsCollect):
        return sorted(sorted(goodsCollect, key=lambda goods: goods.space.volume), key=lambda goods: goods.price,
                      reverse=True)
