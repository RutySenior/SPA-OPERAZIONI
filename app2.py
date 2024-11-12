from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Server web - codice per restituire la homepage
@app.route("/")
def homepage():
    return render_template("homepage2.html")

# Server API - utilizzo di GET per ricevere i parametri dalla query string
@app.route("/calcola", methods=["GET"])
def calcola():
    # Prendere le informazioni dalla query string
    num1 = request.args.get('num1', type=float)
    num2 = request.args.get('num2', type=float)
    operazione = request.args.get('operazione')

    if num1 is None or num2 is None or operazione is None:
        return jsonify(risultato="Mancano i dati")

    # Elaborazione dell'informazione
    if operazione == 'addizione':
        risultato = num1 + num2
    elif operazione == 'sottrazione':
        risultato = num1 - num2
    elif operazione == 'moltiplicazione':
        risultato = num1 * num2
    elif operazione == 'divisione':
        if num2 == 0:
            return jsonify(risultato="Impossibile dividere per zero")
        risultato = num1 / num2  # Usa la divisione normale per ottenere un risultato float

    # Restituire il risultato al front-end
    return jsonify(risultato=risultato)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3245, debug=True)