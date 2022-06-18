import logging
from aiohttp import web
from bot import send_message
from parse import validate_json, parse_webhook

routes = web.RouteTableDef()


@routes.post('/')
async def webhook_catch(request: web.Request) -> web.Response:
    data = await request.text()
    logging.info("Webhook recived: " + data)
    if validate_json(data):
        await send_message(text=parse_webhook(data))
    return web.HTTPCreated()
