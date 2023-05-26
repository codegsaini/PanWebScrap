from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = "Content-Type"

api = Api(app)

class Main(Resource):
    @staticmethod
    def get():
        return "Panda Web Scrapper is working"


class CyberSecuritySkills(Resource):
    @staticmethod
    def post():
        jobType=request.json['type']
        jobSite=request.json['site']
        url="https://www.naukri.com/cyber-security-jobs"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        articles = soup.find_all("article", class_="jobTuple")
        dictionary = {}
        for article in articles:
            link = article.find("a", class_="title", href=True)
            href = link['href']
            specificJob = requests.get(href)
            soup = BeautifulSoup(specificJob.content, "html.parser")
            skills = soup.find("div", class_="key-skill")
            skillList = skills.find_all('a', href=True, class_="chip")
            for skill in skillList:
                dictionary["link['title']"] = skill
        return page.text


api.add_resource(Main, "/api/")
api.add_resource(CyberSecuritySkills, "/api/cyber-security-skills")

if __name__ == "__main__":
    app.run()
