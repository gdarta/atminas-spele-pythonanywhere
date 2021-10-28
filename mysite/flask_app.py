
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def sakums():
    return render_template('main_page.html')

@app.route('/rezultats', methods = ["GET","POST"])
def rezultats():
    if request.method == "POST":
        pirmais = request.form['pirmais']
        otrais = request.form['otrais']
        rez = int(pirmais)*int(otrais)
        return render_template('main_page.html', rez = int(rez))

@app.route('/spelite')
def laukums():
    return render_template('atminas_spele.html')

if __name__ == '__main__':
    app.run()




