from backend.db import db




class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(100),nullable=False)
  email = db.Column(db.String(50))  
  contact = db.Column(db.String(200))
  password = db.Column(db.String(10))


  def __init__(self, name, email,contact,password):
   self.name = name
   self.email = email
   self.contact = contact
   self.password = password


  def __repr__(self):
        return f"<User {self.email} >"
  

        
   #save a new instance
  def save(self):
        db.session.add(self)
        db.session.commit()

   #delete the item
  def delete(self):
        db.session.delete(self)
        db.session.commit()
 