import nltk
from nltk.tokenize import sent_tokenize
from collections import Counter
import re

# Download tokenizer (runs only first time)
nltk.download('punkt')

def summarize_notes(text, num_points=5):

    # Clean text
    text = re.sub(r'\s+', ' ', text)

    # Split text into sentences
    sentences = sent_tokenize(text)

    # Find word frequency
    words = re.findall(r'\w+', text.lower())
    freq = Counter(words)

    # Score sentences
    sentence_scores = {}

    for sentence in sentences:
        for word in sentence.lower().split():
            if word in freq:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + freq[word]

    # Pick top sentences
    summary = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_points]

    return summary


print("Paste your notes below and press Enter:\n")

user_notes = input()

summary_points = summarize_notes(user_notes)

print("\nBullet Point Summary:\n")

for point in summary_points:
    print("•", point)
