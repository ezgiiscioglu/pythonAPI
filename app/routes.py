from flask import render_template, request, redirect
from app import app, db
from app.models import Entry

jedi = "of the jedi"

@app.route('/')
@app.route('/index')
def index():
    entries = db.session.query(Entry)
    print(type(entries))
    if request.args.get("year") != None:
        entries=entries.filter(Entry.year==request.args.get("year"))
    if request.args.get("brand") != None:
        entries=entries.filter(Entry.model==request.args.get("model"))
    if request.args.get("extcolor") != None:
        entries=entries.filter(Entry.model==request.args.get("model"))
    if request.args.get("trans") != None:
        entries=entries.filter(Entry.model==request.args.get("model"))

    return render_template('index.html', entries=entries.all())

@app.route('/add', methods=['POST'])
def add():
    year = db.Column(db.String(64), index=True, nullable=False)
    model = db.Column(db.String(120), index=True, nullable=False)
    extcolor = db.Column(db.String(120), index=True, nullable=False)
    intcolor = db.Column(db.String(120), index=True, nullable=False)
    transmission = db.Column(db.String(120), index=True, nullable=False)
    price = db.Column(db.String(120), index=True, nullable=False)
    contact = db.Column(db.String(120), index=True, nullable=False)


    if request.method == 'POST':
        form = request.form
        year = form.get('year')
        model = form.get('model')
        extcolor = form.get('extcolor')
        intcolor = form.get('intcolor')
        transmission = form.get('transmission')
        price = form.get('price')
        contact = form.get('contact')
        if not year or model or extcolor or intcolor or transmission or price or contact:
            entry = Entry(year = year, model = model, extcolor = extcolor, intcolor = intcolor, transmission = transmission, price = price, contact = contact)
            db.session.add(entry)
            db.session.commit()
            return redirect('/')

    return "of the jedi"

# @app.errorhandler(Exception)
# def error_page(e):
#     return "of the jedi"