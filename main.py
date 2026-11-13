import os
# One joke about AI coding agents. Deterministic: same bytes every run.
JOKE="My AI coding agent writes bug-free code by deleting the feature and calling it 'scope reduction.'\n"
out=os.environ.get('MAKEFUN_OUTPUT_DIR','/output')
os.makedirs(out,exist_ok=True)
with open(os.path.join(out,'entry.txt'),'w',encoding='utf-8') as f:
    f.write(JOKE)
