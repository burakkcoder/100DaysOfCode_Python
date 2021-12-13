sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:
sentence_words = sentence.split(" ")
sentence_words_dict = {x:len(x) for x in sentence_words}

print(sentence_words_dict)