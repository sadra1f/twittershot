import webview

from api import API

TITLE = "TwitterShot"
VIEW = "res/main.html"

CONFIG_PATH = "config.json"


def main() -> None:
    api = API(CONFIG_PATH)

    win = webview.create_window(
        title=TITLE,
        url=VIEW,
        js_api=api,
    )

    webview.start()


if __name__ == "__main__":
    main()
