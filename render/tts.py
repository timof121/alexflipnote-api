from quart import Blueprint, abort, request, send_file 
from gtts import gTTS
from datetime import timedelta
from quart_rate_limiter import rate_limit


blueprint = Blueprint('tts', __name__)

@blueprint.route("/tts", methods=['GET'])
@rate_limit(1, timedelta(seconds=1))
async def tts():
    """?text=text"""
    text = request.args.get('text')
    if not text:
        abort(400, "You must provide some text")

    if len(text) > 200:
        abort(400, "You are limited to 200 characters only, sorry")

    resp = gTTS(text = text, lang = 'en')
    resp.save('tts.wav')
    return await send_file ('tts.wav')
