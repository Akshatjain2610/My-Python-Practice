#Create a dicctionary and take input from user and return the meaning of the word from the dictionary
print("WELCOME TO MY DICTIONARY !")
mydictionary = {"mutable":"Mutable is when something is changeable or has the ability to change.",
                "immutable":"Immutable is the when no change is possible over time. https://en.wikipedia.org/wiki/Immutable_object",
                "dictionary":"a book that contains a list of the words in a language in the order of the alphabet and that tells you what they mean, in the same or another language.",
                "google":"GOOGLE: Global Organization of Oriented Group Language of Earth."}
print("Enter a word for search")
input1=input()
print(mydictionary[input1])