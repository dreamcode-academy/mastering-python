from flask import Flask, render_template, jsonify, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange
import os
from models import db, Car

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cars.db'
db.init_app(app)

with app.app_context():
    db.create_all()


cars=[
    {"id":1, "make":"Toyota", "model":"Yaris"},
    {"id":2, "make":"Ford", "model":"Escape"}
]

if 'SECRET_KEY' in os.environ:
    app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
else:
    raise ValueError("There is no SECRET_KEY")

class CarForm(FlaskForm):
    make = StringField('Make', validators=[DataRequired(), Length(min=2, max=100)])
    model = StringField('Model', validators=[DataRequired(), Length(min=2, max=100)])
    year = IntegerField('Year', validators=[DataRequired(), NumberRange(min=1900, max=2024)])
    submit = SubmitField('Add Vehicle')

# Database
def get_all_cars():
    return Car.query.all()


def add_new_car(make, model, year):
    new_car = Car(make = make, model = model, year = year)
    db.session.add(new_car)
    db.session.commit()
    return new_car

def get_car_by_id(id):
    return Car.query.get(id)

def update_car_by_id(id, make, model, year):
    car = get_car_by_id(id)
    if car:
        car.make = make
        car.model = model
        car.year = year
        db.session.commit()
        return car
    return None

def delete_car_by_id(id):
    car = get_car_by_id(id)
    if car:
        db.session.delete(car)
        db.session.commit()
        return True
    return False





# Views
    
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/view-cars')
def view_cars():
    cars = get_all_cars()
    return render_template('view-cars.html', cars = cars)



@app.route('/car/<int:id>')
def car_details(id):
    return f'<h2>Details for Car ID: {id}</h2>'


@app.route('/add-car', methods=['GET', 'POST'])
def add_car_view():
    form = CarForm()
    if form.validate_on_submit():
        new_car = add_new_car(form.make.data, form.model.data, form.year.data)
        return f'Car {new_car.id} added succesfully!'
       
    return render_template('add-car.html', form=form)


@app.route('/update-car/<int:id>', methods=['PUT'])
def update_car_view(id):
    return f'Car with id {id} has been updated!'


@app.route('/delete-car/<int:id>', methods=['DELETE'])
def delete_car_view(id):
    return f'Car with id {id} has been deleted!'


# API RESTful

# Read
@app.route('/cars', methods=['GET'])
def get_cars_api():
    cars = get_all_cars()
    return jsonify([{'id':car.id,'make':car.make, 'model':car.model, 'year':car.year} for car in cars])

#Create
@app.route('/cars', methods=['POST'])
def add_car_api():
    new_car_data = request.json
    new_car = add_new_car(new_car_data['make'], new_car_data['model'], new_car_data['year'])
    if new_car:
        return jsonify({'id':new_car.id, 'make':new_car.make, 'model':new_car.model, 'year': new_car.year}), 201
    return jsonify({"message": "Bad request"}), 400
    
   
    

#Update


@app.route('/cars/<int:id>', methods=['PUT'])
def update_car_api(id):
    update_data = request.json
    car = update_car_by_id(id, update_data['make'], update_data['model'], update_data['year'])
    if car:
        return jsonify({'id':car.id, 'make':car.make, 'model':car.model, 'year': car.year})       
    return jsonify({"message": "Car not found"}), 404    
 
    
#Delete
    
@app.route('/cars/<int:id>', methods=['DELETE'])
def delete_car_id(id):
    if delete_car_by_id(id):
        return jsonify({"message":"Car deleted"}), 200
    else:
        return jsonify({"message": "Car not found"}), 404










if __name__ == '__main__':
    app.run(debug=True)