from flask import Blueprint, jsonify, request

demo = Blueprint('demo', __name__)

@demo.route('/api/hello', methods=['GET'])
def hello():
    """Simple hello endpoint
    ---
    tags:
      - Demo APIs
    responses:
      200:
        description: Returns greeting message
        examples:
          application/json: { "message": "Hello from Flask Demo!" }
    """
    return jsonify({"message": "Hello from Flask Demo!"})


@demo.route('/api/echo', methods=['POST'])
def echo():
    """Echo back the posted data
    ---
    tags:
      - Demo APIs
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              name:
                type: string
                example: Morjina
    responses:
      200:
        description: Echoes received data
        examples:
          application/json: { "received": { "name": "Morjina" } }
    """
    data = request.get_json()
    return jsonify({"received": data})

