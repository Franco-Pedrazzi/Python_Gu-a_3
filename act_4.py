textEx1="hlooh"
textEx2="hooh"
def revisar(text):
    text2=text[::-1]
    if text==text2:
        print("Palindromo")
    else:
        print("aburrido")
revisar(textEx1)
revisar(textEx2)