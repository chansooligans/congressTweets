from congresstweets import locs
import glob
import pandas as pd
from dataclasses import dataclass
from typing import List

@dataclass
class TweetsTable:
    files: List = glob.glob(f"{locs.DATA_LOC}/senators/*") + glob.glob(f"{locs.DATA_LOC}/representatives/*") 

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
        
    def df(self):
        df = pd.concat(self.dflist)
        df["handle"] = df["file"].str.split('/').str[-1].str.strip('.csv')
        df.to_csv(f"{locs.DATA_LOC}/tweets.csv", index=False)
