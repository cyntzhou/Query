
        
from flask import Flask, render_template, request
from search import searchx
app = Flask(__name__)

#def processWho(L):
#def processWhen(L):

@app.route("/") #,methods=["GET","POST"]
def run():
    #if request.method=="GET":
    #button = request.form["submit"]
    #query = request.form["search"]
    #return redirect("/error")
    button = request.args.get("submit",None)
    query = request.args.get("search",None)
    if button==None:
        return render_template("cover.html")
    elif button=="submit":
        answer = searchx("Who are you?")[0]
        return render_template("results.html",query=query, answer=answer)

@app.route("/results")
def results():
    answer = searchx("Who are you?")[0]
    return render_template("results.html",query="Who are you?", answer=answer)

@app.route("/error")
def error():
    out = "<html>Sorry we couldn't process your search request. Try again!</html>"
    return out

if __name__ == "__main__":
    app.debug = True
    app.run()
