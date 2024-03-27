from aiohttp import web
from http_server import handle_prompt


def main():
    app = web.Application()
    app.add_routes([web.post('/prompt', handle_prompt)])

    web.run_app(app, port=8888)


if __name__ == '__main__':
    main()
