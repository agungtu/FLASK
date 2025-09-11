from flask import Flask, render_template, url_for

app = Flask(__name__)

bio = [
    {'Nama': 'Agung Tri Utomo',
     'Umur': '26 tahun',
     'Asal': 'Salatiga',
     'Pekerjaan': 'Dosen',
     'gambar' : 'image/agungtu.jpg',
     'datas' : 'umur : 26 tahun' 
     },
         {'Nama': 'Agung Tri U',
     'Umur': '18 tahun',
     'Asal': 'Semarang',
     'Pekerjaan': 'Mahasiswa',
          'gambar' : 'image/agungtu2.jpeg',
    'datas' : 'umur : 17 tahun, asal : jakarta, status : Mahasiswa'
     },
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', bio = bio)

@app.route("/about")
def about():
    return render_template('about.html', title = 'About')


if __name__ == '__main__':
    app.run(debug=True)