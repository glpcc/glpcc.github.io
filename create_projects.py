# Script to create card html based on github repos

import requests
import json

# Get the list of repos
url = "https://api.github.com/users/glpcc/repos"

response = requests.get(url)
repos = json.loads(response.text)

# Iterate through the repos and ask user if they want to create a card
wanted_repos = []
for repo in repos:
    print("Do you want to create a card for " + repo["name"] + "?")
    response = input("y/n: ")
    if response == "y":
        wanted_repos.append(repo)

full_html = '<div class="row">'
# Create the card html
def create_card(repo_link, repo_name, repo_description):
    return f"""
          <div class="container project">
            <a href="{repo_link}">
              <div class="card zoom-btn">
                <img class="card-img-top" src="" alt="">
                <div class="card-body">
                  <h5 class="card-title english" id="text-title-clustering">{repo_name}</h5>
                  <p class="card-text english" id="text-description-clustering">{repo_description}</p>
                  <h5 class="card-title spanish" id="text-title-clustering">{repo_name}</h5>
                  <p class="card-text spanish" id="text-description-clustering">{repo_description}</p>
                </div>
              </div>
            </a>
          </div>
    """

columns = 3
for repo in wanted_repos:
    if columns == 3:
        full_html += '</div><div class="row">'
        columns = 0
    full_html += create_card(repo["html_url"], repo["name"], repo["description"])

full_html += '</div>'
print(full_html)