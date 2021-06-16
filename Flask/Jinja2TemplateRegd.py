'''
Jinja2 Template Regd.
{%...%} conditionl statements and for loops
{{ }} expressions to print output
{# ...#} Internal Comments 
'''


from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__)

@app.route('/')  
def home():  
    return render_template("index.html") 

@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score = 0
    if request.method=="POST":
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        english = float(request.form['english'])
        social = float(request.form['social'])
        total_score = ((science+maths+english+social)/4)
    return redirect(url_for('success',count=total_score))
'''
@app.route('/success/<int:count>')
def success(count):
    return render_template("result_1.html",result=count)
'''

@app.route('/success/<int:count>')
def success(count):
    res=""
    if count >= 50:
        res = "PASS"
    else:
        res = "FAIL"
    exp={'score':count,'result':res}
    return render_template("result_2.html",result=exp)

@app.route('/back',methods=['POST','GET'])
def back():
    return redirect(url_for('home'))

if __name__ =='__main__':
    app.run(debug=True)