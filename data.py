# data.py

RULES = [
    # ---------- Pressure tactics ----------
    {
        "pattern": r"\b(urgent|immediately|right now|last chance|expires today|within \d+ ?(hours|hrs|minutes|mins))\b|ഉടൻ|ഇന്ന് തന്നെ|तुरंत|आज ही",
        "weight": 1,
        "ml": "ഉടൻ ചെയ്യണം എന്ന് തിടുക്കം കൂട്ടുന്നു. തട്ടിപ്പുകാർ ഇങ്ങനെയാണ് ചെയ്യുന്നത്.",
        "hi": "संदेश जल्दबाज़ी करवा रहा है। ठग अक्सर ऐसा करते हैं।",
    },
    # ---------- KSEB / electricity ----------
    {
        "pattern": r"(disconnect|cut off|terminate).{0,40}(power|electricity|connection|supply)|(power|electricity|connection|supply).{0,40}(disconnect|cut off|terminated)|വൈദ്യുതി.{0,30}വിച്ഛേദ|बिजली.{0,30}कट",
        "weight": 2,
        "ml": "വൈദ്യുതി കണക്ഷൻ വിച്ഛേദിക്കും എന്ന് ഭീഷണിപ്പെടുത്തുന്നു. KSEB ഇങ്ങനെ SMS അയയ്ക്കില്ല.",
        "hi": "बिजली कनेक्शन कटने की धमकी दी जा रही है। बिजली विभाग ऐसे संदेश नहीं भेजता।",
    },
    {
        "pattern": r"(bill|dues?).{0,20}(pending|overdue|unpaid)|pending.{0,20}bill",
        "weight": 1,
        "ml": "ബിൽ കുടിശ്ശികയുണ്ട് എന്ന് പറയുന്നു. ഔദ്യോഗിക ആപ്പ്/ഓഫീസിൽ പരിശോധിക്കുക.",
        "hi": "बिल बकाया बताया जा रहा है। आधिकारिक ऐप/ऑफिस में जाँच करें।",
    },
    # ---------- Bank / account ----------
    {
        "pattern": r"(account|card|upi|wallet).{0,30}(blocked|suspended|frozen|deactivated|will be closed)|അക്കൗണ്ട്.{0,20}ബ്ലോക്ക്|खाता.{0,20}(बंद|ब्लॉक)",
        "weight": 2,
        "ml": "അക്കൗണ്ട് ബ്ലോക്ക് ആകും എന്ന് ഭയപ്പെടുത്തുന്നു. ബാങ്ക് ഇങ്ങനെ SMS അയയ്ക്കില്ല.",
        "hi": "खाता बंद होने का डर दिखाया जा रहा है। बैंक ऐसे संदेश नहीं भेजता।",
    },
    {
        "pattern": r"\bkyc\b|pan (card )?(update|verification)|aadhaar (update|link)",
        "weight": 2,
        "ml": "KYC/ആധാർ പുതുക്കണം എന്ന് പറയുന്നു. ബാങ്കുകൾ SMS ലിങ്ക് വഴി KYC ചോദിക്കില്ല.",
        "hi": "KYC/आधार अपडेट करने को कहा जा रहा है। बैंक SMS लिंक से KYC नहीं मांगते।",
    },
    # ---------- Sensitive info ----------
    {
        "pattern": r"\b(otp|pin|cvv|password|card number|expiry)\b",
        "weight": 3,
        "ml": "OTP / PIN / CVV ചോദിക്കുന്നു. ഒരിക്കലും ആരോടും പങ്കുവെക്കരുത്.",
        "hi": "OTP / PIN / CVV मांगा जा रहा है। कभी किसी से साझा न करें।",
    },
    # ---------- Links and apps ----------
    {
        "pattern": r"https?://|bit\.ly|tinyurl|goo\.gl|\bwww\.|\.xyz|\.top\b|\.in/[a-z0-9]{4,}",
        "weight": 2,
        "ml": "സംശയാസ്പദമായ ലിങ്ക് ഉണ്ട്. അതിൽ ക്ലിക്ക് ചെയ്യരുത്.",
        "hi": "संदिग्ध लिंक है। उस पर क्लिक न करें।",
    },
    {
        "pattern": r"\.apk\b|install (this )?app|download (this )?app",
        "weight": 3,
        "ml": "അപരിചിതമായ ആപ്പ്/APK ഇൻസ്റ്റാൾ ചെയ്യാൻ പറയുന്നു. ഫോണിലെ വിവരങ്ങൾ മോഷ്ടിക്കപ്പെടാം.",
        "hi": "अनजान ऐप/APK इंस्टॉल करने को कहा जा रहा है। फोन का डेटा चोरी हो सकता है।",
    },
    {
        "pattern": r"anydesk|teamviewer|quicksupport|screen ?share",
        "weight": 3,
        "ml": "ഫോൺ നിയന്ത്രിക്കാൻ കഴിയുന്ന ആപ്പ് ഇൻസ്റ്റാൾ ചെയ്യാൻ പറയുന്നു. ഇത് അപകടമാണ്.",
        "hi": "फोन कंट्रोल करने वाला ऐप इंस्टॉल करने को कहा जा रहा है। यह खतरनाक है।",
    },
    # ---------- Call this number ----------
    {
        "pattern": r"call (now|us|this number|immediately)|contact.{0,20}\d{10}|whatsapp.{0,20}\d{10}",
        "weight": 1,
        "ml": "അപരിചിത നമ്പറിൽ വിളിക്കാൻ ആവശ്യപ്പെടുന്നു.",
        "hi": "अनजान नंबर पर कॉल करने को कहा जा रहा है।",
    },
    # ---------- Prizes and money ----------
    {
        "pattern": r"lottery|you (have )?won|winner|prize|lucky draw|cashback|reward points|സമ്മാനം|ലോട്ടറി|इनाम|लॉटरी",
        "weight": 2,
        "ml": "സമ്മാനം/ലോട്ടറി അടിച്ചു എന്ന് പറയുന്നു. ഇത് സാധാരണ തട്ടിപ്പാണ്.",
        "hi": "इनाम/लॉटरी जीतने की बात कही गई है। यह आम ठगी है।",
    },
    {
        "pattern": r"processing fee|registration fee|advance (fee|payment)|claim fee|send (money|rs|₹)|transfer .{0,15}(rs|₹)",
        "weight": 2,
        "ml": "മുൻകൂർ പണം/ഫീസ് ആവശ്യപ്പെടുന്നു. ശരിയായ സ്ഥാപനങ്ങൾ ഇങ്ങനെ ചോദിക്കില്ല.",
        "hi": "पहले से पैसे/फीस मांगी जा रही है। असली संस्थाएँ ऐसा नहीं करतीं।",
    },
    {
        "pattern": r"refund.{0,40}(upi|pin|link|click)|(upi|pin).{0,40}refund|collect request|scan (the )?qr.{0,20}(receive|refund)",
        "weight": 3,
        "ml": "റീഫണ്ട് തരാം എന്ന് പറഞ്ഞ് UPI PIN/QR ചോദിക്കുന്നു. PIN കൊടുത്താൽ പണം പോകും, കിട്ടില്ല.",
        "hi": "रिफंड के नाम पर UPI PIN/QR मांगा जा रहा है। PIN देने से पैसे कटते हैं, आते नहीं।",
    },
    # ---------- Fake authority ----------
    {
        "pattern": r"\b(cbi|police|customs|narcotics|ed officer|cyber cell|trai)\b.{0,60}(arrest|case|warrant|parcel|illegal|fir)|digital arrest|video call.{0,20}(police|officer)",
        "weight": 3,
        "ml": "പോലീസ്/CBI/കസ്റ്റംസ് എന്ന് പറഞ്ഞ് ഭയപ്പെടുത്തുന്നു. പോലീസ് ഫോണിലൂടെ അറസ്റ്റ് ചെയ്യില്ല.",
        "hi": "पुलिस/CBI/कस्टम का नाम लेकर डराया जा रहा है। पुलिस फोन पर गिरफ्तारी नहीं करती।",
    },
    {
        "pattern": r"(parcel|courier|package|consignment).{0,40}(held|stuck|seized|undelivered|customs|pending)|fedex|dhl.{0,20}(parcel|illegal)",
        "weight": 2,
        "ml": "പാർസൽ/കൊറിയർ തടഞ്ഞു എന്ന് പറഞ്ഞ് പണം ചോദിക്കുന്നു. ഇത് തട്ടിപ്പാണ്.",
        "hi": "पार्सल/कूरियर रुकने की बात कहकर पैसे मांगे जा रहे हैं। यह ठगी है।",
    },
    {
        "pattern": r"sim.{0,30}(block|deactivat|suspend|expire)|mobile number.{0,30}(block|disconnect)",
        "weight": 2,
        "ml": "സിം/നമ്പർ ബ്ലോക്ക് ആകും എന്ന് പറയുന്നു. ഇത് തട്ടിപ്പിന്റെ ഭാഗമാണ്.",
        "hi": "सिम/नंबर बंद होने की बात कही जा रही है। यह ठगी का तरीका है।",
    },
    # ---------- Job and family tricks ----------
    {
        "pattern": r"work from home|earn.{0,15}(per day|daily|\d+ ?k)|part[- ]time job|like(s)? youtube videos|task.{0,15}(earn|income)",
        "weight": 2,
        "ml": "വീട്ടിലിരുന്ന് എളുപ്പത്തിൽ പണം എന്ന വാഗ്ദാനം. ഇത് സാധാരണ തട്ടിപ്പാണ്.",
        "hi": "घर बैठे आसान कमाई का वादा। यह आम ठगी है।",
    },
    {
        "pattern": r"(grandson|granddaughter|son|daughter|nephew|friend).{0,40}(accident|hospital|arrested|emergency|trouble).{0,60}(send|transfer|pay|money)|new number.{0,20}(send|pay|money)|hi (mom|dad|papa|amma)",
        "weight": 3,
        "ml": "ബന്ധുവിന് അപകടം/ആവശ്യം എന്ന് പറഞ്ഞ് പണം ചോദിക്കുന്നു. ആദ്യം അവരെ പഴയ നമ്പറിൽ വിളിച്ച് ഉറപ്പാക്കുക.",
        "hi": "रिश्तेदार की मुसीबत बताकर पैसे मांगे जा रहे हैं। पहले उन्हें पुराने नंबर पर कॉल करके पुष्टि करें।",
    },

    # ---------- SAFE signals (negative weight) ----------
    {
        "pattern": r"do not share|don't share|never share|ആരോടും പങ്കുവെക്കരുത്|किसी से साझा न करें",
        "weight": -2,
        "ml": "",
        "hi": "",
    },
    {
        "pattern": r"(payment|bill|amount).{0,30}(received|successful|paid)|thank you for (your )?payment",
        "weight": -2,
        "ml": "",
        "hi": "",
    },
]

