from flask import Flask, request, render_template, redirect
#from flask_ngrok import run_with_ngrok

from summarize import generate_summary

#Create the flask object
app = Flask(__name__)
#run_with_ngrok(app)

#create route
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
   if request.method=='POST':
      message=request.form['message']
      output=generate_summary(message, 3)
      return render_template('index.html', summarized_text=output)
   else:
      return redirect('/')

if __name__=="__main__":
   app.run()