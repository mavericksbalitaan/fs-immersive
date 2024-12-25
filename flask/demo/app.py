from flask import Flask, render_template

app = Flask(__name__)
app.debug = True


pets = [
    {
        "image": "https://images.unsplash.com/photo-1548366086-7f1b76106622?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTR8fGNhdHN8ZW58MHx8MHx8fDA%3D",
        "name": "Nelly",
        "age": "5 weeks",
        "bio": "I am a tiny kitten rescured by the good people at Paws Rescue Center. I love squeaky toys and cuddles.",
    },
    {
        "image": "https://images.unsplash.com/photo-1548546738-8509cb246ed3?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTl8fGNhdHN8ZW58MHx8MHx8fDA%3D",
        "name": "Yuki",
        "age": "8 months",
        "bio": "I am a handsome gentle-cat. I like to dressup in bow ties.",
    },
    {
        "image": "https://plus.unsplash.com/premium_photo-1668606763482-8dd2042c934e?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTN8fGRvZ3N8ZW58MHx8MHx8fDA%3D",
        "name": "Basker",
        "age": "1 year",
        "bio": "I love barking. But, I love my friends more.",
    },
    {
        "image": "https://images.unsplash.com/photo-1592194996308-7b43878e84a6?w=800&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTJ8fGNhdHN8ZW58MHx8MHx8fDA%3D",
        "name": "Mr. Furkins",
        "age": "5 years",
        "bio": "Probably napping.",
    },
]


@app.route("/")
def home():
    # return "<h1> Paws Rescue Center 🐾 </h1>"
    return render_template("home.html", pets=pets)


@app.route("/about")
def about():
    #     return """
    #     <p>
    # We are a non-profit organization working as an animal rescue. We aim to help you connect with the purrfect furbaby for you! The animals you find on our website are rescued and rehabilitated animals. Our mission is to promote the ideology 'adopt, don't hop'!
    # </p>
    #     """
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
