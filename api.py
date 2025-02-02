import json
import aiohttp


async def check_token(token):
    async with aiohttp.ClientSession() as session:
        url = "https://api.imeicheck.net/v1/account"

        headers = {
            "Authorization": f"Bearer {token}",
            "Accept-Language": "ru",
        }

        async with session.get(url=url, headers=headers) as response:
            return bool((await response.json())["balance"])


async def check_imei(imei, token):
    async with aiohttp.ClientSession() as session:
        url = "https://api.imeicheck.net/v1/checks"

        headers = {
            "Authorization": f"Bearer {token}",
        }

        data = json.dumps({"deviceId": f"{imei}"})
        async with session.get(url=url, headers=headers, data=data) as response:
            return json.dumps((await response.json())[0], indent=4)


async def get_balance(token):
    async with aiohttp.ClientSession() as session:
        url = "https://api.imeicheck.net/v1/account"

        headers = {
            "Authorization": f"Bearer {token}",
        }

        async with session.get(url=url, headers=headers) as response:
            return (await response.json())["balance"]


async def get_services(token):
    async with aiohttp.ClientSession() as session:
        url = "https://api.imeicheck.net/v1/services"

        headers = {
            "Authorization": f"Bearer {token}",
        }

        async with session.get(url=url, headers=headers) as response:
            return json.dumps((await response.json()), indent=4)
