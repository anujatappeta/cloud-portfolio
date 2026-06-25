from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql
import boto3

app = Flask(__name__)
CORS(app)

# Database Connection
connection = pymysql.connect(
    host="portfolio-db.cfuoykquaxbs.ap-south-1.rds.amazonaws.com",
    user="admin",
    password="YOUR_RDS_PASSWORD",
    database="portfolio"
)

# AWS SES Email Function
def send_email(name, email, message):

    ses = boto3.client("ses", region_name="ap-south-1")

    ses.send_email(
        Source="YOUR_VERIFIED_EMAIL@gmail.com",
        Destination={
            "ToAddresses": ["YOUR_VERIFIED_EMAIL@gmail.com"]
        },
        Message={
            "Subject": {
                "Data": "New Portfolio Contact Form Submission"
            },
            "Body": {
                "Text": {
                    "Data": f"""
New Portfolio Contact Received

Name: {name}

Email: {email}

Message: {message}
"""
                }
            }
        }
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
    VALUES(%s,%s,%s)
    """

    cursor.execute(sql, (name, email, message))
    connection.commit()

    # Send email notification using AWS SES
    send_email(name, email, message)

    return jsonify({
        "message": "Data stored and email sent successfully"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
