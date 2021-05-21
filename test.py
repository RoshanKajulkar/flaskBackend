from flask import Flask
import tensorflow as tf
# from tensorflow import keras
from flask import Flask
app = Flask(__name__)
ver=tf.__version__
print(ver)
@app.route('/')
def hello_world():

    return "hello tenserfow versuion::"+ver

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8080)
