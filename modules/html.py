from jinja2 import Environment, FileSystemLoader, select_autoescape


def render_tweet_to_html(tweet: dict, config: dict) -> str:
    template_name = config.get("template") if config.get("template") else "default"

    env = Environment(
        loader=FileSystemLoader("templates"),
        autoescape=select_autoescape(),
    )
    template = env.get_template(f"{template_name}.html")

    return template.render(
        name=tweet["user"]["name"],
        username=tweet["user"]["username"],
        content=tweet["content"]["text"],
        image=tweet["user"]["image_url"],
    )
