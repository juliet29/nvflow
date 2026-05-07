configfile: "smkconfig/local_test.yaml"

rule qois_create:
  input:
    graphs = "<graphs>/{sample}/out.json",
  output:
    "<qois>/{sample}/out.json"
  log:
    "<qois>/{sample}/log.out"
  shell:
    """
    uv run nvflow flowmetrics create-metrics \
        --json-path {input.graphs} \
        --metrics-path {output} 
    """

rule qois_consolidate:
  input:
      paths = expand("<qois>/{sample}/out.json", sample=get_metrics_samples)
  output:
    "<cons_qois>/out.csv"
  params:
      names = expand("{sample}", sample=get_qois_samples)
  log:
    "<cons_qois>/out.log"
  shell:
    """
    uv run nvflow flowmetrics consolidate \
        --metrics-paths {input.paths} \
        --names {params.names} \
        --csv-path {output} \
        2>{log}
    """

