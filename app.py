from flask import Flask

app = Flask(__name__)


@app.route('/api', methods=["POST"])
def create_user():
    print("Hello")
    return {
        'status': 200,
        'message': "User created successfully"
    }

if __name__ == "__main__":
    app.run(debug=True)