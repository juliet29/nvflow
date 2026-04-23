# QOI Histogram for temperature

## v0

- seems like there are two groups for the information at single time
- so probably want to distinguish between temperature of plans that are not ventilated, and plans that are ventilated..
- probably also want to look at across the whole day, instead of just jumping to multiple days..

- when do have multiple days, can see that the temperature is uniformly distributed.. in which case the temperature over time might be well predicted by the median or the mean -> look at the literature on this though..

# Mixing Volume

## v0

Can see that the majority of values are zero... at noon... so when calculate the metric, do need to distinguish the non-mixing rooms..

Once we remove the zeros we can probaly see a clearer distribution.. should percentage of rooms that are mixing be considered as a design metric?

I think once we remove the non-afn rooms that should be good enough..

# Ventilation Volume

## v0

Has a similar pattern, except that it appears to be sparser..
Some of the rooms give negative results.. which is not a great sign..
