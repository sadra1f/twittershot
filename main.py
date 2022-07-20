import json
import tweepy

CONFIG_PATH = "config.json"


def main() -> None:
    config = dict()

    with open(CONFIG_PATH) as conf:
        config = dict(json.load(conf))

    if config.get("bearer_token"):
        client = tweepy.Client(config.get("bearer_token"))

        url = input("Enter tweet URL: ").strip()

        tweet_url_index = url.lower().split("/").index("twitter.com")
        tweet_username = url.split("/")[tweet_url_index + 1]
        tweet_id = url.split("/")[tweet_url_index + 3]

        tweet = client.get_tweet(tweet_id).data
        user = client.get_user(username=tweet_username).data

        print(f"Tweet data: {dict(tweet)} \n")
        print(f"User data: {dict(user)} \n")
        print(f"Profile image: https://unavatar.io/twitter/{user.username}")
    else:
        print("Operation failed.")


if __name__ == "__main__":
    main()
