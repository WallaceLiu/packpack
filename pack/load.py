# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 14:10:40 2017

@author: liuning800202@gmail.com
"""
from pack.goods import Goods
import csv


class load:
    def __init__(self, file):
        self.__file = file

    def load(self):
        goods = []

        csv.register_dialect("packpack", delimiter=",")

        id = 1
        with open(self.__file, "r") as fr:
            rows = csv.DictReader(fr, dialect="packpack")
            for row in rows:
                g = Goods(
                        id=id,
                        pseudoId=str(id),
                        price=int(row['p']),
                        width=int(row['w']),
                        depth=int(row['d']),
                        height=int(row['h']))

                goods.append(g)

                id += 1

        return Goods.sort(goods)
