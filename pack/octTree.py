# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 11:49:23 2017

@author: liuning11
"""
from pack.octreeNode import OctreeNode
from pack.base import space


class Octree:
    def __init__(self, bx):
        self.root = None  #OctreeNode(bx)
        self.box = bx

    def _getOuterCube(self):
        """
        外接正方体
        """
        v = max(
            max(self.box.space.wdh[0], self.box.space.wdh[1]),
            self.box.space.wdh[2])
        edge = v if v % 2 == 0 else v + 1
        return space(edge, edge, edge)

    def create(self):
        def _isFullOrEmpty(s, bx):
            """
            满或空
            """
            bs = bx.space
            xFull = s.xmin >= bs.xmin and s.xmax <= bs.xmax
            yFull = s.ymin >= bs.ymin and s.ymax <= bs.ymax
            zFull = s.zmin >= bs.zmin and s.zmax <= bs.zmax

            isFull = xFull and yFull and zFull

            xIsEmpty = s.xmin >= bs.xmax
            yIsEmpty = s.ymin >= bs.ymax
            zIsEmpty = s.zmin >= bs.zmax

            isEmpyt = xIsEmpty or yIsEmpty or zIsEmpty

            return True if isFull or isEmpyt else False

        def _partitation(s, direction):
            """
            
            对于二维空间：(W,D)
            假设坐标,X或Y的(MIN,MAX)：
            (0,W)(0,D)
            
            平分W和D，划分成四个区域，按顺时针方向：
            R1=(0,W/2)(0,D/2)
            R2=(0,W/2)(D/2,D)
            R3=(W/2,W)(D/2,D)
            R4=(W/2,W)(0,D/2)
            
            R1接着划分:
            R11=(0,W/4)(0,D/4)
            R12=(0,W/4)(D/4,D/2)
            R13=(W/4,W/2)(D/4,D/2)
            R14=(W/4,W/2)(0,D/4)
            
            R2接着划分:
            R2=(0,W/2)(D/2,D)
            (0,w/2)->(0,w/4)(w/4,w/2)
            (d/2,d)->(d/2,3d/4)(3d/4,d)
            划分应该是，两组的排列组合
            
            可以推广到三维空间
            
            """
            xmin = s.xmin
            xmax = s.xmax
            ymin = s.ymin
            ymax = s.ymax
            zmin = s.zmin
            zmax = s.zmax

            x = (xmax - xmin) / 2
            y = (ymax - ymin) / 2
            z = (zmax - zmin) / 2

            shape = {
                "0": (xmin, xmin + x, ymin, ymin + y, zmin, zmin + z),
                "1": (xmin, xmin + x, ymin + y, ymax, zmin, zmin + z),
                "2": (xmin + x, xmax, ymin + y, ymax, zmin, zmin + z),
                "3": (xmin + x, xmax, ymin, ymin + y, zmin, zmin + z),
                "4": (xmin, xmin + x, ymin, ymin + y, zmin + z, zmax),
                "5": (xmin, xmin + x, ymin + y, ymax, zmin + z, zmax),
                "6": (xmin + x, xmax, ymin + y, ymax, zmin + z, zmax),
                "7": (xmin + x, xmax, ymin, ymin + y, zmin + z, zmax)
            }

            m = shape[str(direction)]
            s = space(m[1] - m[0], m[3] - m[2], m[5] - m[4])
            s.setXYZ(m[0], m[1], m[2], m[3], m[4], m[5])

            return s

        def _create(pt, t, direct, bx):
            if _isFullOrEmpty(pt.space, bx):
                t = OctreeNode(
                    data=None, parent=pt, direct=direct, tag=t.tag + 1)
                t.space = _partitation(pt.space, direct)
                # 底部顺时针
                t.bottom_left_front = _create(t, t.bottom_left_front, 0, bx)
                t.bottom_left_back = _create(t, t.bottom_left_back, 1, bx)
                t.bottom_right_back = _create(t, t.bottom_right_back, 2, bx)
                t.bottom_right_front = _create(t, t.bottom_right_front, 3, bx)
                # 顶部顺时针
                t.top_left_front = _create(t, t.top_left_front, 4, bx)
                t.top_left_back = _create(t, t.top_left_back, 5, bx)
                t.top_right_back = _create(t, t.top_right_back, 6, bx)
                t.top_right_front = _create(t, t.top_right_front, 7, bx)
            else:
                t = None

        self.root = OctreeNode()
        self.root.space = self._getOuterCube()
        # 底部顺时针
        self.root.bottom_left_front = _create(
            self.root, self.root.bottom_left_front, 0, self.box)
        self.root.bottom_left_back = _create(
            self.root, self.root.bottom_left_back, 1, self.box)
        self.root.bottom_right_back = _create(
            self.root, self.root.bottom_right_back, 2, self.box)
        self.root.bottom_right_front = _create(
            self.root, self.root.bottom_right_front, 3, self.box)
        # 顶部顺时针
        self.root.top_left_front = _create(self.root.top_left_front, 4,
                                           self.box)
        self.root.top_left_back = _create(self.root.top_left_back, 5, self.box)
        self.root.top_right_back = _create(self.root.top_right_back, 6,
                                           self.box)
        self.root.top_right_front = _create(self.root.top_right_front, 7,
                                            self.box)

        return self
