# %%
import glob
import pandas as pd

files = glob.glob(f"../../data/senators/*") + glob.glob(f"../../data/representatives/*") 
    
# %%
dflist = []
for f in files:
    try:
        dflist.append(
            pd.read_csv(f).assign(file=f)
        )
    except Exception as e:
        print(e, f)
        
# %%
df = pd.concat(dflist)
df["handle"] = df["file"].str.split('/').str[-1].str.strip('.csv')

# %%
df.to_csv(f"../../data/tweets.csv", index=False)

# %%
