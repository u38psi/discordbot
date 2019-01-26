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
bot = commands.Bot(command_prefix = "?")

@bot.event
async def on_message(message):
    if message.content == "==exitNow==":
        quit()

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

        userAgents = [
        'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
        'Opera/9.25 (Windows NT 5.1; U; en)',
        'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
        'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
        'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
        'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9'
        ]


        ret = urllib.request.urlretrieve(imgPath, "downloads/%s.%s" % (kwrd, format))

        print(ret)

        await bot.send_file(message.channel, "downloads/%s.%s" % (kwrd, format))

        os.remove("downloads/%s.%s" % (kwrd, format))
        os.remove("logs/%s.json" % kwrd)
        urllib.request.urlcleanup()

        print("FINISHED! \n")

        time.sleep(0.2)

bot.run("NTM3MjQwMzkxNjM2ODc3MzEz.Dy4qjg.zhP2sZsyN9jF_R_ZTqLg9PaI9Lc")#insert your botoken
