from datetime import datetime
import imgkit


def html_to_image(html: str, config: dict, name_prefix: str = "") -> None:
    if name_prefix and name_prefix != "":
        name_prefix += "-"
    current_time = datetime.today().strftime("%Y-%m-%d-%H-%M-%S")
    file_extention = (
        config["imgkit_options"]["format"]
        if config.get("imgkit_options") and config["imgkit_options"].get("format")
        else "jpg"
    )

    imgkit_config_kwargs = (
        {"wkhtmltoimage": config.get("wkhtmltoimage_path")}
        if config.get("wkhtmltoimage_path")
        else dict()
    )

    imgkit_config = imgkit.config(**imgkit_config_kwargs)
    imgkit_options = (
        config.get("imgkit_options") if config.get("imgkit_options") else dict()
    )

    imgkit.from_string(
        html,
        f"out/{name_prefix}twittershot-{current_time}.{file_extention}",
        config=imgkit_config,
        options=imgkit_options,
    )
