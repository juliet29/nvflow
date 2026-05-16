configfile: "smkconfig/more_test.yaml"

rule plan_qois_create:
  input:
    graphs = "<graphs>/{sample}/out.json",
  output:
    "<plan_qois>/{sample}/out.nc"
  log:
    "<plan_qois>/{sample}/log.out"
  shell:
    """
    uv run nvflow flowmetrics create-plan-qois\
        --json-path {input.graphs} \
        --qoi-path {output} 
    """

rule plan_qois_create_target: 
    input:
        expand("<plan_qois>/{sample}/out.nc", sample=get_graph_samples)
