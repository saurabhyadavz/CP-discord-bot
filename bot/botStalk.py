#cherry
from discord import Embed, Color, Member, utils, File
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType, CommandOnCooldown
import discord
import requests
import json
import random
import time
from datetime import datetime
import asyncio
from random import randint


def read_token():
    with open("token.txt","r") as f:
        lines=f.readlines()
        return lines[0].strip()

token=read_token()

client=discord.Client()

@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return

    channels = ["stalk"]
    if str(message.channel) in channels:
        if message.content.startswith("!stalk"):
            handle = ""
            flag=0
            mess = message.content
            for ele in mess:
                if ele ==' ':
                    flag=1
                elif flag == 1:
                    handle =handle+ele

            embed = discord.Embed(
                description="My Eyes may take some time! Btw are you sure you entered the correct handle 🤔",
                color=Color(randint(0, 0xFFFFFF)))
            await message.channel.send(content=None, embed=embed)

            link = "https://codeforces.com/api/user.status?handle="
            link = link + handle
            request_link = requests.get(link)
            json_obj = json.loads(request_link.text)
            sub = json_obj['result']

            data = []
            mult = {}

            for x in sub:
                if x['verdict'] == 'OK' and x['problem']['name'] not in mult:
                    data.append(x)
                    mult[x['problem']['name']] = 1
                if(len(data) == 10):
                    break

            if(len(data) == 0):
                embed = discord.Embed(
                    description=f'[{handle}](https://codeforces.com/profile/{handle}) had not solved any problems yet!',
                    color=Color(randint(0, 0xFFFFFF)))
                await message.channel.send(content=None, embed=embed)

            pname = ""
            prating = ""
            for x in data:
                pname += f"[{x['problem']['name']}](https://codeforces.com/problemset/problem/{x['problem']['contestId']}/{x['problem']['index']})\n"
                y = x['problem']
                if 'rating' not in y:
                    prating += "Not Defined\n"
                else:
                    prating += f"{x['problem']['rating']}\n"

            embed = Embed(color=Color.green())
            embed.add_field(name="Recent problems Solved by", value=f"[{handle}](https://codeforces.com/profile/{handle})", inline=False)
            embed.add_field(name="Problem Name", value=pname, inline=True)
            embed.add_field(name="Rating", value=prating, inline=True)
            await message.channel.send(content=None, embed=embed)

        elif message.content.startswith("!lags"):
            handle1 = ""
            handle2 = ""
            mes = message.content
            flag = 0
            for ele in mes:
                if ele == ' ':
                    flag = flag + 1
                elif flag == 1:
                    handle1 = handle1 + ele
                elif flag == 2:
                    handle2 = handle2 + ele

            link = "https://codeforces.com/api/user.status?handle="
            link1 = link + handle1
            link2 = link + handle2

            embed = discord.Embed(
                description="My Eyes may take some time! Btw are you sure you entered the correct handles 🤔",
                color=Color(randint(0, 0xFFFFFF)))
            await message.channel.send(content=None, embed=embed)

            request_link = requests.get(link1)
            json_obj = json.loads(request_link.text)
            sub1 = json_obj['result']

            request_link = requests.get(link2)
            json_obj = json.loads(request_link.text)
            sub2 = json_obj['result']

            mult1 = {}
            mult2 = {}

            for x in sub2:
                if x['verdict'] == 'OK' and x['problem']['name'] not in mult1:
                    mult1[x['problem']['name']] = 1

            for x in sub1:
                if x['verdict'] == 'OK' and x['problem']['name'] not in mult2:
                    mult2[x['problem']['name']] = 1


            data = []
            mult3 = {}

            print(len(mult1))
            print(len(mult2))

            for x in sub2:
                if x['verdict'] == 'OK' and x['problem']['name'] not in mult2 and x['problem']['name'] not in mult3:
                    data.append(x)
                    mult3[x['problem']['name']]  =  1
                if(len(data) == 10):
                    break

            print(len(data))

            if(len(data) == 0):
                embed = discord.Embed(description=f'[{handle1}](https://codeforces.com/profile/{handle1}) donot lags any problems from [{handle2}](https://codeforces.com/profile/{handle2})',color=Color(randint(0, 0xFFFFFF)))
                await message.channel.send(content=None,embed=embed)

            pname = ""
            prating = ""
            for x in data:
                pname += f"[{x['problem']['name']}](https://codeforces.com/problemset/problem/{x['problem']['contestId']}/{x['problem']['index']})\n"
                y = x['problem']
                if 'rating' not in y:
                    prating += "Not Defined\n"
                else:
                    prating += f"{x['problem']['rating']}\n"

            embed = Embed(color=Color.green())
            embed.add_field(name="Some Problems you lag from ", value=f"[{handle2}](https://codeforces.com/profile/{handle2})", inline=False)
            embed.add_field(name="Problem Name", value=pname, inline=True)
            embed.add_field(name="Rating", value=prating, inline=True)
            await message.channel.send(content=None, embed=embed)

        elif message.content.startswith("!hardest"):
            handle = ""
            flag = 0
            mess = message.content
            for ele in mess:
                if ele == ' ':
                    flag = 1
                elif flag == 1:
                    handle = handle + ele

            embed = discord.Embed(
                description="My Eyes may take some time! Btw are you sure you entered the correct handle 🤔",
                color=Color(randint(0, 0xFFFFFF)))
            await message.channel.send(content=None, embed=embed)

            link = "https://codeforces.com/api/user.status?handle="
            link = link + handle
            request_link = requests.get(link)
            json_obj = json.loads(request_link.text)
            sub = json_obj['result']

            data = []
            mult = {}

            for x in sub:
                if x['verdict'] == 'OK' and x['problem']['name'] not in mult:
                    y = x['problem']
                    if 'rating' not in y:
                        continue
                    data.append([x['problem']['rating'], x])
                    mult[x['problem']['name']] = 1

            if (len(data) == 0):
                embed = discord.Embed(
                    description=f'[{handle}](https://codeforces.com/profile/{handle}) had not solved any rated problems yet!',
                    color=Color(randint(0, 0xFFFFFF)))
                await message.channel.send(content=None, embed=embed)
            else:
                fdata = sorted(data, key = lambda x: x[0], reverse=True)
                pname = ""
                prating = ""
                count=0
                for y, x in fdata:
                    count = count + 1
                    pname += f"[{x['problem']['name']}](https://codeforces.com/problemset/problem/{x['problem']['contestId']}/{x['problem']['index']})\n"
                    prating += f"{x['problem']['rating']}\n"
                    if count == 10:
                        break

                embed = Embed(color=Color.green())
                embed.add_field(name="Hardest Problem Solved by: ",
                                value=f"[{handle}](https://codeforces.com/profile/{handle})", inline=False)
                embed.add_field(name="Problem Name", value=pname, inline=True)
                embed.add_field(name="Rating", value=prating, inline=True)
                await message.channel.send(content=None, embed=embed)

        elif message.content == '.help':
            embed = discord.Embed(title="Help BOT", description="Some useful commands", color=Color.red())
            val = "Displays the recent problems solved by the user"
            embed.add_field(name="!stalk handle", value=val,inline=False)
            embed.add_field(name="!lags handle1 handle2", value="Displays some of the problems which user1 lags with user2", inline=False)
            embed.add_field(name="!hardest handle",value="Displays some of the hardest problem solved by the user",inline=False)
            await message.channel.send(content=None, embed=embed)

client.run(token)
