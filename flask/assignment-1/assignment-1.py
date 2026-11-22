from flask import Flask, jsonify

app = Flask(__name__)

def check_prime(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

@app.route("/prime_number/<int(signed=True):number>", methods=["GET"])
def prime_number(number):
    return jsonify({"Number": number, "isPrime": check_prime(number)})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, use_reloader=True)