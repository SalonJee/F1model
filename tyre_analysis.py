import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import fastf1
from fastf1 import get_session #function used to load data



fastf1.Cache.enable_cache('./cache') 
#tells FastF1 to enable and use a local cache directory (./cache) to store downloaded data

session = fastf1.get_session(2024 ,'Silverstone','Q')
session.load()   # loads/saves the session dat in the cache directory

print(session.event)
print(session.laps.columns)



