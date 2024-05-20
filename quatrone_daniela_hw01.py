import json

counted_characters = {}

with open('alice.txt') as file:
    for line in file:
        cleaned_lines = line.strip().lower().replace(" ", "")
        for character in cleaned_lines:
            if character not in counted_characters:
                counted_characters[character] = 1
            else:
                counted_characters[character] += 1

with open ('hw01_output.json', mode='w', encoding='utf-8') as file:
    json.dump(counted_characters, file, ensure_ascii=False, indent=4, sort_keys=True)