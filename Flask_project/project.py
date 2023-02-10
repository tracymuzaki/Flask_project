#import statement
from flask import Flask,  jsonify

#initializing the flask class
app = Flask(__name__)

#default route
@app.route('/')
def default():
    return "Welcome to articles landing page"

#articles route
@app.route('/articles', methods = ['GET'])
def get_articles():
    articles = [{
        'id':100,
        'title':'The Future of AI in Healthcare',
        'body':'A comprehensive overview of the potential applications of artificial intelligence in the healthcare industry, including diagnosis, personalized medicine, and drug discovery.',
        'author':'Sarah Smith'
    },
    {
        'id':200,
        'title':'The Rise of Electric Cars',
        'body':'An in-depth examination of the growing popularity of electric cars, exploring the benefits and drawbacks of this new technology and the impact it could have on the environment and the automotive industry.',
        'author':'John Doe'
    },
    {
        'id':300,
        'title':'The Importance of Mental Health',
        'body':'A powerful call to action for increased awareness and support for mental health, including practical tips and resources for anyone struggling with mental health issues.',
        'author':'Jane Doe'
    },
    {
        'id':400,
        'title':'The Benefits of Plant-Based Diets',
        'body':'An informative article exploring the benefits of plant-based diets, including the potential to reduce the risk of chronic diseases, improve the environment, and promote animal welfare.',
        'author':'Michael Green'
    }]
    return jsonify(articles)

if __name__=='__main__':
    app.run(debug=True)