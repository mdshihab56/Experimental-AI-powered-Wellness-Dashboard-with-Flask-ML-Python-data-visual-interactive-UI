def predict_status(
    sleep,
    stress,
    productivity,
    water,
    screen,
    exercise,
    moodText
):
    score = 0
    if sleep >= 7 and sleep <= 9:
        score += 3
    elif sleep >= 5:
        score += 1
    else:
        score -= 2
    if stress <= 3:
        score += 3
    elif stress <= 6:
        score += 1
    else:
        score -= 3
    if productivity >= 8:
        score += 3
    elif productivity >= 5:
        score += 1
    else:
        score -= 2
    if water >= 6:
        score += 2
    else:
        score -= 1
    if screen <= 4:
        score += 2
    elif screen <= 7:
        score += 0
    else:
        score -= 3
    if exercise >= 30:
        score += 3
    elif exercise >= 10:
        score += 1
    else:
        score -= 2
    moodText = moodText.lower()
    positive_words = [
        "happy",
        "good",
        "great",
        "awesome",
        "excellent",
        "motivated",
        "relaxed",
        "calm"
    ]
    negative_words = [
        "sad",
        "angry",
        "depressed",
        "bad",
        "tired",
        "stress",
        "broken",
        "upset"
    ]
    for word in positive_words:
        if word in moodText:
            score += 2
    for word in negative_words:
        if word in moodText:
            score -= 2
    if score >= 10:
        return "Excellent"
    elif score >= 5:
        return "Balanced"
    elif score >= 1:
        return "Stressed"
    else:
        return "Burnout"