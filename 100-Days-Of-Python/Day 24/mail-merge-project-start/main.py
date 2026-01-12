import os

PLACEHOLDER = "[name]"

# This creates paths that work on both Mac and Windows
names_path = os.path.join("Input", "Names", "invited_names.txt")
letter_path = os.path.join("Input", "Letters", "starting_letter.txt")

with open(names_path) as names_file:
    names = names_file.readlines()

with open(letter_path) as letter_file:
    letter_contents = letter_file.read()

    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        
        # Create output path
        output_path = os.path.join("Output", "ReadToSend", f"letter_for_{stripped_name}.txt")
        
        with open(output_path, mode="w") as completed_letter:
            completed_letter.write(new_letter)