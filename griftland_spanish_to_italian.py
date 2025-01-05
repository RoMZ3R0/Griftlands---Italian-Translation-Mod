"""
Title: Griftland translation script
Author: RoMZERO
Version: 1.0

Description:
This script is designed to translate text from a `.po` file (commonly used for localization) 
from Spanish to Italian. It utilizes the Google GenAI API with a specifically configured 
Generative AI model tailored for translating game-related content, ensuring high semantic 
accuracy and contextual relevance.

The translation process adheres to the following principles:
- Maintains the original meaning and context of the source text.
- Avoids literal translations unless necessary, prioritizing fluency and naturalness in Italian.
- Preserves proper names, symbols, and English text without translation.
- Handles escape sequences (`\n`) and special characters properly.
- Ensures variables (e.g., `{1}`, `player:`, `\\n`) remain unaltered.

Features:
- The script reads lines from an input `.po` file (`es.po`) and translates only 
  the content of lines starting with `msgstr`.
- Translated content is cleaned to remove unnecessary quotes, correct formatting, and maintain proper spacing.
- Handles exceptions gracefully, returning the original text if an error occurs during translation.
- Writes the translated content to a new `.po` file (`it.po`) while preserving the file's structure.

Note:
The script includes a 4-second delay between translations to avoid exceeding the API request limit.
"""

import os
import google.generativeai as genai
import time
import re

# Configure GenAI API
genai.configure(api_key="API key")

# Define the model configuration
generation_config = {
    "temperature": 0,  # Controls randomness in text generation
    "top_p": 0.95,  # Nucleus sampling parameter
    "top_k": 40,  # Limits the set of tokens to sample from
    "max_output_tokens": 8192,  # Maximum tokens in the response
    "response_mime_type": "text/plain",  # Defines the MIME type of the response
}

# Initialize the generative model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction=(
        # Instruction to fine-tune the model's behavior for translations
        "This model is specifically tailored for the translation of the card game Griftlands.\n"
        "The model is designed to translate text from Spanish to Italian with high semantic accuracy, preserving the "
        "original meaning and context of the text.\n"
        "It must avoid literal translations unless necessary and ensure that the translation is natural and accurate in Italian.\n"
        "The model does not translate proper names and should refrain from inventing or adding words not present in the original text.\n"
        "The translation must maintain consistency, fluency, and adherence to the linguistic tone of the source text.\n"
        "The model does not translate English text.\n"
        "It must handle game-related terminology, including unique card names, mechanics, dialogues, and story elements, ensuring these remain "
        "faithful to the game's context. Special attention should be given to preserving the tone and style of character dialogues, which often "
        "include colloquial, slang, or region-specific expressions. The model should prioritize clarity and naturalness in conveying gameplay "
        "instructions or narrative elements, making the translation intuitive and engaging for Italian-speaking players.\n"
        "The presence of symbols such as \"{1}\" corresponds to a numeric variable and must be copy/pasted in the translation. This ensures proper "
        "agreement between the variable and the translated term while preserving grammatical accuracy in Italian.\n"
        "The string can contain variables such as \"player:\", \"agent:\", \"\\n\", \"!angry_accuse\", \"!angry\", \"$neutralDirect\" that must not be translated.\n"
        "The model translates the sentence without adding any comment and preserving special characters."
    ),
)

# Start a new chat session
chat_session = model.start_chat(history=[])

# Function to clean translated text
def clean_translated_text(text):
    """
    Cleans and formats the translated text:
    - Removes unnecessary quotes.
    - Ensures proper handling of escaped characters.
    - Reduces multiple spaces to a single space.
    """
    text = text.strip()
    text = re.sub(r'^"+|"+$', '', text)  # Remove leading/trailing double quotes
    text = text.replace('\\"', '"')  # Fix escaped quotes
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    return text

# Function to translate a single line
def translate_line(line):
    """
    Sends a line to the chat session for translation and cleans the result.
    If an error occurs, the original line is returned.
    """
    try:
        response = chat_session.send_message(line)
        translated_text = response.text.strip()
        return clean_translated_text(translated_text)
    except Exception as e:
        print(f"Error while translating line: {line}\nError: {e}")
        return line  # Return the original text in case of an error

# File processing: reading and translating
with open("es_v18_corretto.po", encoding="utf-8") as source_file:
    with open("it_v19.po", "w", encoding="utf-8") as target_file:
        for line in source_file:
            if line.startswith("msgstr "):  # Process lines starting with "msgstr"
                original_text = line.split("msgstr ", 1)[1].strip()  # Extract the original text
                
                # Ensure escape sequences (\n) are preserved
                translated_text = translate_line(original_text)
                translated_text = translated_text.replace("\\n", "\n").replace("\n", "\\n")
                
                # Update the line with the translated text
                line = f'msgstr_ITA "{translated_text}"\n'
                time.sleep(4)  # Pause to avoid hitting the API rate limit

            print(line.strip())  # Print the processed line
            target_file.write(line)  # Write the line to the output file
            target_file.flush()  # Ensure immediate writing to disk
