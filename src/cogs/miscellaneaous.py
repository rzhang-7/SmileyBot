import discord
import random
from discord.ext import commands

class Misc(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    
    # Commands
    
    @commands.command()
    async def castellanos(self, ctx):
        await ctx.send('LOL! Here ya go:)')

    @commands.command(aliases=['8ball', '8'])
    async def _8ball(self, ctx, *, question):
        responses = ['As I see it, yes',
                    'Ask again later :P',
                    'Better not tell you now :P',
                    'Cannot predict now :P', 
                    'Concentrate and ask again :P',
                    "Don't count on it",
                    'It is certain',
                    'It is decidedly so',
                    'Most likely',
                    'My reply is no',
                    'Most likely',
                    'My reply is no',
                    'My sources say no',
                    'Outlook not so good',
                    'Outlook good',
                    'Reply hazy, try again :P',
                    'Signs point to yes',
                    'Very doubtful',
                    'Without a doubt',
                    'Yes',
                    'Yes - definitely',
                    'You may rely on it']
        await ctx.send(f':8ball:  |  {random.choice(responses)}, {ctx.author.name}')

    @commands.command(aliases=['phrase', 'rp'])
    async def randomphrase(self, ctx):
        adjectives = ['painful', 'sexy', 'curvy', 'illiterate','stale', 'beautiful', 'sad', 'depressed', 'hyper', 'seductive', 'embarrassed',
        'big', 'juicy', 'salty', 'rich', 'quiet', 'epic', 'woebegone', 'nervous', 'long', 'miniscule', 'rubbery', 'funny', 'shiny', 'infinite', 'wholesome',
        'sweet', 'pampered', 'smelly','czechoslovakian', 'drunk', 'homosexual', 'heterosexual', 'bisexual', 'dum', 'cute', 'short', 'chibi', 'hot', 'kawaii',
        'emo', 'edgy', 'anime', 'derpy', 'duck', 'shady', 'minimalistic', 'ballistic', 'cannibalistic', 'demonic', 'angelic', 'pixelated', 'interesting', 'spoiled',
        'broken', 'imported', 'deported', 'disappointed', 'angry', 'happy', 'smiling', 'defunctional', 'normal', 'inferior', 'superior', 'golden', 'common',
        'rare', 'expensive', 'exquisite', 'luxurious', 'lucrative', 'limp', 'fiery', 'burning', 'lively', 'heartly', 'judgemental', 'mental', 'serpentine',
        'stone', 'random', 'old', 'lost', 'new', 'abandoned', 'feathered', 'malcontent', 'malnourished', 'corpulent', 'magical', 'solid', 'colourful',
        'draconian', 'thicc', 'acute', 'obtuse', 'insignificant', 'mighty', 'withering', 'supreme', 'sponsored', 'flushed', 'complex', 'stupendous', 
        'horrendous', 'tremendous', 'portentous', 'endless', 'misspelled', 'false', 'confident', 'fake', 'true', 'satanic', 'attractive', 'default', 'realistic',
        'lumpy', 'demented', 'groggy', 'annoyed', 'robotic', 'famous', 'popular', 'accepted', 'awkward', 'corrupt', 'ultimate', 'dark', 'bright', 'fancy', 'athletic',
        'smart', 'cultured', 'uncultured', 'gaming', 'dancing', 'pathetic', 'sympathetic', 'lying', 'dry', "Moon lord's", 'mythical', 'bloody', 'ancient', 'determined',
        'confused', 'geometric', 'circular', 'round', 'redundant', 'godly', 'heavenly', 'ergonomic', 'smol', 'cool', 'satirical', 'ironic', 'roasted', 'burnt', 'illegitimate',
        'forbidden', 'flat', 'braindead', 'sarcastic', 'political', 'dangerous', 'futile', 'illicit', 'discombobulated', 'demonitized', 'demoralized', 'wet', 'majestic', 'nauseous',
        'gassy', 'nasty', 'enthusiastic', 'malicious', 'suspicious', 'sketchy', 'concerned', 'sneaky', 'illegal', 'legal', 'sane', 'insane', 'devastating', 'pensive', 'content',
        'nsfw', 'base-boosted', 'true','skewered', 'suprised', 'dystopic', 'utopic', 'bothersome', 'rabid', 'spicy', 'vegan', 'gangsta']

        nouns = ['dirt', 'dictator','Dhan', 'Edric 😳', 'water', 'labtop', 'emu', 'duck', 'tree', 'stump', 'forest', 'worm', 'cult','cultist', 'eye', 'brain',
        'Cthulhu', 'God', 'potato', 'chicken', 'ramen','cheese', 'dog', 'cat', 'earth', 'clock', 'moon', 'hostage', 'self-esteem', 'ritual', 'humanity', 'people',
        'murderer', 'crab', 'penguin', 'RATS (more specifically, *rattus rattus*, the black rat)', 'hornet', 'bee', 'mushroom', 'plant', 'flower', 'robot', 'empire', 
        'king', 'queen', 'emperor', 'empress', 'star','fish', 'bug', 'moth', 'fanart', 'fanfic','plague', 'ship', 'developer', 'demon', 'angel', 'satan', 'santa', 
        'character', 'meme', 'gamer', 'soul', 'juice', 'tea', 'bowl', 'food', 'senpai', 'legs', 'udon', 'creature', 'pasta', 'lasagna', 'scissors', 'sword', 'Karen',
        'dungeon', 'temple', 'place', 'thing', 'chair', 'scarf', 'rock', 'grass', 'idol', 'sock', 'server', 'phone', 'lie', 'bread', 'determination :heart:', 'confusion',
        'shape', 'circle', 'list', 'budget', 'manager', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'apple', 'squirrel', 'ocean', 'satire', 'irony', 'vegetables', 'sadist',
        'fan', 'child', 'mentality', 'hummus', 'sarcasm', 'autocorrect', 'degenerate', 'hair', 'normie', 'snake', 'locker', 'refridgerator', 'mountain', 'boy', 'girl', 'bathroom',
        'shower', 'enthusiasm', 'carnage', 'worm', 'documents', 'description','corpses', 'bodies', 'blood', 'sanity', 'insanity', 'monstrosity', 'cowboy', 'content', 'comet',
        'wifi', 'waifu', 'spider', 'pikachu', 'kohai', 'pedophile', 'therapist', 'homework', 'dystopia', 'utopia', 'terrorist', 'stalker', 'vacuum', 'peach', 'promise',
        'gangsta']

        await ctx.send(f'{random.choice(adjectives)} {random.choice(nouns)}')
    
    @commands.command(aliases=['descme', 'rd'])
    async def describeme(self, ctx):
        desAdjectives = ['painful', 'sexy', 'curvy', 'illiterate','stale', 'beautiful', 'sad', 'depressed', 'hyper', 'seductive', 'embarrassed',
        'big', 'juicy', 'salty', 'rich', 'quiet', 'epic', 'woebegone', 'nervous', 'long', 'miniscule', 'rubbery', 'funny', 'shiny', 'infinite', 'wholesome',
        'sweet', 'pampered', 'smelly','czechoslovakian', 'drunk', 'homosexual', 'heterosexual', 'bisexual', 'dum', 'cute', 'short', 'chibi', 'hot', 'kawaii',
        'emo', 'edgy', 'anime', 'derpy', 'duck', 'shady', 'minimalistic', 'ballistic', 'cannibalistic', 'demonic', 'angelic', 'pixelated', 'interesting', 'spoiled',
        'broken', 'imported', 'deported', 'disappointed', 'angry', 'happy', 'smiling', 'defunctional', 'normal', 'inferior', 'superior', 'golden', 'common',
        'rare', 'expensive', 'exquisite', 'luxurious', 'lucrative', 'limp', 'fiery', 'burning', 'lively', 'heartly', 'judgemental', 'mental', 'serpentine',
        'stone', 'random', 'old', 'lost', 'new', 'abandoned', 'feathered', 'malcontent', 'malnourished', 'corpulent', 'magical', 'solid', 'colourful',
        'draconian', 'thicc', 'acute', 'obtuse', 'insignificant', 'mighty', 'withering', 'supreme', 'sponsored', 'flushed', 'complex', 'stupendous', 
        'horrendous', 'tremendous', 'portentous', 'endless', 'misspelled', 'false', 'confident', 'fake', 'true', 'satanic', 'attractive', 'default', 'realistic',
        'lumpy', 'demented', 'groggy', 'annoyed', 'robotic', 'famous', 'popular', 'accepted', 'awkward', 'corrupt', 'ultimate', 'dark', 'bright', 'fancy', 'athletic',
        'smart', 'cultured', 'uncultured', 'gaming', 'dancing', 'pathetic', 'sympathetic', 'lying', 'dry', "Moon lord's", 'mythical', 'bloody', 'ancient', 'determined',
        'confused', 'geometric', 'circular', 'round', 'redundant', 'godly', 'heavenly', 'ergonomic', 'smol', 'cool', 'satirical', 'ironic', 'roasted', 'burnt', 'illegitimate',
        'forbidden', 'flat', 'braindead', 'sarcastic', 'political', 'dangerous', 'futile', 'illicit', 'discombobulated', 'demonitized', 'demoralized', 'wet', 'majestic', 'nauseous',
        'gassy', 'nasty', 'enthusiastic', 'malicious', 'suspicious', 'sketchy', 'concerned', 'sneaky', 'illegal', 'legal', 'sane', 'insane', 'devastating',
        'pensive', 'content','nsfw', 'base-boosted', 'true','skewered', 'suprised', 'dystopic', 'utopic', 'bothersome', 'rabid', 'spicy', 'vegan', 'gangsta']

        await ctx.send(f'{ctx.author.name} is {random.choice(desAdjectives)} 😳')
    
    @commands.command()
    async def randint(self, ctx, no1, no2):
        if no1 == None:
            no1 = 1
        await ctx.send(f'Here is your random integer: **{random.randint(int(no1), int(no2))}**')

    @commands.command(aliases=['backwards', '.s'])
    async def reverse(self, ctx, *, text):
        if ctx.author.id == '296396903195607040':
            return
        await ctx.send(text[::-1])

    @commands.command(aliases=['exag'])
    async def exaggerate(self, ctx, *, text):
        pass  

    # Errors

    @_8ball.error
    async def _8ball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Looks like randomly shaking a digital 8 ball without a question won't do you any good... Maybe looking into `s.help misc` would do you some good")

    @reverse.error
    async def reverse_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('pleh rof csim pleh.s ot og nac uoy rO \n.esrever ot em rof ecnetnes ro drow a yficeps esaelP')
def setup(client):
    client.add_cog(Misc(client))           
