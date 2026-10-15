import pandas as pd
from flask import Flask, jsonify

# Création de l'application Flask
app = Flask(__name__)


@app.route("/api/v1/stats/produits", methods=["GET"])
def analyser_produits():

    # 1. EXTRACTION : récupérer les données JSON
    url = "https://dummyjson.com/products"

    donnees = pd.read_json(url, storage_options={"User-Agent": "Mozilla/5.0"})

    # 2. TRANSFORMATION : créer un DataFrame
    df = pd.DataFrame(list(donnees["products"]))

    # 3. Sélectionner la Series des prix
    series_prix = df["price"]

    # 4. Calculer les statistiques
    stats = series_prix.describe().to_dict()

    # 5. Retourner les résultats au format JSON
    return jsonify(
        {
            "total_produits": int(stats["count"]),
            "prix_moyen": round(float(stats["mean"]), 2),
            "prix_min": float(stats["min"]),
            "prix_max": float(stats["max"]),
            "apercu_colonnes": list(df.columns),
        }
    ), 200


if __name__ == "__main__":
    app.run(debug=True)
