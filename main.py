from discord.ext import commands

bot = commands.Bot(command_prefix='!')
TOKEN = 'NzY4MTgzOTA0NTIzNjQ5MDQ0.X48xAw.vjSORgg2gaq0JO_FL8whbkcgx2M'
cogs_to_add = [
    'cogs.hello_world',
    'cogs.events_watch_cog',
    'cogs.start_deal_cog'
]

if __name__ == "__main__":
    for cog in cogs_to_add:
        print(f'Loading : {cog}')
        bot.load_extension(cog)

bot.run(TOKEN)