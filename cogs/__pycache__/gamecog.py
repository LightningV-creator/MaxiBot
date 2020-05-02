import discord
from discord.ext import commands
import random


class Gamecog(commands.Cog):

    def __init__(self, client):
        self.client = client

    
    @commands.Cog.listener()  
    async def on_ready(self):
        print('gamecog is ready')   

    @commands.command()
    async def pingtwo(self, ctx):
        await ctx.send('works?')     


    @commands.command()
    async def rps(self, ctx, choice):
        choices = [ 'rock', 'paper', 'scissors' ]
        mychoice = random.choice(choices)

        winning = [] 
        winning.append('I got ' + mychoice + ', get rekt!')
        winning.append(mychoice + '... Hah! I won. I am winning so much I got sick and tired of winning.')
        winning.append('I won! I got ' + mychoice + '. Wunderbar!')
   

        losing = []
        losing.append('O mein gott, I got ' + mychoice +'... You won, smh.')
        losing.append('Aw man I got ' + mychoice + '... How are you so lucky?')
        losing.append(mychoice + '... Nein nein nein you got lucky this time')
 
        drawEmojis = [ ':thinking:', ':sweat_smile:', ':innocent:' ]
        winningEmojis = [ ':sunglasses:', ':rofl:', ':wink:' ]
        losingEmojis = [ ':cry:', ':crying_cat_face:', ':knife:' ]
    
        if (choice not in choices):
            await ctx.send('Nah ah, you have to choose `rock`, `paper`, or `scissors`. For example, you can try `' + '.' + 'rps rock`')
        else:
            if (mychoice == choice):
                await ctx.send("Lucky you, I got " + choice + " as well, it is a draw!" + " " + random.choice(drawEmojis))
            elif (mychoice == 'rock' and choice == 'paper'):
                await ctx.send(random.choice(losing) + " " + random.choice(losingEmojis))
            elif (mychoice == 'scissors' and choice == 'rock'):
                await ctx.send(random.choice(losing) + " " + random.choice(losingEmojis))
            elif (mychoice == 'paper' and choice == 'scissors'):
                await ctx.send(random.choice(losing) + " " + random.choice(losingEmojis))
            elif (mychoice == 'paper' and choice == 'rock'):
               await ctx.send(random.choice(winning) + " " + random.choice(winningEmojis))
            elif (mychoice == 'rock' and choice == 'scissors'):
                await ctx.send(random.choice(winning) + " " + random.choice(winningEmojis))
            elif (mychoice == 'scissors' and choice == 'winning'):
                await ctx.send(random.choice(winning) + " " + random.choice(winningEmojis))    


def setup(client):
   client.add_cog(Gamecog(client))        