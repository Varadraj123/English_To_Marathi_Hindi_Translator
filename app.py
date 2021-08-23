from flask import Flask,request,render_template
from textblob import TextBlob

app = Flask(__name__)  
  
@app.route('/')  
def customer():  
    return render_template('form.html')  
  
@app.route('/dictionary',methods = ['POST', 'GET'])  
def print_data():  
    if request.method == 'POST':  
        text_data= request.form.get("text")
        print(f'******************** Input Text is :{text_data}:')

        lang = request.form.get("Languges")
        print(f'***************** Input Language is :{lang}:')

        blob = TextBlob(text_data)
        converted_data = blob.translate(to=lang)
              
    return render_template("form.html",final_result = '{}'.format(converted_data))

if __name__ == '__main__':  
    app.run(host="0.0.0.0",debug=True)