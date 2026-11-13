import os
j="My AI coding agent writes bug-free code by deleting the feature and calling it 'scope reduction.'\n"
o=os.environ.get('MAKEFUN_OUTPUT_DIR','/output')
os.makedirs(o,exist_ok=True)
open(os.path.join(o,'entry.txt'),'w').write(j)
