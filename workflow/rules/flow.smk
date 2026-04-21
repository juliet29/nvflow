
configfile: "smkconfig/local_test.yaml"

rule graphs_create:
    input:
        unpack(make_eplus_inputs)
    output:
        graphs = "<intermed>/{sample}/graphs/out.json",
        data = directory("<intermed>/{sample}/graphs/data") 
    params:
        expansion = config["expansion"],
        year = config["time_selection"]["year"],
        month = config["time_selection"]["month"],
        days = config["time_selection"]["days"],
        hours = config["time_selection"]["hours"],
        dataname = config["data_folder_name"]
    log:
      "<intermed>/{sample}/graphs/log.out"
    shell:
        """
        uv run nvflow flowmetrics create \
          --idf-path {input.idf} \
          --sql-path {input.sql} \
          --ts.year {params.year} \
          --ts.month {params.month} \
          --ts.days {params.days} \
          --ts.hours {params.hours} \
          --cardinal-expansion-factor {params.expansion} \
          --json-path {output.graphs} \
          --data-folder-name {params.dataname} \
          2>{log}
        """

rule graph_metrics_create:
  input:
    "<intermed>/{sample}/graphs/out.json"
  output:
    "<intermed>/{sample}/metrics/out.json"
  log:
    "<intermed>/{sample}/graphs/log.out"
  shell:
    """
    uv run nvflow flowmetrics create-metrics \
        --json-path {input} \
        --metrics-path {output} \
        2>{log}
    """

rule consolidate:
  input:
      paths = expand("<intermed>/{sample}/metrics/out.json", sample=get_metrics_samples)
  output:
    "<shared>/flowmetrics/out.csv"
  params:
      names = expand("{sample}", sample=get_metrics_samples)
  log:
    "<shared>/flowmetrics/log.out"
  shell:
    """
    uv run nvflow flowmetrics consolidate \
        --metrics-paths {input.paths} \
        --names {params.names} \
        --csv-path {output} \
        2>{log}
    """





# Targets ----------
rule graph_metrics_create_target: 
    input:
        expand("<intermed>/{sample}/metrics/out.json", sample=get_eplus_samples)

rule consolidate_target:
  input: 
    "<shared>/flowmetrics/out.csv"

