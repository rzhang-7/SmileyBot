import discord
import os
import json
from discord.ext import commands, tasks
from itertools import cycle

def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
    
    return prefixes[str(message.guild.id)] 

client = commands.Bot(command_prefix = get_prefix)
status = cycle(['In the depths of the Underworld requesting s.help', \
    "s.help | Support hasn't arrived yet...", 's.help | (_ _|||)', \
    's.help | I may be a bot, but I still have feelings...! >-<', \
    's.help | Hide and Seek', 's.help | in the dark', \
    '❤️ Using s.help fills you with DETERMINATION', \
    's.help | ❤️🧡💛💚💙💜 = almost god(???)', \
    "s.help | If bot is disable then I'll flip the table", \
    "s.help | Opinions can't be wrong, but they can be socially unacceptable", \
    's.help | “Never argue with an idiot. They will drag you down to their level and beat you with experience.”', \
    's.help | Snapping non-existent people out of existence'])
client.remove_command('help')

def is_it_me(ctx):
    return ctx.author.id == 447929605110628363

@client.event
async def on_ready():
    change_status.start()
    print(f'This is {client.user.name}, User ID {client.user.id}')
    print(f'{client.user.name} has entered the chat')
    print('---------')
    

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='welcomes-and-goodbyes')
    await channel.send(f'{member.mention} has entered the chat')

@client.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, name='welcomes-and-goodbyes')
    await channel.send(f'{member.mention} has left the chat')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! Time taken: `{round(client.latency * 1000)}ms`  :ping_pong:')

