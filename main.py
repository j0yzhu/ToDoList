from flask import Flask, render_template, url_for, redirect, request

class ToDoListApp():
    def __init__(self):
        self.app = Flask(__name__)
        self.toDo = [{"task": "code", "done": False}]
        self.routes()

    def routes(self):
        self.app.add_url_rule('/', 'home', self.home)
        self.app.add_url_rule('/add', 'add', self.add, methods=['POST'])
        self.app.add_url_rule('/edit/<int:index>', 'edit', self.edit, methods=['GET', 'POST'])
        self.app.add_url_rule('/check/<int:index>', 'done', self.done)
        self.app.add_url_rule('/remove/<int:index>', 'remove', self.remove)

    def home(self):
        return render_template("home.html", toDo=self.toDo)

    def add(self):
        todo = request.form['todo']
        self.toDo.append({"task": todo, "done": False})
        return redirect(url_for('home'))

    def edit(self, index):
        todo = self.toDo[index]
        if request.method == "POST":
            todo["task"] = request.form["todo"]
            return redirect(url_for('home'))
        else:
            return render_template('edit.html', todo=self.todo, index=index)

    def done(self, index):
        self.toDo[index]['done'] = not self.toDo[index]['done']
        return redirect(url_for('home'))

    def remove(self, index):
        del self.toDo[index]
        return redirect(url_for('home'))

    def run(self):
        self.app.run(debug=True)

if __name__ == '__main__':
    app = ToDoListApp()
    app.run()
