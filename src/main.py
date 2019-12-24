from waitress import serve
from app import app

server = app.server
serve(server, port=8050, threads=10)