@client.command(aliases=['we', 'insanity', 'emoji', 'emote', 'windowemotes'])
@commands.check(is_it_me)
async def windowemojis(ctx):
    await ctx.send('😀😁😂🤣😃😄😅😆😉😊😋😎😍😘🥰😗😙😚☺🙂🤗🤩🤔🤨😐😑😶🙄😏😣😥😮🤐😯😪😫🥱😴😌😛😜😝🤤😒😓😔😕🙃🤑😲☹🙁😖😞😟😤😢😭😦😧😨😩🤯😬😰😱🥵🥶😳🤪😵🥴😠😡🤬😷🤒🤕🤢🤮🤧😇🥳🥺🤠🤡🤥🤫🤭🧐🤓😈👿👹👺💀☠👻👽👾🤖💩😺😸😹😻😼😽🙀😿😾🐱‍👤🐱‍🏍🐱‍💻🐱‍🐉🐱‍👓🐱‍🚀🙈🙉🙊🐵🐶🐺🐱🦁🐯🦒🦊🦝🐮🐷🐗🐭🐹🐰🐻🐨🐼🐸🦓🐴🦄🐔🐲🐽🐾🐒🦍🦧🦮🐕‍🦺🐩🐕🐈🐅🐆🐎🦌🦏🦛🐂🐃🐄🐖🐏🐑🐐🐪🐫🦙🦘🦥🦨🦡🐘🐁🐀🦔🐇🐿🦎🐊🐢🐍🐉🦕🦖🦦🦈🐬🐳🐋🐠🐡🦐🦑🐙🦞🦀🐚🦆🐓🦃🦅')
    await ctx.send('🕊🦢🦜🦩🦚🦉🐦🐧🐥🐤🐣🦇🦋🐌🐛🦟🦗🐜🐝🐞🦂🕷🕸🦠🧞‍♀️🧞‍♂️🗣👤👥👁👀🦴🦷👅👄🧠🦾🦿👣🤺⛷🤼‍♂️🤼‍♀️👯‍♂️👯‍♀️💑👩‍❤️‍👩👨‍❤️‍👨💏👩‍❤️‍💋‍👩👨‍❤️‍💋‍👨👪👨‍👩‍👦👨‍👩‍👧👨‍👩‍👧‍👦👨‍👩‍👦‍👦👨‍👩‍👧‍👧👨‍👨‍👦👨‍👨‍👧👨‍👨‍👧‍👦👨‍👨‍👦‍👦👨‍👨‍👧‍👧👩‍👩‍👦👩‍👩‍👧👩‍👩‍👧‍👦👩‍👩‍👦‍👦👩‍👩‍👧‍👧👩‍👦👩‍👧👩‍👧‍👦👩‍👦‍👦👩‍👧‍👧👨‍👦👨‍👧👨‍👧‍👦👨‍👦‍👦👨‍👧‍👧👭👩🏻‍🤝‍👩🏻👩🏼‍🤝‍👩🏻👩🏼‍🤝‍👩🏼👩🏽‍🤝‍👩🏻👩🏽‍🤝‍👩🏼👩🏽‍🤝‍👩🏽👩🏾‍🤝‍👩🏻👩🏾‍🤝‍👩🏼👩🏾‍🤝‍👩🏽👩🏾‍🤝‍👩🏾👩🏿‍🤝‍👩🏻👩🏿‍🤝‍👩🏼👩🏿‍🤝‍👩🏽👩🏿‍🤝‍👩🏾👩🏿‍🤝‍👩🏿👫👩🏻‍🤝‍🧑🏻👩🏻‍🤝‍🧑🏼👩🏻‍🤝‍🧑🏽👩🏻‍🤝‍🧑🏾👩🏻‍🤝‍🧑🏿👩🏼‍🤝‍🧑🏻👩🏼‍🤝‍🧑🏼👩🏼‍🤝‍🧑🏽👩🏼‍🤝‍🧑🏾👩🏼‍🤝‍🧑🏿👩🏽‍🤝‍🧑🏻👩🏽‍🤝‍🧑🏼👩🏽‍🤝‍🧑🏽👩🏽‍🤝‍🧑🏾👩🏽‍🤝‍🧑🏿👩🏾‍🤝‍🧑🏻👩🏾‍🤝‍🧑🏼👩🏾‍🤝‍🧑🏽👩🏾‍🤝‍🧑🏾👩🏾‍🤝‍🧑🏿👩🏿‍🤝‍🧑🏻👩🏿‍🤝‍🧑🏼👩🏿‍🤝‍🧑🏽👩🏿‍🤝‍🧑🏾👩🏿‍🤝‍🧑🏿👬👨🏻‍🤝‍👨🏻👨🏼‍🤝‍👨🏻👨🏼‍🤝‍👨🏼👨🏽‍🤝‍👨🏻👨🏽‍🤝‍👨🏼👨🏽‍🤝‍👨🏽👨🏾‍🤝‍👨🏻👨🏾‍🤝‍👨🏼👨🏾‍🤝‍👨🏽👨🏾‍🤝‍👨🏾👨🏿‍🤝‍👨🏻👨🏿‍🤝‍👨🏼👨🏿‍🤝‍👨🏽👨🏿‍🤝‍👨🏾👨🏿‍🤝‍👨🏿👨🧑👧👦🧒👶👵👴🧓👩‍🦰👨‍🦰👩‍🦱👨‍🦱👩‍🦲👨‍🦲👩‍🦳👨‍🦳👱‍♀️👱‍♂️👸🤴👳‍♀️👳‍♂️👲🧔👼🤶🎅👮‍♀️👮‍♂️🕵️‍♀️🕵️‍♂️💂‍♀️💂‍♂️👷‍♀️👷‍♂️👩‍⚕️👨‍⚕️👩‍🎓👨‍🎓👩‍🏫👨‍🏫👩‍⚖️👨‍⚖️👩‍🌾👨‍🌾👩‍🍳👨‍🍳👩‍🔧👨‍🔧👩‍🏭👨‍🏭👩‍💼👨‍💼👩‍🔬👨‍🔬👩‍💻👨‍💻👩‍🎤👨‍🎤👩‍🎨👨‍🎨👩‍✈️👨‍✈️👩‍🚀👨‍🚀👩‍🚒')
    await ctx.send('👨‍🚒🧕👰🤵🤱🤰🦸‍♀️🦸‍♂️🦹‍♀️🦹‍♂️🧙‍♀️🧙‍♂️🧚‍♀️🧚‍♂️🧛‍♀️🧛‍♂️🧜‍♀️🧜‍♂️🧝‍♀️🧝‍♂️🧟‍♀️🧟‍♂️🙍‍♀️🙍‍♂️🙎‍♀️🙎‍♂️🙅‍♀️🙅‍♂️🙆‍♀️🙆‍♂️🧏‍♀️🧏‍♂️💁‍♀️💁‍♂️🙋‍♀️🙋‍♂️🙇‍♀️🙇‍♂️🤦‍♀️🤦‍♂️🤷‍♀️🤷‍♂️💆‍♀️💆‍♂️💇‍♀️💇‍♂️🧖‍♀️🧖‍♂️🤹‍♀️🤹‍♂️👩‍🦽👨‍🦽👩‍🦼👨‍🦼👩‍🦯👨‍🦯🧎‍♀️🧎‍♂️🧍‍♀️🧍‍♂️🚶‍♀️🚶‍♂️🏃‍♀️🏃‍♂️💃🕺🧗‍♀️🧗‍♂️🧘‍♀️🧘‍♂️🛀🛌🕴🏇🏂🏌️‍♀️🏌️‍♂️🏄‍♀️🏄‍♂️🚣‍♀️🚣‍♂️🏊‍♀️🏊‍♂️🤽‍♀️🤽‍♂️🤾‍♀️🤾‍♂️⛹️‍♀️⛹️‍♂️🏋️‍♀️🏋️‍♂️🚴‍♀️🚴‍♂️🚵‍♀️🚵‍♂️🤸‍♀️🤸‍♂️🤳💪🦵🦶👂🦻👃🤏👈👉☝👆👇✌🤞🖖🤘🤙🖐✋👌👍👎✊👊🤛🤜🤚👋🤟✍👏👐🙌🤲🙏🤝💅🎈🎆🎇🧨✨🎉🎊🎃🎄🎋🎍🎎🎏🎐🎑🧧🎀🎁🎗🎞🎟🎫🎠🎡🎢🎪🎭🖼🎨🧵🧶🛒👓🕶🦺🥽🥼🧥👔👕👖🩳🧣🧤🧦👗🥻👘👚🩲🩱👙👛👜👝🛍🎒👞👟🥾🥿👠👡👢🩰👑🧢⛑👒')
    await ctx.send('🎩🎓💋💄💍💎⚽⚾🥎🏀🏐🏈🏉🎱🎳🥌⛳⛸🎣🤿🎽🛶🎿🛷🥅🏒🥍🏏🏑🏓🏸🎾🥏🪁🎯🥊🥋🥇🥈🥉🏅🎖🏆🎮🕹🎰🎲🔮🧿🧩🧸🪀🎴🃏🀄♟♠♣♥♦🔈🔉🔊📢📣🔔🎼🎵🎶🎙🎤🎚🎛🎧📯🥁🎷🎺🎸🪕🎻🎹📻🔒🔓🔏🔐🔑🗝🪓🔨⛏⚒🛠🔧🔩🧱⚙🗜🛢⚗🧪🧫🧬🩺💉🩸🩹💊🔬🔭⚖📿🔗⛓🧰🧲🦯🛡🏹🗡⚔🔪🔫☎📞📟📠📱📲📳📴🚬⚰⚱🗿🔋🔌💻🖥🖨⌨🖱🖲💽💾💿📀🧮🎥🎬📽📡📺📷📸📹📼🔍🔎🕯🪔💡🔦🏮📔📕📖📗📘📙📚📓📒📃📜📄📑📰🗞🔖🏷💰💴💵💶💷💸💳🧾🏧✉📧📨📩📤📥📦')
    await ctx.send('📫📪📬📭📮🗳✏✒🖋🖊🖌🖍📝🗒💼📁📂🗂📅📆🗓📇📈📉📊📋📌📍📎🖇📏📐✂🗃🗄🗑⌛⏳⌚⏰⏱⏲🕰🍕🍔🍟🌭🍿🧂🥓🥚🍳🧇🥞🧈🍞🥐🥨🥯🥖🧀🥗🥙🥪🌮🌯🥫🍖🍗🥩🍠🥟🥠🥡🍱🍘🍙🍚🍛🍜🦪🍣🍤🍥🥮🍢🧆🥘🍲🍝🥣🥧🍦🍧🍨🍩🍪🎂🍰🧁🍫🍬🍭🍡🍮🍯🍼🥛🧃☕🍵🧉🍶🍾🍷🍸🍹🍺🍻🥂🥃🧊🥤🥢🍽🍴🥄🏺🥝🥥🍇🍈🍉🍊🍋🍌🍍🥭🍎🍏🍐🍑🍒🍓🍅')
    await ctx.send('🍆🌽🌶🍄🥑🥒🥬🥦🥔🧄🧅🥕🌰🥜💐🌸🏵🌹🌺🌻🌼🌷🥀☘🌱🌲🌳🌴🌵🌾🌿🍀🍁🍂🍃🚗🚓🚕🛺🚙🚌🚐🚎🚑🚒🚚🚛🚜🚘🚔🚖🚍🦽🦼🛹🚲🛴🛵🏍🏎🚄🚅🚈🚝🚞🚃🚋🚆🚉🚊🚇🚟🚠🚡🚂🛩🪂✈🛫🛬💺🚁🚀🛸🛰⛵🚤🛥⛴🛳🚢⚓🚏⛽🚨🚥🚦🚧🏁🏳‍🌈🏳🏴🏴‍☠️🚩🌌🪐🌍🌎🌏🗺🧭🏔⛰🌋🗻🛤🏕🏞🛣🏖🏜🏝🏟🏛🏗🏘🏙🏚🏠🏡⛪🕋🕌🛕🕍⛩🏢🏣🏤🏥🏦🏨')
    await ctx.send('🏩🏪🏫🏬🏭🏯🏰💒🗼🌉🗽🗾🎌⛲⛺🌁🌃🌄🌅🌆🌇♨💈🛎🧳🪑🚪🛏🛋🚽🧻🚿🛁🧼🧽🧴🪒🧷🧹🧺🧯☁⛅⛈🌤🌥🌦🌧🌨🌩🌪🌫🌝🌑🌒🌓🌔🌕🌖🌗🌘🌙🌚🌛🌜☀🌞⭐🌟❤🧡💛💚💙💜🤎🖤🤍💔❣💕💞💓💗💖💘💝💟💌💢💥💤💦💨💫🕳☮✝☪🕉☸✡🔯🕎☯☦🛐⛎♈♉♊♋♌♍♎♏♐♑♒♓🆔⚕♾⚛🈳🈹🈶🈚🈸🈺🈷✴🆚🉑💮🉐㊙㊗🈴🈵🈲🚼')
    await ctx.send('🅰🅱🆎🆑🅾🆘⛔🛑📛❌⭕🚫🔇🔕🚭🚷🚯🚳🚱🔞📵❗❕❓❔‼⁉💯🔅🔆🔱⚜〽☢☣⚠🚸🔰♻🈯💹❇✳❎✅💠🌐Ⓜ🈂➿🛂🛃🛄🛅♿🚾🅿🚰🚹🚺🚻🚮📶🈁🆖🆗🆙🆒🆕🆓#️⃣*️⃣0️⃣1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣🔟🔢▶⏸⏯⏹⏺⏭⏮⏩⏪🔀🔁🔂')
    await ctx.send('◀🔼⏫🔽⏬⏏🎦➡⬅⬆⬇↗↘↙↖↕↔🔄↪↩⤴⤵ℹ🔤🔡🔠🔣🔃🔛🔝🔜☑🔚🔙〰➰✔💲💱➕➖✖➗©®™🔘🔴🟠🟡🟢🔵🟣🟤⚫⚪🟥🟧🟨🟩🟦🟪🟫⬛⬜◼◻◾◽▪▫🔶🔸🔷🔹🔺🔻🔲🔳💭🗯💬🗨👁‍🗨🕐🕑🕒🕓🕔🕕🕖🕗🕘🕙🕚🕛🕜🕝🕞🕟🕠🕡🕢🕣🕤🕥🕦🕧')

