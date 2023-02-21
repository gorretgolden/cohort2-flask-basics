from backend import create_app, db
from flask_migrate import Migrate
# We still need to create our models
# The following code you can comment out 
# if you want to run the application now
# Otherwise wait until we build these models next
from backend.users.model import User
from backend.profile.model import Profile



app = create_app('development')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
   return dict(db=db, User = User,Profile=Profile)