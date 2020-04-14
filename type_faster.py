import time as t
import matplotlib.pyplot as plt
import random

words = ["milk", "butter", "tea", "orange", "juice", "bread", "cheese", "coffee"]

word = random.choice(words)

times = []

mistakes = 0

print ("Hello! I'll help you to type faster. I'll give you word and you type this five times.")
print ("Our word will be " + word)

input ("If you will be redy press enter")

while len(times) < 5:
    start = t.time()
    userWord = input ("Write " + word + " ")
    end = t.time()
    elapsed = end - start
    times.append(elapsed)
    
    if word != userWord.lower():
        mistakes += 1
    continue

print ("You made " + str(mistakes) + " mistake(s)")

plt.plot(times)
plt.show()
