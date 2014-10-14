
        
from flask import Flask, render_template, request
app = Flask(__name__)

#def processWho(L):
#def processWhen(L):

@app.route("/", methods=["GET","POST"])
def run():
    if request.method=="GET":
        return render_template("cover.html")
    else:
        query = request.form["search"]
        query = query.lower()
        terms = query.split(" ")
        if "who" in terms:
            processWho(terms)
        elif "when" in terms:
            processWhen(terms)
        else:
            return redirect("/error")

@app.route("/error")
def error():
    out = "<html>Sorry we couldn't process your search request. Try again!</html>"
    return out

if __name__ == "__main__":
    app.debug = True
    app.run()
