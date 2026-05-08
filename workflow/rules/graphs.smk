
configfile: "smkconfig/local_test.yaml"

rule graphs_create:
    input:
        unpack(make_eplus_inputs)
    output:
        graphs = "<graphs>/{sample}/out.json",
        data = directory("<graphs>/{sample}/data"),
        done = "<graphs>/{sample}/.done"
    params:
        expansion = config["expansion"],
        year = config["time_selection"]["year"],
        month = config["time_selection"]["month"],
        days = config["time_selection"]["days"],
        hours = config["time_selection"]["hours"],
        dataname = config["data_folder_name"]
    log:
      "<graphs>/{sample}/log.out"
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
          touch {output.done}
        """



rule graphs_create_target:
    input:
        expand("<graphs>/{sample}/out.json", sample=get_eplus_samples)


