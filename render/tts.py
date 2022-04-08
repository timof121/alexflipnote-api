from quart import Blueprint, abort, request, send_file 
from gtts import gTTS
from datetime import timedelta
from time import sleep


blueprint = Blueprint('tts', __name__)

@blueprint.route("/tts", methods=['GET'])
async def tts():
    """?text=text"""
    text = request.args.get('text')
    if not text:
        abort(400, "You must provide some text")

    if len(text) > 200:
        abort(400, "You are limited to 200 characters only, sorry")

    resp = gTTS(text = text, lang = 'en', gender = 'male')
    resp.save('tts.wav')
    return (
        await send_file ('tts.wav')
        )

