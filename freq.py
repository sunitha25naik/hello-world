def calculate_letter_frequency(sentence):
    # Initialize an empty dictionary to store letter frequencies
    letter_frequency = {}

    # Iterate through each character in the sentence
    for char in sentence:
        # Check if the character is a letter (ignore case)
        if char.isalpha():
            # Convert the letter to lowercase to make the counting case-insensitive
            char = char.lower()

            # Update the letter frequency in the dictionary
            if char in letter_frequency:
                letter_frequency[char] += 1
            else:
                letter_frequency[char] = 1

    return letter_frequency

# Get a sentence input from the user
user_sentence = input("Enter a sentence: ")

# Call the function and get the letter frequency
result = calculate_letter_frequency(user_sentence)

# Display the letter frequency
print("Letter Frequency:")
for letter, frequency in result.items():
    print(f"{letter}: {frequency}")
