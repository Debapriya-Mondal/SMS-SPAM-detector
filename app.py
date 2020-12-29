from flask import Flask, render_template,redirect, url_for, flash, request
import pickle
app = Flask(__name__)
app.config['SECRET_KEY'] = 'debudaisasecretkey'
fileobj = open("model/bnb.pkl","rb")
BNB = pickle.load(fileobj)
fileobj.close()
fileobj  = open("model/cv.pkl","rb")
CV = pickle.load(fileobj)
fileobj.close()
@app.route("/", methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.form.get('data')
        bow = CV.transform([data])
        predict = BNB.predict(bow)
        if predict == 1:
            x = 'This is Spam.'
            return render_template('home page.html', x=x)
            
        else:
            x = 'This is Ham.'
            return render_template('home page.html', x=x)

    return render_template('home page.html')

if __name__ == '__main__':
    app.run()