import datetime
from flask import Flask, render_template,request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    parameter = request.args.get('parameter')
    return render_template('index.html', utc_dt=datetime.datetime.utcnow(),parameter=parameter)



if __name__ == '__main__':
    app.run()
