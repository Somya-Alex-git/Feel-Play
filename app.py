from flask import Flask, render_template, request, redirect, url_for
import webbrowser

app = Flask(__name__)

USER_DATA = {
    "feelplay": "music"
}

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login_check():
    username = request.form.get("username")
    password = request.form.get("password")

    if username in USER_DATA and USER_DATA[username] == password:
        return redirect(url_for("home"))
    else:
        return render_template("login.html", error="Invalid Username or Password")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/mood")
def mood():
    mood_type = request.args.get("type")
    return render_template("mood.html", mood_type=mood_type)

@app.route("/playlist", methods=["POST"])
def playlist():
    user_input = request.form.get("mood", "")
    text_input = user_input.lower()

    # emojis
    happy = ["😊","😄","😁","😃","🙂","🥰","😍"]
    sad = ["😢","😭","😞","😔"]
    angry = ["😡","😠","🤬"]
    party = ["🎉","🥳","🔥"]
    romantic = ["❤️","💕","😘"]
    surprise = ["😲","😮","😳","😱"]
    shock = ["🤯","🙀","🫢"]

    mood = "neutral"

    if any(e in user_input for e in happy):
        mood = "happy"
    elif any(e in user_input for e in sad):
        mood = "sad"
    elif any(e in user_input for e in angry):
        mood = "angry"
    elif any(e in user_input for e in party):
        mood = "party"
    elif any(e in user_input for e in romantic):
        mood = "romantic"
    elif any(e in user_input for e in surprise):
        mood = "surprise"
    elif any(e in user_input for e in shock):
        mood = "shock"

    elif "happy" in text_input:
        mood = "happy"
    elif "sad" in text_input:
        mood = "sad"
    elif "angry" in text_input:
        mood = "angry"
    elif "party" in text_input:
        mood = "party"
    elif "love" in text_input:
        mood = "romantic"
    elif "surprise" in text_input:
        mood = "surprise"
    elif "shock" in text_input:
        mood = "shock"

    mood_links = {
        "happy": "https://open.spotify.com/embed/playlist/37i9dQZF1DXdPec7aLTmlC",
        "sad": "https://open.spotify.com/embed/playlist/37i9dQZF1DX7qK8ma5wgG1",
        "angry": "https://open.spotify.com/embed/playlist/37i9dQZF1DX1tyCD9QhIWF",
        "party": "https://open.spotify.com/embed/playlist/37i9dQZF1DX0BcQWzuB7ZO",
        "romantic": "https://open.spotify.com/embed/playlist/37i9dQZF1DWYcDQ1hSjOpY",
        "surprise": "https://open.spotify.com/embed/playlist/37i9dQZF1DX0BcQWzuB7ZO",
        "shock": "https://open.spotify.com/embed/playlist/37i9dQZF1DX0BcQWzuB7ZO",
        "neutral": "https://open.spotify.com/embed/playlist/37i9dQZF1DWYcDQ1hSjOpY"
    }

    return render_template("playlist.html",
                           link=mood_links.get(mood),
                           mood=mood)

# ✅ CRASH SAFE WEBCAM
@app.route("/webcam_detect")
def webcam_detect():
    try:
        from emotion_model import detect_emotion
        mood = detect_emotion()
    except Exception as e:
        print("Webcam error:", e)
        mood = "neutral"

    mood_links = {
        "happy": "https://open.spotify.com/embed/playlist/37i9dQZF1DXdPec7aLTmlC",
        "sad": "https://open.spotify.com/embed/playlist/37i9dQZF1DX7qK8ma5wgG1",
        "angry": "https://open.spotify.com/embed/playlist/37i9dQZF1DX1tyCD9QhIWF",
        "neutral": "https://open.spotify.com/embed/playlist/37i9dQZF1DWYcDQ1hSjOpY",
        "surprise": "https://open.spotify.com/embed/playlist/37i9dQZF1DX0BcQWzuB7ZO"
    }

    return render_template("playlist.html",
                           link=mood_links.get(mood),
                           mood=mood)

if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000/")
    app.run(debug=False, use_reloader=False)