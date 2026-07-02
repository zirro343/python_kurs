"""
# main.py
# messages werden im Wechsel an den Bot gesendet.
# System -> User -> Assistant -> User -> Assistant -> User -> Assistant
"""

import os

from dotenv import load_dotenv

from chatbot import Chatbot, ChatbotError


def main():
    load_dotenv()
    system_prompt: str = os.getenv("SYSTEM_PROMPT", "default: talk spanish")
    chatbot = Chatbot(model="gpt-4o-mini", system_prompt=system_prompt)

    while True:
        ui = input("> ")

        if ui in ["quit", "exit", "goodbye"]:
            print("Goodbye!")
            break

        if ui == ":messages":
            for msg in chatbot.messages:
                print(msg)
            continue

        try:
            text = chatbot.talk(ui)
            print(f"Bot: {text}")
        except ChatbotError as e:
            print(f"Fehler: {e}")


if __name__ == "__main__":
    main()
