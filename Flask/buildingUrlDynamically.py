from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/home')  
def home():  
    return "Hello, Welcome to our website";  


@app.route('/message/<title>')  
def message(title):  
    return "Hello, Welcome to Message Page" + " "+ title;  

@app.route('/success/<int:count>')
def success(count):
    return "This is Success Page"+ str(count);


app.add_url_rule("/message","message",message) 
app.add_url_rule("/success","success",success) 


@app.route('/fail/<int:count>')
def fail(count):
    return "Your Result is Fail and Your Score is"+ str(count);

@app.route('/passed/<int:count>')
def passed(count):
    return "Your Result is Pass and Your Score is"+ str(count);


## Result Checker
@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks<50:
        result='fail'
    else:
        result='passed'
    #return result
    return redirect(url_for(result,count=marks))



if __name__ =='__main__':
    app.run(debug=True)