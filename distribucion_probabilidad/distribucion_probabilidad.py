import random

candidate_words = ["ingeniero", "homeless", "loco"]

# Las probabilidades de c/palabra están definidas
your_mental_model = [0.99, 0.001, 0.009]

chosen_word = random.choices(candidate_words, weights=your_mental_model)

print(f"Edu es {chosen_word[0]}.")