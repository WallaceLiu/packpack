# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 14:10:40 2017

@author: liuning11
"""
from pack.load import load
import unittest
from pack.goods import Goods


class TestLoad(unittest.TestCase):
    def test(self):
        l = load('goods-1.csv')
        l.load()

        a = Goods.sort(l.goods)
