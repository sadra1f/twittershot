import tweepy


def get_tweet(url: str, config: dict) -> dict:
    client = tweepy.Client(config.get("bearer_token"))

    tweet_url_index = url.lower().split("/").index("twitter.com")
    tweet_username = url.split("/")[tweet_url_index + 1]
    tweet_id = url.split("/")[tweet_url_index + 3]

    tweet = client.get_tweet(tweet_id).data
    user = client.get_user(username=tweet_username).data

    return {
        "user": {
            "username": user.username,
            "name": user.name,
            "image_url": f"https://unavatar.io/twitter/{user.username}",
        },
        "content": {
            "text": str(tweet.text).strip(),
        },
    }
