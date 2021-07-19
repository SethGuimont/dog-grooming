from flask import Flask, jsonify, request, render_template
# from flask_mail import Mail, Message
#import tweepy

app = Flask(__name__)

#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)

#tapi = tweepy.API(auth)
#for tweet in public_tweets:
    #print(tweet.text).first()


@app.route('/')
def index():
    return render_template('index-multipage.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/service')
def service():
    return render_template('service.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


'''
@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        theresult = request.form
        return render_template("result.html", theresult=theresult)
'''

if __name__ == '__main__':
    app.run()
