from flask import Blueprint

main=Blueprint("main",__name__,url_prefix="/")


@main.route('/')
def homePage():
    return "<h1>Home Page</h1>"


@main.route('/about')
def aboutPage():
    return "<h1>About Page</h1>"




@main.route('/contact')
def contactPage():
    return "<h1>Contact Page</h1>"