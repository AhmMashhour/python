def count_vowels(text: str) -> int:
    """
    Count the number of vowels (a, e, i, o, u) in the given text.
    The count is case-insensitive.
    """
    vowels = "aeiou"
    return sum(text.lower().count(v) for v in vowels)


if __name__ == "__main__":
    user_input = input("Enter a string: ")
    vowel_count = count_vowels(user_input)
    print(f"Number of vowels: {vowel_count}")
