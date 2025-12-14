from flask import Flask,request,jsonify
from flask_cors import CORS
from Table_creation import create_table,db_connect
from werkzeug.security import generate_password_hash,check_password_hash
import psycopg2,re,os
import psycopg2.extras


app=Flask(__name__)
CORS(app)

create_table()

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "Backend is running"}), 200


@app.route("/signup",methods=['POST'])
def signup():

    data=request.json
    
    required_fields=["fullname","email","password","confirm_password"]
    for field in required_fields:
        if not data.get(field):
            return jsonify({"message":"Please fill required fields"}),400
        
    fullname=data.get("fullname")
    email=data.get("email")
    password=data.get("password")
    confirm_password=data.get("confirm_password")

    email_regex= r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if not re.match(email_regex,email):
        return jsonify({"message":"Invalid email format"}),400
    
    if password != confirm_password:
        return jsonify({"message":"Password do not match"}),400
    
    hashed_password=generate_password_hash(password)

    try:
        conn=db_connect()
        cursor=conn.cursor()

        cursor.execute("SELECT email FROM users WHERE email=%s",(email,))
        if cursor.fetchone():
            return jsonify({"message":"Email already exists"}),400
        
        cursor.execute("""
            INSERT INTO users (fullname,email,password)
            VALUES (%s,%s,%s)
        """,(fullname,email,hashed_password))

        conn.commit()
        conn.close()

        return jsonify({"message":"Signup successfully"}),200
    
    except Exception as e:
        return jsonify({"message":"Something went wrong"}),400
    
@app.route("/login",methods=['POST'])
def login_user():
    
    data=request.json

    if not data.get("email"):
        return jsonify({"message": "Email is required"}), 400

    if not data.get("password"):
        return jsonify({"message": "Password is required"}), 400
    
    email=data.get("email")
    password=data.get("password")

    try:
        conn=db_connect()
        cursor=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor.execute("SELECT fullname,password FROM users WHERE email=%s",(email,))
        result=cursor.fetchone()

        conn.close()

        if not result:
            return jsonify({"message":"Email not found"}),400
        
        hashed_password=result["password"]

        if not check_password_hash(hashed_password,password):
            return jsonify({"message":"Incorrect password"}),400
        
        return jsonify({"message":"Login successfully","fullname": result["fullname"]}),200
    
    except Exception as e:
        return jsonify({"message":"somethind went error"}),500

if __name__=="__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
