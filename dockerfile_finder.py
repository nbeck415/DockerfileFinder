import requests, os
from dotenv import load_dotenv

def setup():
    load_dotenv()
    token = os.getenv('GH_ACCESS')

    auth = {'Authorization': f'Bearer {token}'}
    return auth
    

def find_dockerfile(auth):
    repo_addrs = []
    url = 'https://api.github.com/search/repositories?q=sort=stars&order=desc&per_page=100'
    response = requests.get(url, headers=auth)
    if response.status_code == 200:
        data = response.json()
        popular_repos = data.get('items', [])
        for repo in popular_repos:
            name = repo['name']
            owner = repo['owner']['login']
            repo_url = f'https://api.github.com/repos/{owner}/{name}/contents'
            contents = requests.get(repo_url, headers=auth)
            repo_contents = contents.json()
            for item in repo_contents:
                if item['name'] == 'Dockerfile':
                    repo_addrs.append((owner, name))
    else:
        print(f'Status code: {response.status_code}')
    return repo_addrs

def main():
    auth = setup()
    repos = find_dockerfile(auth)
    print(repos)

if __name__ == "__main__":
    main()