import qrcode #Biblioteca já existente;
from PIL import Image #Python Imaging Library é o modulo que trabalha com imagens e estou importando a classe Image que serve para representar imagens;
link = "https://github.com/HendrylXamann"

#Gerando o QRCODE
qrcode = qrcode.QRCode(version=1, box_size=10, border=5) #Criando um object do tipo QRCode e dentro são três parâmetros que indica a versão e tamanho;
qrcode.add_data(link) #Atribuindo o link que irá ficar no QRCODE;
qrcode.make(fit=True) #Método make para de fato criar, o fit=true serve para o qrcode ajustar automaticamente o tamanho dos dados do link;

#Criando a imagem para ser escaneada
Image = qrcode.make_image(fill="black", back_color="white")

#Salvando a imagem
Image.save("QRCODE com python.jpg")
