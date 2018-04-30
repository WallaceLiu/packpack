# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 14:10:40 2017

@author: liuning11
"""
from goods import goods
import csv


class load:
    def __init__(self, file):
        self.__file = file
        self.goods = []
        self.volume = 0
        self.cardinal = 999999999

    def load(self):
        self.goods.clear()

        csv.register_dialect("packpack", delimiter=",")

        id = 1
        with open(self.__file, "r") as fr:
            rows = csv.DictReader(fr, dialect="packpack")
            for row in rows:
                g = goods(
                        id=str(id),
                        price=int(row['p']),
                        width=int(row['w']),
                        depth=int(row['d']),
                        height=int(row['h']))
                self.goods.append(g)

                id = id + 1
                self.volume = self.volume + g.space.volume
                if self.cardinal > min(g.space.wdh):
                    self.cardinal = min(g.space.wdh)