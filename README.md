
# A simple calculator website
This is the 4th implementation of this website. This time the backend uses Flask and MySQL. The site is live here: http://52.15.174.58/frontend 

## Host it yourself
Do the following:
* Install python3 and 2 python libraries: Flask, mysql-connector
* Install MySQL. Put a valid mysql username and password into the data/DBUtilities.py file
* Create a folder called `react_compiled` in the static directory. Compile the react code (I used the steps in [this](https://reactjs.org/docs/add-react-to-a-website.html) tutorial) and put it into the new `react_compiled` folder
* Run app.py using Flask. For example on Linux:
```
export FLASK_APP=app.py
python3 -m flask run
```
