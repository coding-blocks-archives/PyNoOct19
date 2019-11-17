from flask import Flask, render_template, request

app = Flask(__name__)
forms = []

@app.route('/')
def index():
  print(forms)
  return render_template('index.html')

@app.route('/feedbackSubmit', methods = ['POST'])
def feedbackSubmit():
  forms.append(dict(request.form))
  return "Success !"

@app.route('/feedback')
def feedback():
  return render_template('feedback.html')

def main():
  app.run(port = 8000, debug = True)

if __name__ == "__main__":
  main()