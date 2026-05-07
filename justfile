
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
