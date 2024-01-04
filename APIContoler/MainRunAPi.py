import atexit

from flask import Flask, request
from DataProvider.MetatradeDataColector import  MetatradeDataColector
import pandas as pd

app = Flask(__name__)
#define global object
mdcGlobal: MetatradeDataColector
mdcGlobal = None
pathCSVFile ='../DataProvider/CSVFilePlace'

# Cleanup function
def cleanup():
    global mdcGlobal
    # Perform cleanup
    mdcGlobal = None
    print("Cleaned up global object")

# Register cleanup function with atexit
atexit.register(cleanup)


@app.route('/getpredictpertickers', methods=['GET'])
def getpredictpertickers():
    #back test date
    symbol = request.args.get('symbol', 'Blank-Blank')
    timeframe = request.args.get('timeframe', 'Blank')
    timeframe =timeframe_to_string(int(timeframe))
    barsCount = request.args.get('barsCount', 0)
    _from= request.args.get('from', '1/1/1000 00:01:01')

    #candel data
    candeltime = request.args.get('candeltime', '1/1/1000')
    ticktime = request.args.get('ticktime', '1/1/1000')
    isstartcandel = request.args.get('isstartcandel', 'False')
    open = request.args.get('open', -1.0)
    close = request.args.get('close', -1.0)
    high = request.args.get('high', -1.0)
    low = request.args.get('low', -1.0)

    global mdcGlobal
    if mdcGlobal is None:
        mdcGlobal=MetatradeDataColector(_symbol= symbol,_interval=timeframe, _start=_from, _end="", _path=pathCSVFile)

    df = mdcGlobal.save_OCHL_info(datetime=candeltime,ticktime=ticktime, open=open, high=high, low=low, close=close, isstartcandel=isstartcandel)

    print(_from ,",",timeframe,",",ticktime,"," ,candeltime,",",isstartcandel,",", open,",",close,",", high ,",", low,)

    # Use the 'name' parameter in the response message
    return {"message": f"dataframe:{candeltime}"}

@app.route('/saveddata', methods=['GET'])
def saveddata():
    to = request.args.get('to',  '1/1/1000 00:01:01')
    if mdcGlobal is not None:
        mdcGlobal.save_DF_to_csv(to)
        cleanup()

    return "saved"
def timeframe_to_string(timeframe):
    timeframe_dict = {
        1: "M1",
        5: "M5",
        15: "M15",
        30: "M30",
        60: "H1",
        240: "H4",
        1440: "D1",
        10080: "W1",
        43200: "MN"
    }
    return timeframe_dict.get(timeframe, "Unknown")

# # Example usage
# print(timeframe_to_string(15))  # Output: M15
# print(timeframe_to_string(43200))  # Output: MN
# print(timeframe_to_string(999))  # Output: Unknown

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)