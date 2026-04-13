import os
from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# الروابط بتاعتك
URL_ALL = "https://api.sheety.co/b579acfc81bbbc07d7e0674b9cc32193/sahlaAllProducts/sahlaAllProducts"
URL_NEW = "https://api.sheety.co/8756d4e92d8c1f63c9533ac55c20fc5a/sahlaNewProducts/sahlaNewProducts"

@app.route('/')
def home():
    return "Sahla Store API is Running!"

# طريق (Route) لجلب كل المنتجات
@app.route('/products/all', methods=['GET'])
def get_all_products():
    response = requests.get(URL_ALL)
    return jsonify(response.json())

# طريق (Route) لجلب المنتجات الجديدة بس
@app.route('/products/new', methods=['GET'])
def get_new_products():
    response = requests.get(URL_NEW)
    return jsonify(response.json())

if __name__ == "__main__":
    # مهم جداً لـ Railway عشان يقرأ البورت صح
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
