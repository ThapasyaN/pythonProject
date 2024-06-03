# constructor is the part of the blueprint that allows us to specify what should happen when our
# object is constructed. It is also called as initialise.

# def __init__(self): - creating starting values to the attributes

# CONSTRUCTOR:
class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.user_name = user_name
        self.follower = 0
        self.following = 0

    def follow(self, user):
        user.follower += 1
        self.following += 1


user_1 = User("001", "Thapasya")
user_2 = User("002", "Sandeep")

user_1.follow(user_2)
print(f"user ones followers are: {user_1.follower}")
print(f"user ones followings are: {user_1.following}")
print(f"user two followers are: {user_2.follower}")
print(f"user two followings are: {user_2.following}")


class Car:
    def __init__(self, seats):
        print("The number of seats.")
        self.seats = seats


my_car = Car(3)
# or
my_car.seats = 2
