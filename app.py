from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
todos = []

@app.route('/')
def index():
    return render_template("index.html", todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    task = request.form.get("task")
    if task:
        todos.append({"id": len(todos)+1, "task": task, "done": False})
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo["id"] != todo_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
