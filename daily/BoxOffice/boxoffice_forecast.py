# -*- coding: <utf-8> -*-
import pandas as pd
import numpy as np
from fbprophet import Prophet

import matplotlib.pyplot as plt


plt.style.use('ggplot')

df = pd.read_csv('/Users/zhangmimi/Desktop/box_office.csv')
df['InsertDate'] = pd.to_datetime(df['InsertDate'])
df = df[df.InsertDate <= '2016-12-31']
df['BoxOffice'] = np.log(df['BoxOffice'])
new = df.loc[:, ['InsertDate', 'BoxOffice']].sort_values(by='InsertDate')
# print(new.tail())
plt.plot(new['InsertDate'], new['BoxOffice'])
plt.show()
# new.columns = ["ds", "y"]
# print(new.tail())
# m = Prophet()
# m.fit(new)
# future = m.make_future_dataframe(periods=365)
# forecast = m.predict(future)
# print(forecast.tail())
# m.plot(forecast).show()
# m.plot_components(forecast).show()
