from flask import Flask, render_template
import dockerfile_finder as dff

app = Flask(__name__)

@app.route('/')
def index():
    topics = dff.get_topics()
    return render_template('index.html', topics=topics)

if __name__ == '__main__':
    app.run()
