# 🛡️ Scam Shield

**A scam message checker for senior citizens, with results in simple Malayalam or Hindi and voice read-aloud.**

Built for a 3-hour Social Impact hackathon.

---

## The Problem

Senior citizens are a growing target for online and phone scams. Fake "KSEB bill pending, call now" messages, bank KYC links, lottery prizes, parcel and "digital arrest" calls, and "I'm your son, send money" messages arrive every day. Most elders cannot tell a real message from a fake one, and most scam-awareness tools are only in English.

## Our Solution

Scam Shield lets a user **paste a suspicious SMS, WhatsApp message or call script**. The app instantly says:

- **⚠️ Likely scam** or **✅ Looks safe**
- **Why**, in simple Malayalam or Hindi
- **What to do next**, including the official helplines
- A **🔊 Listen** button that reads the result aloud for elders who find reading difficult

---

## Features

- Detects 17 scam patterns, including:
  - Electricity (KSEB) disconnection threats
  - Bank account blocked and KYC update scams
  - OTP, PIN and CVV requests
  - Suspicious links and fake APK or app installs
  - Remote-access apps (AnyDesk, TeamViewer)
  - Lottery, prize and cashback scams
  - Advance-fee and refund (UPI PIN / QR) scams
  - Fake police, CBI, customs and "digital arrest" calls
  - Parcel and courier scams
  - SIM block scams
  - Work-from-home and job scams
  - Family emergency ("Hi Amma, new number") scams
- Simple **scoring system** with safe signals (such as "Do not share your OTP") to avoid false alarms
- **Case-insensitive** matching ("URGENT", "Urgent" and "urgent" all work)
- Results in **Malayalam and Hindi**
- **Text-to-speech** in both languages, working in any browser
- **Sample messages dropdown** for quick demos
- Large fonts and a simple layout designed for elders

---

## How It Works

1. The user pastes a message and selects a language.
2. Flask checks the message against a list of scam rules (regular expressions) in `data.py`.
3. Each matching rule adds its **weight** to a score. Safe signals have a **negative weight** and lower the score.
4. If the score is **3 or more**, the message is flagged as **Likely scam**.
5. The result page shows the reasons and next steps in the chosen language.
6. When the user clicks **Listen**, the text is sent to the `/speak` route, which uses Google Text-to-Speech (gTTS) to create an MP3 that the browser plays.

We used a rule-based approach on purpose. It is fast, works without training data, gives the same result every time, and can explain exactly why a message was flagged.

---

## Tech Stack

| Part | Technology |
|---|---|
| Backend | Python, Flask |
| Detection | Regular expressions (`re`) with weighted rules |
| Frontend | HTML, CSS, a little JavaScript |
| Voice | gTTS (Google Text-to-Speech) |

---

## Project Structure

```
Scam_shield/
├── app.py              # Flask app: routes, scoring logic, text-to-speech
├── data.py             # Scam rules, Malayalam/Hindi text, helplines, sample messages
├── templates/
│   └── index.html      # Web page
└── README.md
```

---

## Installation and Setup

### Requirements
- Python 3.8 or higher
- An internet connection (needed only for the voice feature)

### Steps

1. **Open a terminal in the project folder.**

2. **(Optional) Create a virtual environment:**
   ```
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # Mac / Linux
   ```

3. **Install the dependencies:**
   ```
   pip install flask gtts
   ```

4. **Run the app:**
   ```
   python app.py
   ```

5. **Open your browser and go to:**
   ```
   http://127.0.0.1:5000
   ```

> Flask will show a "development server" warning. This is normal and can be ignored for local use.

---

## How to Use

1. Pick a sample from the dropdown, or paste your own message.
2. Choose **മലയാളം** or **हिन्दी**.
3. Click **Check ✔**.
4. Read the result, or click **🔊 Listen** to hear it.

### Try these samples

| Sample | Expected result |
|---|---|
| KSEB scam | ⚠️ Likely scam |
| Bank KYC scam | ⚠️ Likely scam |
| Lottery scam | ⚠️ Likely scam |
| Parcel / digital arrest | ⚠️ Likely scam |
| Family emergency | ⚠️ Likely scam |
| Real OTP (safe) | ✅ Looks safe |
| Real payment (safe) | ✅ Looks safe |

---

## Customising the Rules

All scam knowledge lives in `data.py`. To add a new scam type, add a block to the `RULES` list:

```python
{
    "pattern": r"your|words|here",
    "weight": 2,                      # 1 = mild, 2 = strong, 3 = very strong
    "ml": "Malayalam explanation",
    "hi": "Hindi explanation",
},
```

Use a **negative weight** for signals that suggest a message is genuine. To make the app stricter or more relaxed, change `SCAM_THRESHOLD` in `app.py`.

---

## Important Helplines

| Helpline | Number |
|---|---|
| Cyber crime helpline (report fraud, or if money was lost) | **1930** |
| KSEB customer care | **1912** |
| Cyber crime reporting portal | https://cybercrime.gov.in |

---

## Limitations

- The checker is **rule-based**, so a new type of scam that matches none of the rules may be marked "Looks safe". The app says to ask family when in doubt.
- Messages written in English letters for Malayalam or Hindi ("Manglish") are only partly covered.
- Voice output needs an **internet connection**.
- The Malayalam and Hindi text should be reviewed by a native speaker before wider use.
- It is a helper tool, not a guarantee. Users should never share OTPs or PINs and should verify through official channels.

---

## Future Scope

- 📷 Screenshot upload with OCR (Malayalam and Hindi)
- 💬 WhatsApp bot: forward a message and get a reply
- 🤖 AI model combined with the rules to catch new scams
- 🔤 Support for Manglish and more Indian languages
- 📢 Community reporting to keep the rules up to date
- 🎙️ Voice input and call recording analysis
- 🚦 Risk meter and highlighting of suspicious words

---

## Team

- Members: Gouri I S and Visal Bijendra Kumar

---

## Disclaimer

Scam Shield gives guidance only. If you suspect fraud or have lost money, contact your bank and call **1930** immediately.
