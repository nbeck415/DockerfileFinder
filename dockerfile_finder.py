import requests, os
from dotenv import load_dotenv

n_stars = 1000
pages = 10
sort = 'stars'
order = 'desc'
per_page = 100
cur_topic = "hacktoberfest"
target_filenames = ["Dockerfile", "docker-compose.yaml", "docker-compose.yml", "compose.yaml", "compose.yml"]

def setup():
    load_dotenv()
    token = os.getenv('GH_ACCESS')

    auth = {'Authorization': f'Bearer {token}'}
    return auth

def get_topics():
    url = 'https://api.github.com/search/topics?q=language'
    response = requests.get(url)
    
    if response.status_code == 200:
        topics = response.json()
        topic_names = []
        for topic in topics['items']:
            topic_names.append(topic['name'])
        topic_names.remove("language")
        topic_names.remove("programming-language")
        return topic_names[:15]
    else:
        print(f"Status code: {response.status_code}")
        return []

def find_dockerfile(auth, stars=n_stars, topic=cur_topic):
    repo_addrs = []
    url = f'https://api.github.com/search/repositories?q=topic:{topic}&sort={sort}&order={order}&per_page={per_page}&stars:>{stars}'
    response = requests.get(url, headers=auth)
    if response.status_code == 200:
        data = response.json()
        popular_repos = data.get('items', [])
        for repo in popular_repos:
            name = repo['name']
            owner = repo['owner']['login']
            desc = repo['description']
            star_ct = repo['stargazers_count']
            repo_url = f'https://api.github.com/repos/{owner}/{name}/contents'
            headers = {'Authorization': auth['Authorization'], 'Accept': 'application/vnd.github.v3.raw'}
            contents = requests.get(repo_url, headers=headers)
            repo_contents = contents.json()
            for item in repo_contents:
                if item['name'] in target_filenames:
                    found_file = item['name']
                    repo_addr = (owner, name, desc, star_ct)
                    if repo_addr not in repo_addrs:
                        repo_addrs.append(repo_addr)
                    print(f'{found_file} found in {owner}/{name}')
    else:
        print(f'Status code: {response.status_code}')
    return repo_addrs
'''
def main():
    auth = setup()
    topics = get_topics()
    repos = find_dockerfile(auth)
    print(topics)

if __name__ == "__main__":
    main()
'''
