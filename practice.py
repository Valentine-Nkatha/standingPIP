# def add_user(user_id,username,followers):
#     users={}
#     if user_id not in users:
#       users[user_id]={username,followers}
# print(add_user(1,"val",27))
# def add_follower(user_id, follower_id):
#     users={}
#     if user_id in users:
#         users[user_id]["followers"].append(follower_id)

# def remove_follower(user_id, follower_id):
#      users={}
#     if user_id in users:
#         users[user_id]["followers"].remove(follower_id)

# def get_followers(user_id):
#     if user_id in users:
#         return users[user_id]["followers"]
def initialize_users(users):
    users={}
    
def add_user(username,user_id,users):
    if user_id not in users:
        users[user_id]=[username]

def add_follower(users, user_id, follower):
    if user_id in users and follower not in users[user_id]:
        users[user_id].append(follower)

def get_user_and_followers(users,user_id):
    if user_id in users:
        return users[user_id]
    else:
        return None
    
add_user(users,1)
 

    
 