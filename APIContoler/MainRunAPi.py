import atexit

from flask import Flask, request
from DataProvider.MetatradeDataColector import  MetatradeDataColector
import pandas as pd

app = Flask(__name__)
#define global object
mdcGlobal: MetatradeDataColector

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
    # Retrieve the 'name' parameter from the URL query string
    global mdcGlobal
    mdcGlobal=MetatradeDataColector("", "", "", "", "")
    datetime = request.args.get('datetime', '1/1/1000')
    symbol = request.args.get('symbol', 'Blank-Blank')
    open = request.args.get('open', -1.0)
    close = request.args.get('close', -1.0)
    high = request.args.get('high', -1.0)
    low = request.args.get('low', -1.0)
    print(open,",",close,",", high ,",", low)
    islastTicker = request.args.get('islastTicker', 0)
    if islastTicker == 1 :
        mdcGlobal.save_DF_to_csv()
        cleanup()

    df = mdcGlobal.save_OCHL_info(datetime=datetime, open=open, high=high, low=low, close=close)
    # Use the 'name' parameter in the response message
    return {"message": f"dataframe:{datetime}"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)