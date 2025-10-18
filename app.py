from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from helper import text_preprocessing, vectorizer, get_prediction

app = Flask(__name__)

# Simple in-memory storage for demo purposes
data = dict()
comments = []  # list of dicts: {text, time}

reviews = []
positive = 0
negative = 0

@app.route('/')
def index():
    data['reviews'] = reviews
    data['positive'] = positive
    data['negative'] = negative
    data['updated'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', data=data, comments=comments)


@app.route('/comment', methods=['POST'])
def comment():
    text = request.form['comment']
    if text:
        comments.append({'text': text, 'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')})

    preprocessed_text = text_preprocessing(text)
    vectorizered_text = vectorizer(preprocessed_text)
    prediction = get_prediction(vectorizered_text)

    if prediction == 'Positive':
        global positive
        positive += 1
    else:
        global negative
        negative += 1

    reviews.insert(0, text)
    

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

