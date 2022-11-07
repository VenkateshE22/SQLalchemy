from main import User, Session, engine

local_session = Session(bind=engine)
#return all objects
users = local_session.query(User).all()

for user in users:
    print(user.username)

#query to return a specific record
# tom=local_session.query(User).filter(User.username=="Tom").first()
# print(tom)