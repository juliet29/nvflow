from plyze.qoi.data.data import TimeSelection

# single time
YEAR = 2017
MONTH = 7
month = (YEAR, MONTH)
days = (*month, [1, 2, 3])


class SampleTimes:
    single = TimeSelection(*month, [1], [12]).calc_datetimes()
    across = TimeSelection(*days, []).calc_datetimes()
    day_across = TimeSelection(*days, list(range(6, 18))).calc_datetimes()
    night_across = (
        TimeSelection(*days, list(range(18, 23))).calc_datetimes()
        + TimeSelection(*days, list(range(0, 6))).calc_datetimes()
    )

    @property
    def samples(self):
        return [
            ("Single Time - Noon", self.single),
            ("Multiple Days - All Times", self.across),
            ("Multiple Days, DayTime", self.day_across),
            ("Multiple Days, NightTime", self.night_across),
        ]
