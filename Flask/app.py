from flask import Flask

app = Flask(__name__)

@app.route('/home')  
def home():  
    return "Hello, Welcome to our website";  


@app.route('/message')  
def message():  
    return "Hello, Welcome to Message Page";  


def about():  
    return "This is about Page";  

def details():
    return "Details Page"
  
app.add_url_rule("/about","about",about) 
app.add_url_rule("/details","details",details) 

if __name__ =="__main__":
    app.run(debug=True)