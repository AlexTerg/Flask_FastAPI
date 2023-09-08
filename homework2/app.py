# Создать страницу, на которой будет форма для ввода имени 
# и электронной почты, при отправке которой будет создан cookie-файл 
# с данными пользователя, а также будет произведено перенаправление на страницу приветствия, 
# где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка «Выйти», 
# при нажатии на которую будет удалён cookie-файл с данными пользователя и 
# произведено перенаправление на страницу ввода имени и электронной почты.

from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key ='5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['user'] = {'name': request.form.get('name'),
                           'mail': request.form.get('mail')}
        return redirect(url_for('login'))
    return render_template('base.html')

@app.route('/login/')
def login():
    if 'user' in session:
        return render_template('login.html', name=session['user'].get('name'))
    else:
        return redirect(url_for('index'))
    
@app.route('/logout/')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
