import requests

def get_word_definition(word):
    """
    Fetches the definition of a word using the Free Dictionary API.

    Args:
        word (str): The word to look up.

    Returns:
        dict: The JSON response from the API if successful.
        str: Error message if the API call fails.
    """
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

def pretty_print_definitions(definitions):
    """
    Prints the word definitions in a clean and readable format.

    Args:
        definitions (list or dict): The JSON response containing the word definitions.
    """
    if not isinstance(definitions, list):
        print(definitions)
        return

    for entry in definitions:
        word = entry.get("word", "Unknown Word")
        print(f"\n🔤 Word: {word}")

        phonetics = entry.get("phonetics", [])
        for phonetic in phonetics:
            text = phonetic.get("text")
            audio = phonetic.get("audio")
            if text:
                print(f"   📌 Pronunciation: {text}")
            if audio:
                print(f"   🔊 Audio: {audio}")

        meanings = entry.get("meanings", [])
        for meaning in meanings:
            part_of_speech = meaning.get("partOfSpeech", "Unknown")
            print(f"\n📖 Part of Speech: {part_of_speech}")

            for definition in meaning.get("definitions", []):
                definition_text = definition.get("definition", "No definition provided.")
                example = definition.get("example", None)
                print(f"   - {definition_text}")
                if example:
                    print(f"     e.g., \"{example}\"")

        print("\n" + "-" * 50)  # Separator for readability

def main():
    print("Free Dictionary API Word Lookup")
    word = input("Enter a word to look up: ").strip()
    result = get_word_definition(word)
    pretty_print_definitions(result)

if __name__ == "__main__":
    main()
