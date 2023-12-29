import talib
import numpy as np
import pandas as pd
from twelvedata import TDClient
import os
from PreprocessIndicatorsFromDF import PreprocessIndicatorsFromDF


class TwelvedataDownloadData:
    def __init__(self, _symbol: str, _start, _end, _interval, _path):
        self.symbol = _symbol
        self.start = _start
        self.end = _end
        self.interval = _interval
        self.path = f"{_path}/OrginalData/Twelvedata{_symbol.replace('/', '-')}_{_start}_{_end}_{_interval}.csv"

    def ifNotExistDownloda(self):
        if not os.path.exists(self.path):
            # Initialize client - apikey parameter is requiered
            td = TDClient(apikey="f82e2cf8359a4189b7332f267aaa6320")
            # Construct the necessary time series
            ts = td.time_series(
                symbol=self.symbol,
                interval=self.interval,
                outputsize=5000,
                timezone="Asia/Singapore",  # "America/New_York",  # TODO
                start_date=self.start,
                end_date=self.end
            )
            # Returns pandas.DataFrame
            df = ts.as_pandas()
            df = df.sort_index()
            df.to_csv(self.path, index=True)
        else:
            df = pd.read_csv(self.path, parse_dates=["datetime"], index_col='datetime')

        indicator= PreprocessIndicatorsFromDF()
        df1 = indicator.GetIndicatorsFromDF(df)
        # _symbol= _symbol.replace("/","-")
        # print(path)
        # df1.to_csv(path, index = False)
        return df1
