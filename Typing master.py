import time
import random

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "A journey of a thousand miles begins with a single step.",
    "To be or not to be, that is the question.",
    "All that glitters is not gold.",
    "The early bird catches the worm."
]

def calculate_accuracy(original, typed):
    original_words = original.split()
    typed_words = typed.split()

    correct_words = 0
    for original_word, typed_word in zip(original_words, typed_words):
        if original_word == typed_word:
            correct_words += 1

    accuracy = (correct_words / len(original_words)) * 100
    return accuracy

def main():
    text_to_type = random.choice(sentences)
    print("Type the following text:")
    print(text_to_type)
    print()

    start_time = time.time()
    user_input = input("Start typing here: ")
    end_time = time.time()
    time_taken = end_time - start_time
    accuracy = calculate_accuracy(text_to_type, user_input)

    print(f"\nTime taken: {time_taken:.2f} seconds")
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    main()