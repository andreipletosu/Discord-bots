import requests
import discord
import os
import json
import time
import datetime
import sys
import pytz
from discord.ext import tasks
from dotenv import load_dotenv
load_dotenv('.env')


def main():
  url = "https://api.opensea.io/api/v1/collection/holoheadz/stats"

  headers = {"Accept": "application/json"}
 
    

  Client = discord.Client(intents=discord.Intents.default())


  @Client.event
  async def on_ready():
      owners = Client.get_channel("""******************""")
      volume = Client.get_channel("""******************""")
      floor = Client.get_channel("""******************""")
      total = Client.get_channel("""******************""")
      ETH_channel = Client.get_channel("""******************""")
      VC_OpenSea.start(owners,volume,floor,total,ETH_channel)

  @tasks.loop(seconds=25)
  async def VC_OpenSea(owners,volume,floor,total,ETH_channel):
        response = requests.request("GET", url, headers=headers)
        total_volume = response.json()["stats"]["total_volume"]
        holders = response.json()["stats"]["num_owners"]
        total_supply = response.json()["stats"]["total_supply"]
        floor_price = response.json()["stats"]["floor_price"]
        await owners.edit(name = "Holders: {}" .format(holders))
        await volume.edit(name = "Traded Volume: Ξ {:.1f}" .format(total_volume))
        await floor.edit(name = "Current F. Price: Ξ {:.3f}" .format(floor_price))
        await total.edit(name = "Minted Items: {}" .format(int(total_supply)))


        
        # i = os.getenv('NEXT_GOAL')
        # if total_volume >= (int(total_volume)+0.95) or int(i) == int(total_volume):  
        #         if int(i)==round(total_volume):
        #             if total_volume < 10:
        #                 await ETH_channel.send('Woah! The traded Ethereum volume of **HOLOHEADZ** just reached **Ξ{}**! @everyone' .format(round(total_volume)))
        #                 z = int(i)
        #                 z += 1
        #                 os.environ.pop('NEXT_GOAL')
        #                 os.environ['NEXT_GOAL'] = str(z)
        #             elif total_volume < 100 and total_volume >= 10:
        #                 await ETH_channel.send('Woah! The traded Ethereum volume of **HOLOHEADZ** just reached **Ξ{}**! @everyone' .format(round(total_volume)))
        #                 z = int(i)
        #                 z += 5
        #                 os.environ.pop('NEXT_GOAL')
        #                 os.environ['NEXT_GOAL'] = str(z)
        #             else:
        #                 await ETH_channel.send('Woah! The traded Ethereum volume of **HOLOHEADZ** just reached **Ξ{}**! @everyone' .format(round(total_volume)))
        #                 z = int(i)
        #                 z += 10
        #                 os.environ.pop('NEXT_GOAL')
        #                 os.environ['NEXT_GOAL'] = str(z)
        print("Discord updated", datetime.datetime.now(pytz.timezone('Europe/Rome')).strftime("%Y-%m-%d %H:%M:%S"))

  Client.run(os.getenv('TOKEN'))


if __name__ == "__main__":
    print("<-----------------Program started----------------->")
    time.sleep(float(30))
    main()
    #while True:
      #r = requests.head("https://discord.com/api/v1")
      #try:
        #print(f"Rate limit {int(r.headers['Retry-After']) / 60} minutes left")
        #time.sleep(float(60))
      #except:
        #print("No rate limit")