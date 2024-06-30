from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__, template_folder='templates')

toDo = [{"task": "do some coding", "done": False}]

@app.route('/')
def home():
    return render_template("home.html", toDo=toDo)

@app.route("/add", methods=["POST"])
def add():
    todo = request.form['todo']
    toDo.append({"task": todo, "done": False})
    return redirect(url_for('home'))

@app.route("/done/<int:index>", methods=["GET", "POST"])
def edit(index):
    todo = toDo[index]
    if request.method == "POST":
        todo["task"] = request.form["todo"]
        return redirect(url_for('home'))
    else:
        return render_template('edit.html', todo=todo, index=index)

@app.route("/check/<int:index>")
def done(index):
    toDo[index]['done'] = not toDo[index]['done']
    return redirect(url_for('home'))

@app.route("/remove/<int:index>")
def remove(index):
    del toDo[index]
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
