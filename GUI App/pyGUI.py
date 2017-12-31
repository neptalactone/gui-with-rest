#!/usr/bin/env  python3.6
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import requests
import base64
import json
from urllib import request, error as urlerr

qtCreatorFile = "Form.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.res_out.setText("Validasi NIM dahulu sebelum melakukan submit/update!")
        self.pbClear.clicked.connect(self.clear_input)
        self.pbValidate.clicked.connect(self.validate_nim)
        self.pbUpdate.clicked.connect(self.update_data)
        self.pbSubmit.clicked.connect(self.submit_form)

    def validate_nim(self):
        nim = self.teNIM.toPlainText()
        url = "http://127.0.0.1:8000/mahasiswa/"+nim

        try:
            respon = request.urlopen(url)
            data = json.loads(respon.read())
            nama, alamat, no_telp, stat = data["nama"], data["alamat"], data["no_telp"], data["stat"]
            gender, email, agama, dob, pwd = data["gender"], data["email"], data["agama"], data["dob"], data["pwd"]
            self.teNama.setText(nama)
            self.teAlamat.setText(alamat)
            self.teNoTelp.setText(no_telp)
            self.teStatus.setText(stat)
            self.teGender.setText(gender)
            self.teEmail.setText(email)
            self.teAgama.setText(agama)
            self.teDoB.setText(dob)
            self.tePwd.setText(pwd)
            self.res_out.setText("Data ditemukan! silahkan ubah jika ingin merubah!")
            self.pbSubmit.setEnabled(False)
            self.pbUpdate.setEnabled(True)
        except urlerr.HTTPError as e:
            if e.code == 404:
                self.res_out.setText("NIM tidak ditemukan, Masukkan data yang baru!")
                self.pbSubmit.setEnabled(True)
                self.pbUpdate.setEnabled(False)
            else:
                raise

    def submit_form(self):
        nim = self.teNIM.toPlainText()
        nama = self.teNama.toPlainText()
        alamat = self.teAlamat.toPlainText()
        no_telp = self.teNoTelp.toPlainText()
        stat = self.teStatus.toPlainText()
        gender = self.teGender.toPlainText()
        email = self.teEmail.toPlainText()
        agama = self.teAgama.toPlainText()
        dob = self.teDoB.toPlainText()
        pwd = self.tePwd.toPlainText()
        en_pwd = base64.b64encode(pwd.encode('utf-8'))

        mahasiswa = {'nim': nim, 'nama': nama, 'alamat': alamat, 'no_telp': no_telp,
                     'stat': stat, 'gender': gender, 'email': email, 'agama': agama, 'dob': dob,
                     'pwd': pwd, 'en_pwd': en_pwd}

        try:
            requests.post("http://127.0.0.1:8000/mahasiswa.json", data=mahasiswa)
            self.res_out.setText("Data berhasil dimasukkan,\ncek web http://127.0.0.1:8000/mahasiswa/" + nim)
        except requests.HTTPError as e:
            if e.response == 500:
                self.res_out.setText("Data tidak dapat dimasukkan!, Server tidak dapat diakses")
            elif e.response == 400:
                self.res_out.setText("Ada data yang tidak sesuai!, Ulangi pengisian data")
                self.clear_input()
            else:
                raise

    def update_data(self):
        nim = self.teNIM.toPlainText()
        nama = self.teNama.toPlainText()
        alamat = self.teAlamat.toPlainText()
        no_telp = self.teNoTelp.toPlainText()
        stat = self.teStatus.toPlainText()
        gender = self.teGender.toPlainText()
        email = self.teEmail.toPlainText()
        agama = self.teAgama.toPlainText()
        dob = self.teDoB.toPlainText()
        pwd = self.tePwd.toPlainText()
        en_pwd = base64.b64encode(pwd.encode('utf-8'))

        mahasiswa = {'nim': nim, 'nama': nama, 'alamat': alamat, 'no_telp': no_telp,
                     'stat': stat, 'gender': gender, 'email': email, 'agama': agama, 'dob': dob,
                     'pwd': pwd, 'en_pwd': en_pwd}

        try:
            requests.put("http://127.0.0.1:8000/mahasiswa/"+nim+".json", data=mahasiswa)
            self.res_out.setText("Data berhasil dimasukkan,\ncek web http://127.0.0.1:8000/mahasiswa/" + nim)
        except requests.HTTPError as e:
            if e.response == 500:
                self.res_out.setText("Data tidak dapat dimasukkan!, Server tidak dapat diakses")
            else:
                raise

    def clear_input(self):
        self.teNIM.setText("")
        self.teNama.setText("")
        self.teAlamat.setText("")
        self.teNoTelp.setText("")
        self.teStatus.setText("")
        self.teGender.setText("")
        self.teEmail.setText("")
        self.teAgama.setText("")
        self.teDoB.setText("")
        self.tePwd.setText("")
        self.res_out.setText("Validasi NIM dahulu sebelum melakukan submit/update!")
        self.pbSubmit.setEnabled(True)
        self.pbUpdate.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec())
