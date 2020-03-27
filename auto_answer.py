from flask import Flask, render_template, redirect, request, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    title = StringField('Заголовок:', validators=[DataRequired()])
    surname = StringField('Фамилия:', validators=[DataRequired()])
    name = StringField('Имя:', validators=[DataRequired()])
    education = StringField('Образование:', validators=[DataRequired()])
    profession = StringField('Профессия:', validators=[DataRequired()])
    sex = StringField('Пол:', validators=[DataRequired()])
    motivation = StringField('Мотивация:', validators=[DataRequired()])
    ready = BooleanField('Вы точно готовы?')
    submit = SubmitField('Войти')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/answer', methods=['GET', 'POST'])
@app.route('/auto_answer', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        title = request.form["title"]
        surname = request.form["surname"]
        name = request.form["name"]
        education = request.form["education"]
        profession = request.form["profession"]
        sex = request.form["sex"]
        motivation = request.form["motivation"]
        ready = request.form["ready"]
        return render_template('auto_answer.html', title=title, surname=surname, name=name, education=education,
                               profession=profession, sex=sex, motivation=motivation, ready=ready)
    return render_template('handler.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.run(port=8080, host="127.0.0.1")
