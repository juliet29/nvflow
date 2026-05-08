from pathlib import Path 

def make_eplus_inputs(wildcards):
    loc = Path(config["pathvars"]["samples"])
    idf = loc / "{wildcards.sample}/out.idf".format(wildcards=wildcards),
    sql = loc / "{wildcards.sample}/eplusout.sql".format(wildcards=wildcards)

    return {"idf": idf, "sql": sql}


def get_eplus_samples(wildcards): 
  loc = Path(config["pathvars"]["samples"])
  samples = [i.name for i in loc.iterdir() if i.is_dir()]

  return samples



def get_graph_samples(wildcards): 
  loc = Path(config["pathvars"]["graphs"])
  samples = [p.parent.name for p in loc.glob("*/.done")]

  return samples


def get_metric_samples(wildcards): 
  loc = Path(config["pathvars"]["metrics"])
  samples = [p.parent.name for p in loc.glob("*/.done")]

  return samples

def get_sql_input(wildcards):
    loc = Path(config["pathvars"]["samples"])
    sql = loc / config["refsql"] / "eplusout.sql"
    return sql


