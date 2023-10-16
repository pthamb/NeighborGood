from flask import Flask, render_template, request, jsonify, session
from math import radians, sin, cos, sqrt, atan2
from flask_sqlalchemy import SQLAlchemy
# from flask_socketio import SocketIO, send
# from app import db
import json
app = Flask(__name__)
# app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:purnendu123@localhost/users_22345678'
# app.config['SQLALCHEMY_DATABASE_URI'] = ''
db = SQLAlchemy(app)

users = []

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True) 
    person = db.Column(db.String(200), nullable=False)
    age = db.Column(db.Integer, nullable=False) 
    email = db.Column(db.String(200), nullable=False)
    address = db.Column(db.Integer, nullable=False)
    mobile = db.Column(db.String(120), nullable=False, unique=True)
    walking = db.Column(db.String(200), nullable=False)
    running = db.Column(db.String(200), nullable=False)
    gardening = db.Column(db.String(200), nullable=True)
    swim = db.Column(db.String(200), nullable=False)
    tea = db.Column(db.String(200), nullable=True)
    like = db.Column(db.String(200), nullable=True)
    tv = db.Column(db.String(200), nullable=True)
    movie = db.Column(db.String(200), nullable=True)
    shopping = db.Column(db.String(200), nullable=True)
    happy = db.Column(db.String(200), nullable=True)
    erands = db.Column(db.String(200), nullable=True)
    rides = db.Column(db.String(200), nullable=True)
    childcare = db.Column(db.String(200), nullable=True)
    eldercare = db.Column(db.String(200), nullable=True)
    petcare = db.Column(db.String(200), nullable=True)
    tutoring = db.Column(db.String(200), nullable=True)
    home = db.Column(db.String(200), nullable=True)
    landscape = db.Column(db.String(200), nullable=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    sharePreference = db.Column(db.String(200))

@app.route('/')
def front():
    return render_template("index.html")


@app.route('/form', methods=['GET', 'POST'])
def index():
#   if request.method == 'POST':
#     required_fields = ["walking", "running", "swim"]
#     missing_fields = [field for field in required_fields if not request.form.get(field)]

#     if missing_fields:
#         return render_template('form.html', message="Please fill out the required fields: " + ', '.join(missing_fields))
#         person = request.form.get['person']
#         age = request.form['age']
#         email = request.form['email']
#         address = request.form['address']
#         mobile = request.form['mobile']
#         walking = request.form['walking']
#         running = request.form['running']
#         # bicycle_ride = request.form['enableRunning']
#         # dog_walking = request.form['enableRunning']
#         gardening = request.form['gardening']
#         swim = request.form['swim']
#         tea = request.form['tea']
#         # draw = request.form['draw']
#         like = request.form['likes']
#         # casual = request.form['casual']
#         tv = request.form['tv']
#         movie = request.form['movie']
#         shopping = request.form['shopping']
#         happy = request.form['happy']
#         erands = request.form['erands']
#         rides = request.form['rides']
#         childcare = request.form['childcare']
#         eldercare = request.form['eldercare']
#         petcare = request.form['petcare']
#         tutoring = request.form['tutoring']
#         home = request.form['home']
#         landscape = request.form['landscape']
#         latitude = request.form['latitude']
#         longitude = request.form['longitude']
#         # about = request.form['about']
#         sharePreference = request.form['sharePreference']  


#         # email="noemail"
#         # mobile="nomobile"
#         if sharePreference == 'yes':
#             email = request.form['email']
#             mobile = request.form['mobile']
#             print(mobile)
#             print(email)
#             print("sharePreference:", request.form.get('sharePreference'))
#         else:
#             email = "*"*len(request.form["email"])
#             mobile="*"*len(request.form["mobile"])
#     #     if 'sharePreference' in request.form:
#     #         sharePreference = request.form['sharePreference']
#     #     if sharePreference == 'yes':
#     #         # Include email and mobile in user data
#     #         email = request.form['email']
#     #         mobile = request.form['mobile']
#     #     else:
#     #         # Don't include email and mobile in user data
#     #         email = None
#     #         mobile = None
#     # else:
#     #     # "sharePreference" field is not present, so default to not sharing
#     #     email = None
#     #     mobile = None

#         # details_dict = {"person": person, "age": age, "email":email, "address":address, "mobile":mobile, "walking":walking, "running":running,   "gardening":gardening, "swim":swim, "tea":tea, "like":like,  "tv":tv, "movie":movie, "shopping":shopping, "happy":happy, "erands":erands, "rides":rides, "childcare":childcare, "eldercare":eldercare, "petcare":petcare, "tutoring":tutoring, "home":home, "landscape":landscape}
#         users.append({"person": person, "age": age, "email":email, "address":address, "mobile":mobile, "walking":walking, "running":running,   "gardening":gardening, "swim":swim, "tea":tea, "like":like,  "tv":tv, "movie":movie, "shopping":shopping, "happy":happy, "erands":erands, "rides":rides, "childcare":childcare, "eldercare":eldercare, "petcare":petcare, "tutoring":tutoring, "home":home, "landscape":landscape, "latitude":latitude, "longitude":longitude})
#         # with open("user_details.json", "w") as f:
#         #     json.dump(details_dict, f)
#         return render_template('form.html', message="Data submitted successfully!")
#     return render_template('form.html', message="")
 if request.method == 'POST':
        required_fields = ["walking", "running", "swim"]
        missing_fields = [field for field in required_fields if not request.form.get(field)]

        if missing_fields:
            return render_template('dashboard.html', message="Please fill out the required fields: " + ', '.join(missing_fields))

        person = request.form.get('person', "")
        age = int(request.form.get('age', ""))
        email = request.form.get('email', "")
        address = int(request.form.get('address', ""))
        mobile =int(request.form.get('mobile', ""))
        walking= request.form.get('walking', "")
        running= request.form.get('running', "")
        gardening = request.form.get('gardening', "")
        swim= request.form.get('swim', "")
        tea = request.form.get('tea', "")
        like = request.form.get('likes', "")
        tv = request.form.get('tv', "")
        movie = request.form.get('movie', "")
        shopping = request.form.get('shopping', "")
        happy = request.form.get('happy', "")
        erands = request.form.get('erands', "")
        rides = request.form.get('rides', "")
        childcare = request.form.get('childcare', "")
        eldercare = request.form.get('eldercare', "")
        petcare = request.form.get('petcare', "")
        tutoring = request.form.get('tutoring', "")
        home = request.form.get('home', "")
        landscape = request.form.get('landscape', "")
        latitude = float(request.form.get('latitude', ""))
        longitude = float(request.form.get('longitude', ""))
        sharePreference = request.form.get('sharePreference', "")

        if sharePreference == 'yes':
            email = request.form.get('email', "")
            mobile = request.form.get('mobile', "")
            print(mobile)
            print(email)
            print("sharePreference:", request.form.get('sharePreference'))
        else:
            email = "*"*len(request.form.get("email", ""))
            mobile="*"*len(request.form.get("mobile", ""))

        # users.append({
        #     "person": person,
        #     "age": age,
        #     "email": email,
        #     "address": address,
        #     "mobile": mobile,
        #     "walking": walking,
        #     "running": running,
        #     "gardening": gardening,
        #     "swim": swim,
        #     "tea": tea,
        #     "like": like,
        #     "tv": tv,
        #     "movie": movie,
        #     "shopping": shopping,
        #     "happy": happy,
        #     "erands": erands,
        #     "rides": rides,
        #     "childcare": childcare,
        #     "eldercare": eldercare,
        #     "petcare": petcare,
        #     "tutoring": tutoring,
        #     "home": home,
        #     "landscape": landscape,
        #     "latitude": latitude,
        #     "longitude": longitude
        # })

        existing_user = User.query.filter_by(mobile=mobile).first()
        if existing_user:
            message = "User with the same mobile number already exists. Data not submitted."
        else:
            users = User(person=person, age=age,  address=address, mobile=mobile, email=email, walking=walking, running=running, gardening= gardening, swim=swim, tea=tea, like=like, tv=tv, movie=movie, shopping=shopping, happy=happy, erands=erands, rides=rides, childcare= childcare, eldercare=eldercare, petcare=petcare, tutoring=tutoring, home=home, landscape=landscape, latitude=latitude, longitude=longitude, sharePreference=sharePreference)
            db.session.add(users)
            db.session.commit()
            message= "data submitted successfully"

        return render_template('form.html', message="Data submitted successfully!")
 return render_template('form.html', message="")
    
@app.route('/get_users')
def get_users():
    users = User.query.all()
    user_data = []
    for user in users:
        user_data.append({
            "id": user.id,
            "person": user.person,
            "age": user.age,
            "email": user.email,
            "address": user.address,
            "mobile": user.mobile,
            "walking": user.walking,
            "running": user.running,
            "gardening": user.gardening,
            "swim": user.swim,
            "tea": user.tea,
            "like":user.like ,
            "tv": user.tv,
            "movie": user.movie,
            "shopping": user.shopping,
            "happy": user.happy,
            "erands": user.erands,
            "rides": user.rides,
            "childcare": user.childcare,
            "eldercare": user.eldercare,
            "petcare": user.petcare,
            "tutoring": user.tutoring,
            "home": user.home,
            "landscape": user.landscape,
            "latitude": user.latitude,
            "longitude": user.longitude
        })
    app.logger.info(f"Retrieved {len(user_data)} users from the database.")
    app.logger.info(user_data)
    user_data_length = len(user_data)
    print(user_data_length)

    user_length = len(users)
    print("length_user",user_length)


    return jsonify(user_data)





        



    



if __name__ == '__main__':
    with app.app_context():
     db.create_all() 
    #  socketio.run(app, host='192.168.42.106', port=5000, debug=True)
     app.run(debug=True)
