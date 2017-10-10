from flask import Flask, render_template, session, request, redirect, url_for
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'change to environ variable later'

@app.route('/')
def future_dash():
    test_message = 'This is a test!'
    return render_template('future_dash.html', the_test=test_message)

# @app.route('/will_not_hit', methods=['GET', 'POST'])
# def index():
#     form = {}
#     if form.validate_on_submit():
#         old_name = session.get('name')
#         session['name'] = form.name.data
#         form.form_name.data = ''
#         return redirect(url_for('index'))
#     return render_template('index.html', form=form, name=session.get('name'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')