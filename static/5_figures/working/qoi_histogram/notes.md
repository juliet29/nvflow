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

Also strange that ther are negative values.. may have to do with the wholes in the data.. 

# Ventilation Volume

## v0

Has a similar pattern, except that it appears to be sparser..


Some of the rooms give negative results.. which is not a great sign..


# Mix Norm 
Basically similar pattern to the mixing volume although there may be more variance 
Looking at the entire day,  somewhat approximates the dist of looking at several days.. 
The data at noon is very holey.. 

Seems like plans follow pattern of having some have high mixing, some habe medium mixing, and some have low mixing.. 

So its good to see this consistency.. 

Or -> some have higher than wind speed, some have just same amount, somem have half of wind speed.. 

Better metric for this would be the normalized flow rate in to a building.. as the mixing volume already depends on the room size? 

Possible that all of these have one big room that gives high mixing volume.. 


Need to compute a flow in metric.. 


# Vent Norm 

For vent, the results are even more sparse.. but they are very differnt across the plans.. probably has to do with orientation. 


