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


class AmbientDataNames(StrEnum):
    # TODO: add to plyze
    wind_direction = "wind_direction"
    wind_group = "wind_group"
