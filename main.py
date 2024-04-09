from discord.ext import commands

bot = commands.Bot(command_prefix='!')
TOKEN = 'MTIyNzIxMDEwMjAwMDU4MjcxNw.G1I9bJ.VlIx33JwQb0_7lOX4MW2fVaNNsokOkirPrO0D8'
cogs_to_add = [
    'cogs.events_watch_cog',
    'cogs.start_deal_cog',
    'cogs.get_fees_cog',
    'cogs.help_cog'
]

if __name__ == "__main__":
    for cog in cogs_to_add:
        print(f'Loading : {cog}')
        bot.load_extension(cog)

bot.run(TOKEN)
