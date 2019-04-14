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
df.set_index(["Country","City","District","first_name","Age","ID"],inplace=True)
df.sort_index(inplace=True)
```

the magic starts here:
```python
#basic selection
#regular pandas:
df.loc[(slice(None),slice(None),slice(None),slice(None),24),:]
#with fastindex
df.fidx.slice(Age=24)

#slices
#regular pandas
df.loc[("Spain",slice(None),slice(None),slice(None),slice(23,25)),:]
#with fastindex
df.fidx.slice(Age=slice(23,25),Country="Spain")


#columns
#regular pandas 
df.loc[("Spain",slice(None),slice(None),slice(None),slice(23,25)),["last_name"]]

#with fastindex
df.fidx.slice(Age=slice(23,25),Country="Spain",columns = ["last_name"])


#setting values using f_slice:
slc = df.fidx.f_slice(Age=slice(23,25),ID=234,Country="Spain")
df.loc[slc,"last_name"] = "Leonardo"
```
