from flask import Flask, render_template, request, redirect
from models import db, Customer, Vehicle, Battery, ServiceRecord

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return redirect('/customers')

# ---------------- CUSTOMER ----------------
@app.route('/customers')
def customers():
    return render_template('customers.html', customers=Customer.query.all())

@app.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        c = Customer(
            name=request.form['name'],
            phone=request.form['phone'],
            address=request.form['address']
        )
        db.session.add(c)
        db.session.commit()
        return redirect('/customers')
    return render_template('add_customer.html')

# ---------------- VEHICLE ----------------
@app.route('/vehicles/<int:customer_id>')
def vehicles(customer_id):
    customer = Customer.query.get(customer_id)
    vehicles = Vehicle.query.filter_by(customer_id=customer_id).all()
    return render_template(
        'vehicles.html',
        customer=customer,
        vehicles=vehicles
    )

@app.route('/add_vehicle/<int:customer_id>', methods=['GET', 'POST'])
def add_vehicle(customer_id):
    if request.method == 'POST':
        v = Vehicle(
            customer_id=customer_id,
            vehicle_type=request.form['vehicle_type'],
            model_name=request.form['model_name'],
            registration_number=request.form['registration_number']
        )
        db.session.add(v)
        db.session.commit()
        return redirect(f'/vehicles/{customer_id}')
    return render_template('add_vehicle.html', customer_id=customer_id)

# ---------------- BATTERY ----------------
@app.route('/batteries/<int:vehicle_id>')
def batteries(vehicle_id):
    batteries = Battery.query.filter_by(vehicle_id=vehicle_id).all()
    return render_template(
        'batteries.html',
        batteries=batteries,
        vehicle_id=vehicle_id
    )

@app.route('/add_battery/<int:vehicle_id>', methods=['GET', 'POST'])
def add_battery(vehicle_id):
    if request.method == 'POST':
        b = Battery(
            vehicle_id=vehicle_id,
            brand=request.form['brand'],
            capacity=request.form['capacity'],
            date=request.form['date']
        )
        db.session.add(b)
        db.session.commit()
        return redirect(f'/batteries/{vehicle_id}')
    return render_template('add_battery.html', vehicle_id=vehicle_id)

# ---------------- SERVICE ----------------
@app.route('/services/<int:vehicle_id>')
def services(vehicle_id):
    services = ServiceRecord.query.filter_by(vehicle_id=vehicle_id).all()
    return render_template(
        'services.html',
        services=services,
        vehicle_id=vehicle_id
    )

@app.route('/add_service/<int:vehicle_id>', methods=['GET', 'POST'])
def add_service(vehicle_id):
    if request.method == 'POST':
        s = ServiceRecord(
            vehicle_id=vehicle_id,
            date=request.form['date'],
            problem=request.form['problem'],
            work=request.form['work'],
            cost=request.form['cost']
        )
        db.session.add(s)
        db.session.commit()
        return redirect(f'/services/{vehicle_id}')

    return render_template(
        'add_service.html',
        vehicle_id=vehicle_id
    )

# ---------------- INVOICE ----------------
@app.route('/invoice/<int:service_id>')
def invoice(service_id):
    service = ServiceRecord.query.get(service_id)
    return render_template(
        'invoice.html',
        service=service
    )


if __name__ == '__main__':
    app.run(debug=True)
