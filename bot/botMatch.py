#cherry

from discord import Embed, Color, Member, utils, File
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType, CommandOnCooldown
import discord
import requests
import json
import random
import time
import string
from datetime import datetime
import asyncio
from random import randint


def read_token():
    with open("token1.txt","r") as f:
        lines=f.readlines()
        return lines[0].strip()

token=read_token()

client=discord.Client()

@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return

    channels = ["match"]

    if str(message.channel) in channels:
        if message.content.startswith("!challenge"):
            handle1 = ""
            handle2 = ""
            tim = ""
            flag = 0
            mess = message.content
            for ele in mess:
                if ele == ' ':
                    flag = flag + 1
                elif flag == 1:
                    handle1 = handle1 + ele
                elif flag == 2:
                    handle2 = handle2 + ele
                elif flag == 3:
                    tim = tim + ele

            if(handle1 == handle2):
                embed = discord.Embed(
                    description="You cannot challenge yourself!",color=Color(randint(0, 0xFFFFFF)))
                await message.channel.send(content=None, embed=embed)
            elif tim != '60' and tim != '120':
                embed = discord.Embed(
                    description="Hey! Please Enter Valid Time", color=Color(randint(0, 0xFFFFFF)))
                await message.channel.send(content=None, embed=embed)
            else:
                res = ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))
                embed = discord.Embed(
                    description=f'Both of the players, Please change your first name on this [link](https://codeforces.com/settings/social) to `{res}` within 60 seconds',
                    color=Color(randint(0, 0xFFFFFF)))
                await message.channel.send(content=None, embed=embed)

                await asyncio.sleep(60)
                print("Back")
                link1 = f"https://codeforces.com/api/user.info?handles={handle1}"
                request_link = requests.get(link1)
                did1 = json.loads(request_link.text)

                link2 = f"https://codeforces.com/api/user.status?handle={handle2}&from=1&count=1"
                request_link = requests.get(link2)
                did2 = json.loads(request_link.text)

                flag1 = 0
                flag2 = 0

                nam1 = did1["result"][0]
                nam2 = did2["result"][0]

                if nam1['firstName'] == res:
                    flag1 = 1

                if nam1['firstName'] == res:
                    flag2 = 1

                if flag1 == 1 and flag2 == 1:
                    embed = discord.Embed(
                        description="Please Wait! Starting your Match within few seconds",
                        color=Color(randint(0, 0xFFFFFF)))
                    await message.channel.send(content=None, embed=embed)

                    tags = ['implementation', 'dp', 'math', 'greedy', 'brute force', 'data structures', 'constructive algorithms', 'dfs and similar', 'sortings', 'binary-search', 'graphs', 'trees', 'strings', 'number-theory',
                        'geometry', 'combinatorics', 'two-pointers', 'dsu', 'bitmasks', 'probabilities', 'shortest-paths', 'hashing', 'divide-and-conquer', 'games', 'matrices', 'flows', 'string-suffix-structures', 'expression-parsing', 'graph-matchings']

                    pick = tags[0]
                    print(pick)

                    link = "https://codeforces.com/api/problemset.problems?tags="
                    link = link + pick

                    request_link = requests.get(link)
                    json_obj = json.loads(request_link.text)
                    obj_result = json_obj['result']
                    data = obj_result['problems']

                    give = []
                    mult = {}

                    fdata = []

                    for x in data:
                        if 'rating' not in x:
                            continue
                        if x['rating'] <= 2000:
                            fdata.append(x)

                    while True:
                        x = random.choice(fdata)
                        if x['name'] not in mult:
                            mult[x['name']] = 1
                            give.append(x)
                        if(tim == '60' and len(give) == 3):
                            break
                        if(len(give) == 5):
                            break

                    pname = ""
                    i = 0

                    for x in give:
                        pname += f"[{x['name']}](https://codeforces.com/problemset/problem/{x['contestId']}/{x['index']})\n"
                        i = i + 1

                    embed = Embed(color=Color.green())
                    embed.add_field(name="Best of Luck! Your Match Starts Now!",
                                value=f"[{handle1}](https://codeforces.com/profile/{handle1}) vs [{handle2}](https://codeforces.com/profile/{handle2})", inline=False)
                    if(tim == '60'):
                        val = "A\nB\nC"
                    else:
                        val = "A\nB\nC\nD\nE"
                    embed.add_field(name="Index", value=val, inline=True)
                    embed.add_field(name="Problem Name", value=pname, inline=True)
                    await message.channel.send(content=None, embed=embed)

                    if(tim == '60'):
                        clk = 60*60
                    else:
                        clk = 120*60

                    await asyncio.sleep(clk)

                    sc1 = 0
                    sc2 = 0
                    print("Game Over!")
                    link1 = f"https://codeforces.com/api/user.status?handle={handle1}&from=1&count=30"
                    request_link = requests.get(link1)
                    json_obj = json.loads(request_link.text)
                    sub1 = json_obj['result']

                    link2 = f"https://codeforces.com/api/user.status?handle={handle2}&from=1&count=30"
                    request_link = requests.get(link2)
                    json_obj = json.loads(request_link.text)
                    sub2 = json_obj['result']

                    msub1 = {}

                    for x in sub1:
                        for y in give:
                            if x['problem']['name'] == y['name'] and x['verdict'] == 'OK' and y['name'] not in msub1:
                                sc1 = sc1 + 100
                                msub1[y['name']] = 1

                    msub2 = {}

                    for x in sub2:
                        for y in give:
                            if x['problem']['name'] == y['name'] and x['verdict'] == 'OK' and y['name'] not in msub2:
                                sc2 = sc2 + 100
                                msub2[y['name']] = 1


                    embed = Embed(color=Color.green())
                    embed.add_field(name=f"Match Over!",
                                        value=f"[{handle1}](https://codeforces.com/profile/{handle1}) vs [{handle2}](https://codeforces.com/profile/{handle2})\n{sc1}    -    {sc2}",
                                        inline=False)
                    await message.channel.send(content=None, embed=embed)

                else:
                    embed = discord.Embed(
                        description=f"[{handle1}](https://codeforces.com/profile/{handle1}) and [{handle2}](https://codeforces.com/profile/{handle2}) Match cannot be Started! Try Again!",
                        color=Color(randint(0, 0xFFFFFF)))
                    await message.channel.send(content=None, embed=embed)

        elif message.content == '.help':
            embed = discord.Embed(title="Help BOT", description="Some useful commands", color=Color.red())
            embed.add_field(name="!challenge handle1 handle2 time(60 or 120)", value="Sets a match between two given players", inline=False)
            await message.channel.send(content=None, embed=embed)

client.run(token)