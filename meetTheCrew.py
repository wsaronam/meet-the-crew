from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  return '''
  <h1>Join the Crew!</h1>
  <p>Look through the links provided to see if you want to join the Strawhat pirates!</p>
  <ul>
    <li>Thousand Sunny</li>
    <li>Captain Chopper</li>
    <li>Crewmate Luffy</li>
  </ul>
  '''

@app.route("/crewmates/<string:crewmate_name>")
def crewmates(crewmate_name):
  html = "<h1>Meet the crewmate: {crewmate_name} </h1>"
  return html