import os

from modules.config import get_config
from modules.html import render_tweet_to_html
from modules.image import html_to_image
from modules.twitter import get_tweet

CONFIG_PATH = "config.json"


def main() -> None:
    config = get_config(CONFIG_PATH)

    if config.get("bearer_token"):
        url = input("Enter tweet URL: ").strip()

        if not os.path.exists("out"):
            os.makedirs("out")

        tweet = get_tweet(url, config)
        html = render_tweet_to_html(tweet, config)
        html_to_image(html, config)
    else:
        print("Operation failed.")


if __name__ == "__main__":
    main()
