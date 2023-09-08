from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    title = 'Главная'
    return render_template('base.html', title=title)


@app.route('/shoes/')
def shoes():
    title = 'Обувь'
    return render_template('shoes.html', title=title)


@app.route('/jacket/')
def jacket():
    title = 'Куртка'
    return render_template('jacket.html', title=title)

@app.route('/cloth/')
def cloth():
    title = 'Одежда'
    return render_template('cloth.html', title=title)

if __name__ == '__main__':
    app.run(debug=True)