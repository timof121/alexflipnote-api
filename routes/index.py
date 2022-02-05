import quart

blueprint = quart.Blueprint('index', __name__)

@blueprint.route('/')
async def index():
    return quart.jsonify({
        "routes": [
            "/achievement?text=text[&icon=int]",
            "/challenge?text=text[&icon=int]",
            "/amiajoke?image=url",
            "/bad?image=url",
            "/calling?text=text",
            "/captcha?text=text",
            "/didyoumean?top=text&bottom=text",
            "/drake?top=text&bottom=text",
            "/facts?text=text",
            "/floor?image=url&text=text",
            "/fml",
            "/jokeoverhead?image=url",
            "/trash?face=url&trash=url",
            "/pornhub?text=text&text2=text",
            "/salty?image=url",
            "/scroll?text=text",
            "/shame?image=url",
            "/ship?user=url&user2=url",
            "/tts?text=text"
            "/what?image=url",
            "/zalgo?text=text"
        ],
        "credits": [
            "AlexFlipnote"
        ]
    }, 200)