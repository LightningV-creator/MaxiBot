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
        winning.append('I have ' + mychoice + ', Better Luck Next Time!')
        winning.append(mychoice + ' I won! Try Aagain!')
        winning.append('I won! I got ' + mychoice + 'R.I.P')
   
        losing = []
        losing.append('Well.. I have ' + mychoice +' You win')
        losing.append('bruh I got ' + mychoice + ' smh')
        losing.append(mychoice + ' I let you win on purpose this time')
 
        drawEmojis = [ ':thinking:', ':sweat_smile:', ':innocent:' ]
        winningEmojis = [ ':sunglasses:', ':rofl:', ':wink:' ]
        losingEmojis = [ ':cry:', ':crying_cat_face:', ':knife:' ]
    
        if (choice not in choices):
            await ctx.send('Check your spelling(Rock, Paper, or Scissors)')
        else:
            if (mychoice == choice):
                await ctx.send("Lucky you, I have " + choice + " it is a draw!" + " " + random.choice(drawEmojis))
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