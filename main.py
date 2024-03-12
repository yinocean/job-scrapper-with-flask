from flask import Flask, render_template, request, redirect, send_file
from extrators.berlin import Berlin_Scrapper
from extrators.wework import Wework_Scrapper
from extrators.web3 import Web3_Scrapper
from file import save_to_file


app = Flask("JobScrapper")
db = {}

@app.route("/")
def home():
    return render_template("home.html",\
                           name="ocean")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword in db:
        jobs = db[keyword]
    if keyword == None:
        return redirect("/")
    else:
        berlin = Berlin_Scrapper.scrape_page(keyword)
        wework = Wework_Scrapper.scrape_page(keyword)
        web3 = Web3_Scrapper.scrape_page(keyword)
        jobs = berlin + wework + web3
        db[keyword] = jobs
    if jobs == None or jobs == "":
        return redirect("/")
    return render_template("search.html", keyword=keyword, jobs=jobs)


@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None or keyword == "":
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    
    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)

app.run(("0.0.0.0"))