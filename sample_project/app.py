from flask import Flask

app = Flask(__name__)

def home():
    return "Hello World"

username = "default_user"
print(username)

print("End of file")