from plyze.qoi.data.data import TimeSelection
from utils4plans.lists import chain_flatten

# single time
YEAR = 2017
MONTH = 7
month = (YEAR, MONTH)
days = (*month, [1, 2])


def create_time_samples():
    lst = [
        ("Single Time - Noon", TimeSelection(*month, [1], [12])),
        ("Single Day - All Times", TimeSelection(*month, [1], [])),
        ("Multiple Days - All Times", TimeSelection(*days, [])),
        ("Multiple Days, DayTime", TimeSelection(*days, list(range(6, 18)))),
    ]

    dt = [(name, dt.calc_datetimes()) for name, dt in lst]
    night_samples = (
        TimeSelection(*days, list(range(18, 23))),
        TimeSelection(*days, list(range(0, 6))),
    )
    night_dt = chain_flatten([i.calc_datetimes() for i in night_samples])
    dt.append(("Multiple Days, NightTime", night_dt))
    return dt
