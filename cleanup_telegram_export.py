import json

def clean_telegram_chat(input_file, output_file):
    # Load the Telegram export JSON
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    cleaned_data = {'messages': []}
    
    for message in data['messages']:
        # Check if the message is a text message; adjust conditions as needed
        if message['type'] == 'message' and 'text' in message:
            # Create a new dictionary for the cleaned message
            cleaned_message = {
                'date': message['date'],
                'from': message.get('from'),  # Use .get() to avoid KeyError if the key doesn't exist
                'text': message['text']
            }
            cleaned_data['messages'].append(cleaned_message)
    
    # Save the cleaned data to a new JSON file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(cleaned_data, f, ensure_ascii=False, indent=4)

# Example usage
input_file_path = '/Users/path-to-file/result.json'
output_file_path = '/Users/path-to-file/cleaned_telegram_chat.json'
clean_telegram_chat(input_file_path, output_file_path)
