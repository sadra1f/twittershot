import os
import webview

from modules.config import get_config
from modules.html import render_tweet_to_html
from modules.image import html_to_image
from modules.twitter import get_tweet


class API:
    def __init__(self, config_path: str) -> None:
        self.config_path = config_path

    def exit(self) -> None:
        webview.windows[self.win_index].destroy()

    def render(self, url: str) -> None:
        config = get_config(self.config_path)

        if config.get("bearer_token"):

            if not os.path.exists("out"):
                os.makedirs("out")

            tweet = get_tweet(url, config)
            html = render_tweet_to_html(tweet, config)
            html_to_image(html, config)
        else:
            print("Operation failed.")
