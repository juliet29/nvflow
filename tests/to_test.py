from functools import partial

from nvflow.analysis_2.helpers import (
    filter_rooms,
    filter_time,
    read_csv_and_update_time_type,
)
from nvflow.constants import RoomNames
from nvflow.paths import ProjectPaths


from nvflow.times import TimeSamples


def test_prep_qois():
    qoi_path = ProjectPaths.sample_results.qois

    room_name = RoomNames.kitchen
    dt = TimeSamples().single_time_noon
    time_filter = partial(filter_time, dt=dt)
    room_filter = partial(filter_rooms, room_name=room_name)

    return read_csv_and_update_time_type(qoi_path).pipe(room_filter).pipe(time_filter)
