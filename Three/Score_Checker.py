def scoreChecker(score):
    result = score

    if(score >= 90):
        print("Selamat! Anda mendapatkan nilai A.")
    elif(score >= 80 and score <= 89):
        print("Anda mendapatkan nilai B.")
    elif(score >= 70 and score <= 79):
        print("Anda mendapatkan nilai C.")
    elif(score >= 60 and score <= 69):
        print("Anda mendapatkan nilai D.")
    else:
        print("Anda mendapatkan nilai E.")

    return result


score = 90

scoreChecker(90)
