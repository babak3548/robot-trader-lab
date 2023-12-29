import torch
import numpy as np
from sklearn.model_selection import train_test_split
from DataProvider.TwelvedataDownloadData import TwelvedataDownloadData

class DataFactory:
    def __init__(self, _symbol: str, _interval, _start_date, _end_date, _pathCSVFile ):
        self.symbol = _symbol
        self.interval = _interval
        self.start_date = _start_date
        self.end_date = _end_date
        self.pathCSVFile = _pathCSVFile

    def LoadTwelvedata(self):
        d_loader = TwelvedataDownloadData(_symbol=self.symbol, _start=self.start_date, _interval=self.interval, _end=self.end_date,
                                          _path=self.pathCSVFile)
        df = d_loader.ifNotExistDownloda()
        print("df.values.shape", df.values.shape)
        data = df.values
        mask = np.array([all([not np.isinf(item) and not np.isnan(item) for item in row]) for row in data])
        data = data[mask]
        print("data=data[mask]:", data.shape)

        return data


