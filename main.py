import os

import requests
from flask import Flask, send_file, Response, render_template, url_for
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


def pig_latin():

    url = "https://hidden-journey-62459.herokuapp.com/piglatinize/"
    params = {"input_text": f"{get_fact()}"}

    response = requests.post(url=url,
                             data=params,
                             allow_redirects=True
                             )

    response_url = response.request.url

    return response_url


@app.route('/')
def home():

    the_link = str(pig_latin())

    return render_template('base.jinja2', url=the_link)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

