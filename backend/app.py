from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)

# Database Connection
connection = pymysql.connect(
    host="portfolio-db.cfuoykquaxbs.ap-south-1.rds.amazonaws.com",
    user="admin",
    password="SIRILEKKALA",   # replace with your password
    database="portfolio"
)

@app.route("/contact", methods=["POST"])
def contact():
    data = request.get_json()

    name = data["name"]
    email = data["email"]
    message = data["message"]

    # Store in database
    cursor = connection.cursor()

    sql = """
    INSERT INTO contacts(name,email,message)
