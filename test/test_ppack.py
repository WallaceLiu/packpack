# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 14:10:40 2017

@author: liuning11
"""
import unittest
from pack.ppack import ppack


class TestPack(unittest.TestCase):
    def test(self):
        p = ppack('goods-2.csv')
        p.packing()
        print('-------------------------------------------')
        p.boxRoot.print()
