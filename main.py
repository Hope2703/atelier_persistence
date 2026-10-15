from pathlib import Path

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


@app.route("/api/v1/stats/produits/locaux", methods=["GET"])
def analyser_produits_locaux():

    # 1. Localiser le fichier JSON
    chemin = Path(__file__).resolve().parent / "data_local.json"

    # 2. Lire les données locales avec Pandas
    df = pd.read_json(chemin)

    # 3. Extraire la Series des prix
    series_prix = df["prix"]

    # 4. Calculer les statistiques
    stats = series_prix.describe().to_dict()

    # 5. Retourner les produits et les statistiques
    return jsonify(
        {
            "source": "data_local.json",
            "total_produits": int(stats["count"]),
            "prix_moyen": round(float(stats["mean"]), 2),
            "prix_min": float(stats["min"]),
            "prix_max": float(stats["max"]),
            "produits": df.to_dict(orient="records"),
        }
    ), 200


if __name__ == "__main__":
    app.run(debug=True)
