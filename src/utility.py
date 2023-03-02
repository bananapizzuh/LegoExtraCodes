import os, time, yaml, requests

config = {}


def wait(ms):
    start = int(round(time.time() * 1000))
    now = int(round(time.time() * 1000))
    while now <= start + ms:
        now = int(round(time.time() * 1000))
    # print(f"Waited: {abs(start-now)} Target: {ms}ms ")
    return now - start


def load_games():
    load_config()
    # print(config)
    games = []
    game_codes = []
    code_names = []

    for game in config["games"]:
        try:
            games.append(config["games"][game]["name"])
            game_codes.append(config["games"][game]["codes"])
            code_names.append(config["games"][game]["code_names"])
        except:
            print(f"Failed to load {game} from config.")
    return games, game_codes, code_names, config["games"]


def load_config():
    global config

    if not os.path.isfile("config.yaml"):
        with open("config.yaml", "w") as f:
            f.write(
                requests.get(
                    "https://raw.githubusercontent.com/bananapizzuh/LegoExtraCodes/main/src/config.yaml"
                ).text
            )
            print("fr")
    with open("config.yaml", "r") as openfile:
        config = yaml.safe_load(openfile)
    # print(config)


def update():
    load_config()
    current_version = config["version"]
    try:
        response = requests.get(
            "https://raw.githubusercontent.com/bananapizzuh/LegoExtraCodes/main/src/config.yaml"
        )
    except:
        print(
            "Could not get response. If you would like to update please visit the github repository."
        )
        return
    newest_version = yaml.safe_load(response.content)["version"]
    if current_version < newest_version:
        print("Update available.")
        # open('update.zip', 'wb').write(r.content)


update()
