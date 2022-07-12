maindict = {}; secdict = {}

codascii = ['á','é','í','ó','ú','ü','\n','...',
        ' ','!','¡',"'",'#','$','%','&','"','(',')','*',',','-','.','/',
          '0','1','2','3','4','5','6','7','8','9',
          ':',';','<','=','>','?','¿','@',
          'a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q',
          'r','s','t','u','v','w','x','y','z','[',']','^','_']

brailles = ['⠷','⠮','⠌','⠬','⠾','⠳','\n',' ',
        ' ','⠖','⠖','⠦','⠼','⠸⠎','⠸⠴','⠠⠯',"⠦",'⠣','⠜','⠔','⠂','⠤','⠄','⠠⠂',
        '⠼⠚','⠼⠁','⠼⠃','⠼⠉','⠼⠲','⠼⠑','⠼⠋','⠼⠛','⠼⠓','⠼⠊',
        '⠱','⠰','⠣','⠿','⠜','⠢','⠢','⠈','⠁','⠃','⠉','⠙','⠑','⠋','⠛','⠓','⠊','⠚','⠅',
        '⠇','⠍','⠝','⠻','⠕','⠏','⠟','⠗','⠎','⠞','⠥','⠧','⠺','⠭','⠽','⠵','⠣','⠜','⠘','⠸']

longitudascii = len(codascii); longitudbraille = len(brailles)
contador = 0; contadorr = 0

while contador < longitudascii:
    maindict[codascii[contador]] = brailles[contador]
    contador = contador + 1

while contadorr < longitudbraille:
    secdict[brailles[contadorr]] = codascii[contadorr]
    contadorr = contadorr + 1    

def tradBraille(entry):
    texto = ""
    for char in entry:
        char = char.lower()
        if char in codascii:
            texto = texto + maindict[char]
    return texto


def tradEsp(entry):
    texto = ""
    for char in entry:
        if char in brailles:
            texto = texto + secdict[char]
    return texto