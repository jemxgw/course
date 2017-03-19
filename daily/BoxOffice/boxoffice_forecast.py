# -*- coding: <utf-8> -*-
'''
{
  'InsertDate': '日期',
  'BoxOffice': '票房',
  'ServicePrice': '服务费',
  'ShowCount': '场次',
  'AudienceCount': '人次',
  'BoxOfficeMoM': '票房环比',
  'PerAudienceShow': '场均人次',
  'PerAudienceOffice': '人均票房',
  'PerShowBoxOffice': '场均票房',
}
'''
import pandas as pd
import numpy as np
from fbprophet import Prophet
import matplotlib.pyplot as plt

plt.style.use('ggplot')

df = pd.read_csv('/Users/zhangmimi/Git/course/daily/BoxOffice/box_office.csv')
df['InsertDate'] = pd.to_datetime(df['InsertDate'])
df = df[df.InsertDate <= '2016-12-31']
df['PerAudienceOffice'] = df['BoxOffice'] / df['AudienceCount']
df['PerShowBoxOffice'] = df['BoxOffice'] / df['ShowCount']
df['PerAudienceShow'] = df['AudienceCount'] / df['ShowCount']

# 年度票房冠军


df['BoxOffice'] = np.log(df['BoxOffice'])

new = df.loc[:, ['InsertDate', 'BoxOffice']].sort_values(by='InsertDate')
plt.plot(new['InsertDate'], new['BoxOffice'], '.')
# plt.savefig('/Users/zhangmimi/Git/course/daily/BoxOffice/BoxOffice.png', dpi=200)
plt.show()
new.columns = ["ds", "y"]

# print(new.tail())

newyear = pd.DataFrame({
    'holiday': 'New Year\'s Day',
    'ds': pd.to_datetime(
        ['2010-01-01', '2011-01-01', '2012-01-01', '2013-01-01', '2013-12-31', '2015-01-01', '2016-01-01',
         '2016-12-31']),
    'lower_window': -1,
    'upper_window': 3,
})

spring = pd.DataFrame({
    'holiday': 'Spring Festival',
    'ds': pd.to_datetime(
        ['2010-02-13', '2011-02-02', '2012-01-28', '2013-02-09', '2014-01-30', '2015-02-18', '2016-02-07',
         '2017-01-27']),
    'lower_window': 0,
    'upper_window': 7,
})

national = pd.DataFrame({
    'holiday': 'National Day',
    'ds': pd.to_datetime(
        ['2010-10-01', '2011-10-01', '2012-09-30', '2013-10-01', '2014-10-01', '2015-10-01', '2016-10-01',
         '2017-10-01']),
    'lower_window': -1,
    'upper_window': 7,
})

christmas = pd.DataFrame({
    'holiday': 'Christmas Eve',
    'ds': pd.to_datetime(
        ['2010-12-24', '2011-12-24', '2012-12-24', '2013-12-24', '2014-12-24', '2015-12-24', '2016-12-24',
         '2017-12-24', ]),
    'lower_window': 0,
    'upper_window': 1,
})

holidays = pd.concat((newyear, spring, national, christmas))

m = Prophet(interval_width=0.8, holidays=holidays, holidays_prior_scale=20)
m.fit(new)
future = m.make_future_dataframe(periods=365)
forecast = m.predict(future)
# print(forecast.tail())
m.plot(forecast).savefig('/Users/zhangmimi/Git/course/daily/BoxOffice/BoxOfficeforecast.png', dpi=200)
m.plot_components(forecast).savefig('/Users/zhangmimi/Git/course/daily/BoxOffice/BoxOfficetrend.png', dpi=200)
