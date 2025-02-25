from flask import Blueprint,redirect,url_for

auth=Blueprint("auth",__name__,url_prefix="/auth")


@auth.route('/login')
def loginPage():
    return "<h1>Login Page</h1>"

@auth.route('/signup')
def signupPage():
    return "<h1>Signup Page</h1>"


@auth.route('/logout')
def logout():
    return redirect('signup')

