from main import User, Session, engine


users = [
    {
        "username": "Tom",
        "email": "Tom@company.com"
    },
    {
        "username": "Ramesh",
        "email": "Ramesh@company.com"
    },
    {
        "username": "Payal",
        "email": "Payal@rastogi.com"
    },
]
local_session = Session(bind=engine)

for u in users:
    new_user = User(username=u["username"], email=u["email"])
    local_session.add(new_user)
    local_session.commit()
    print(f"Added {u['username']}")