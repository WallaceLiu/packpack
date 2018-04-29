# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 14:10:40 2017

@author: liuning11
"""
from goods import goods


def unfold(gs):
    for g in gs:
        g.gs.append(
            goods(
                id=g.id,
                pseudoId=str.format('%s-%s' % (g.id, '1')),
                price=g.price,
                width=g.space.wdh[0],
                depth=g.space.wdh[1],
                height=g.space.wdh[2]))

        g.gs.append(
            goods(
                id=g.id,
                pseudoId=str.format('%s-%s' % (g.id, '2')),
                price=g.price,
                width=g.space.wdh[1],
                depth=g.space.wdh[2],
                height=g.space.wdh[0]))

        g.gs.append(
            goods(
                g.id,
                pseudoId=str.format('%s-%s' % (g.id, '3')),
                price=g.price,
                width=g.space.wdh[2],
                depth=g.space.wdh[0],
                height=g.space.wdh[1]))
