from flask import Flask, jsonify, request

app = Flask(__name__)

from products import products

@app.route('/ping')
def ping():
  return jsonify({"message": "pong"});

@app.route('/products')
def getProducts():
  return jsonify({"products": products, "message": "Products list"}); 

@app.route('/products/<string:product_name>')
def getProduct(product_name):
  productFound = [product for product in products if product['name'] == product_name]
  if (len(productFound) > 0):
    return jsonify({"product": productFound[0]})
  return jsonify({"message": "product not found"})

@app.route('/products', methods=['POST'])
def addProducts():
  new_product = {
    "name": request.json["name"],
    "price": request.json["price"],
    "quantity": request.json["quantity"]
  }
  products.append(new_product)
  return jsonify({"message": "product added succesfully", "products": products})

@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
  productF = [product for product in products if product["name"] == product_name]
  if (len(product_name)>0 ):
    productF[0]['name'] = request.json['name']
    productF[0]['price'] = request.json['price']
    productF[0]['quantity'] = request.json['quantity']
    return jsonify({
      "message": "product updated",
      "product": productF[0]
    })
  return jsonify({"message": "product not found"})

@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
  productF = [product for product in products if product['name'] == product_name]
  if (len(product_name)>0): 
    products.remove(productF[0])
    return jsonify({
      "message": "product deleted",
      "products": products
    })
  return jsonify({
    "Message": "product not found"
  })


if __name__ == '__main__':
  app.run(debug=True, port=4000)
