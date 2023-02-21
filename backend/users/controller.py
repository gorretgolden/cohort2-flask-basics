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
      

#    @app.route('/cars/<car_id>', methods=['GET', 'PUT', 'DELETE'])
# def handle_car(car_id):
#     car = CarsModel.query.get_or_404(car_id)

#     if request.method == 'GET':
#         response = {
#             "name": car.name,
#             "model": car.model,
#             "doors": car.doors
#         }
#         return {"message": "success", "car": response}

#     elif request.method == 'PUT':
#         data = request.get_json()
#         car.name = data['name']
#         car.model = data['model']
#         car.doors = data['doors']
#         db.session.add(car)
#         db.session.commit()
#         return {"message": f"car {car.name} successfully updated"}

#     elif request.method == 'DELETE':
#         db.session.delete(car)
#         db.session.commit()
#         return {"message": f"Car {car.name} successfully deleted."}   
  
        
  
   
