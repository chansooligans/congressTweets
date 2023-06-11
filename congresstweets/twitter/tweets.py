from congresstweets import locs
from functools import cached_property
import pandas as pd

class TweetsTable:
    
    def __init__(self, files, loc):
        self.files = files
        self.loc = loc

    @property
    def dflist(self):
        dflist = []
        for f in self.files:
            try:
                dflist.append(
                    pd.read_csv(f).assign(file=f)
                )
            except Exception as e:
                print(e, f)
        return dflist
    
    def save_df(self):
        df = pd.concat(self.dflist)
        df["handle"] = df["file"].str.split('/').str[-1].str.strip('.csv')
        df.to_csv(f"{self.loc}/tweets.csv", index=False)

    @cached_property        
    def df(self, save=False):
        if save:
            return self.save_df()
        return pd.read_csv(f"{self.loc}/tweets.csv")
