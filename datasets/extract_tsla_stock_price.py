from pandas_datareader import data
import pandas as pd

start_date = '2012-11-16'
end_date = '2017-09-29'

tsla_data = data.DataReader('TSLA', 'yahoo', start_date, end_date)

tsla_data.to_csv('tsla_stock_price.csv')
