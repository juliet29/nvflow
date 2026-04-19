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

def get_metrics_samples(wildcards): 
  loc = Path(config["pathvars"]["intermed"])
  samples = [i.name for i in loc.iterdir() if i.is_dir() and (i/"metrics/out.json").exists()]

  return samples

# TODO: NOTE: This is an ANTIPATTERN! -> Snakemake can only have flat lists as input
# def make_sample_inputs(wildcards):
#   loc = Path(config["pathvars"]["intermed"])
#   json = loc / "metrics/{wildcards.sample}/out.json".format(wildcards=wildcards)
#   name = "{wildcards.sample}".format(wildcards=wildcards)
#
#   result =  {"json": json, "name": name}
#   print(result)
#   return result
#

