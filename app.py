# app.py
import io
from flask import send_file
from gtts import gTTS
from flask import Flask, render_template, request
import re
from data import RULES, VERDICT, NEXT_STEPS, SAFE_NOTE, SAMPLES

app = Flask(__name__)

SCAM_THRESHOLD = 3   # score needed to call it a scam

def analyze(text, lang):
    score = 0
    reasons = []
    for rule in RULES:
        if re.search(rule["pattern"], text, re.IGNORECASE):
            score += rule["weight"]
            if rule["weight"] > 0:          # only show scam reasons
                reasons.append(rule[lang])

    is_scam = score >= SCAM_THRESHOLD
    return {
        "scam": is_scam,
        "score": score,
        "verdict": VERDICT[lang]["scam" if is_scam else "safe"],
        "reasons": reasons if is_scam else [],
        "steps": NEXT_STEPS[lang] if is_scam else [],
        "note": "" if is_scam else SAFE_NOTE[lang],
    }

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    message = ""
    lang = "ml"
    if request.method == "POST":
        message = request.form.get("message", "").strip()
        lang = request.form.get("lang", "ml")
        if message:
            result = analyze(message, lang)
    return render_template("index.html", result=result,
                           message=message, lang=lang, samples=SAMPLES)
@app.route("/speak", methods=["POST"])
def speak():
    text = request.form.get("text", "")
    lang = request.form.get("lang", "ml")      # "ml" or "hi"
    mp3 = io.BytesIO()
    gTTS(text=text, lang=lang, slow=False).write_to_fp(mp3)
    mp3.seek(0)
    return send_file(mp3, mimetype="audio/mpeg")
if __name__ == "__main__":
    app.run(debug=True)