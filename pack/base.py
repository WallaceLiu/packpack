# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 14:10:40 2017

@author: liuning800202@gmail.com
"""
import math


class Base:
    """商品
    """

    def __init__(self, id, width, depth, height):
        """
        """
        self.id = id
        self.space = Space(width, depth, height)


class Space:
    """商品
    """

    def __init__(self, width, depth, height):
        """
        参数
            wdh   长宽高
        """
        self.wdh = []
        self.wdh.append(width)
        self.wdh.append(depth)
        self.wdh.append(height)
        self.xmin = 0
        self.xmax = width
        self.ymin = 0
        self.ymax = depth
        self.zmin = 0
        self.zmax = height
        self.isUsed = False
        self.volume = width * depth * height  # 体积
        self.diagonal = math.sqrt(
            width * width + depth * depth + height * height)  # 对角线
        self.angle = math.sqrt(width * width + depth * depth) / self.diagonal
        self.area = 2 * width * depth + 2 * depth * height + 2 * width * height
        self.partition = []

    def setXYZ(self, xmin, xmax, ymin, ymax, zmin, zmax):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.zmin = zmin
        self.zmax = zmax

    def setWDH(self):
        self.wdh.clear()
        self.wdh.append(self.xmax - self.xmin)
        self.wdh.append(self.ymax - self.ymin)
        self.wdh.append(self.zmax - self.zmin)

    def partition(self, cardinal):
        width = self.wdh[0]
        depth = self.wdh[1]
        height = self.wdh[2]

        if width < cardinal and depth < cardinal and height < cardinal:
            self.partition.append(Space(self.wdh[0], self.wdh[1], self.wdh[2]))
        else:
            for i in range(0, int(width / cardinal)):
                sp = Space(cardinal, depth, height)
                self.partition.append(sp)

            for i in range(0, int(depth / cardinal)):
                sp = Space(width, cardinal, height)
                self.partition.append(sp)

            for i in range(0, int(height / cardinal)):
                sp = Space(width, cardinal, cardinal)
                self.partition.append(sp)
