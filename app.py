from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  # Akan mencari di folder "templates"

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    message = data.get("message", "").lower()

    if "halo" in message:
        response = "Halo juga! Ada yang bisa saya bantu?"
    elif "film" in message:
        response = "Silakan cari judul film di atas ya!"
    elif "siapa kamu" in message:
        response = "Saya chatbot FAQ MovliX!"
    else:
        response = "Maaf, saya belum mengerti pertanyaan itu."

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
