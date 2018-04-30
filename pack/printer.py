# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 14:10:40 2017

@author: liuning11
"""


def g(g):
    print('%s\t%s\t%d\t%s\t%d\t%d\t%f\t%f' %
          (g.id, g.pseudoId, g.price, g.space.wdh, g.space.volume,
           g.space.area, g.space.diagonal, g.space.angle))


def goods(gs):
    def _goods(gs):
        for g in gs:
            print('%s\t%s\t%d\t%s\t%d\t%d\t%f\t%f' %
                  (g.id, g.pseudoId, g.price, g.space.wdh, g.space.volume,
                   g.space.area, g.space.diagonal, g.space.angle))

    print('goods:')
    print('=============================================================')
    print('ID(PID)\tPri\tWDH\t\tVol\tAr\tDi\tA')
    print('-------------------------------------------------------------')
    for g in gs:
        print('%s(%s)\t%d\t%s\t%d\t%d\t%f\t%f' %
              (g.id, g.pseudoId, g.price, g.space.wdh, g.space.volume,
               g.space.area, g.space.diagonal, g.space.angle))
        _goods(g.gs)
    print('-------------------------------------------------------------')
    print('ID(PID)\tPri\tWDH\t\tVol\tAr\tDi\tA')
    print('=============================================================')


def boxes(boxes):
    print('boxes:')
    print('=============================================================')
    print('ID|\tWDH|\t\tVol|\tAr|\tDi|\tA')
    print('-------------------------------------------------------------')
    for box in boxes.boxes:
        print('\t%s\t%s\t%s' % (box.id, box.space.wdh, box.isFull))
    print('-------------------------------------------------------------')
    print('ID|\tWDH|\t\tVol|\tAr|\tDi|\tA')
    print('=============================================================')


def box(box):
    print('=============================================================')
    print('Box:\t%s\t%s\t%s' % (box.id, box.space.wdh, box.isFull))
    goods(box.goods)
    print('=============================================================')


def boxGoods(boxes):
    print('solution:')
    print('=============================================================')
    print('ID|\tCOSTED|\tVOLUSED')
    print('-------------------------------------------------------------')
    for box in boxes.boxes:
        print('%s\t%d\t%d' % (box.id, box.costed, box.volUsed))
        goods(box.goods)
    print('-------------------------------------------------------------')
    print('ID|\tCOSTED|\tVOLUSED')
    print('=============================================================')
