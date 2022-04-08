from bs4 import BeautifulSoup
from quart import Blueprint, jsonify, abort, request
from utils import http
import art

blueprint = Blueprint('ascii', __name__)


@blueprint.route("/ascii", methods=['GET'])
async def asciiart():
    """?text=text"""
    text = request.args.get('text')
    if not text:
        abort(400, "You must provide some text")

    if len(text) > 500:
        abort(400, "You are limited to 500 characters only, sorry")

    resp = art.text2art(text)
    return (
        resp
    )
