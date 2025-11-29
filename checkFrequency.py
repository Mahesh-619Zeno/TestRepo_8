import os

file_path = "sample_text.txt"

if not os.path.exists(file_path):
    with open(file_path, "w") as f:
        f.write("apple banana apple orange banana apple grape")

words = []
with open(file_path, "r") as f:
    for l in f:
        for w in l.strip().split():
            words.append(w)

freq = {}
for w in words:
    if w not in freq:
        freq[w] = 0
    freq[w] += 1

with open("word_count_report.txt", "w") as f:
    for w, c in freq.items():
        f.write(f"{w}: {c}\n")

print("Word count report generated in 'word_count_report.txt'")
