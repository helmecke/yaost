#!/usr/bin/env python

from yaost.construction import m_thread_external, m_thread_internal_hole
from yaost.project import Project
from yaost.scad import cylinder

p = Project('bolt and nut')


@p.add_part
def bolt(diameter=18, length=20):
    h = diameter * 0.4
    solid = m_thread_external(d=diameter, h=length + h)
    solid += cylinder(d=diameter * 1.9, h=h, fn=6)
    return solid


@p.add_part
def nut(diameter=18, length=15, tol=0.01):
    h = diameter * 0.4
    solid = cylinder(d=diameter * 1.9, h=h, fn=6)
    solid -= m_thread_internal_hole(d=diameter, h=h + tol * 2).tz(-tol)
    return solid


if __name__ == '__main__':
    p.run()