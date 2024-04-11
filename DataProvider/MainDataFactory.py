from DataProvider.DataFactory import DataFactory
#call method place
symbol = "BTC/USD"  # "USD/JPY" #"AUD/EUR"55 #"USD/JPY"#"BTC/USD" #"AUD/USD" #"CAD/USD" #"USD/JPY"53
interval ="4h" #"4h" #"1day" "30min"
start_date = "2018-02-01"
end_date = "2020-02-01"
pathCSVFile ='CSVFilePlace'
daFa = DataFactory(_symbol= symbol, _interval=interval, _start_date = start_date, _end_date=end_date, _pathCSVFile= pathCSVFile)
data = daFa.LoadTwelvedata()
print("DataFactory data.shape:", data.shape)