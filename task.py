from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route("/power/europe", methods=["GET"])
def get_europe_power_co2_emissions():
    try:
        carbonwatch_url = "https://carbonwatch.kayrros.com/route/europe"
        response = requests.get(carbonwatch_url)
        response.raise_for_status()  # Raise an exception for bad responses

        data = response.json()
        europe_power_co2_emissions = data["power"]["europe"]["co2_emissions"]

        return jsonify({"co2_emissions": europe_power_co2_emissions / 1000000})

    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to fetch data from CarbonWatch", "details": str(e)})

    except (KeyError, ValueError) as e:
        return jsonify({"error": "Data format error from CarbonWatch", "details": str(e)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
