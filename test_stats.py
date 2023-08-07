import json

from stats import (
    API_URL,
    get_hero_stats_summary,
    get_player_summary,
    is_private_profile,
    parse_battletag,
)


def test_parse_battletag():
    expected = "KRUSHER99-8008"

    actual = parse_battletag("KRUSHER99#8008")

    assert actual == expected


def test_get_player_summary(requests_mock):
    TEST_PLAYER_ID = "KRUSHER99-8008"
    requests_mock.get(
        f"{API_URL}{TEST_PLAYER_ID}/summary", json={"username": "KRUSHER99"}
    )
    expected = {"username": "KRUSHER99"}

    actual = get_player_summary(TEST_PLAYER_ID)

    assert actual == expected


def test_is_private_profile():
    TEST_PLAYER_SUMMARY = {"username": "KRUSHER99-8008", "privacy": "private"}
    expected = True

    actual = is_private_profile(TEST_PLAYER_SUMMARY)

    assert actual == expected


def test_get_hero_stats_summary(requests_mock):
    TEST_PLAYER_ID = "KRUSHER99-8008"
    TEST_HERO_NAME = "Jetpack Cat"
    HERO_STATS_SUMMARY_JSON = {
        "general": "",
        "heroes": {"Jetpack Cat": {"games_won": 6, "games_lost": 9}},
        "roles": "",
    }
    requests_mock.get(
        f"{API_URL}{TEST_PLAYER_ID}/stats/summary", json=HERO_STATS_SUMMARY_JSON
    )
    expected = {"games_won": 6, "games_lost": 9}

    actual = get_hero_stats_summary(TEST_PLAYER_ID, TEST_HERO_NAME)

    assert actual == expected
