import re
import data.DataInterface as DF

#Checks if an account can be created with the given username and password
#returns bool, message with why it can't on failure
def validateUsernameAndPassword(username, password):
    if len(username) < 5:
        return False, "Username must be 5 characters long"
    if DF.usernameTakenAsBool( username ):
        return False, "Username is taken"
    if len(password) < 10:
        return False, "Password must be 10 characters long"
    if re.search( '[A-Z]', password ) is None:
        return False, "Password must contain uppercase letter"
    if re.search( '[a-z]', password ) is None:
        return False, "Password must contain lowercase letter"
    if re.search( '[0-9]', password ) is None:
        return False, "Password must digit"
    if re.search( '[!@#$%^&*()]', password ) is None:
        return False, "Password must special character"
    return True, ""