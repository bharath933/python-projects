import textblob
from textblob import TextBlob

wrong_spelling = ["machane learning", "data scenece"]
correct_words = []

for word in wrong_spelling:
    correct_words.append(TextBlob(word))

for i in correct_words:
    print(i.correct(), end=" ")
