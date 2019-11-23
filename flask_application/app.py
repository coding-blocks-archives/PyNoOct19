from flask import Flask, render_template, request

app = Flask(__name__)

USERS = [
  {
    "name": "Jatin",
    "language": "python",
    "designation": "Developer"
  },
  {
    "name": "Bipin",
    "language": "python",
    "designation": "Developer"
  },
  {
    "name": "Rahul",
    "language": "python",
    "designation": "Developer"
  },
]

@app.route('/users')
def users():
  return render_template('users.html', users = USERS, enumerate=enumerate)

@app.route('/users/<int:id>')
def user(id):
  return render_template('user.html', user = USERS[id])


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/feedbackSubmit', methods = ['POST'])
def feedbackSubmit():
  with open('data.csv', 'a') as file:
    form = dict(request.form)
    values = []
    for v in form.values():
      values.append(v[0])
    file.write(",".join(values) + '\n')
  return "Success !"

@app.route('/feedback')
def feedback():
  return render_template('feedback.html')

def main():
  app.run(port = 8000, debug = True)

if __name__ == "__main__":
  main()