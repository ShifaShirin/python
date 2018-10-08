from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/About us')
def ab():
    return render_template('about.html')


@app.route('/Contact')
def con():
    return render_template('contact.html')


@app.route('/send', methods=['GET', 'POST'])
def send():
    if(request.method == 'POST'):
        Name = request.form['getname']
        Email = request.form['getemail']
        return render_template('success.html', myname=Name, myemail=Email)


if(__name__ == '__main__'):
    app.run(debug=True)
