from flask import Flask, request, render_template, redirect

from summarize import generate_summary

#Create the flask object
app = Flask(__name__)

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