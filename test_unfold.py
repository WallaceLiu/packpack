# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 14:10:40 2017

@author: liuning11
"""
from load import load
import unfold
import printer


def DoTest():

    l = load()
    l.load()
    g = unfold.unfold(l.goods)
    printer.goods(g)


if __name__ == '__main__':
    DoTest()
