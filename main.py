from datetime import datetime
from jinja2 import Environment, PackageLoader, select_autoescape
import os
import json
import tweepy
import imgkit

CONFIG_PATH = "config.json"


def main() -> None:
    config = dict()

    with open(CONFIG_PATH) as conf:
        config = dict(json.load(conf))

    template_name = config.get("template") if config.get("template") else "default"
    imgkit_config = imgkit.config(wkhtmltoimage="./bin/wkhtmltoimage.exe")
    imgkit_options = (
        config.get("imgkit_options") if config.get("imgkit_options") else dict()
    )

    if config.get("bearer_token"):
        client = tweepy.Client(config.get("bearer_token"))

        url = input("Enter tweet URL: ").strip()

        tweet_url_index = url.lower().split("/").index("twitter.com")
        tweet_username = url.split("/")[tweet_url_index + 1]
        tweet_id = url.split("/")[tweet_url_index + 3]

        tweet = client.get_tweet(tweet_id).data
        user = client.get_user(username=tweet_username).data

        env = Environment(loader=PackageLoader("main"), autoescape=select_autoescape())
        template = env.get_template(f"{template_name}.html")

        if not os.path.exists("out"):
            os.makedirs("out")

        current_time = datetime.today().strftime("%Y-%m-%d-%H-%M-%S")
        imgkit.from_string(
            template.render(
                name=user.name,
                username=user.username,
                content=str(tweet.text).strip(),
                image=f"https://unavatar.io/twitter/{user.username}",
            ),
            f"out/twittershot-{current_time}.jpg",
            config=imgkit_config,
            options=imgkit_options,
        )
    else:
        print("Operation failed.")


if __name__ == "__main__":
    main()
