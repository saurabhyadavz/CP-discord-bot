import discord
from discord.ext import commands


# https://discordapp.com/oauth2/authorize?client_id=738424005345804370&scope=bot&permissions=0
# id = 738424005345804370
def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()
client = commands.Bot(command_prefix='.')
client.remove_command('help')


@client.event
async def on_ready():
    print(f"{client.user} has connected to discord")


@client.command(pass_context=True)
async def help(ctx):
    channel = discord.utils.get(ctx.guild.channels, name="prepare")
    embed =discord.Embed(title="Commands", description="These are commands to be used here")
    embed.add_field(name="type -> **.prepare [topic]**",value="[topic]->\n **cp-faq**\n **cpsites**\n **stack**\n **queue**\n **segment-tree**", inline=False)
    if ctx.channel == channel:

        await channel.send(embed=embed)


@client.event
async def on_member_join(member):
    mention=member.mention
    guild=member.guild
    await member.create_dm()
    await member.dm_channel.send(str(f"{mention}, Welcome to my server {guild}").format(mention=member,guild=guild))

    embed=discord.Embed(title=str("**New Member joined**"), colour=0x33c946, description=str(f"{mention} joined the {guild} :tulip: :cherries: :shaved_ice:").format(mention=member,guild=guild))
    embed.set_thumbnail(url=f"{member.avatar_url}")
    embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
    embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
    embed.timestamp=datetime.datetime.utcnow()
    embed.add_field(name="User ID:", value=member.id)
    embed.add_field(name="User Name :", value=member.display_name)
    embed.add_field(name="Server Name :", value=guild)
    embed.add_field(name="User Serial :", value=str(len(list(guild.members))))
    # Now get the channel where the message it to be posted by bot
    channel=discord.utils.get(member.guild.channels, id=int("738703325234462760"))
    await channel.send(embed=embed)


