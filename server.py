from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = 'OWNOWbrownCOW1983'

@app.route('/')
def survey_form():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def result():
    session['name'] = request.form['full_name']
    session['location'] = request.form['location']
    session['favorite_language'] = request.form['favorite_language']
    session['comments'] = request.form['comments']
    # print(request.form)
    # return render_template('results.page.html') #to test if we got information through the form
    return redirect('/result')

@app.route('/result')
def results_page():
    return render_template('results_page.html', name = session['name'],
    location = session['location'], favorite_language = session['favorite_language'],
    comments = session['comments'])

@app.route('/<path:path>')
def not_found(path):
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)