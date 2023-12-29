import pandas as pd
from DataProvider.PreprocessIndicatorsFromDF import PreprocessIndicatorsFromDF
#datetime	open	high	low	close
#pathCSVFile ='CSVFilePlace'
class MetatradeDataColector:
    def __init__(self, _symbol: str, _start, _end, _interval, _path):
        self.symbol = _symbol
        self.start = _start
        self.end = _end
        self.interval = _interval
        self.dataframe = pd.DataFrame(columns=['open', 'high', 'low', 'close'])  # Initialize the DataFrame with column names
        self.path = f"{_path}/OrginalData/Metatrade{_symbol.replace('/', '-')}_{_start}_{_end}_{_interval}.csv"

    def save_OCHL_info(self,datetime, open, high, low, close):
        new_row = pd.DataFrame({'datetime': [datetime],'open': [open], 'high': [high], 'low': [low], 'close': [close]})
        self.dataframe = pd.concat([self.dataframe, new_row], ignore_index=True)
        return self.dataframe

#BTC-USD_2015-02-01_2023-07-12_1day.csv
    def save_DF_to_csv(self):
        df = self.dataframe.sort_index()
        self.dataframe.to_csv(self.path, index=True)
        return "Saved"



# # Example usage
# financial_data = MetatradeDataColector()
#
# for i in range(10):
#     # Example data for each iteration
#     open_price = 100 + i
#     close_price = 102 + i
#     high_price = 105 + i
#     low_price = 99 + i
#
#     financial_data.save_OCHL_info(open_price, high_price, low_price, close_price)
#
# print(financial_data.dataframe)
