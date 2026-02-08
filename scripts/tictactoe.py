import requests
import json
import os
import random
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

LINKS = {
    "Tile 0": "https://tinyurl.com/Fused-t1",
    "Tile 1": "https://tinyurl.com/Fused-t2", 
    "Tile 2": "https://tinyurl.com/Fused-t3",
    "Tile 3": "https://tinyurl.com/Fused-t4",
    "Tile 4": "https://tinyurl.com/Fused-t5",
    "Tile 5": "https://tinyurl.com/Fused-t6",
    "Tile 6": "https://tinyurl.com/Fused-t7",
    "Tile 7": "https://tinyurl.com/Fused-t8",
    "Tile 8": "https://tinyurl.com/Fused-t9"
}

# Extract alias from TinyURL
def extract_alias(url):
    """Extract the alias from a TinyURL link"""
    return url.split("/")[-1]

def get_tile_count():
    import datetime

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Authorization": f"Bearer {os.getenv('API_KEY')}"
    }

    tile_click_count_new = {}
    tile_click_count_difference = {}

    # Example: last 7 days of analytics
    now = datetime.datetime.utcnow()
    week_ago = now - datetime.timedelta(days=7)
    from_time = week_ago.strftime("%Y-%m-%dT%H:%M:%SZ")
    to_time = now.strftime("%Y-%m-%dT%H:%M:%SZ")

    for tile_name, url in LINKS.items():
        alias = extract_alias(url)
        analytics_url = "https://api.tinyurl.com/analytics/raw/json"
        params = {
            "alias": alias,
            "from": from_time,
            "to": to_time
        }

        try:
            response = requests.get(url=analytics_url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()

            # TinyURL analytics logs: each entry in 'data' is a click event
            clicks = len(data.get('data', []))
            tile_click_count_new[tile_name] = clicks
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for {tile_name}: {e}")
            tile_click_count_new[tile_name] = 0
        except (KeyError, ValueError) as e:
            print(f"Error parsing data for {tile_name}: {e}")
            tile_click_count_new[tile_name] = 0

    # Calculate differences
    if not os.path.exists("tile_count.json"):
        tile_click_count_difference = tile_click_count_new.copy()
    else:
        with open("tile_count.json", "r") as f:
            tile_click_counter_old = json.load(f)
            tile_click_count_difference = {
                key: tile_click_count_new[key] - tile_click_counter_old.get(key, 0)
                for key in tile_click_count_new
            }

    # Save new counts
    with open("tile_count.json", "w") as f:
        json.dump(tile_click_count_new, f)

    print(f"Click since last run: {tile_click_count_difference}")
    return tile_click_count_difference

def tictactoe(tile_click_count):
    if not os.path.exists("game_state.json"):
        game_state = {
            "last_played": None,
            "tiles": {
                "Tile 0": None,
                "Tile 1": None,
                "Tile 2": None,
                "Tile 3": None,
                "Tile 4": None,
                "Tile 5": None,
                "Tile 6": None,
                "Tile 7": None,
                "Tile 8": None,
            },
        }
    else:
        with open("game_state.json", "r") as f:
            game_state = json.load(f)

    if game_state["last_played"] is None:
        game_state["last_played"] = random.choice([True, False])

    move = max(
        tile_click_count,
        key=lambda x: tile_click_count[x] if game_state["tiles"][x] is None else -1,
    )

    print(game_state)
    print(move)

    game_state["last_played"] = not game_state["last_played"]
    game_state["tiles"][move] = game_state["last_played"]

    print(game_state)

    winner = None
    # Check rows
    for row in range(3):
        if (
            game_state["tiles"][f"Tile {3 * row}"] is not None
            and game_state["tiles"][f"Tile {3 * row}"]
            == game_state["tiles"][f"Tile {3 * row + 1}"]
            == game_state["tiles"][f"Tile {3 * row + 2}"]
        ):
            winner = game_state["tiles"][f"Tile {3 * row}"]

    # Check columns
    for col in range(3):
        if (
            game_state["tiles"][f"Tile {col}"] is not None
            and game_state["tiles"][f"Tile {col}"]
            == game_state["tiles"][f"Tile {col + 3}"]
            == game_state["tiles"][f"Tile {col + 6}"]
        ):
            winner = game_state["tiles"][f"Tile {col}"]

    # Check diagonals
    if (
        game_state["tiles"]["Tile 0"] is not None
        and game_state["tiles"]["Tile 0"]
        == game_state["tiles"]["Tile 4"]
        == game_state["tiles"]["Tile 8"]
    ):
        winner = game_state["tiles"]["Tile 0"]

    if (
        game_state["tiles"]["Tile 2"] is not None
        and game_state["tiles"]["Tile 2"]
        == game_state["tiles"]["Tile 4"]
        == game_state["tiles"]["Tile 6"]
    ):
        winner = game_state["tiles"]["Tile 2"]

    # Check for draw
    if winner is None and all(v is not None for k, v in game_state["tiles"].items()):
        winner = "Draw"

    print(winner)

    if winner is not None and os.path.exists("game_state.json"):
        os.remove("game_state.json")
    else:
        with open("game_state.json", "w") as f:
            json.dump(game_state, f)

    return game_state, winner


def update_readme(game_state, winner):
    tile_content = {}
    for tile in range(9):
        if game_state["tiles"][f"Tile {tile}"] is None:
            tile_content[f"Tile {tile}"] = (
                f"[![Tile {tile}](https://github.com/Fused-Gaming/Fused-Gaming/blob/main/assets/{game_state['tiles'][f'Tile {tile}']}.png)]({LINKS[f'Tile {tile}']})"
            )
        else:
            tile_content[f"Tile {tile}"] = (
                f"[![Tile {tile}](https://github.com/Fused-Gaming/Fused-Gaming/blob/main/assets/{game_state['tiles'][f'Tile {tile}']}.png)](https://github.com/Fused-Gaming)"
            )

    README = f"""# Welcome to Fused Gaming! 🎮
### Your ultimate <img src="https://img.icons8.com/color/96/000000/github--v1.png" height="24"/>Gaming Community Hub

<p align="center">
  <a href="https://github.com/Fused-Gaming"><img src="https://img.icons8.com/color/96/000000/internet.png" height="16"/>Our Projects</a> •
  <a href="https://x.com/fuseddotgg"><img src="https://img.icons8.com/color/96/000000/twitter-circled.png" height="16"/>Twitter</a> •
  <a href="https://www.linkedin.com/company/fusedgg/"><img src="https://img.icons8.com/color/96/000000/linkedin-circled.png" height="16"/>LinkedIn</a> •
  <a href="https://t.me/fusedgg"><img src="https://img.icons8.com/color/96/000000/telegram.png" height="16"/>Telegram</a>
</p>

#### Why not play a game of Tic-Tac-Toe<img src="https://img.icons8.com/material-outlined/96/000000/delete-sign.png" height="16"/><img src="https://img.icons8.com/material-outlined/96/000000/unchecked-circle.png" height="16"/> while you're here
Click on a tile to play  
The most picked move is chosen every hour

{
        f'Current turn: <img src= "https://github.com/Fused-Gaming/Fused-Gaming/blob/master/assets/{not game_state["last_played"]}.png" alt="Current Turn" width="32"/>'
        if winner is None
        else f'Winner: <img src= "https://github.com/Fused-Gaming/Fused-Gaming/blob/master/assets/{winner}.png" alt="Winner" width="32"/>'
    }

| Tic | Tac | Toe |
|--|--|--|
| {tile_content["Tile 0"]} | {tile_content["Tile 1"]} | {tile_content["Tile 2"]} |
| {tile_content["Tile 3"]} | {tile_content["Tile 4"]} | {tile_content["Tile 5"]} |
| {tile_content["Tile 6"]} | {tile_content["Tile 7"]} | {tile_content["Tile 8"]} |

## How it works

Each open tile is a hyperlink embedded in an image which tracks the number of clicks and redirects you back to our profile.
Every time the program is run it plays the move with maximum number of clicks.
It uses GitHub Actions to run every hour using a cron job.
The rest is just a regular game of Tic-Tac-Toe
    
## About Fused Gaming

Welcome to Fused Gaming! 🚀 We're a passionate gaming organization 🎯 that brings together innovation 💡, creativity 🎨, and cutting-edge technology 💻 to create exceptional gaming experiences. Our team is dedicated to pushing the boundaries of what's possible in the gaming world 🌟.

At Fused Gaming, we specialize in developing innovative gaming solutions 🛠️, building engaging community experiences 👥, and creating tools that enhance the gaming ecosystem 🔧. From competitive esports 🏆 to casual gaming experiences 🎲, we're committed to delivering quality and excitement in everything we do.

Our community spans across multiple platforms and games 🎮, bringing together players, developers, and gaming enthusiasts from around the world 🌍. Whether you're interested in strategy games ♟️, action-packed adventures ⚔️, or competitive tournaments 🥇, there's something for everyone in the Fused Gaming universe.

We believe in the power of technology to transform gaming 🔮, and we're constantly exploring new ways to innovate and improve the gaming experience. From Discord bots 🤖 and web applications 🌐 to game modifications and community tools 🔨, our projects are designed to bring gamers together and enhance their gameplay.

Join our growing community and be part of the future of gaming! Connect with us on our social platforms 📱, contribute to our open-source projects 💻, or simply follow along as we continue to build amazing gaming experiences. Let's level up together! 🎊
"""

    with open("README.md", "w") as f:
        f.write(README)


if __name__ == "__main__":
    tile_click_count = get_tile_count()
    game_state, winner = tictactoe(tile_click_count)
    update_readme(game_state, winner)