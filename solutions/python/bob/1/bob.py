def response(hey_bob):
    hey_bob = hey_bob.strip()
    if hey_bob == "":
        return "Fine. Be that way!"

    Is_a_question = (hey_bob[-1] == '?')
    Is_all_capital_letters = hey_bob.isupper()

    if Is_a_question and Is_all_capital_letters:
        return "Calm down, I know what I'm doing!"
    if Is_a_question:
        return "Sure."
    if Is_all_capital_letters:
        return "Whoa, chill out!"
    
    return "Whatever."
