import discord
from discord.ext import commands
import random

class Cogone(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()  
    async def on_ready(self):
        print('cogone is ready')

        
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong!')
         
     
    @commands.command()
    async def advice(self, ctx, *, question):
        responses = ['Yes, but do it drunk as f*ck',
    'My sources say no, but they also said Hillary would win',
    'What would Jesus do?',
    'Trump uses me when deciding to go to war',]   
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


    @commands.command()
    async def fact(self, ctx):
        responses = ['Some cats are actually allergic to humans.',
    "{A shrimp's heart is in it's head.}",
    "A crocodile can't stick it's tongue out.",
    "People say \"Bless you\" when you sneeze because when you sneeze,your heart stops for a mili-second.",
    "In a study of 200,000 ostriches over a period of 80 years, no one reported a single case where an ostrich buried its head in the sand.",
    "It is physically impossible for pigs to look up into the sky.",
    "More than 50'%' of the people in the world have never made or received a telephone call.",
    "Rats and horses can't vomit",
    "If you sneeze too hard, you can fracture a rib",
    "If you try to suppress a sneeze, you can rupture a blood vessel in your head or neck and die.",
    "If you keep your eyes open by force when you sneeze, you might pop an eyeball out.",
    "Rats multiply so quickly that in 18 months, two rats could have over a million descendants.",
    "Wearing headphones for just an hour will increase the bacteria in your ear by 700 times.",
    "In every episode of Seinfeld there is a Superman somewhere.",
    "The cigarette lighter was invented before the match.",
    "Thirty-five percent of the people who use personal ads for dating are already married.",
    "A duck's quack doesn't echo, and no one knows why.",
    "23% of all photocopier faults worldwide are caused by people sitting on them and photocopying their butts.",
    "In the course of an average lifetime you will, while sleeping, eat 70 assorted insects and 10 spiders.",
    "Most lipstick contains fish scales.",
    "Like fingerprints, everyone's tongue print is different.",
    "Over 75% of people who read this will try to lick their elbow.",
    "A crocodile can't move its tongue and cannot chew. Its digestive juices are so strong that it can digest a steel nail.",
    "Every human spent about half an hour as a single cell.",
    "Every year about 98% of atoms in your body are replaced.",
    "Hot water is heavier than cold.",
    "If you went out into space, you would explode before you suffocated because there's no air pressure.",
    "Sound travels 15 times faster through steel than through the air.",
    "On average, half of all false teeth have some form of radioactivity.",
    "Only one satellite has been ever been destroyed by a meteor: the European Space Agency's Olympus in 1993.",
    "Seals used for their fur get extremely sick when taken aboard ships.",
    "Sloths take two weeks to digest their food.",
    "Guinea pigs and rabbits can't sweat.",
    "According to the Wall Street Journal, the cockfighting market is huge: The Philippines has five million roosters used for exactly that.",
    "Young beavers stay with their parents for the first two years of their lives before going out on their own.",
    "Deer can't eat hay.",
    "Skunks can accurately spray their smelly fluid as far as ten feet.",
    "The lifespan of a squirrel is about nine years.",
    "You are now breathing manually",
    "You are not blinking manually",
    "You are now aware of the fact your clothes are touching your skin",
    "You are now aware that there is no comfortable place to put your tongue in your mouth",
    "You are now aware that your jaw has weight and you're holding it up",
    "You are now aware that everytime you swallow you hear a little crackle",
    "You are now swallowing and producing saliva manually",
    "You are now aware that you have an itch somewhere on your body",
    "You are now aware your nose is always in your line of sight",
    ]    
        await ctx.send(f'Fact: {random.choice(responses)}')

def setup(client):
   client.add_cog(Cogone(client))