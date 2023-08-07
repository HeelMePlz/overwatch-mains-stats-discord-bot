import requests

API_URL = "https://overfast-api.tekrop.fr/players/"
# HERO_NAME = "ana"
# BATTLE_NET_TAG = "HeelMePlz#2652"


def parse_battletag(battletag: str) -> str:
    return battletag.replace("#", "-")


def get_player_summary(player_id: str) -> dict:
    response = requests.get(url=API_URL + player_id + "/summary")
    return response.json()


def is_private_profile(player_summary: dict) -> bool:
    if player_summary["privacy"] == "private":
        return True


def get_hero_stats_summary(player_id: str, hero_name: str) -> dict:
    response = requests.get(url=API_URL + player_id + "/stats/summary")
    return response.json()["heroes"][hero_name]


def get_gamemode_hero_stats(player_id: str, gamemode: str, hero_name: str) -> dict:
    response = requests.get(url=API_URL + player_id + "/stats/career", params=gamemode)
    return response.json()[hero_name]


# PLAYER_ID = parse_battletag(BATTLE_NET_TAG)
# PLAYER_SUMMARY = get_player_summary(PLAYER_ID)

# if is_private_profile(PLAYER_SUMMARY):
#     print("Profile is private.")

# HERO_STATS = get_hero_stats_summary(PLAYER_ID, HERO_NAME)

# QUICK_PLAY = {"gamemode": "quickplay"}
# QUICK_PLAY_HERO_STATS = get_gamemode_hero_stats(PLAYER_ID, QUICK_PLAY, HERO_NAME)

# COMPETITIVE = {"gamemode": "competitive"}
# COMPETITIVE_HERO_STATS = get_gamemode_hero_stats(PLAYER_ID, COMPETITIVE, HERO_NAME)
