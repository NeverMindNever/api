import easyEstimate2
from flask import Flask, jsonify, request

app = Flask(__name__)
version = "0.2.0"
base = ""


@app.route('/v0/estimate', methods=['GET', 'POST'])
def estimate():
    if request.method == 'POST':
        hab = request.get_json()
        return jsonify({"Estimation": easyEstimate2.estimer(hab["numero"], hab["type_voie"], hab["voie"],
                                                            hab["code_postal"], hab["surface"], hab["nbr_piece"],
                                                            hab["nature"], hab["surface_terrain"])})
    else:
        return jsonify({
            "App Name": "The API",
            "Version": version,
            "Description": "Get easily an estimation for any property in France, The estimation is calculated based",
            "Model": "Random forest Regressor",
            easyEstimate2.__name__: "0.5.0"

        })


@app.errorhandler(404)
def invalid_route(e):
    return "Invalid route.", 404


if __name__ == '__main__':
    app.run(debug=True)
