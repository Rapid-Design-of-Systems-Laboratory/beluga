import sys
import dill

with open(sys.argv[1],'rb') as f:
    out = dill.load(f)

print(type(out['solution'][0]))
print(type(out['solution'][0][0]))
out['solution'] = [list(_) for _ in out['solution']]

with open(sys.argv[1]+'.out','wb') as f:
    dill.dump(out, f)
