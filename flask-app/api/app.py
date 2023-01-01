from flask import Flask, jsonify, render_template, request
from utilities import predict_pipeline

app = Flask(__name__)

@app.get("/")
def home():
    # return "Hello, World!"
    return render_template("home.html")

@app.post('/check')
def check():
    data = request.form.get("tweet")
    print(data)
    try:
        sample = data
    except KeyError:
        return jsonify({'error': 'No text sent'})

    sample = [sample]
    predictions = predict_pipeline(sample)
    try:
        result = jsonify(predictions[0])
    except TypeError as e:
        result = jsonify({'error': str(e)})
    return result
    return render_template("home.html")

    
