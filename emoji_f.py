from emoji.core import emojize
import re


def text_to_emoji(text):
    emoji_dict = {
        "looking": "👀",
        "eat": "🍲",
        "hungry": "😋",
        "chef": "🧑‍🍳",
        "happy": "😊",
        "sad": "😢",
        "love": "❤️",
        "fire": "🔥",
        "star": "⭐",
        "sun": "☀️",
        "moon": "🌙",
        "music": "🎵",
        "dance": "💃",
        "sleep": "😴",
        "book": "📚",
        "car": "🚗",
        "plane": "✈️",
        "phone": "📱",
        "computer": "💻",
        "coffee": "☕",
        "dog": "🐶",
        "cat": "🐱",
    }
    words = re.findall(r"\b\w+\b", text.lower())
    emojis = []

    for word in words:
        if word in emoji_dict:
            emojis.append(emoji_dict[word])
        else:
            for key in emoji_dict:
                if key in word:
                    emojis.append(emoji_dict[key])
                    break
            else:
                emojis.append(emojize(f":{word}:", language="alias"))

    return "".join(emojis)

# Fun purpose
if __name__ == "__main__":
    while True:
        user_input = input("Enter text to convert to emoji (or type 'exit' to quit): ")
        if user_input.lower() == "exit":
            break
        print(text_to_emoji(user_input))
