# 1.10
def anonymousLetter(letter, magazine):
    H = {}
    for l in list(letter):
        if l != " ":
            if l in H:
                H[l] = H[l] + 1
            else:
                H[l] = 1

    for m in list(magazine):
        if m != " ":
            if m in H:
                H[m] = H[m] - 1

    for h in H:
        if H[h] > 0:
            return -1
    return 1

letter = "whats up dudes"
magazine = "super man whats up i dont dudes know"
print anonymousLetter(letter, magazine)
magazine = "super man whats up i dont know"
print anonymousLetter(letter, magazine)
print
