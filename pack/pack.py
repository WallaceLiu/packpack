# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 14:10:40 2017

@author: liuning11
"""
from goods import goods
from load import load
import unfold
import printer
from functools import reduce
from box import box, boxTree


class pack:

    __cost = 2000
    __width = 2
    __depth = 2
    __height = 3
    __volume = __width * __depth * __height

    def __init__(self, file='goods.csv'):
        l = load(file)
        l.load()
        self.goods = l.goods
        self.used = {}
        #unfold.unfold(self.goods)
        self.boxTree = boxTree(
            width=self.__width,
            depth=self.__depth,
            height=self.__height,
            cnt=len(self.goods),
            cardinal=1)

        self.createUsed(self.goods)
        self.boxed()
        #self.printer()

    def createUsed(self, gs):
        for g in gs:
            self.used[g.id] = 0

    def _haveGoods(self):
        return len(list(filter(lambda x: x == 0, self.used.values()))) > 0

    # boxed
    def boxed(self):
        s = {"volUsed": 0, "costed": 0, "goods": []}
        gs = []
        gs.append(self.goods)
        print('-------------')
        for g in gs:
            self._boxed(g, s)

    def _boxed(self, gs, s):
        for g in gs:

            isAdd = self._isAdd(g, s)

            printer.g(g)
            print("-IsAdd: %s" % (isAdd))

            if isAdd:
                self._add(g, s)
            else:
                self._pk(s)
                self._pt(s, g)
                #print(s["goods"])

            #print(s["goods"])
            haveGoods = self._haveGoods()
            print('-haveGoods: %s\n\t\t%s' % (haveGoods, self.used))
            if not haveGoods:
                self._pk(s)
                s["goods"] = []

            self._boxed(g.gs, s)

    def _isAdd(self, g, s):
        return True if g.isUsed == False and (
            s["volUsed"] + g.space.volume <= self.__volume and
            s["costed"] + g.price <= self.__cost) else False

    def _add(self, g, s):
        s["volUsed"] = s["volUsed"] + g.space.volume
        s["costed"] = s["costed"] + g.price
        s["goods"].append(g)

        g.isUsed = True
        self.used[g.id] = 1
        print("-g:%s\tVolUsed: %d\tcosted: %d" %
              (g.id, s["volUsed"], s["costed"]))

    def _pk(self, s):
        b = self.boxTree.findFstBoxAvailable()

        b.costed = s["volUsed"]
        b.volUsed = s["costed"]
        for g in s["goods"]:
            b.goods.append(g)
        b.isFull = True

        s["volUsed"] = 0
        s["costed"] = 0
        s["goods"] = []

        printer.box(b)

    def _pt(self, s, g):
        s["volUsed"] = s["volUsed"] + g.space.volume
        s["costed"] = s["costed"] + g.price
        s["goods"].append(g)
        g.isUsed = True
        self.used[g.id] = 1

    def _sort(self):
        """按体积，价值剩下排序
        """
        pass

    def printer(self):
        #printer.goods(self.goods)
        #printer.box(self.boxTree)
        printer.boxGoods(self.boxTree)


#p = pack()
