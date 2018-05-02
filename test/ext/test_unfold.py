# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 14:10:40 2017

@author: liuning11
"""
from pack.load import load
from pack.ext.unfold import unfold
import unittest


class TestUnfold(unittest.TestCase):
    def test(self):
        l = load('goods-1.csv')
        unfold(l.load())
