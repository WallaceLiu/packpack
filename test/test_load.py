# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 14:10:40 2017

@author: liuning11
"""
from pack.load import load
import unittest


class TestLoad(unittest.TestCase):
    def test(self):
        l = load('g.csv')
        l.load()
