##Author: Bruno Miranda de Souza
##Project: Simulation of a license plates recognition system that allows only registered plates to pass

import cv2

try:

    from PIL import Image
except ImportError:
    import Image
    
import pytesseract
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


#thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

listaPlacas = ['placa1.jpg', 'placa2.jpg', 'placa3.jpg', 'placa4.jpg']
listaPlacasReconhecidas = []
listaPlacasCadastradas = ["HQW5678", "BSE3R52"]

print()
print("------------------------------------------------")
print('Placas cadastradas:')
for plc in listaPlacasCadastradas:
    print(plc)

print("------------------------------------------------")
print()

for plc in listaPlacas:
    image1 = cv2.imread(plc)
    image1_resized = cv2.resize(image1, (300, 100))
    cv2.imshow('Original', image1_resized)
##    cv2.imshow('Original',image1 )

    ##### Tratamento da imagem ######
    image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    thresh = thresholding(image1)
##    cv2.imshow('Thresh',image1 )

##    print ('Final com tratamento')
    custom_config = r'-c tessedit_char_blacklist=abcdefghijklmnopqrstuvwxyz/ --psm 10'
    a=(pytesseract.image_to_string(thresh, config=custom_config))
##    print('Reconhecido: ', a)
    placaCorrigida = ''
    for letra in a:
        if letra in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
            placaCorrigida += letra
        else:
            continue
    print("Placa " + str(listaPlacas.index(plc)+1) + ": " + placaCorrigida)
    if placaCorrigida in listaPlacasCadastradas:
        print("Entrada Liberada!")
    else:
        print("Entrada não liberada!")
        print("Placa não cadastrada.")
    listaPlacasReconhecidas.append(placaCorrigida)
    print()
    cv2.waitKey()

##print(listaPlacasReconhecidas)



   
   
 

