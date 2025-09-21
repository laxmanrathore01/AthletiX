from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Dummy users 
users = {
    "admin": "1234",
    "athlete": "password"
}

@app.route("/")
def home():
    return render_template("login.html")  

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username in users and users[username] == password:
        return jsonify({"success": True, "message": "Login successful!"})
    else:
        return jsonify({"success": False, "message": "Invalid username or password."})

@app.route("/dashboard")
def dashboard():
    return "<h1>Welcome to AthletiX Dashboard 🏆</h1>"

if __name__ == "__main__":
    app.run(debug=True)
