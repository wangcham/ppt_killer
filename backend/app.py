from quart import send_from_directory, render_template
from quart import Quart, request, Blueprint
from route.getfile import getfile_app
from route.getanswer import getanswer_app
from route.saveanswer import saveanswer_app
import os
import asyncio
import db

app = Quart(__name__, template_folder="../frontend/dist", static_folder="../frontend/dist", static_url_path="")

app.register_blueprint(getfile_app)
app.register_blueprint(getanswer_app)
app.register_blueprint(saveanswer_app)

@app.route('/')
async def index():
    return await render_template("index.html")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        database = db.database()
        database.create()
        loop.run_until_complete(app.run_task(host='0.0.0.0', port=5000))
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()