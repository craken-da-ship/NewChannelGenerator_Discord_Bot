import discord
from discord.ext import commands

#Creates the prefix for the commands
client = commands.Bot(command_prefix='/')

#Gives info to the bot owner to let them know that the bot is connected and who it is running as
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

#Beginning of /NewText    
@client.command()
async def NewText(ctx, arg):
    #opens blacklist file and checks if user has created a channel before.
    with open('userlisttext.txt') as f:
        if ctx.message.author.mention in f.read():
            test = 1
        else:
            test = 0
            
    #Checks output from with loop. If true, lets user know they have already created a channel and ends command.
    #If output was false, creates channel, informs the user of so, and writes user ID to blacklist file
    f=open("userlisttext.txt","a+")   
    if test==1:
        await ctx.channel.send("{} you have already made your channel".format(ctx.message.author.mention))
        return
    else:
        guild = ctx.guild
        await guild.create_text_channel(arg)
        await ctx.channel.send("{} you have made your channel".format(ctx.message.author.mention))
        f.write(ctx.message.author.mention + "\n")
    f.close()
#End of /NewText

#Beginning of /NewVoice    
@client.command()
async def NewVoice(ctx, arg):
    #opens blacklist file and checks if user has created a channel before.
    with open('userlistvoice.txt') as f:
        if ctx.message.author.mention in f.read():
            test = 1
        else:
            test = 0

    #Checks output from with loop. If true, lets user know they have already created a channel and ends command.
    #If output was false, creates channel, informs the user of so, and writes user ID to blacklist file            
    f=open("userlistvoice.txt","a+")   
    if test==1:
        await ctx.channel.send("{} you have already made your channel".format(ctx.message.author.mention))
        return
    else:
        guild = ctx.guild
        await guild.create_voice_channel(arg)
        await ctx.channel.send("{} you have made your channel".format(ctx.message.author.mention))
        f.write(ctx.message.author.mention + "\n")
    f.close()
#End of /NewVoice

#Client Token, be sure to replace with your own
client.run('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
