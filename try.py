import numpy as np
import pandas as pd
import anomaly_detection

dat = np.random.random(24*4*30) + 10
dts = pd.date_range(start='2018-08-01', freq='15min', periods=24*4*30)
df = pd.DataFrame(dat, index=dts, columns=['y'])

outliers = np.random.randint(low=0, high=24*4*30, size=20)
df.y.iloc[outliers] = df.y.iloc[outliers]*2

