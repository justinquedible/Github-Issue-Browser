from flask import Flask, redirect, url_for, render_template
import requests, GithubIssueRequest


ISSUES_PER_PAGE = 10
app = Flask(__name__)


@app.route("/home/page<num>")
def home(num):
    num = int(num)
    currentIssuesList = GithubIssueRequest.getIssues(issues, (num-1)*ISSUES_PER_PAGE, ISSUES_PER_PAGE)
    return render_template("home.html", issuesList=currentIssuesList, num=num)


@app.route("/home/issue<number>")
def issueInfo(number):
    number = int(number)
    issueInfo = GithubIssueRequest.getIssueInfo(issues, number)
    return render_template("issueInfo.html", issue=issueInfo)


if __name__ == '__main__':
    response = requests.get("https://api.github.com/repos/walmartlabs/thorax/issues")
    issues = response.json()
    # page = 1
    app.run(debug=True)
