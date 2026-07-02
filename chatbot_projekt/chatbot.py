# chatbot.py
from openai import OpenAI, APIError


class ChatbotError(Exception):
    pass


class Chatbot:
    def __init__(self, model: str, system_prompt: str) -> None:
        self.model = model
        self.system_prompt = system_prompt
        self.client = OpenAI()
        self.messages = [{"role": "system", "content": system_prompt}]

    def talk(self, user_prompt: str) -> str | None:
        """Frage Openai mit userprompt an."""

        if not user_prompt.strip():
            raise ChatbotError("Prompt darf nicht leer sein!")

        self.messages.append({"role": "user", "content": user_prompt})
        response = self._call_chatbot()
        if not response:
            raise ChatbotError("Leere Response von API.")

        self.messages.append({"role": "assistant", "content": response})
        return response

    def _call_chatbot(self) -> str | None:
        """Interne Methode zur Anfrage an die OPEN AI Api."""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages,  # type:ignore
            )
            return response.choices[0].message.content

        except APIError as e:
            # hier fehler loggen!
            raise ChatbotError(f"Fehler in der Kommunikation mit der API: {e}")
