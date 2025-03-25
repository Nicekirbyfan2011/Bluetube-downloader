import click
import requests
from bs4 import BeautifulSoup


@click.command()
@click.argument("id")
@click.option("--instance", default="newbluetube.yooco.org")
def dl(id, instance):
    r = requests.get("https://" + instance + "static.yooco.de/n2/99/799231/u/3b/3878539/videos/" + id)
    soup = BeautifulSoup(r.text, "html.parser")
    src = soup.find("video").find("source")
if src:
        url = src["src"].replace("../", "https://" + instance + "/")
        r2 = requests.get(url, stream=True)
        with open(id + ".mp4", "wb") as f:
            for chunk in r2.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
app.add_command(dl)
if __name__ == '__main__':
    app()
