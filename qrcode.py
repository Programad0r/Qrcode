import pyqrcode

#representando a variavel para o Qrcode
s = 'www.google.com'

#Criando o Qrcode
url = pyqrcode.create(s)


url.svg("myqr.svg", scale = 8)