from flask import Flask, render_template



app = Flask(__name__)

@app.route('/play', defaults = {'number': 3, 'color': "aqua"})
@app.route('/play/<int:number>', defaults = {'color': "aqua"})
@app.route('/play/<int:number>/<string:color>')
def play(number , color):
    return render_template('index.html', count = number , color = color)




if __name__ == "__main__":
    app.run(debug=True, port = 5000)