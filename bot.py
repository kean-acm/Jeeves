import discord
import praw
import random
from discord.ext import commands

client = discord.Client()

reddit = praw.Reddit(client_id='GiJpLeUa2EzUoaODmjfLSQ',
                     client_secret='REDDITAPPTOKEN',
                     user_agent='Jeeves')

#Event to show Bot Running Status in Terminal
@client.event
async def on_ready():
        print("Bot is live")

#Event to respond to messages
@client.event
async def on_message(message):
    if message.author == client.user:  
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('!howdy'):
        await message.channel.send('*Tips Hat*')

    if message.content.startswith('!meme'):
        subreddit = reddit.subreddit('cleanmemes')
        all_subs = []
        hot = subreddit.hot(limit = 75)

        for submission in hot:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)
        name = random_sub.title
        url = random_sub.url
        em = discord.Embed(title = name, color = 0x0000b3)

        em.set_image(url = url)
        await message.channel.send('Very good, sir')
        await message.channel.send(embed = em)


    if message.content.startswith('!badmeme'):
        subreddit = reddit.subreddit('comedyheaven')
        all_subs = []
        hot = subreddit.hot(limit = 75)

        for submission in hot:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)
        name = random_sub.title
        url = random_sub.url
        em = discord.Embed(title = name, color = 0x0000b3)

        em.set_image(url = url)
        await message.channel.send('If you insist, sir')
        await message.channel.send(embed = em)



client.run("TOKEN")
