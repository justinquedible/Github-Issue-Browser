import requests


ISSUES_PER_PAGE = 10


def getIssues(issues, idx, count):
    """
    Given issues as a JSON object, index, and count, display the list of issues with some basic information (title,
    issue number, state). The list of issues start at the 'idx' position and show 'count' issues. Returns the list of
    issues as well.
    """
    issuesList = []
    print("-------------------------------------------------------------------------")
    print(f"Showing issues {idx+1} - {idx+count}\n")
    for issue in issues[idx: idx + count]:
        print("Title:        ", issue["title"])
        print("Issue Number: ", issue["number"])
        print("State:        ", issue["state"])
        print()
        issuesList.append({"title": issue["title"], "number": issue["number"], "state": issue["state"]})
    return issuesList


def getIssueInfo(issues, issueNum):
    """
    Given issues as a JSON object and an issue number, display more information on the issue at that index (title,
    issue number, state, owner, created time, body). Returns the information as well.
    """
    issue = [issue for issue in issues if issue["number"] == issueNum][0]
    print("-------------------------------------------------------------------------")
    print(f"Showing issue number: {issue['number']}\n")
    print("Title:        ", issue["title"])
    print("Issue Number: ", issue["number"])
    print("State:        ", issue["state"])
    name = requests.get(issue["user"]["url"]).json()["name"]
    print("Created by:   ", name)
    print("Created at:   ", issue["created_at"][:10], issue["created_at"][11:-1])
    print("Body:         ", issue["body"])
    print()
    return {"title": issue["title"], "number": issue["number"], "state": issue["state"],
            "created_by": issue["user"]["login"], "created_at": issue["created_at"], "body": issue["body"]}


def printWelcomeMessage():
    print("\n-------------------------------------------------------------------------")
    print("\nWelcome to the Github Issue Browser!")
    print("\n-------------------------------------------------------------------------\n")


def run():
    response = requests.get("https://api.github.com/repos/walmartlabs/thorax/issues")
    issues = response.json()
    printWelcomeMessage()
    page = 1
    while True:
        currentIssuesList = getIssues(issues, (page-1)*ISSUES_PER_PAGE, ISSUES_PER_PAGE)
        choice = int(input(f"[1] Select an issue\n"
                           f"[2] Go to another page (Current page: {page})\n"
                           f"[3] Quit\n"))
        if choice == 1:
            issueNum = int(input("Select an issue number\n"))
            # idx = [currentIssuesList.index(issue) for issue in currentIssuesList if issue["number"] == issueNum][0]
            getIssueInfo(issues, issueNum)
            input("Press Enter to go back\n")
        if choice == 2:
            page = int(input(f"What page do you want to go to? (Current page: {page})\n"))
        if choice == 3:
            break


if __name__ == '__main__':
    run()
