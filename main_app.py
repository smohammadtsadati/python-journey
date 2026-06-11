import text_tools

user_text = input("Enter a sentence: ")

word_count = text_tools.count_words(user_text)
upper_text = text_tools.make_uppercase(user_text)

print(f"Number of words: {word_count}")
print(f"Uppercase version: {upper_text}")