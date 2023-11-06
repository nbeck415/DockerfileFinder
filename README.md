# DockerfileFinder
Use GitHub API to find all popular repos with Dockerfiles and Compose files

## Setup
Generate a GitHub personal access token (PAT) and give it repo permissions. Save it as an env var called `GH_ACCESS`. The program ingests env vars from a `.env` file.

Run `pip install requirements.txt` in the project's root.

## Usage
Run `python app.py` and go to `http://127.0.0.1:5000/` to access the app. 
