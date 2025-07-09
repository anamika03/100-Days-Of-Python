class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.name = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1 

user_1 = User("001", "angela")

print(user_1.id, user_1.name)
# user_2 = User()
# user_2.id = "002"
# user_2.name = "Jack"
# instead of these 3 lines now we can write it in 1 line because of the self & __init__ method /function
user_2 = User("002", "Krishan")
print(user_2.id, user_2.name)
print(user_1.followers, user_2.followers)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
