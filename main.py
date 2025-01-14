import jsons
from parsers import (
    kwejk,
    jbzd,
    demoty,
    mistrzowie,
    anonimowe,
    ninegag,
    ifunnyco,
    faktopedia,
)
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def to_response(page):
    return jsons.dumps(page)


@app.route("/")
def hello():
    return to_response(
        [
            "/kwejk",
            "/jbzd",
            "/9gag",
            "/9gagnsfw",
            "/demotywatory",
            "/mistrzowie",
            "/anonimowe",
            "/ifunnyco",
            "/faktopedia",
        ]
    )

@app.route("/kwejk")
def kwejk_root():
    return to_response(kwejk.scrap("https://kwejk.pl"))


@app.route("/kwejk/page/<page>")
def kwejk_page(page):
    return to_response(kwejk.scrap("https://kwejk.pl/strona/{}".format(page)))

@app.route("/jbzd")
def jbzd_root():
    return to_response(jbzd.scrap("https://jbzd.com.pl"))

@app.route("/jbzd/page/<page>")
def jbzd_page(page):
    return to_response(jbzd.scrap("https://jbzd.com.pl/str/{}".format(page)))

@app.route("/jbzd/<category>/page/<page>")
def jbzd_category_page(category, page):
    return to_response(jbzd.scrap("https://jbzd.com.pl/{0}/{1}".format(category,page)))

@app.route("/mistrzowie")
def mistrzowie_root():
    return to_response(mistrzowie.scrap("http://mistrzowie.org"))


@app.route("/mistrzowie/page/<page>")
def mistrzowie_page(page):
    return to_response(mistrzowie.scrap("http://mistrzowie.org/page/{}".format(page)))


@app.route("/anonimowe")
def anonimowe_root():
    return to_response(anonimowe.scrap("https://anonimowe.pl"))


@app.route("/anonimowe/page/<page>")
def anonimowe_page(page):
    return to_response(anonimowe.scrap("https://anonimowe.pl/{}".format(page)))


@app.route("/demotywatory")
def demotywatory_root():
    return to_response(demoty.scrap("https://m.demotywatory.pl"))


@app.route("/demotywatory/page/<page>")
def demotywatory_page(page):
    return to_response(demoty.scrap("https://m.demotywatory.pl/page/{}".format(page)))


@app.route("/faktopedia")
def faktopedia_root():
    return to_response(faktopedia.scrap("https://m.faktopedia.pl"))


@app.route("/faktopedia/page/<page>")
def faktopedia_page(page):
    return to_response(faktopedia.scrap("https://m.faktopedia.pl/page/{}".format(page)))


@app.route("/9gag")
def ninegag_root():
    return to_response(
        ninegag.scrap("https://9gag.com/v1/group-posts/group/default/type/hot")
    )


@app.route("/9gag/page/<page>")
def ninegag_page(page):
    return to_response(
        ninegag.scrap(
            "https://9gag.com/v1/group-posts/group/default/type/hot?c=10&after={}".format(
                page
            )
        )
    )


@app.route("/9gagnsfw")
def ninegagnsfw_root():
    return to_response(
        ninegag.scrap("https://9gag.com/v1/group-posts/group/nsfw/type/hot", nsfw=True)
    )


@app.route("/9gagnsfw/page/<page>")
def ninegagnsfw_page(page):
    return to_response(
        ninegag.scrap(
            "https://9gag.com/v1/group-posts/group/nsfw/type/hot?c=10&after={}".format(
                page
            ),
            nsfw=True,
        )
    )


@app.route("/ifunnyco")
def ifunnyco_root():
    return to_response(
        ifunnyco.scrap("https://ifunny.co/api/v1/feeds/featured?page=1", 1)
    )


@app.route("/ifunnyco/page/<page>")
def ifunnyco_page(page):
    return to_response(
        ifunnyco.scrap(
            "https://ifunny.co/api/v1/feeds/featured?page={}".format(page), page
        )
    )


if __name__ == "__main__":
    app.run(debug=True)
