import fileinput
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from datetime import datetime

sd = pd.datetime(2018, 11, 27)
ed = pd.datetime(2018, 11, 28)

#####
tempfile = 'c:\\cGas\\python\\Input\\DataItem_27-11-2018_28-11-2018 - Demand system entry volume.txt'
paul_tempfile = f'c:\cGas\python\Input\DataItem_{sd:%d-%m-%Y} - Demand system entry volume.txt'
rawdata = pd.read_csv(tempfile)

rawdata["Applicable At"]=pd.to_datetime(rawdata["Applicable At"], format='%d/%m/%Y %H:%M:%S')
rawdata["Generated Time"]=pd.to_datetime(rawdata["Generated Time"], format='%d/%m/%Y %H:%M:%S')
rawdata["Applicable For"]=pd.to_datetime(rawdata["Applicable For"], format='%d/%m/%Y')
rawdata["Value"]=int(rawdata["Value"]) 
print(rawdata)

