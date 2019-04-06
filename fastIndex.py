import pandas as pd

def get_arg(i,indx,vargs,kwargs):
    if i<len(vargs):
        return vargs[i]
    else:
        return kwargs.get(indx,slice(None))
    

def create_slice(index_names,*vargs,**kwargs):
    return tuple(map(lambda elm:get_arg(elm[0],elm[1],vargs,kwargs) ,enumerate(index_names)))

def fast_index(pd):
    return pd.api.extensions.register_dataframe_accessor("fidx")(FastIndex)

# @pd.api.extensions.register_dataframe_accessor("fidx")
class FastIndex(object):
    def __init__(self, df):
        self._df = df

    @staticmethod
    def _validate(obj):
        pass


    def f_slice(self,*vargs,**kwargs):
        # return the geographic center point of this DataFrame
        slc = create_slice(self._df.index.names,*vargs,**kwargs)
        if isinstance(self._df.index, pd.core.index.MultiIndex):    
            return slc
        else:
            return slc[0]
    
    def slice(self,*vargs,columns =slice(None),**kwargs):
        return self._df.loc[self.f_slice(*vargs,**kwargs),columns]
 


