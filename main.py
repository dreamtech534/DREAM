
from flask import Flask, request

app = Flask(__name__)

@app.route("/sms", methods=["POST"])
def sms_reply():
    from_number = request.form.get("From")
    message_body = request.form.get("Body")

    print(f"Gelen mesaj: {message_body} Gönderen: {from_number}")

    # Burada istediğin işlemi yapabilirsin
    if "fullcapacity" in message_body.lower():
        print("yessirr!!")

    return "OK", 200

if __name__ == "__main__":
    app.run(debug=True)
