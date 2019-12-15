from app import app


@app.route('/index')
def index():
    return app.send_static_file('index.html')
