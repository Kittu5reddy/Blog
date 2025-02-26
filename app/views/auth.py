from flask import Blueprint,redirect,url_for,render_template

auth=Blueprint("auth",__name__,url_prefix="/auth")


@auth.route('/login')
def loginPage():
    return render_template('auth/login.html')

@auth.route('/signup')
def signupPage():
    return render_template('auth/signup.html')


@auth.route('/logout')
def logout():
    return redirect('signup')

