import talib
import numpy as np
import pandas as pd
from twelvedata import TDClient
import os

class PreprocessIndicatorsFromDF:

    def GetIndicatorsFromDF(self, df):
        # Calculate selected indicators
        high_low = df['high'] - df['low']
        ma = talib.SMA(df['close'], timeperiod=14)
        wma = talib.WMA(df['close'], timeperiod=14)
        mom = talib.MOM(df['close'], timeperiod=10)
        k, d = talib.STOCH(df['high'], df['low'], df['close'], fastk_period=14, slowk_period=3, slowk_matype=0,
                           slowd_period=3, slowd_matype=0)
        rsi = talib.RSI(df['close'], timeperiod=14)
        macd, macdsignal, macdhist = talib.MACD(df['close'], fastperiod=12, slowperiod=26, signalperiod=9)
        lw = talib.WILLR(df['high'], df['low'], df['close'], timeperiod=14)
        ad = (df['high'] - df['close'].shift(1)) / (df['high'] - df['low'])
        # y_orgin=(df['Close'] - df['Open']) > 0
        y_Current = (df['close'] - df['open']) > 0
        y = (df['close'] - df['open']) > 0
        y_shift = y.shift(-1)
        y_shift = [1 if x else 0 for x in y_shift]
        max_min = self.get_max_min_series(df['close'])
        t_up_down = max_min - df['close'] > 0
        close = df['close']
        resultsCol = np.column_stack((df.index.strftime('%y%m%d').astype(int), ma, wma, mom, k, d, rsi, macd, lw,
                                      ad, high_low, close, y_Current, y_shift))  # t_up_down,y_shift,close
        df1 = pd.DataFrame(resultsCol,
                           columns=['datetime', 'ma', 'wma', 'mom', 'k', 'd', 'rsi', 'macd', 'lw', 'ad', 'high_low'
                               , 'close', 'y_Current', 'y_shift'])  # index=df['datetime'] 'max_min'
        return df1

    def local_max_min(self, data):
        """
        This function finds all local maximum and minimum points of a Pandas data series with a datetime index and puts them into an array.
        """
        # Find the indices where the first derivative changes sign
        diff = np.sign(np.diff(data.values))
        sign_changes = np.diff(diff)

        # Find the indices of the local maximum and minimum points
        maxima = np.where(sign_changes < 0)[0] + 1
        minima = np.where(sign_changes > 0)[0] + 1

        # Combine the indices and sort them
        extrema = np.sort(np.concatenate((maxima, minima)))

        # Create a DataFrame to store the results
        result = pd.Series(data=data.iloc[extrema].values, index=data.index[extrema])

        # Set the type of each point (maximum or minimum)
        #     result.loc[data.index[maxima], 'Type'] = 'Max'
        #     result.loc[data.index[minima], 'Type'] = 'Min'
        return result

    def get_max_min_series(self, data):
        data = data.sort_index()
        df_max_min = self.local_max_min(data)
        df_max_min = df_max_min.sort_index()

        new_col = np.empty((len(data)))
        new_col[:] = np.nan
        new_series = pd.Series(new_col, data.index)

        old_idx = data.index[0]
        # print(old_idx)
        for idx in df_max_min.index:
            new_series[old_idx:idx] = df_max_min[idx]
            old_idx = idx

        #     cols=np.column_stack((data.values, new_series.values))
        #     data_max_min_df = pd.DataFrame(cols,
        #                        columns=['data', 'new_series'], index=data.index)
        return new_series