# %%
from dataclasses import dataclass
from congresstweets.twitter.handles import CongressHandles

# %%
senators = CongressHandles(
    url="https://ucsd.libguides.com/congress_twitter/senators", _type="Senator"
)
senate_handles = senators.get_handles()
senate_handles.to_csv("../../data/senator_handles.csv")

# %%
reps = CongressHandles(
    url="https://ucsd.libguides.com/congress_twitter/reps", _type="Representative"
)
rep_handles = reps.get_handles()
senate_handles.to_csv("../../data/rep_handles.csv")

# %%
