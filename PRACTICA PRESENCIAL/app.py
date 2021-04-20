from flask import Flask, jsonify
from flask_cors import CORS
from flask.globals import request

app = Flask(__name__)
CORS(app)


@app.route('/analisis-lexico',methods=['POST'])
def analisis_lexico():

    vocales = 0 
    consonantes = 0
    palabras = 0

    frase = request.json['frase']

    frase = frase.lower()

    for c in frase:

        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':

            vocales += 1

        elif ord(c) >= 97 and ord(c) <= 122:

            consonantes += 1

    palabras = len(frase.split())

    return {
        'vocales' : vocales,
        'consonantes' : consonantes,
        'palabras' : palabras
    }


@app.route('/numeros-primos',methods=['POST'])
def numeros_primos():

    inicio = int(request.json['inicio']) #1
    final = int(request.json['final'])   #10

    resultado = 0

        #1
    for num in range(inicio, final+1):

            #2
        for x in range (2, num):

            if num%x == 0:
                break

        else:
            print(num)
            resultado += 1

    return {
        'resultado' : resultado
    }

    
@app.route('/calculadora-basica',methods=['POST'])
def calculadora():

    numero1 = float(request.json['numero1'])
    numero2 = float(request.json['numero2'])
    signo = request.json['signo']
    resultado = 0

    if signo == '+':
        resultado = numero1 + numero2
    elif signo == '-':
        resultado = numero1 - numero2
    elif signo == '*':
        resultado = numero1 * numero2
    elif signo == '/':
        resultado = numero1 / numero2
    else:
        resultado = "Signo no válido"

    return {
        'resultado' : resultado
    }


@app.route('/')
def index():
    return 'The server is up!'

if __name__ == "__main__":
    app.run(threaded=True, port=6700, debug=True)