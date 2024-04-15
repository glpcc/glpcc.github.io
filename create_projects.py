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
        img_name = input("Enter the image name: ")
        repo["image_name"] = img_name
        wanted_repos.append(repo)

full_html = ''
# Create the card html
def create_card(repo_link, repo_name, repo_description,image_name):
    return f"""
        <a href="{repo_link}">
          <div class="card zoom-btn">
            <img class="card-img-top" src="/static/projects/{image_name}" alt="Clustering Project">
            <div class="card-body">
              <h5 class="card-title" id="text-title-clustering2">{repo_name}</h5>
              <p class="card-text" id="text-description-clustering2">{repo_description}</p>
            </div>
          </div>
        </a>
    """

columns = 3
for repo in wanted_repos:
    full_html += create_card(repo["html_url"], repo["name"], repo["description"],repo["image_name"])

print(full_html)