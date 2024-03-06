from flask import Flask, render_template, request
from extrators.berlin import Berlin_Scrapper
from extrators.wework import Wework_Scrapper
from extrators.web3 import Web3_Scrapper
from flask import jsonify
from werkzeug.exceptions import HTTPException
import traceback

app = Flask("JobScrapper")

@app.route("/")
def home():
    return render_template("home.html",\
                           name="ocean")

db = {

}

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    print()
    if keyword in db:
        jobs = db[keyword]
        
    else:
        berlin = Berlin_Scrapper.scrape_page(keyword)
        wework = Wework_Scrapper.scrape_page(keyword)
        web3 = Web3_Scrapper.scrape_page(keyword)
        jobs = berlin + wework + web3
        db[keyword] = jobs
    
    return render_template("search.html", keyword=keyword, jobs=jobs)

@app.errorhandler(Exception)
def all_exception_handler(e):
    error = str(traceback.format_exc())

app.run(("0.0.0.0"))