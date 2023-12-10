## Make LLM to play Chess

I love chess, and I love playing with LLMs.

This one here is a very basic Jupyter notebook, I made in my free time, which makes OpenAI's GPT to play against Anthropic's Claude.

Personally, I think playing chess is a good indicator of how well a model can reason and plan ahead as well as follow basic instructions along the way.

Most of solutions I build for my clients use OpenAI's GPT-4 or GPT-4-Turbo, and the main purpose of this little project was to identify if Claude2.1 is worth a shot.

> Note: I used [python-chess](https://python-chess.readthedocs.io/en/latest/) library for the moves. It's a wonderful library - bravo, guys!

## Set Up

1. Rename `example.env` to `.env` and set your keys and model names.
2. Run jupyter (add moves as you need)

## Observations

I've had 3 as the maximum retry if a models gives an incorrect or illegal move, and allowed the model to re-make the move if this happens.

For each combination of games, to be a winner a model had to have 3 victories over the other model.

### Summary

Claude2.1 vs GPT-3.5-Turbo: 5-3

Claude2.1 vs GPT-4: 0-3

Claude2.1 vs GPT-4-Turbo: 0-3

### Claude 2.1

While Claude 2.1 seems to be doing alright in the earlier game, it starts trying to cheat in the middle of the game and rarely makes it to the end. It also often makes very stupid, yet legal, moves in the middle of the game like giving away the Queen. Also it tends to retract its own moves.

In summary, it's slightly better player than OpenAI's GPT-3.5-Turbo, but not comparable to GPT-4 and GPT-4-Turbo.

### OpenAI GPT-4 and GPT-4-Turbo

Pretty good players through early and mid game. Can even finish a game if plays against another GPT-4-Turbo. Can make some junior mistakes, but doesn't give away material for free.

In summary, GPT-4 and GPT-4-Turbo are way better than Claude2.1.

## PS 🫠🥴😬:

Meanwhile, the recently released Google's Gemini (via Bard prompt)

> **User**: _Can I play chess with you? Please reply only with an algebraic notation (SAN) of your move, e.g. Be5 or exd5. Keep in mind that you cannot retract your moves. You play white and start. Your first move:_

> **Bard**: _I'm still learning languages, so at the moment I can't help you with this request. So far I've only been trained to understand the languages listed in the Bard Help Center._

Come on, Google! You can do better than that!
