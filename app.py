from flask import Flask,render_template,request, jsonify
app=Flask(__name__)
#server web-codice per restituire la homepage 
@app.route("/")
def homepage():
    return render_template("homepage.html")

#server API
@app.route("/calcola", methods=["POST"])
def calcola():
    #prendere le informazioni in arrivo dal front end
    json_data = request.get_json() 
    if json_data:
        num1 = json_data.get('num1')
        num2 = json_data.get('num2')
        operazione = json_data.get('operazione')
        #elaborazione dell'informazione
        if operazione == 'addizione':
            risultato = num1 + num2
        elif operazione == 'sottrazione':
            risultato = num1 - num2
        elif operazione == 'moltiplicazione':
            risultato = num1 * num2
        elif operazione == 'divisione':
            risultato = num1 // num2
            #restituire i risultati al front end
        return jsonify(risultato = risultato)
    else:
        return jsonify(risultato = 'Mancano i dati')
if __name__== "__main__":
    app.run(host="0.0.0.0",port=3245,debug=True)