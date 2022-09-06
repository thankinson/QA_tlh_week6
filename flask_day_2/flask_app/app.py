from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render

# @app.route('/about', methods=['GET', 'POST'])
# def get_method():
#     if request.method == 'POST':
#         return 'This is a post request'
#     else:
#         return 'This is a get request'

# @app.route('/dynamic/<word>')
# def dynamic(word):
#     return word.upper()

# app.route('/math/<int:number>')
# def mathtimes(number):
#     result = number * 8
#     return f'{number} * 8 = {result}'

# ################################################
# ## user log in 
# def user_logged_in(user):
#     if user == 'tom':
#         return True
#     else:
#         return False

# @app.route('/login/<user>')
# def login(user):
#     if user_logged_in(user) == True:
#         return redirect(url_for('account'))
#     else:
#         return 'Login Fail'

# @app.route('/account')
# def account():
#     return 'user logged into account'

#########################################################

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)