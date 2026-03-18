dicionario = {
    "CRINGE": "Algo vergonhoso ou constrangedor",
    "VLW": "Abreviação de 'valeu'",
    "TMJ": "Abrevição de tamo junto",
    "HATER": "Pessoa que critica constantimente coisas ou pessoas",
    "GAG": "É utilizado quando alguem esta surpreso",
    }

palavra = input("Digite uma palavra que você nao sebe o significado(por favor colocar em letra maiuscula): ")
if palavra in dicionario.keys():
    print(dicionario[palavra])
else:
    print("esse palavra não esta no nosso sistema")
