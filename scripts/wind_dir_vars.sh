#!/bin/bash
cols_to_yaml() {
  local data=$(cat | tail -n +2)
  local names=("month" "day" "hour" "minute")
  for i in 1 2 3 4; do
    local vals=$(echo "$data" | cut -d',' -f$i | tr '\n' ',' | sed 's/,$//')
    echo "${names[$((i - 1))]}: [$vals]"
  done
}

xan filter 'month > 6 and month < 9' palo_alto_20.csv |
  xan select "month,day,wind_direction,hour,minute" |
  xan groupby wind_direction 'first(month), first(day), first(hour), first(minute)' |
  xan drop "wind_direction" |
  xan sort -N | cols_to_yaml
