# Extract-information-from-financial-news
This file could extract information from txt files, especially for financial news.
The information contain:
  data: pairs of variables and their value, eg. (average, 0.77)
  time: words related to time,  eg.(2018-07-02, weekly)
  tags: companies, person, proper noun
  location: geographic information
For test, I input an article from wallstreetmorning.com, the link is: 
http://www.wallstreetmorning.com/2018/06/08/meridian-bioscience-inc-vivo-stock-technical-analysis/
The output is:
'data':
{'percent': [(is, 100%), (valued, 0.98%), (are, 6.54%), (away, 5.71%), (a distance, 5.81%), (seen, 15.36%),
(a change, 4.05%), (an activity trend, 10.00%), (a shift, 4.05%), (stands, 2.67%), (stands, 4.05%), (volatility, 2.24%),
(is, 2.38%)], 'currency': [(it, one), (valued, 15.40), (A total volume, 0.17 million shares), (average volume, 0.24 million shares),
(Relative Strength Index, 70.71), (Bioscience, Inc., 41.92 million outstanding shares), (float, 41.65 million), (stands, 0.34), 
(based, 14 periods), (beta, 0.97), (is, 3.20)]}
'tags':
['Meridian Bioscience, Inc.', 'Meridian Bioscience, Inc.', 'Simple Moving averages', 'RSI', 'ATR', 'Shares of Meridian Bioscience, Inc.',
'Simple Moving averages\n\nChart patterns', 'Meridian Bioscience, Inc.', 'Meridian Bioscience, Inc.', 'Bioscience, Inc.', 'RSI', 
'\n\nMeridian Bioscience, Inc.', 'RSI', 'RSI', 'RSI', 'J. Welles Wilder', 'Bioscience, Inc.', 'Meridian Bioscience, Inc.', 'YTD) 
performance', 'Meridian Bioscience, Inc.', 'ATR', 'the Average True Range', 'ATR']
time:
['decades', 'Thursday, June 08', 'a given period of time', '50', '50-day', '20-day average', 'the 200-day', '52 week', 
'the last 52 weeks', 'the last year', 'between 0 and 30', 'weekly performance', 'the last week', 'the last month',
'quarterly performance', 'the past six months', 'the past week', 'the previous month volatility move']
location:
'VIVO'
