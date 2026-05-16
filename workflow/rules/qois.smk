configfile: "smkconfig/more_test.yaml"

rule qois_create:
  input:
    graphs = "<graphs>/{sample}/out.json",
  output:
    "<qois>/{sample}/out.json"
  log:
    "<qois>/{sample}/log.out"
  shell:
    """
    uv run nvflow flowmetrics create-qois\
        --json-path {input.graphs} \
        --qoi-path {output} 
    """

rule qois_consolidate:
  input:
      paths = expand("<qois>/{sample}/out.json", sample=get_graph_samples)
  output:
    "<cons_qois>/out.csv"
  params:
      names = expand("{sample}", sample=get_graph_samples)
  log:
    "<cons_qois>/out.log"
  shell:
    """
    uv run nvflow flowmetrics consolidate-qois \
        --qoi-paths {input.paths} \
        --names {params.names} \
        --csv-path {output} \
        2>{log}
    """

# Targets ----------
rule qois_create_target: 
    input:
        expand("<qois>/{sample}/out.json", sample=get_graph_samples)

rule qois_consolidate_target:
  input: 
    "<cons_qois>/out.csv"
