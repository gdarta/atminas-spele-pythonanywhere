
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)
app.config["DEBUG"] = True

#def hello_world():
   #return 'Hello from my stinky butt!'
@app.route('/')
def huina():
    return render_template('main_page.html')

