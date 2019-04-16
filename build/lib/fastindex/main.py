import pandas as pd
import pdb
def get_arg(i,indx,vargs,kwargs):
    if i<len(vargs):
        return vargs[i]
    else:
        return kwargs.get(indx,slice(None))
    

def create_slice(index_names,*vargs,**kwargs):
    for key in kwargs.keys():
        assert(key in index_names),"Key {} is not in index".format(key)
    return tuple(map(lambda elm:get_arg(elm[0],elm[1],vargs,kwargs) ,enumerate(index_names)))

def fast_index(pd):
    return pd.api.extensions.register_dataframe_accessor("fidx")(FastIndex)


def get_multi_index(df, column_names=[], index_names=[], order=None, names=None, name_map_f=None):
    index_frame = df.index.to_frame()
    index_frame[column_names] = df[column_names]
    if order is None:
        order = column_names + index_names
    if names is None:
        names = order
    if name_map_f is not None:
        names = list(map(name_map_f, names))

    return pd.MultiIndex.from_frame(index_frame[order], names=names)
        


# @pd.api.extensions.register_dataframe_accessor("fidx")
class FastIndex(object):
    def __init__(self, df):
        self._df = df

    def f_slice(self,*vargs,**kwargs):
        # return the geographic center point of this DataFrame
        slc = create_slice(self._df.index.names,*vargs,**kwargs)
        if isinstance(self._df.index, pd.core.index.MultiIndex):    
            return slc
        else:
            return slc[0]
    
    def slice(self,*vargs,columns =slice(None),**kwargs):
        return self._df.loc[self.f_slice(*vargs,**kwargs),columns]
    
    
 


