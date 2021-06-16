# HTTP verbs GET and POST # We should import and use 'request' for this

# Integrate with HTML
# We will use render_template for bringing in required HTML file. All the html files should be in templates


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

@app.route('/success/<int:count>')
def success(count):
    res= ""
    if count>50:
        res="Pass"
    else:
        res="Fail"

    return render_template("result.html",result=res)



"""  
@app.route('/fail/<int:count>')
def fail(count):
    return "Your Result is Fail and Your Score is"+ str(count);

@app.route('/passed/<int:count>')
def passed(count):
    return "Your Result is Pass and Your Score is"+ str(count);
"""


if __name__ =='__main__':
    app.run(debug=True)