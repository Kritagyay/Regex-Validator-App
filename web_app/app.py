from flask import Flask, render_template, request, redirect
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    test_string = ""
    regex = ""
    if request.method == 'POST':
        test_string = request.form.get('test_string')
        regex = request.form.get('regex')
        email = request.form.get('email')
        if email == 'yes':
            return redirect("/validate")
        else:
            return redirect("/results")
    return render_template('index.html', test_string=test_string, regex=regex)

@app.route("/results", methods=["GET","POST"])
def results():
    test_string = request.form.get("test_string")
    regex = request.form.get("regex")
    matches = []
    error = ""
    try:
        pattern = re.compile(regex)
        matches = pattern.findall(test_string)
    except re.error as e:
        error = "Invalid regular expression: " + str(e)
    return render_template("index.html", test_string=test_string, regex=regex, matches=matches, error=error)


@app.route("/validate", methods=["GET","POST"])
def validate():
    
    email = request.form.get("email")
    valid = False
    invalid = False
    pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
    if pattern.match(email):
        valid = True
    else:
        invalid = True
        
    return render_template("index.html", email=email, valid=valid, invalid=invalid)

if __name__ == '__main__':
    app.run(debug=True)
