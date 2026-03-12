import math
import string

common=["password","123456","admin","qwerty"]

def entropy(password):

    charset=0

    if any(c.islower() for c in password):
        charset+=26

    if any(c.isupper() for c in password):
        charset+=26

    if any(c.isdigit() for c in password):
        charset+=10

    if any(c in string.punctuation for c in password):
        charset+=32

    return len(password)*math.log2(charset)


def analyze(password):

    ent=entropy(password)

    weak=False

    for w in common:
        if w in password.lower():
            weak=True

    strength="Weak"

    if ent>60:
        strength="Strong"
    elif ent>40:
        strength="Medium"

    recommendations=[]

    if len(password)<12:
        recommendations.append("Increase password length")

    if not any(c in string.punctuation for c in password):
        recommendations.append("Add symbols")

    if weak:
        recommendations.append("Avoid dictionary words")

    return ent,strength,recommendations
