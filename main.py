import aiohttp
import asyncio
import sys
import os
import json
import random
def clear():
  os.system("clear")

clear()

os.system("mode 175,30 & title [Vanity Sniper - Ericxxxx]")

token = input([>] Token: "OTk4NTg0ODg0NjE0NDE4NDkz.GaZXXB.UtEklMUx47VM818gM7jFa8szUliWMHdUttJEI0")
bot = input([>] Bot True/False: "True")
guild = int(input([>] Enter Guild ID To Add Sniped Vanity Code: "998525869687570482"))
code = input("[>] Vanity Code To Snipe, discord.gg/: "playzop")
randno = random.randint(10, 99)
api_ = [6,9,8]
api = random.choices(api_)

clear()

if bot in ["True", "true", True]:
  headers = {"Authorization": "Bot {}".format(token)}

elif bot in ["False", "false", False]:
  headers = {"Authorization": token}

async def snipe_vanity():
  nigger = {
    "code": code,
    "reason": f"EricPlayz-Sniper-{randno}"
  }
  async with aiohttp.ClientSession() as ssss:
    async with ssss.patch(f"https://discord.com/api/v9/guilds/{guild}/vanity-url", json=nigger, headers=headers) as bruh:
      if bruh.status in (200, 201, 204):
        print("[>] EriCPlayZ | Vanity Sniped")
        sys.exit()

async def check_vanity():
  async with aiohttp.ClientSession() as idk:
    while True:
      async with idk.get(f"https://discord.com/api/v9/invites/{code}", headers=headers) as gg:
        if gg.status == 404:
          await snipe_vanity()
        else:
          print(f"[>] EricPlayZ | Vanity Is Taken, Still Trying To Snipe discord.gg/{code}.")


loop = asyncio.get_event_loop()
loop.run_until_complete(check_vanity())
loop.close()
