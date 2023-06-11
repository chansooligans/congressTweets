import pandas as pd

def get_handles(path):
    """
    given path to CSV containing twitter users, return twitter handles from
    links
    """
    senators = pd.read_csv(path)

    return senators.loc[
        senators["Link"].notnull(),
        "Link"
    ].str.split("/").str[-1].values
