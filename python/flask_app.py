import pickle
from flask import Flask, request, render_template
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
cache.init_app(app)

@app.route('/' , methods=['GET', 'POST'])
def clipboard():
    if request.method == 'GET':
        try:
            form_data = cache.get('form_data')
        except KeyError:
            form_data=None
        return render_template('form.html', form_data=form_data)

    if request.method == 'POST':
        form_data = request.form
        cache.set('form_data', form_data)
        return render_template('form.html', form_data=form_data)

app.run(host='localhost', port=5000)
