import requests
import pandas as pd

def fetchData(url: str) -> pd.DataFrame:
    """
    Fetches data from the SpaceX API and stores it in a pandas dataframe

    Args:
        url (str) -> API url to fetch data
    
    Returns:
        pd.DataFrame -> Returns pandas dataframe with api data
    """

    res = requests.get(url)
    data = res.json()

    df = pd.DataFrame(data)
    return df

df = fetchData("https://api.spacexdata.com/v5/launches")
print(df.head())