def generate_hashtag(s):
    hashtag = "#"
    if len(s) > 140:
        return False
    if s == "":
        return False
    for i in s.split():
        hashtag += i.capitalize()
    print(hashtag)
    return hashtag