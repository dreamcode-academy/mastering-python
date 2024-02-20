from flask import Flask, request, jsonify, url_for, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/items')
def items():
    items = ['Apple', 'Banana', 'Cherry']
    return render_template('items.html', items = items)

@app.route('/welcome/<username>')
def welcome(username):
    return render_template('welcome.html',username=username)





@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/data')
def data():
    return jsonify({'message':'This is a JSON response'})


@app.route('/user')
def user_list():
    return f'User list: {url_for("show_user_profile", username="Alice")}'

@app.route('/user/<username>')
def show_user_profile(username):
    return f"User: {username}"




if __name__ == '__main__':
    app.run(debug = True)

