configfile: "smkconfig/more_test.yaml"

rule ambient_create:
  input:
    sql = get_sql_input
  output:
    "<cons_ambient>/out.csv"
  log:
    "<cons_ambient>/log.out"

  params:
      year = config["time_selection"]["year"],
      month = config["time_selection"]["month"],
      days = config["time_selection"]["days"],
      hours = config["time_selection"]["hours"],
      listwise = "--ts.listwise" if config["time_selection"]["listwise"] else "--ts.no-listwise",
  shell:
    """
    uv run nvflow flowmetrics create-ambient-qois\
        --sql-path {input.sql} \
        --ambient-data-path {output} \
        --ts.year {params.year} \
        --ts.month {params.month} \
        --ts.days {params.days} \
        --ts.hours {params.hours} \
        {params.listwise} \
    """

rule ambient_create_target:
  input:
    "<cons_ambient>/out.csv"
