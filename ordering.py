from main import Session, engine, User
from sqlalchemy import desc

local_session=Session(bind=engine)

users=local_session.query(User).order_by(User.username).all()

for user in users:
    print(f"User {user.username}")

users_dessc=local_session.query(User).order_by(desc(User.username)).all()

for user in users_dessc:
    print(f"User {user.username}")