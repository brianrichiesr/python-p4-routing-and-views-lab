#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<string:user_str>")
def print_string(user_str):
    print(f"{user_str}")
    return f"{user_str}"

@app.route("/count/<int:user_int>")
def count(user_int):
    count = ""
    for num in range(0, user_int):
        count += f"{num}\n"
    return count

@app.route("/math/<int:num1>/<string:operation>/<int:num2>")
def math(num1, operation, num2):
    if operation == "+":
        return f"{num1 + num2}"
    if operation == "-":
        return f"{num1 - num2}"
    if operation == "*":
        return f"{num1 * num2}"
    if operation == "div":
        return f"{num1 / num2}"
    if operation == "%":
        return f"{num1 % num2}"

if __name__ == '__main__':
    app.run(port=5555, debug=True)
