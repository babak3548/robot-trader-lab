from DataProvider.DataFactory import DataFactory
from LogisticRegressionModel import LogisticRegressionModel
from LogiRegrPolynomialFeaturesModel import LogiRegrPolynomialFeaturesModel
from LinearRegressionPolynomialFeaturesModel import LinearRegressionPolynomialFeaturesModel


#call method place
symbol = "BTC/USD"  # "USD/JPY" #"AUD/EUR"55 #"USD/JPY"#"BTC/USD" #"AUD/USD" #"CAD/USD" #"USD/JPY"53
interval = "1day"
start_date = "2015-02-01"
end_date = "2023-07-10"
pathCSVFile ='../DataProvider/CSVFilePlace'

daFa = DataFactory(_symbol= symbol, _interval=interval, _start_date = start_date, _end_date=end_date, _pathCSVFile=pathCSVFile)
data= daFa.LoadTwelvedata()


# LogRegModel = LogisticRegressionModel(data=data )
#LogRegModel = LogiRegrPolynomialFeaturesModel(data=data )
LogRegModel = LinearRegressionPolynomialFeaturesModel(data=data )
LogRegModel.TrainModel()