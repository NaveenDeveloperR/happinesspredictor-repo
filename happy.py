from flask import Flask, render_template, request

app = Flask(__name__)# interface between my server and my application wsgi

import pickle
model = pickle.load(open(r'D:\Flask\rf.pkl','rb'))


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict')
def predict():
    return render_template("contact.html")
@app.route('/predict happiness', methods =['POST'])#binds to an url
def predict_happiness():
   
    p =request.form["a"]
    q= request.form["b"]
    r= request.form["c"]
    s=request.form["d"]
    u=request.form["e"]
    v=request.form["f"]
    
    t=[[int(p),int(q),int(r),int(s),int(u),int(v)]]
    output= model.predict(t)
    print(str(output[0]))  
    return render_template("ANS.html",y = "The Predicted Happiness Score is  " + str(output[0]) )   

    

@app.route('/we_do')

def we_do():
    return render_template('we_do.html')

@app.route('/country rankings')
def ranking():
    return render_template('portfolio.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

