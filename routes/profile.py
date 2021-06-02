from __main__ import app, render_template

@app.route('/test',methods=['GET'])
def test():
    return "It works!"

@app.route('/profile')
def profile():
    return render_template('user_profile/preview_profile.html')
