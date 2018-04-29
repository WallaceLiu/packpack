# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 14:10:40 2017

@author: liuning11
"""
from goods import goods


class load:
    def __init__(self, file):
        self.__file = file
        self.goods = []
        self.volume = 0
        self.cardinal = 999999999

    def load(self):
        self.goods.clear()

        f = open(self.__file)
        id = 1
        line = f.readline()

        while line:
            prefx = line[0:1]
            attr = line.split('\t')

            if prefx is not '#' and len(attr) == 4:
                g = goods(
                    id=str(id),
                    price=int(attr[0]),
                    width=int(attr[1]),
                    depth=int(attr[2]),
                    height=int(attr[3]))
                self.goods.append(g)

                id = id + 1
                self.volume = self.volume + g.space.volume
                if self.cardinal > min(g.space.wdh):
                    self.cardinal = min(g.space.wdh)

            line = f.readline()

        f.close()
