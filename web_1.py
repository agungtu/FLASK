from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello selamat datang Flask</h1>"

# flask --app my_blog_1 run
#lakukan di terminal untuk debug diubah menjadi 1 agar saat edit dan save content bisa berubah
# export FLASK_DEBUG= 1 

# @app.route("/about")
# def about():
#     return "<p>This is the about page!</p>"

# @app.route("/contact")
# def contat():
#     return "<p>085647427024</p>"

if __name__ == '__main__':
    app.run(debug=True)
