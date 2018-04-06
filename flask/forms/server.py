from flask import Flask, render_template, request, redirect
flask_app = Flask(__name__)

# '/' is the URL we put into our browser
@flask_app.route('/')
def index():
    some_str = 'this is proof'
    # access templates folder, makes HTML real
    # something=some_str => variable we can pass in so that we can use that var in template
    return render_template('index.html', something=some_str)

# same URL...different method
# POST is issued from the form in HTML
@flask_app.route('/', methods=['POST'])
def index_post():
    # x = [1,2,3] => x[0]
    # request.form = {'username': whatever_i_typed_in} => request.form['username']
    print request.form['username'] # print username entered in form
    print request.headers
    return redirect('/') # takes back to the route in parenthesis

flask_app.run(debug=True)
