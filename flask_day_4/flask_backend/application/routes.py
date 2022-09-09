from flask import Flask, request, render_template
from application import app, db
from application.models import Games
from application.forms import AddGamesForm, DeleteGamesForm

@app.route('/')
@app.route('/add', methods=['GET', 'POST'])
def add():
    message = ""
    add_game_form = AddGamesForm()
    if add_game_form.validate_on_submit():
        if request.method == 'POST':
            new_game = Games(name=add_game_form.name.data.lower())
            db.session.add(new_game)
            db.session.commit()
            message = f'{add_game_form.name.data} added to database'
        else:
            message = "request was not a post please try again"
    # else:
    #     message = "Validation failed, try again"
    return render_template('add_game.html', form=add_game_form, message=message)

@app.route('/read')
def read():
    all_games = Games.query.all()
    # games_string = ""
    # for game in all_games:
    #     games_string += "<br>"+ game.name
    return render_template('read_game.html', games=all_games)

@app.route('/update/<name>')
def update(name):
    first_game = Games.query.first()
    first_game.name = name
    db.session.commit()
    return first_game.name

@app.route('/count')
def count():
    count_all = Games.query.count()
    return f"There is {count_all} games in database"

@app.route('/delete', methods=['GET','POST'])
def delete():
    message = ""
    delete_game_form = DeleteGamesForm()
    if request.method == 'POST':
        if delete_game_form.validate_on_submit():
            delete_game = Games.query.filter_by(name=delete_game_form.name.data.lower()).first()
            db.session.delete(delete_game)
            db.session.commit()
            message = f"{delete_game.name.capitalize()}: Has been removed from database"
        else:
            message = "Error could not remove game"
   
    return render_template('delete_game.html', form=delete_game_form, message=message)