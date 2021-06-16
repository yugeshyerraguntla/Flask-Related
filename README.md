# Flask-Related

- Flask is a web framework(micro-framework) that provides libraries to build lightweight web applications in python. {Developed by POCCO}
- Based on WSGI toolkit and jinja2 template engine

- WSGI: web server gateway interface. universal interface between the web server and web application.
- Jinja2: web template engine which combines a template with a certain data source to render the dynamic web pages.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

from flask import Flask  
  
app = Flask(_name_) #creating the Flask class object   
 
@app.route('/') #decorator drfines the   
def home():  
    return "hello, this is our first flask website";  
  
if __name__ =='__main__':  
    app.run(debug = True)  
    
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1. app.route(rule, options)  - rule: It represents the URL binding with the function. options: It represents the list of parameters to be associated with the rule object
2. app.run(host, port, debug, options)  
3. add_url_rule()
    - app.add_url_rule("/about","about",about)  
    - app.add_url_rule("/details","details",details)  

4. HTTP Methods
    - <form action="/submit" method="POST"> ; @app.route('/login',methods = ['POST', 'GET'])
    - GET, POST, PUT, DELETE, HEAD
  
5. From one function path to another path:
    - return redirect(url_for('success',count=total_score))
  
  
5. Templates: Instead of harcoding HTML in the def message(): we can use Templates folder and place htmls. (Rendering external HTML)
    - We need to import redirect,url_for,render_template,request
    - render_template() function which can be used to render the external HTML file. return render_template('message.html') 

6. Using Delimiters - Jinja2 Templates for dynamic data representation. 
    - {% ... %} for statements
    - {{ ... }} for expressions to print to the template output
    - {# ... #} for the comments that are not included in the template output
  This can be used to embed the simple python statements into the HTML.
  
7. To include CSS and JavaScript - Create a 'static' folder and inside that place CSS and JavaScript files.
    - Include the css and js in HTML head tag as     <link rel= "stylesheet" type= "text/css" href= "{{ url_for('static',filename='style/css.css') }}">
  
8. 
  
