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
#expanding pandas with fastindex
fast_index(pd)
```
example usage:
```python
#setting pandas MultiIndex
df = read_csv("data.csv")
df.set_index(["Country","City","District","first_name","Age","ID"],inplace=True)
df.sort_index(inplace=True)
```

the magic starts here:
### Basic Selection
---
**Regular Pandas:**
```python
df.loc[(slice(None),slice(None),slice(None),slice(None),24),:]
```

**With fastindex**
```python
df.fidx.slice(Age=24)
```

### Ranges
---
**Regular Pandas:**
```python
df.loc[("Spain",slice(None),slice(None),slice(None),slice(23,25)),:]
```
**With fastindex**
```python
df.fidx.slice(Age=slice(23,25),Country="Spain")
```


### Selecting columns 
---
**Regular Pandas:**
```python
df.loc[("Spain",slice(None),slice(None),slice(None),slice(23,25)),["last_name"]]
```
**With fastindex**
```python
df.fidx.slice(Age=slice(23,25),Country="Spain",columns = ["last_name"])
```


### setting values using f_slice:
---
```python
slc = df.fidx.f_slice(Age=slice(23,25),Country="Spain")
df.loc[slc,"last_name"] = "Leonardo"
```
