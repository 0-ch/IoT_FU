from flask import Flask
from flask import render_template
from flask import request,jsonify
from flask_cors import CORS
import urllib.parse
import time
import base64
import pyimgur
from db import InsertMongo
from db import getMongo

app = Flask(__name__)
CORS(app)

@app.route('/upload',methods=['POST'])
def uploadProcess():
    print("in upload process")
    if not request.is_json:
        return jsonify({"message": "Missing JSON in request"}), 400

    data = request.get_json()

    
    if 'base64String' not in data:
        return jsonify({"message": "Missing 'base64String' in JSON"}), 400
    if 'name' not in data:
        return jsonify({"message": "Missing 'nameg' in JSON"}), 400
    if 'num' not in data:
        return jsonify({"message": "Missing 'num' in JSON"}), 400
    imageBase = ""
    
    base64String = data['base64String']
    name = data['name']
    num = data['num']
    base64String=urllib.parse.unquote(base64String)
    print(base64String)
    nowTime = time.time()
    local_img_file = f"iot_test_{nowTime}_{num}.jpg"
    imgdata = base64.b64decode(base64String)
    filename = local_img_file 
    
    with open(filename, 'wb') as f:
        f.write(imgdata)

    CLIENT_ID = "Your Client ID"
    im = pyimgur.Imgur(CLIENT_ID)
    PATH = local_img_file #A Filepath to an image on your computer"
    title = "QuizBank upload PyImgur"

    uploaded_image = im.upload_image(PATH, title=title)
    print(uploaded_image.title)
    print(uploaded_image.link)
    print(uploaded_image.type)
    InsertMongo(uploaded_image.link, num, name)

    return jsonify({"message": uploaded_image.link}), 200


# @app.route("/uploadToDB",methods=['POST'])
# def uploadmongodb():
    
#     if not request.is_json:
#         return jsonify({"message": "Missing JSON in request"}), 400
        
#     data = request.get_json()
#     print("data\n")
#     print(data)
#     image_list = data.get('list', [])
#     print(image_list)
#     # 在這裡進行您對圖片列表的處理
    
#     return jsonify(success=True)



# @app.route("/getImage",methods=['GET'])
# def readMongodb():
    
#     data = request.get_json()
#     print("data\n")
#     print(data)
#     image_list = data.get('list', [])
#     print(image_list)
#     # 在這裡進行您對圖片列表的處理
    
#     return jsonify(success=True)

if __name__ == '__main__':
  app.run()
  