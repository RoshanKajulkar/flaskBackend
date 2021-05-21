from flask import Flask, request
from flask import jsonify
from flask_cors import CORS, cross_origin


import json
from tensorflow import keras

import numpy as np
import cv2

vgg_model = keras.models.load_model('./vgg16.h5')

app = Flask(__name__)        
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def hello_world():
    	return "hello app"
    
@app.route('/RequestImageWithMetadata', methods=['POST'])
def post():
	imagefile = request.files.get('imagefile', '')
	imagefile.save('./test_image.png')
	img=cv2.imread('./test_image.png')
	img = cv2.resize(img, (300, 300))
	img = img/255.0
	img = np.reshape(img, (1,300,300,3))
	vgg_prediction= vgg_model.predict(img)
	result = vgg_prediction[0][0]
	return jsonify({"result":str(result)}), 200

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8080)
