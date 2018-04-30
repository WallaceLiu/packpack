# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 14:10:40 2017

@author: liuning11
"""
from pack.load import load
from pack.unfold import unfold
import pack.printer
import unittest


class TestUnfold(unittest.TestCase):
    def test(self):
        l = load('g.csv')
        l.load()
        g = unfold(l.goods)
