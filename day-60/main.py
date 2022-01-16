from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

OWN_EMAIL = "phelixdusengimana@gmail.com"
OWN_PASSWORD = "phelix@gmail.com"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def contact_data():
    error = None
    if request.method == 'POST':
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(OWN_EMAIL, OWN_PASSWORD)
            connection.sendmail(
                from_addr=request.form['email'],
                to_addrs=OWN_EMAIL,
                msg=f"Subject:Contacting from {request.form['firstname'] + ' ' + request.form['lastname']}\n"
                    f"{request.form['message']}"
            )
        return f"Thanks for contacting mr/mrs {request.form['firstname'] + ' ' + request.form['lastname']}"
    else:
        return "No message sent"


if __name__ == "__main__":
    app.run(debug=True)
