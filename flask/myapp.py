from flask import*
app=Flask(__name__) #flask file

@app.route("/") # "/" should always be there
@app.route("/home")

def home():
    return "<h1>Welcome to Home Page</h1>"
@app.route("/aboutus")
def aboutus():
    return "<h1>Welcome to about us page</h1>"
@app.route("/something")
def page2():
    return render_template("something.html")
@app.route("/newthing")
def page3():
    var="Rohit"
    return render_template("newthing.html",data=var)



if (__name__=="__main__"):
    app.run(debug=True) #no need to close cmd again and again