VERDICT = {
    "ml": {"scam": "⚠️ തട്ടിപ്പാകാൻ സാധ്യത", "safe": "✅ സുരക്ഷിതമെന്ന് തോന്നുന്നു"},
    "hi": {"scam": "⚠️ धोखाधड़ी की संभावना", "safe": "✅ सुरक्षित लगता है"},
}

SAFE_NOTE = {
    "ml": "വ്യക്തമായ തട്ടിപ്പ് ലക്ഷണങ്ങൾ കണ്ടില്ല. എങ്കിലും സംശയമുണ്ടെങ്കിൽ കുടുംബാംഗങ്ങളോട് ചോദിക്കുക.",
    "hi": "कोई साफ़ ठगी के संकेत नहीं मिले। फिर भी शक हो तो परिवार से पूछें।",
}

NEXT_STEPS = {
    "ml": [
        "ലിങ്കിൽ ക്ലിക്ക് ചെയ്യരുത്. നമ്പറിൽ തിരികെ വിളിക്കരുത്.",
        "OTP, PIN, പാസ്‌വേഡ് ആരുമായും പങ്കുവെക്കരുത്.",
        "KSEB ആണെങ്കിൽ ഔദ്യോഗിക നമ്പർ 1912 ൽ വിളിച്ച് ഉറപ്പാക്കുക.",
        "പണം നഷ്ടപ്പെട്ടെങ്കിൽ ഉടൻ 1930 (സൈബർ ഹെൽപ്പ്‌ലൈൻ) ൽ വിളിക്കുക.",
        "ഈ സന്ദേശം കുടുംബാംഗങ്ങളെ കാണിക്കുക.",
    ],
    "hi": [
        "लिंक पर क्लिक न करें। नंबर पर वापस कॉल न करें।",
        "OTP, PIN, पासवर्ड किसी से साझा न करें।",
        "बिजली विभाग हो तो आधिकारिक नंबर पर खुद कॉल करके पुष्टि करें।",
        "पैसे कट गए हों तो तुरंत 1930 (साइबर हेल्पलाइन) पर कॉल करें।",
        "यह संदेश परिवार को दिखाएँ।",
    ],
}

SAMPLES = {
    "KSEB scam": "KSEB bill pending. Your power will be disconnected tonight. Call now 9876543210 immediately.",
    "Bank KYC scam": "Dear customer, your SBI account will be blocked. Update KYC now: http://bit.ly/sbi-kyc",
    "Lottery scam": "Congratulations! You have won Rs 25 lakh lucky draw. Pay registration fee to claim your prize.",
    "Parcel / digital arrest": "This is CBI. A parcel in your name is held at customs with illegal items. Join video call or face arrest.",
    "Family emergency": "Hi Amma, this is my new number. I had an accident, please send money urgently.",
    "Real OTP (safe)": "123456 is your OTP for login. Do not share it with anyone.",
    "Real payment (safe)": "Your KSEB bill payment of Rs 450 was successful. Thank you for payment.",
}