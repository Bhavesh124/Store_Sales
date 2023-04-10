from StoreSales.exception import CustomException
from StoreSales.logger import logging
from flask import Flask
import os,sys

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    try:
        raise Exception("we are testing custom exception")
    except Exception as e:
        StoreSales = CustomException(e,sys)
        logging.info(StoreSales.error_message)
        logging.info("we are testing logging file")

if __name__ == "__main__":
    app.run(debug=True)