from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Cloud Computing Test</h1>
    <h2>Google Cloud PaaS (Render Alternative)</h2>
    <h3>Poloko Chaane</h3>
    """

if __name__ == "__main__":
    app.run()
