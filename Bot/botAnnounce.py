# sarthakeddy file
import discord
import requests
import json
import random
import datetime

from discord import Color

client = discord.Client()

contest_list = {}

@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return
    channels = ["practice"]
    tags = ["implementation", "dp", "math", "greedy", "brute-force", "data-structures", "constructive-algorithms", "dfs-and-similar",
            "sortings", "binary-search", "graphs", "trees", "strings", "number-theory", "geometry", "combinatorics", "two-pointers",
            "dsu", "bitmasks", "probabilities", "shortest-paths", "hashing", "divide-and-conquer", "games", "matrices", "flows",
            "string-suffix-structures", "expression-parsing", "graph-matchings", "ternary-search", "meet-in-the-middle", "fft", "2-sat",
            "chinese-remainder-theorem", "schedules"]

    if str(message.channel) in channels:
        if message.content == '.help':
            embed = discord.Embed(title="Help BOT", description="Some useful commands", color=Color.red())
            val = "\nDifficulty min and max is the level of difficulty\n quantity is the number of questions required (must be an integer between 1 and 10)\ntags_for_questions are tags for which user want questions (must be separated by space)."
            embed.add_field(name="!tags [difficulty_min] [difficulty_max] [quantity] [tags_for_questions]", value=val, inline=False)
            embed.add_field(name="!tags enlist", value="Enlist all tags of Codeforces", inline=False)
            await message.channel.send(content=None, embed=embed)
        elif message.content == "!tags enlist":
            answer = "```\nList of tags:\n"
            temp = ""
            for tg in tags:
                temp += tg + "; "
                if len(temp) >= 50:
                    answer += temp
                    answer += '\n'
                    temp = ""
            answer += "```"
            embed = discord.Embed(title="List of tags:", description=answer, color=Color.blue())
            await message.channel.send(answer)
        elif message.content.startswith("!tags"):
            prbl_tags = []
            mess = message.content
            start = 0
            i = 0
            for x in range(0, len(mess)):
                if " " == mess[i:i + 1][0]:
                    prbl_tags.append(mess[start:i + 1])
                    # print string[start:i+1]
                    start = i + 1
                i += 1
            prbl_tags.append(mess[start:i + 1])
            prbl_tags.pop(0)
            try :
                difficulty_min = int(prbl_tags[0])
            except Exception as e:
                print(e)
                await message.channel.send("Difficulty must be integer")
                return
            prbl_tags.pop(0)
            print(difficulty_min)
            try:
                difficulty_max = int(prbl_tags[0])
            except Exception as e:
                print(e)
                await message.channel.send("Difficulty must be integer")
                return
            prbl_tags.pop(0)
            print(difficulty_max)
            if difficulty_max < difficulty_min:
                await message.channel.send("How can min be greater than max")
                return
            try :
                quantity = int(prbl_tags[0])
            except Exception as e:
                print(e)
                await message.channel.send("# of questions must be integer")
                return
            if quantity > 10:
                await message.channel.send("# of questions must be less than 10")
                return
            prbl_tags.pop(0)
            link = "https://codeforces.com/api/problemset.problems?tags="
            for tag in prbl_tags:
                temp = tag
                if temp[len(temp)-1] == ' ':
                    temp = temp[:len(temp)-1]
                if temp == "meet-in-the-middle" or temp == "2-sat":
                    k = 1
                else:
                    temp = temp.replace('-', ' ')
                if temp not in tags:
                    print(temp)
                    await message.channel.send("Invalid tag")
                    return
                link += temp+";"
            request_link = requests.get(link)
            json_obj = json.loads(request_link.text)
            obj_result = json_obj['result']
            problems = obj_result['problems']
            problems_stat = obj_result['problemStatistics']
            i = 0
            flag = -1
            # print(problems[i]["rating"])
            rnd_prblms = []
            for prb in problems:
                # print(problems[i]["name"])
                if "rating" in problems[i]:
                    if difficulty_min <= problems[i]["rating"] <= difficulty_max:
                        flag = i
                        rnd_prblms.append(i)
                i += 1

            answer = ""
            if flag == -1:
                answer += "Sorry No problem exist for given tags.\nTry specifying tags individually."
                await message.channel.send(answer)
                return
            else:
                embed = discord.Embed(title="Problem Search Successful", description="Try solving all of them.", color=Color.green())
                index_list = []
                cnt = 0
                for i in range(quantity):
                    while True:
                        ind = random.choice(rnd_prblms)
                        cnt += 1
                        if cnt == 100:
                            break
                        if ind not in index_list:
                            index_list.append(ind)
                            break
                    if cnt == 100:
                        break
                k = 0
                for i in index_list:
                    problem_link = "https://codeforces.com/problemset/problem/"
                    problem_link += str(problems[i]['contestId']) + "/"
                    problem_link += problems[i]['index']
                    embed.add_field(name=str(k+1)+") "+problems[i]["name"], value=f"[Link to problem]({problem_link})\nDifficulty is "+str(problems[i]['rating'])+" and "+str(problems_stat[i]['solvedCount'])+" solved this question.", inline=False)
                    k += 1
                await message.channel.send(content=None, embed=embed)

asd = "abcd erf"
print(asd.replace(' ', ''))
# carl bot
client.run("bot's token")
