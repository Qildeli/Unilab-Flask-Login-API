from flask import render_template, request, Blueprint

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route("/")
@main_blueprint.route("/home")
def home():
    return render_template('home.html')


@main_blueprint.route("/about")
def about():
    return render_template('about.html', title='About')