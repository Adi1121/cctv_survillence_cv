# app.py
from flask import Flask, render_template
from in_out import in_out
from motion import noise
from rect_noise import rect_noise
from record import record

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/in_out')
def in_out_route():
    in_out()
    return "In Out Function Executed"

@app.route('/noise')
def noise_route():
    noise()
    return "Noise Function Executed"

@app.route('/record')
def record_route():
    record()
    return "Record Function Executed"

@app.route('/rect_noise')
def rect_noise_route():
    rect_noise()
    return "Rect Noise Function Executed"

# This block is added for Lambda compatibility
def lambda_handler(event, context):
    with app.test_request_context(event['path'], method=event['httpMethod']):
        response = app.full_dispatch_request()

    return {
        'statusCode': response.status_code,
        'body': response.get_data(as_text=True),
        'headers': dict(response.headers)
    }
