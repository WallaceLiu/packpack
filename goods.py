# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 14:10:40 2017

@author: liuning11
"""
from base import base, space


class goods(base):
    """商品
    """

    def __init__(self, id, pseudoId='', price=0, width=0, depth=0, height=0):
        """
        参数
            p   价值
            w   长
            d   宽
            h   高
        """
        base.__init__(self, id, width, depth, height)
        self.pseudoId = pseudoId
        self.price = price
        self.isUsed = False
        self.gs = []
