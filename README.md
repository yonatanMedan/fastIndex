# fastIndex
awesome way to select from pandas multi index and more

**Warning! this repository is on early develoapment stage!**

installation:
```
pip install fastindex
```
configuration:

```python
from fastindex import fast_index
import pandas as pd
fast_index(pd)
```
example usage:
```python
#configuring pandas MultiIndex
df = read_csv("data.csv")
df.set_index(["Age","ID","Country"],inplace=True)
df.sort_index(inplace=True)
```

the magic starts here:
```python
#to select based on index just type:
df.fidx.slice(Age=34,ID=234,Country="Spain")
#you can also enter slices
df.fidx.slice(Age=slice(23,25),ID=234,Country="Spain")
#and query columns
df.fidx.slice(Age=slice(23,25),ID=234,Country="Spain",columns = ["Name"])

#use f_slice to set values
slc = df.fidx.f_slice(Age=slice(23,25),ID=234,Country="Spain")
df.loc[slc,"Name"] = "Leonardo"
```
