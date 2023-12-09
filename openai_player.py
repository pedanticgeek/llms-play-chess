import os
from typing import Dict
import openai


MODEL = os.getenv("OPENAI_MODEL")

class OpenAIPlayer(openai.Client):
    
    moves = []

    def make_move(self, move: str):
        self.moves.append({'role': 'user', 'content': move})
        response = self.chat.completions.create(
            messages=self.moves,
            model=MODEL,
            max_tokens=200
        )
        move = response.choices[0].message.content
        print(f"OpenAIPlayer: {move}")
        self.moves.append({'role': 'assistant', 'content': move})
        return move