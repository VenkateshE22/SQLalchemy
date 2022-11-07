from main import Session, engine, User

local_session = Session(bind=engine)

user_to_update=local_session.query(User).filter(User.username == "Tom").first()

user_to_update.username= "Tommy"
local_session.commit()