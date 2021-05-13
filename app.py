from flask import Flask, render_template, url_for

app = Flask(__name__) #создаем обьект на основе класса фласк


#отслеживание адрессов
@app.route('/') #main page - '/'
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/help')
def about():
    return render_template("help.html")


@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "user page: " + name + " - " + str(id)


if __name__ == '__main__':
    app.run(debug=True)
