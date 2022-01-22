from bs4 import BeautifulSoup
from quart import Blueprint, jsonify, abort, request
from utils import http
from zalgo_text import zalgo

blueprint = Blueprint('zalgo', __name__)


@blueprint.route("/zalgo", methods=['GET'])
async def fml():
    """?text=text"""
    text = request.args.get('text')
    if not text:
        abort(400, "You must provide some text")

    if len(text) > 500:
        abort(400, "You are limited to 500 characters only, sorry")
    resp = zalgo.zalgo().zalgofy(text)

    return jsonify({
        "text": resp
    })
