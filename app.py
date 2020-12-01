import data.DataInterface as DF
import util
from flask import Flask, request, send_from_directory, jsonify, session
app = Flask(__name__)

#The key used to encrypt variables
#TODO Load this from environmental var
app.secret_key = 'This is not production safe'

#serves the html and javascript files in the static directory
@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

#Tries to create a user with the given username and password
@app.route('/CreateAccount', methods=['POST'])
def createAccount():
    try:
        username = request.form['username']
        password = request.form['password']
        success, message = util.validateUsernameAndPassword(username, password)
        if( success ):
            DF.insertUser(request.form['username'], request.form['password'])
    except Exception as ex:
        print("Exception in create account:", ex)
        success = False
        message = "There was an exception"
    return jsonify({
        "error": False,
        "createdAccount": success,
        "message": message
    })

#Starts a session with the client if the given username and password
#are valid
@app.route('/StartSession', methods=['POST'])
def startSession():
    try:
        username = request.form['username']
        password = request.form['password']
        hasSession = DF.authorizeUserAsBool(username, password)
        if( hasSession ):
            id = DF.getUserIdAsInt(username)
            session['userKey'] = id
    except Exception as ex:
        print('Exception in startSession:', ex)
        hasSession = False
    return jsonify(
        {
            "error": False,
            "hasSession": hasSession
        }
    )

#Checks if the client has a session
@app.route('/CheckSession', methods=['POST'])
def checkSession():
    return jsonify({
        "hasSession": 'userKey' in session
    })

#Ends the session with the user
@app.route('/EndSession', methods=['POST'])
def endSession():
    session.pop('userKey', None)
    return jsonify({
        "error": False
    })

#Adds the specified calculation for the user
#The user needs a session for this to work
@app.route('/AddCalculation', methods=['POST'])
def addCalculation():
    if( 'userKey' not in session ):
        abort(500)
    try:
        x = request.form['x']
        op = request.form['op']
        y = request.form['y']
        val = request.form['val']
        date = request.form['date']
        user_id = session['userKey']
        DF.insertCalculation(user_id, x, op, y, val, date)
        success = True
    except:
        success = False
    return jsonify({
        "error": not success
    })

#gets up to the last 10 calculations
#returns json containing the calculations
@app.route('/GetLast10Calculations', methods=['POST'])
def getLast10Calculations():
    try:
        calculations = DF.getLast10CalculationsFormatted()
    except:
        calculations = []
    return jsonify({
        "error": False,
        "calculations": calculations
    })