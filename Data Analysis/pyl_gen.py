import re
import pandas as pd
import numpy as np

s = "1-37 2-36.5 3-35.5 4-35 5-35 12-34 16-33 18-32.5 19-32 22-32 31-31 37-30.5 41-31 55-29.5 69-29 72-28.5 90-28 117-26 128-26 158-24"

pattern = re.compile(r'(\d+(?:\.\d+)?)-(\d+(?:\.\d+)?)')
pairs = [(int(a), float(b)) for a, b in pattern.findall(s)]
pairs.append((393, 0.0))
pairs.sort(key=lambda x: x[0])
full = {}
for (i1,v1),(i2,v2) in zip(pairs, pairs[1:]):
    full[i1]=v1
    if i2>i1+1:
        for x in range(i1+1,i2):
            t=(x-i1)/(i2-i1)
            v=v1+(v2-v1)*t
            full[x]=v
full[pairs[-1][0]] = pairs[-1][1]
def round05(x): return round(x*2)/2
full = {k: round05(v) for k,v in full.items()}
df = pd.DataFrame(sorted(full.items()), columns=["Index","Value"])
path="linearised.xlsx"
df.to_excel(path, index=False)

