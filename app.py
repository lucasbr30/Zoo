from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

# Caminhos dos arquivos
if not os.path.exists("data"):
    os.makedirs("data")

animals_file = "data/animals.json"
care_file = "data/care.json"

# Garantir que os arquivos existem
for file in [animals_file, care_file]:
    if not os.path.exists(file):
        with open(file, "w") as f:
            json.dump([], f)

# Funções utilitárias
def load_data(file):
    with open(file, "r") as f:
        return json.load(f)

def save_data(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

# Rotas de animais
@app.route("/animais", methods=["GET"])
def get_animais():
    return jsonify(load_data(animals_file))

@app.route("/animais", methods=["POST"])
def add_animal():
    data = request.get_json()
    animais = load_data(animals_file)
    animais.append(data)
    save_data(animals_file, animais)
    return jsonify({"mensagem": "Animal adicionado com sucesso!"}), 201

# Rotas de cuidados
@app.route("/cuidados", methods=["GET"])
def get_cuidados():
    return jsonify(load_data(care_file))

@app.route("/cuidados", methods=["POST"])
def add_cuidado():
    data = request.get_json()
    cuidados = load_data(care_file)
    cuidados.append(data)
    save_data(care_file, cuidados)
    return jsonify({"mensagem": "Cuidado adicionado com sucesso!"}), 201

if __name__ == "__main__":
    app.run(debug=True)