@client.command(pass_context=True, aliases= ['logout', 'leave'])
@commands.check(is_it_me)
async def stop(ctx):
    await ctx.channel.send('`Smiley has left the chat`')
    await client.logout()

@stop.error
async def stop_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You can't do that >:<")

@tasks.loop(seconds=60)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command(pass_context=True)
async def help(ctx, category=None):
    owoThonk = '<:owo_thonk:670457546078814236>'
    coin = '<:coin:726445902205550632>'
    embedh = discord.Embed(
        colour=discord.Colour.dark_blue(),
        title='The Glorious list of commands :fireworks:',
        description='Bot prefix is `s.`'
    )

    embedh.set_author(name="It's a me, m̶̧̉͌̔͛͛a̵̖̤̒̿̈͐r̵̡̼̺̠̲̤̫͗͛̉́͗̊̎̌͒͘͜ḭ̸̤͚̟̖̑̀̉̋͛̊͒͘̕o̸̡͖̻̹̔̋̌̑̂̓͂̎͘ͅ Smiley", icon_url="https://cdn.discordapp.com/attachments/594634531940728862/723187066304987246/owocoolimagepfp.jpg")
    embedh.add_field(name="⚙ General", value='`ping`', inline=False)
    embedh.add_field(name="🃏 Fun (s.fun)", value='`summon` '+'`temmie` '+'`coinflip`', inline=False)
    embedh.add_field(name="🔧 Utilities", value='`factorial` '+'`factors` '+'`pfactor`', inline=False)
    embedh.add_field(name="🔒 Administrative", value='`clear` '+'`kick` '+'`ban` '+'`unban` '+'`setprefix`', inline=False)
    embedh.add_field(name=f"{owoThonk} Miscellaneous", value='`8ball` '+'`randomphrase` '+'`describeme` '+'`randint` '+'`reverse`', inline=False)
    embedh.set_footer(text='❤️ The knowledge of knowing these commands by reading them off of here fills you with DETERMINATION')
    
    embedu = discord.Embed(
        colour=discord.Colour.dark_blue(),
        title="Utility help 🔧",
        description="help with helping commands?"
    )
    
    embedu.set_author(name="Help menu", icon_url='https://cdn.discordapp.com/attachments/594634531940728862/723187066304987246/owocoolimagepfp.jpg')
    embedu.add_field(name='❗ `factorial`', value='Find the factorial of an integer. Please do not include an exclamation mark and please specify a number. You may use "!" in place of factorial', inline=False)
    embedu.add_field(name='🔢 `factors`', value='Find all the factors of an integer.  Please specify an integer. "factor" works too', inline=False)
    embedu.add_field(name='🔢 `pfactor`', value='Gives you the prime factorization of a given number. Please provide the number. Note that "⋅" is a multiplication symbol', inline=False)
    
    embedf = discord.Embed(
        colour=discord.Colour.dark_blue(),
        title='Fun help 🃏',
        description="Surely you can't be this bad at having fun to need help..."
    )

    embedf.set_author(name="Help menu", icon_url="https://cdn.discordapp.com/attachments/594634531940728862/723187066304987246/owocoolimagepfp.jpg") 
    embedf.add_field(name='🕯 `summon [@user#4200]`', value="Summons a user via ritual. Currently under maintenance and doesn't function well. DO NOT USE", inline=False)
    embedf.add_field(name='♥ `temmie`', value='Special enemy Temmie appears here to defeat you!!', inline=False)
    embedf.add_field(name=f'{coin} `coinflip`', value='You have a 50/50 chance of winning self-esteem! Please enter your guess in the command in all lower case. Aliase are: `cf`, `coin`, `flip`', inline=False )
    
    
    embedm = discord.Embed(
        colour=discord.Colour.dark_blue(),
        title=f'Miscellaneous help {owoThonk}',
        description="Doesn't seem to fit anywhere else, does it?"
    )
    embedm.set_author(name="Help menu", icon_url='https://cdn.discordapp.com/attachments/594634531940728862/723187066304987246/owocoolimagepfp.jpg')
    embedm.add_field(name='🎱 `8ball`', value='Foretells your future(?). Please ask a question when using this command', inline=False)
    embedm.add_field(name='🎲 `randomphrase`', value="Just a random adjective and noun. Decent for drawing ideas. List keeps growing. Aliases are: `s.rp`, `s.phrase`", inline=False)
    embedm.add_field(name='🎲 `describeme`', value="Give yourself a random description. List keeps growing. Aliases are: `s.descme`, `s.rd`", inline=False)
    embedm.add_field(name="🎲 `randint`", value='Returns a random integer between two specified integers. Please specify both numbers. The first integer should be less than the second integer', inline=False)
    embedm.add_field(name='🔄 `reverse`', value='Reverse a given sentence or word. Aliases are: `backwards`, `.s`', inline=False)
    
    if category == None:
        await ctx.send(embed=embedh)
    elif category == "util":
        await ctx.send(embed=embedu)
    elif category == 'fun':
        await ctx.send(embed=embedf)
    elif category == 'misc':
        await ctx.send(embed=embedm)
    else:
        await ctx.send("Can't help you with that mate, please try something else or screw off")

# Cogs

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send('Extension successfully loaded :thumbsup:')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send('Extension successfully unloaded :thumbsup:')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send('Successfully reloaded :thumbsup:')
 
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# Prefixes

@client.event
async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
 
    prefixes[str(guild.id)] = 's.'

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)
 
    prefixes.pop(str(guild.id))

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

@client.command()
@commands.has_permissions(administrator=True)
async def setprefix(ctx, prefix):
    
    
    with open('prefixes.json', 'r') as f:   
        prefixes = json.load(f)
 
    prefixes[str(ctx.guild.id)] = prefix

    with open('prefixes.json', 'w') as f:
        json.dump(prefixes, f, indent=4)

    await ctx.send(f'Prefix has been set to: "{prefix}"')


client.run('token')