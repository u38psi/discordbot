import discord
import random
import os
import urllib
import urllib.request
import sys
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import json
import time
from google_images_download import google_images_download

Client = discord.Client()
bot = commands.Bot(command_prefix = "?")

@bot.event
async def on_message(message):
    if message.content.upper().startswith("?PICPLS"):
        pic = message.content.split(" ")

        command = "?picpls"
        gif = "gif"
        png = "png"
        jpg = "jpg"

        format = "jpg"

        kwrd = ""

        for i in pic:
            if (i == command.lower()):
                continue

            if (i == gif.lower()):
                format = gif
                continue
            elif (i == png.lower()):
                format = png
                continue
            elif (i == jpg.lower()):
                format = jpg
                continue

            kwrd = kwrd + str(i) + " "

        kwrd = kwrd.rstrip()

        print("%s" % kwrd)

        rpic = random.randint(0, 100)

        if (not rpic):
            print("ERROR: Failed random link init\n")
        else:
            print("Passed random link init with: %s\n" % rpic)

        response = google_images_download.googleimagesdownload()
        pth = response.download({"keywords":"%s" % kwrd, "limit":rpic, "offset":rpic, "no_directory":1, "extract_metadata":1, "no_download":1, "format":"%s" % format})

        if (not response):
            print("ERROR: Failed response\n")
        elif (not pth):
            print("ERROR: Failed download\n")
        else:
            print("Passed link gather\n")

        with open("logs/%s.json" % kwrd) as f:
            imgData = json.load(f)
            for img in imgData:
                imgPath = str(img['image_link'])

        if (not imgPath):
            print("ERROR: Failed opening link\n")
        else:
            print("Passed opening link\n")

        print("Uploading...")

        url = urllib.request.urlretrieve(imgPath, "downloads/%s.%s" % (kwrd, format))

        await bot.send_file(message.channel, "downloads/%s.%s" % (kwrd, format))

        os.remove("downloads/%s.%s" % (kwrd, format))
        os.remove("logs/%s.json" % kwrd)
        urllib.request.urlcleanup()

        print("FINISHED! \n")

        time.sleep(0.2)

bot.run()#insert your botoken
