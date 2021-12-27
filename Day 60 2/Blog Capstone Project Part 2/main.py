from flask import Flask, render_template, request
import requests
from requests.api import get
import smtplib

app = Flask(__name__)

MY_EMAIL = "burakkcode@gmail.com"
MY_PASSWORD = "000"

def get_posts():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts =response.json()
    return all_posts

@app.route('/')
def home():
    get_posts()
    return render_template("index.html", posts = get_posts())

@app.route('/about')
def about():
    return render_template("about.html")

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}".encode("utf-8")
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(MY_EMAIL, MY_EMAIL, email_message)

@app.route('/contact', methods=["GET","POST"])
def contact():
    if request.method == "POST":
        data = request.form
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

@app.route("/post/<int:index>")
def post(index):
    all_posts = get_posts()
    requested_post = None
    for blog_post in all_posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)



if __name__ == "__main__":
    app.run(debug=True)