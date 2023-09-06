#!/usr/bin/python3


def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', '?', and ':' characters.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Initialize an empty string to store the formatted text
    formatted_text = ""

    # Initialize a flag to track whether to add 2 new lines
    add_new_lines = False

    # Iterate through each character in the text
    for char in text:
        # Append the character to the formatted_text
        formatted_text += char

        # Check if the character is '.', '?', or ':'
        if char in ".?: ":
            add_new_lines = True

            # If it's a space, skip adding new lines
            if char == ' ':
                continue

        # If it's the end of a sentence, add 2 new lines
        if add_new_lines:
            formatted_text += '\n\n'
            add_new_lines = False

    # Print the formatted text
    print(formatted_text, end='')

# Example usage:
# text_indentation("This is a test. A simple test: With some punctuation? And more.")

