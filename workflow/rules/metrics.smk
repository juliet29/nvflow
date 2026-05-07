configfile: "smkconfig/local_test.yaml"

rule metrics_create:
  input:
    graphs = "<graphs>/{sample}/out.json",
  output:
    "<metrics>/{sample}/out.json"
  log:
    "<metrics>/{sample}/log.out"
  shell:
    """
    uv run nvflow flowmetrics create-metrics \
        --json-path {input.graphs} \
        --metrics-path {output} 
    """

rule metrics_consolidate:
  input:
      paths = expand("<metrics>/{sample}/out.json", sample=get_graph_samples)
  output:
    "<cons_metrics>/out.csv"
  params:
      names = expand("{sample}", sample=get_graph_samples)
  log:
    "<cons_metrics>/out.log"
  shell:
    """
    uv run nvflow flowmetrics consolidate-metrics \
        --metrics-paths {input.paths} \
        --names {params.names} \
        --csv-path {output} \
        2>{log}
    """

# Targets ----------
rule metrics_create_target: 
    input:
        expand("<metrics>/{sample}/out.json", sample=get_graph_samples)

rule metrics_consolidate_target:
  input: 
    "<cons_metrics>/out.csv"
