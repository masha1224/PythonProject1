from flask import Flask, request

app = Flask(__name__)

# Strona główna
@app.route('/')
def home():
    return "Witaj na stronie głównej!"

# /calculate
@app.route('/calculate')
def calculate():
    """ Execute given calculation on given numbers"""
    op = request.args.get('op', type=str)
    arg1 = request.args.get('arg1', type=int)
    arg2 = request.args.get('arg2', type=int)

    if op == 'sum':
        return f"<b>{arg1} + {arg2} = {arg1 + arg2}</b>"

    return "Operation not recognized"

if __name__ == '__main__':
    app.run()