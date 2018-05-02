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

        id = 0
        with open(self.__file, "r") as fr:
            rows = csv.DictReader(fr, dialect="packpack")
            rows_list = list(rows)
            goods = [Goods(
                    id=i + 1,
                    pseudoId=str(id),
                    price=int(rows_list[i]['p']),
                    width=int(rows_list[i]['w']),
                    depth=int(rows_list[i]['d']),
                    height=int(rows_list[i]['h'])) for i in range(len(rows_list))]

        return Goods.sort(goods)
