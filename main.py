import quart

from routes.index import blueprint as index_blueprint

from render.achievement import blueprint as achievement_blueprint
from render.amiajoke import blueprint as amiajoke_blueprint
from render.bad import blueprint as bad_blueprint
from render.calling import blueprint as calling_blueprint
from render.captcha import blueprint as captcha_blueprint
from render.didyoumean import blueprint as didyoumean_blueprint
from render.drake import blueprint as drake_blueprint
from render.facts import blueprint as facts_blueprint
from render.floor import blueprint as floor_blueprint
from render.fml import blueprint as fml_blueprint
from render.jokeoverhead import blueprint as jokeoverhead_blueprint
from render.opinion import blueprint as opinion_blueprint
from render.pornhub import blueprint as pornhub_blueprint
from render.salty import blueprint as salty_blueprint
from render.scroll import blueprint as scroll_blueprint
from render.shame import blueprint as shame_blueprint
from render.ship import blueprint as ship_blueprint
from render.what import blueprint as what_blueprint
from render.zalgo import blueprint as zalgo_blueprint

app = quart.Quart(__name__)

app.register_blueprint(index_blueprint)

app.register_blueprint(achievement_blueprint)
app.register_blueprint(amiajoke_blueprint)
app.register_blueprint(bad_blueprint)
app.register_blueprint(calling_blueprint)
app.register_blueprint(captcha_blueprint)
app.register_blueprint(didyoumean_blueprint)
app.register_blueprint(drake_blueprint)
app.register_blueprint(facts_blueprint)
app.register_blueprint(floor_blueprint)
app.register_blueprint(fml_blueprint)
app.register_blueprint(jokeoverhead_blueprint)
app.register_blueprint(opinion_blueprint)
app.register_blueprint(pornhub_blueprint)
app.register_blueprint(salty_blueprint)
app.register_blueprint(scroll_blueprint)
app.register_blueprint(shame_blueprint)
app.register_blueprint(ship_blueprint)
app.register_blueprint(what_blueprint)
app.register_blueprint(zalgo_blueprint)