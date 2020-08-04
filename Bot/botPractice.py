import discord
import requests
import json
import random
import datetime
import asyncio

client = discord.Client()

contest_list = {}

async def reminder_contest():
    await client.wait_until_ready()
    while not client.is_closed():
        try:
            link = "https://codeforces.com/api/contest.list?gym=false"
            request_link = requests.get(link)
            json_obj = json.loads(request_link.text)
            contests = json_obj['result']
            answer = ""
            i = 0
            for temp in contests:
                if contests[i]['phase'] == 'BEFORE':
                    time_left = contests[i]['relativeTimeSeconds']
                    time_neg = time_left
                    time_left = abs(time_left)
                    if time_left <= 18000 and time_neg < 0:
                        contest_link = "https://codeforces.com/contest/"
                        seconds = time_left
                        mint, sec = divmod(seconds, 60)
                        hour, mint = divmod(mint, 60)
                        answer = discord.Embed(title=contests[i]['name'], url=contest_link+str(contests[i]['id']), description="Contest begins in "+str(hour)+" hrs and "+str(mint)+" minutes.\nGet ready to compete.")
                        channel = client.get_channel(channel_id)
                        await channel.send(content=None, embed=answer)
                    i += 1
                else:
                    break
            # channel = client.get_channel(channel_id)
            # await channel.send(answer)
            await asyncio.sleep(19000)
        except Exception as e:
            print(e)
            await asyncio.sleep(19000)

async def update_contest_list():
    await client.wait_until_ready()
    # global contest_list
    while not client.is_closed():
        try:
            link = "https://codeforces.com/api/contest.list?gym=false"
            request_link = requests.get(link)
            json_obj = json.loads(request_link.text)
            contests = json_obj['result']
            i = 0
            flag = 0
            answer = discord.Embed(title="Upcoming Contest", description="These are the upcoming contests on Codeforces.")
            for temp in contests:
                if contests[i]['phase'] == 'BEFORE':
                    contest_id = contests[i]['id']
                    contest_id = str(contest_id)
                    if contest_id not in contest_list:
                        flag += 1
                        contest_list[contest_id] = contests[i]['name']
                        seconds = contests[i]['durationSeconds']
                        contest_link = "https://codeforces.com/contest/"
                        mint, sec = divmod(seconds, 60)
                        hour, mint = divmod(mint, 60)
                        contest_link += str(contest_id)
                        val = f"[Link to contest]({contest_link})\nBegins at "+str(datetime.datetime.fromtimestamp(contests[i]['startTimeSeconds']).strftime('%Y-%m-%d %H:%M:%S')) + "\nDuration is "+str(hour) + " hrs. and " + str(mint) + " minutes\n"
                        answer.add_field(name=str(i+1)+") "+contests[i]['name'], value=val, inline=False)
                    i += 1
                else:
                    break
            channel = client.get_channel(channel_id)
            if flag != 0:
                await channel.send(content=None, embed=answer)
            await asyncio.sleep(93600)
        except Exception as e:
            # print(e)
            await asyncio.sleep(93600)

client.loop.create_task(update_contest_list())
client.loop.create_task(reminder_contest())
# carl bot
client.run("bot's token")