import discord
import random
import os
import urllib
import urllib.request
from urllib.request import FancyURLopener
import sys
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import json
import time
from google_images_download import google_images_download

Client = discord.Client()
bot = commands.Bot(command_prefix = "%")

@bot.event
async def on_message(message):
    if message.content == "exitB":
        quit()

    if message.content.upper().startswith("%B"):
        pic = message.content.split(" ")

        command = "%b"
        gif = "gif"
        png = "png"
        jpg = "jpg"

        format = "jpg"

        kwrd = []
        imgPath = []
        first = True

        kcount = 0

        for i in pic:

            if (i.lower() == command.lower()):
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

            if (first):
                kwrd.insert(kcount, str(i))
                first = False
            elif (i == "|"):
                kcount += 1
                first = True
            else:
                kwrd.insert(kcount, kwrd[kcount] + " " + str(i))

        for i in range(0, kcount+1):
            print(kwrd[i])

        rpic = random.randint(0, 100)

        if (not rpic):
            print("ERROR: Failed random link init\n")
        else:
            print("Passed random link init with: %s\n" % rpic)

        response = google_images_download.googleimagesdownload()
        for i in range(0, kcount+1):
            pth = response.download({"keywords":"%s" % kwrd[i], "limit":rpic, "offset":rpic, "no_directory":1, "extract_metadata":1, "no_download":1, "format":"%s" % format})

        if (not response):
            print("ERROR: Failed response\n")
        elif (not pth):
            print("ERROR: Failed download\n")
        else:
            print("Passed link gather\n")

        for i in range(0, kcount+1):
            with open("logs/%s.json" % kwrd[i]) as f:
                imgData = ""
                imgData = json.load(f)
                for img in imgData:
                    imgPath.insert(i, str(img['image_link']))

        if (not imgPath):
            print("ERROR: Failed opening link\n")
        else:
            print("Passed opening link\n")

        print("Uploading...")

        opener = urllib.request.URLopener()
        opener.addheader("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")

        for i in range(0, kcount+1):
            ret = opener.retrieve(imgPath[i], "downloads/%s.%s" % (kwrd[i], format))
            print(ret)
            await bot.send_file(message.channel, "downloads/%s.%s" % (kwrd[i], format))
            os.remove("downloads/%s.%s" % (kwrd[i], format))
            os.remove("logs/%s.json" % kwrd[i])

        urllib.request.urlcleanup()

        print("FINISHED! \n")

        time.sleep(0.2)

bot.run()#insert your botoken