@client.event
async def on_message(message):
    await client.process_commands(message)
    id = client.get_guild(738424219821670470)
    message.content = message.content.lower()
    if message.author == client.user:
        return
    channels = ["prepare"]
    if str(message.channel) in channels and message.content.startswith(".help"):
        embed = discord.Embed(title=str("#Stack"), colour=0x00F000)

    if str(message.channel) in channels and message.content.startswith(".prepare"):
        print(message.content)
        content = message.content
        count = 0
        topic = ""
        for i in content:
            if i == " ":
                count = count + 1
                if count == 2:
                    break
                topic = ""
            else:
                topic = topic + i

        if topic == "stack":
            link1 = "https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/tutorial/"
            link2 = "https://www.youtube.com/watch?v=vZEuSFXSMDI&list=PLqM7alHXFySF7Lap-wi5qlaD8OEBx9RMV"
            link3 = "https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/"
            embed = discord.Embed(title=str("#Stack"), colour=0x00FF00)
            embed.add_field(name="Basics of stack:", value=f"Refer to [this]({link1}) blog by hackerearth",
                            inline=False)
            embed.add_field(name="Video Editorial:", value=f"Refer to [this]({link2}) video editorial by GeeksforGeeks",
                            inline=False)
            embed.add_field(name="Practice Problems:",
                            value=f"Solve these [basics problems]({link3}) before moving to <#738998620606431242> section",
                            inline=False)

            embed.set_thumbnail(url=f"https://cdn-media-1.freecodecamp.org/images/K4D9kYqy74hwfMaEvoj6TMVAioUxmyUY5vfG")
            embed.set_image(url="https://miro.medium.com/max/873/0*SESFJYWU5a-3XM9m.gif")

            await message.channel.send(content=None, embed=embed)

        if topic == "queue":
            link1 = "https://www.hackerearth.com/practice/data-structures/queues/basics-of-queues/tutorial/"
            link2 = "https://www.youtube.com/watch?v=q5oOYxfOD1c&list=PLqM7alHXFySG6wgjVeEat_ouTIi0IBQ6D"
            link3 = "https://www.hackerearth.com/practice/data-structures/queues/basics-of-queues/practice-problems/"
            embed = discord.Embed(title=str("#Queue"), colour=0x00FF00)
            embed.add_field(name="Basics of Queue:", value=f"Refer to [this]({link1}) blog by hackerearth",
                            inline=False)
            embed.add_field(name="Video Editorial:", value=f"Refer to [this]({link2}) video editorial by GeeksforGeeks",
                            inline=False)
            embed.add_field(name="Practice Problems:",
                            value=f"Solve these [basics problems]({link3}) before moving to <#738998620606431242> section",
                            inline=False)

            embed.set_thumbnail(url=f"https://cdn-media-1.freecodecamp.org/images/aQcmAeS9hN4ormkWg3L00rJZEfk3mmJdx6Pk")
            embed.set_image(url="https://miro.medium.com/max/873/1*UKVABqYxsiR6YvV2385nFQ.gif")

            await message.channel.send(content=None, embed=embed)

        if topic == "stl":
            vector = "https://www.geeksforgeeks.org/vector-in-cpp-stl/"
            pair = "https://www.geeksforgeeks.org/pair-in-cpp-stl/"
            set = "https://www.hackerearth.com/practice/data-structures/queues/basics-of-queues/practice-problems/"
            multiset = "https://www.geeksforgeeks.org/multimap-associative-containers-the-c-standard-template-library-stl/"
            orderedset = "https://codeforces.com/blog/entry/11080"
            stack = "https://www.geeksforgeeks.org/stack-in-cpp-stl/"
            queue = "https://www.geeksforgeeks.org/queue-cpp-stl/"
            dequeue = "https://www.geeksforgeeks.org/deque-cpp-stl/"
            PriorityQueue = "https://www.geeksforgeeks.org/priority-queue-in-cpp-stl/"
            map = "https://www.geeksforgeeks.org/map-associative-containers-the-c-standard-template-library-stl/"
            unorderedMap = "https://codeforces.com/blog/entry/21853"
            videoEditorial = "https://www.youtube.com/watch?v=zBhVZzi5RdU"
            embed = discord.Embed(title=str("#STL IN C++"), colour=0x00FF00)
            embed.add_field(name="Pair:", value=f"Refer to [this]({pair}) blog by GeeksforGeeks",
                            inline=True)
            embed.add_field(name="Vector:", value=f"Refer to [this]({vector}) blog by GeeksforGeeks",
                            inline=True)
            embed.add_field(name="Set:", value=f"Refer to [this]({set}) blog by GeeksforGeeks",
                            inline=True)
            embed.add_field(name="Multiset:", value=f"Refer to [this]({multiset}) blog by GeeksforGeeks",
                            inline=True)
            embed.add_field(name="Ordered Set(PBDS):",
                            value=f"Refer to [this]({orderedset}) blog by [Codeforces](https://codeforces.com/)",
                            inline=True)
            embed.add_field(name="Map:", value=f"Refer to [this]({map}) blog by GeeksforGeeks",
                            inline=True)
            embed.add_field(name="Unordered Map:", value=f"Refer to [this]({unorderedMap}) blog by Codeforces",
                            inline=True)
            embed.add_field(name="Stack:", value=f"Refer to [this]({stack}) blog by GeeksForGeeks",
                            inline=True)
            embed.add_field(name="Queue:", value=f"Refer to [this]({queue}) blog by GeeksForGeeks",
                            inline=True)
            embed.add_field(name="Dequeue:", value=f"Refer to [this]({dequeue}) blog by GeeksForGeeks",
                            inline=True)
            embed.add_field(name="Priority Queue:", value=f"Refer to [this]({PriorityQueue}) blog by GeeksForGeeks",
                            inline=True)
            embed.add_field(name="Video Editorial on STL C++:",
                            value=f"Refer to [this]({videoEditorial}) video editorial by [Striver](https://codeforces.com/profile/striver_79)",
                            inline=True)

            embed.set_thumbnail(url=f"https://www.bobyhermez.com/wp-content/uploads/2019/09/VW3m9xM-980x520.jpg")

            await message.channel.send(content=None, embed=embed)
        if topic == "cpsites":
            codechef="https://www.codechef.com/"
            codeforces="https://codeforces.com/"
            atcoder="https://atcoder.jp/"
            spoj="https://www.spoj.com/"
            hackerearth="https://www.hackerearth.com/challenges/"
            topcoder="https://www.topcoder.com/community/competitive-programming/"
            embed = discord.Embed(title=str("**#Programming Sites**"), colour=0x00FF00)
            embed.add_field(name="**Codechef** a non-profit educational initiative of Unacademy", value=f"[Codechef]({codechef})",
                            inline=False)
            embed.add_field(name='**CodeForces** maintained by a group of competitive programmers from ITMO University led by Mikhail Mirzayanov',
                            value=f"[Codefoces]({codeforces})",
                            inline=False)
            embed.add_field(name="**AtCoder** is a programming contest site for anyone from beginners to experts ",
                            value=f"[Atcoder]({atcoder})",
                            inline=False)
            embed.add_field(name="**Hackerearth** hosts competitive programming contests and hiring challenges",
                            value=f"[Hackerearth]({hackerearth})",
                            inline=False)
            embed.add_field(name="**SPOJ** an online judge having over 20,000 problems.",
                            value=f"[Spoj]({spoj})",
                            inline=False)
            embed.add_field(name="**Topcoder** hosts Single Round Matches (SRMs)",
                            value=f"[TopCoder]({topcoder})",
                            inline=False)
            embed.set_thumbnail(url=f"https://miro.medium.com/max/546/1*dtpWxk4u-KwPQ3K-Zjx2zQ.gif")
            embed.set_image(url="https://miro.medium.com/max/928/1*IRGHmiGsa16stedQvIaZfw.gif")
            await message.channel.send(content=None, embed=embed)
        if topic == "cp-faq":
            guide="https://www.codechef.com/guide-to-competitive-programming"
            modulo="https://www.hackerearth.com/practice/notes/abhinav92003/why-output-the-answer-modulo-109-7/"
            powermod="https://www.geeksforgeeks.org/modular-exponentiation-power-in-modular-arithmetic/"
            timecomplexity="https://www.hackerearth.com/practice/basic-programming/complexity-analysis/time-and-space-complexity/tutorial/"
            icpc="https://www.quora.com/What-is-the-ACM-ICPC"
            howto="https://codeforces.com/blog/entry/23054"
            embed = discord.Embed(title=str("**#Programming FAQ**"), colour=0x00FF00)
            embed.add_field(name="Q.1- Guide-to-competitive-programming? ", value=f"[Answer]({guide})",
                            inline=False)
            embed.add_field(name="Q.2- Why “OUTPUT THE ANSWER MODULO **10^9 + 7**? ", value=f"[Answer]({modulo})",
                            inline=False)
            embed.add_field(name="Q.3- What is **Modular Exponentiation**? ", value=f"[Answer]({powermod})",
                            inline=False)
            embed.add_field(name="Q.4- What is **Time Complexity**? ", value=f"[Answer]({timecomplexity})",
                            inline=False)
            embed.add_field(name="Q.5- What is **ACM-ICPC**? ", value=f"[Answer]({icpc})",
                            inline=False)
            embed.add_field(name="Q.6- How to study? ", value=f"[Answer]({howto})",
                            inline=False)
            embed.add_field(name="Q.7- How do I go about becoming a target coder? ", value=f"[Answer](https://www.quora.com/How-do-I-go-about-becoming-a-target-coder)",
                            inline=False)
            embed.add_field(name="Q.8- How do we get better at preparing for programming contests? ", value=f"[Answer](https://www.quora.com/How-do-we-get-better-at-preparing-for-programming-contests)",
                            inline=False)
            embed.add_field(name="Q.9- What was the biggest mistake you made while practicing for a programming contest?", value=f"[Answer](https://www.quora.com/What-was-the-biggest-mistake-you-made-while-practicing-for-a-programming-contest)",
                            inline=False)

            embed.add_field(name="Q.10- 6 mistakes that students make in college?",value=f"[Answer](https://www.youtube.com/watch?v=NzbbQptp--U)",
                inline=False)



            embed.set_thumbnail(url=f"https://i2.wp.com/multivendorshoppingcarts.com/wp-content/uploads/2019/03/FAQ.gif?fit=800%2C458&ssl=1")
            embed.set_image(url="https://media.giphy.com/media/8L21cgvkrqS48IRqHV/giphy.gif")
            await message.channel.send(content=None, embed=embed)
        if topic == "segment-tree":
            link1="https://codeforces.com/edu/course/2/lesson/4"
            link2="https://cp-algorithms.com/data_structures/segment_tree.html"
            link3="https://www.quora.com/What-are-some-SPOJ-CodeChef-problems-to-learn-segment-tree"
            link4="https://codeforces.com/blog/entry/71925"
            link5="https://visualgo.net/bn/segmenttree?slide=1"
            embed = discord.Embed(title=str("**#Segment Tree**"), colour=0x00FF00)
            embed.add_field(name="Codeforces EDU tutorial on Segment tree:", value=f"[Here is the link]({link1})",
                            inline=False)
            embed.add_field(name="CP algorithms blog on Segment tree", value=f"[Here is the link]({link2})",
                            inline=False)
            embed.add_field(name="Segment Tree Visualization", value=f"[Here is the link]({link5})",
                            inline=False)
            embed.add_field(name="Question Bank-1", value=f"[Here is the link]({link3})",
                            inline=False)
            embed.add_field(name="Question Bank-2", value=f"[Here is the link]({link4})",
                            inline=False)

            embed.set_thumbnail(url=f"https://media.geeksforgeeks.org/wp-content/cdn-uploads/segment-tree1.png")
            await message.channel.send(content=None, embed=embed)



client.run(token)
