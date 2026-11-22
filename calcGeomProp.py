from dataclasses import dataclass
from functools import cached_property
from math import pi
from mpmath import mp
from qgis.core import QgsGeometry

class CalcGeomProp:
    def __init__(self, geometry: QgsGeometry):
        self.geom = geometry

    @cached_property
    def hull(self) -> QgsGeometry:
        return self.geom.convexHull()

    @cached_property
    def area(self) -> float:
        return self.geom.area()

    @cached_property
    def perimeter(self) -> float:
        return self.geom.length()

