

# 91. Book Library
class Library:
    def __init__(self):
        self.books = []

    def add(self, name):
        self.books.append(name)

lib = Library()
lib.add("Python")
print(lib.books)


# 92. Secure Password
class Password:
    def __init__(self, password):
        self.__password = password

    def verify(self, p):
        return self.__password == p

print(Password("123").verify("123"))


# 93. User Authentication
class Auth:
    users = {"admin": "1234"}

    def login(self, u, p):
        return self.users.get(u) == p

a = Auth()
print(a.login("admin", "1234"))


# 94. File Reader
class Reader:
    def read(self):
        return "Reading file"

r = Reader()
print(r.read())


# 95. Music Player
class Player:
    def play(self):
        return "Music playing"

print(Player().play())


# 96. Notification System
class Notification:
    def send(self):
        return "Notification sent"

class Email(Notification):
    pass

print(Email().send())


# 97. Shape Comparison
class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

print(Square(5).area())


# 98. Smart Home
class Lamp:
    def on(self):
        return "Lamp ON"

class Home:
    def __init__(self):
        self.lamp = Lamp()

h = Home()
print(h.lamp.on())


# 99. User Role
class User:
    def __init__(self, role):
        self.role = role

    def is_admin(self):
        return self.role == "admin"

print(User("admin").is_admin())


# 100. Chat System
class Message:
    def __init__(self, text):
        self.text = text

class Chat:
    def send(self, msg):
        return f"Sent: {msg.text}"

c = Chat()
print(c.send(Message("Hello")))

