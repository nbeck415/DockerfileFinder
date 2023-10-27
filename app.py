from flask import Flask, render_template, request
import dockerfile_finder as dff

app = Flask(__name__)
auth = dff.setup()

@app.route('/')
def index():
    topics = dff.get_topics()
    return render_template('index.html', topics=topics)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        print(request.form.get('num-stars'))
        print(request.form.get('topics'))
        repos = dff.find_dockerfile(auth, stars=request.form.get('num-stars'), topic=request.form.get('topics'))
        print(len(repos))
        if len(repos) == 0:
            repos=-1
        return render_template('results.html', repos=repos)
    return render_template('results.html', repos=repos)

if __name__ == '__main__':
    app.run(debug=True)
