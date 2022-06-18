from aiohttp import web
from settings import LISTEN_HOST, LISTEN_PORT
from routes import routes


def main():
    app = web.Application()
    app.add_routes(routes)
    web.run_app(app, host=LISTEN_HOST,
                port=LISTEN_PORT,
                access_log=None,
                shutdown_timeout=10)


if __name__ == '__main__':
    main()
