import polars as pl
from pathlib import Path
from datetime import datetime

from nvflow.constants import Constants, RoomNames


# select certain rooms..
def read_csv_and_update_time_type(path: Path):
    return pl.read_csv(path, schema_overrides={Constants.DATETIME: pl.Datetime("us")})


def filter_rooms(df: pl.DataFrame, room_name: RoomNames):
    return df.filter(pl.col(Constants.SPACE).str.contains(room_name))


def filter_time(df: pl.DataFrame, dt: list[datetime]):
    return df.filter(pl.col(Constants.DATETIME).is_in(dt))
