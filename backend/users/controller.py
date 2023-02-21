#register a new user
from flask import  jsonify, request, Blueprint
# from validate_email import validate_email
from werkzeug.security import check_password_hash,generate_password_hash
from backend.users.model import User
from backend.db import db

users = Blueprint('users', __name__, url_prefix='/users')

#get all users
@users.route("/")
def all_users():
    users= User.query.all()
    results = [
            {
                "name": user.name,
                "email": user.email,
                "contact": user.contact
            } for user in users]

    return {"count": len(results), "users": results}


@users.route('/create', methods= ['POST',"GET"])
def create_user():
    if request.method == "POST":
          
          if request.is_json:
            data = request.get_json()
            new_user = User(name=data['name'], email=data['email'], contact=data['contact'],password=data['password'])
            db.session.add(new_user)
            db.session.commit()
            return {"message": f"car {new_user.name} has been created successfully."}
          else:
               return jsonify({'error':'Failed to register'}),400
   
    elif request.method == "GET":
        users= User.query.all()
        results = [
           {
                "name": user.name,
                "email": user.email,
                "contact": user.contact
            } for user in users]

        return {"count": len(results), "users": results}
      


#update,get and delete user by id
@users.route('/users/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_user(user_id):
    user = User.query.get_or_404(user_id)

    if request.method == 'GET':
        response = {
            "name": user.name,
            "email": user.email,
            "contact": user.contact,
            "password":user.password,
            "address":user.address
        }
        return {"message": "success", "user": response}

    elif request.method == 'PUT':
        data = request.get_json()
        user.name = data['name']
        user.email = data['email']
        user.contact = data['contact']
        user.address = data['address']
        user.password = data['password']
        db.session.add(user)
        db.session.commit()
        return {"message": f"User details of {user.name} successfully updated"}

    elif request.method == 'DELETE':
        db.session.delete(user)
        db.session.commit()
        return {"message": f"User {user.name} successfully deleted."}   
  
        
  
   
