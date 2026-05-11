import polars as pl
from pathlib import Path
from datetime import datetime

from nvflow.constants import AmbientDataNames, Constants, RoomNames


def read_csv_and_update_time_type(path: Path):
    return pl.read_csv(path, schema_overrides={Constants.DATETIME: pl.Datetime("us")})


def filter_rooms(df: pl.DataFrame, room_name: RoomNames):
    return df.filter(pl.col(Constants.SPACE).str.contains(room_name))


def filter_time(df: pl.DataFrame, dt: list[datetime]):
    return df.filter(pl.col(Constants.DATETIME).is_in(dt))


# --- ambient data


class HandleWindDir:
    degree_pairs = [(i * 10, (i * 10) + 10) for i in range(36)]

    def map_wind_dir(self, val: float):
        for a, b in self.degree_pairs:
            if val >= a and val <= b:
                return f"({a},{b})"
                # return {"a": a, "b": b

    @classmethod
    def make_wind_group(cls, start: int):
        assert start in [i[0] for i in cls.degree_pairs]
        end = start + 10
        return f"({start},{end})"


def segment_wind_directions(df: pl.DataFrame):
    # this will be pretty tailored to ambient data..
    wind_mapper = HandleWindDir()
    return df.with_columns(
        wind_group=pl.col(AmbientDataNames.wind_direction).map_elements(
            wind_mapper.map_wind_dir, return_dtype=pl.String
        )
    )
