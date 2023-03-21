from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
  return "<p>Nama : Regita Ceza Dara Denanta </p><p>Tempat, tanggal lahir : Malang, 17 Desember 2003</p><p>Alamat : Ngembes, Modo, Lamongan</p><p>Jenis Kelamin : Perempuan</p><p>Agama : Islam</p>"



if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
