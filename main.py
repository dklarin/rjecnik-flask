from flask import Flask, render_template
from flask_bootstrap import Bootstrap

from komponente.rijeci_sve import rijeci

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.register_blueprint(rijeci)

@app.route('/')
def index():
    name = 'Baltazar'
    return render_template('index.html', name=name)

# error pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

#if __name__ == "__main__":
    #app.run(debug=True)
    #app.run(host='0.0.0.0', port=5000)
