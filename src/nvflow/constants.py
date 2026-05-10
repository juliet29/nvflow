from enum import StrEnum
from plyze.utils import XArrayNames
from plyze.flow_graph.interfaces import ZoneNodeQOINames
from plyze.metrics.registries import MetricRegistry


def keep():
    _ = ZoneNodeQOINames
    _ = MetricRegistry


class Constants(XArrayNames):
    CASE = "case_name"


class RoomNames(StrEnum):
    living = "LIVING_DINING"
    kitchen = "KITCHEN"
    room = "ROOM"


class WindDirections:
    _0_10 = (0, 10)
    _320_330 = (320, 330)
