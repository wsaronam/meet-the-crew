from flask import Flask
import helper


app = Flask(__name__)

@app.route("/")
def index():
  return '''
  <h1>Meet the Crew!</h1>
  <p>Look through the links provided to see if you want to meet the Strawhat pirates!</p>
  <ul>
    <li><a href="/crewmates/thousandsunny">Thousand Sunny</a></li>
    <li><a href="/crewmates/chopper">Captain Chopper</a></li>
    <li><a href="/crewmates/crewmates">Other Crewmates</a></li>
  </ul>
  '''

@app.route("/crewmates/<string:crewmate_name>")
def crewmates(crewmate_name):
  html = f"<h1>Meet the crewmates: {crewmate_name} </h1>"
  return html