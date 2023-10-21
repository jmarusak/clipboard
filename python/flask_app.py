import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/' , methods=['GET', 'POST'])
def clipboard():
    form_data = pickle.load(open('form_data.p', 'rb'))

    if request.method == 'GET':
        return render_template('form.html', form_data=form_data)

    if request.method == 'POST':
        form_data = request.form
        pickle.dump(form_data, open('form_data.p', 'wb'))
        return render_template('form.html', form_data=form_data)
