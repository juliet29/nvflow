
# -------------- DEPENDENCIES -------------
update-plyze:
  uv add plyze --upgrade-package plyze

add-local-plyze:
  uv add --editable "plyze @ /Users/julietnwagwuume-ezeoke/_UILCode/gqe-phd/fpopt/plyze"


# ------ SHARING CODE

push-tag end:
  @echo "Have you pushed the code you want this number to reflect?" 
  @read status;
  git tag -a s0.1.{{end}} -m s0.1.{{end}}
  git push --tag

# -------- FOR SNAKEMAKE
reset-test:
  ls static/4_temp/local_test
  rm -rfI static/4_temp/local_test


reset-local_results:
  ls static/4_temp/local_results
  rm -rfI static/4_temp/local_results

# -------- TEST CLI

generate-time-wind-yaml:
  uv run nvflow setup gen-time-sel-yaml-for-wind-dir --sql_path "static/4_temp/more_eplus_samples/100270/eplusout.sql" --yaml-path "test.yaml"
