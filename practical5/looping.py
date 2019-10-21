from flask import Flask, render_template
app = Flask(__name__)

@app.route('/users/')
def users():
    names = ['Simon', 'Your', 'Ma', 'Is', 'Ur', 'Da']
    return render_template('looping.html', names=names)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
