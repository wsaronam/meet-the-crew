from flask import Flask
import helper


app = Flask(__name__)

@app.route("/")
def index():
  return '''
  <h1>Meet the Crew!</h1>
  <p>Look through the links provided to see if you want to meet the Strawhat pirates!</p>
  <ul>
    <li><a href="/crewmates/ship">Thousand Sunny</a></li>
    <li><a href="/crewmates/captain">Captain Chopper</a></li>
    <li><a href="/crewmates/crewmates">Other Crewmates</a></li>
  </ul>
  '''

@app.route("/crewmates/<string:crewmate_type>")
def crewmates(crewmate_type):
  html = f"<h1>Meet the crewmates: {crewmate_type} </h1>"
  html += "<ul>"
  loopCounter = 0
  for crewmate in helper.crew[crewmate_type]:
    crewmateText = f"<li><a href='/crewmates/{crewmate_type}/{loopCounter}'>{crewmate['name']}</a></li>"
    html += crewmateText
    loopCounter += 1
  html += "</ul>"
  return html

@app.route("/crewmates/<string:crewmate_type>/<int:crewmate_id>")
def crewmate(crewmate_type, crewmate_id):
  crewmateObj = helper.crew[crewmate_type][crewmate_id]
  return f'''
  <h1>{crewmateObj['name']}</h1>
  <img src='{crewmateObj["url"]}'>
  <p>{crewmateObj['description']}</p>
  <ul>
    <li>{crewmateObj['race']}</li>
    <li>{crewmateObj['age']}</li>
  </ul>
  '''
  
