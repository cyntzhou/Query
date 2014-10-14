
from  flask import Flask, render_template, request,redirect,url_for
import search 
app = Flask(__name__)

#def processWho(L):
#def processWhen(L):

@app.route("/", methods=["GET","POST"])
def run():
    if request.method=="GET":
        
        return render_template("cover.html")
    else:
        print " Post mode"
        query = request.form["searches"]
        
        terms = query.split(" ")
        
        if "who" in terms or "Who" in terms:
            result = search.searchx(query)
            return render_template("results.html",query= query,answer =result[0],answer2 = result[1])
        elif "when" in terms or "When" in terms:
           
            result = search.searchx(query)
            return render_template("results.html",query= query,answer =result[0],answer2 = result[1])
        else:
            return redirect(url_for('error'))


@app.route("/error")
def error():
    out = "<html>Sorry we couldn't process your search request. Please include <b>When</b> or <b>Who</b> in your search! <a href='/'>Try Again!<a> </html>"
    return out

if __name__ == "__main__":
    app.debug = True
    app.run()
