from flask import Flask, request, jsonify

app = Flask(__name__)

users = {}

# Create User (POST)
@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    user_id = str(len(users) + 1)  # auto-generate ID
    users[user_id] = data
    return jsonify({"id": user_id, "user": data}), 201


# Get All Users (GET)
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users), 200


# Get Single User by ID (GET)
@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    if user_id in users:
        return jsonify({user_id: users[user_id]}), 200
    return jsonify({"error": "User not found"}), 404


# Update User (PUT)
@app.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id in users:
        data = request.json
        users[user_id].update(data)
        return jsonify({user_id: users[user_id]}), 200
    return jsonify({"error": "User not found"}), 404


# Delete User (DELETE)
@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id in users:
        deleted = users.pop(user_id)
        return jsonify({"message": "User deleted", "user": deleted}), 200
    return jsonify({"error": "User not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)