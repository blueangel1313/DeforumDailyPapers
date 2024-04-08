import os
import discord
from discord.ext import commands, tasks
import requests

HF_KEY = os.environ.get("HFREADME")
DISCORD_KEY = os.environ.get("DISCORDKEY")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

guild_channels = {}

def get_daily_papers(limit=12, full=True, config=True):
    url = 'https://huggingface.co/api/daily_papers'
    headers = {'Authorization': f'Bearer {HF_KEY}'}
    params = {'limit': limit, 'full': str(full), 'config': str(config)}
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch daily papers. Status code: {response.status_code}")
        return None

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')
    publish_latest_paper.start()

@bot.slash_command(description="Set the channel for daily papers")
async def setchannel(ctx, channel: discord.Option(discord.TextChannel, "Select a channel")):
    guild_channels[ctx.guild.id] = channel.id
    await ctx.respond(f"Papers will now be sent to {channel.mention}")

latest_published_paper_id = None

@tasks.loop(minutes=1)
async def publish_latest_paper():
    global latest_published_paper_id
    daily_papers = get_daily_papers(limit=1)
    if daily_papers:
        latest_paper = daily_papers[0]
        paper_id = latest_paper['paper']['id']
        if paper_id != latest_published_paper_id:
            latest_published_paper_id = paper_id
            paper_data = latest_paper['paper']
            title = paper_data['title']
            url = f"https://arxiv.org/abs/{paper_data['id']}"
            media_url = latest_paper.get('mediaUrl', None)
            embed = discord.Embed(title="Latest Paper", color=discord.Color.blue())
            embed.add_field(name="Title", value=title, inline=False)
            embed.add_field(name="URL", value=url, inline=False)
            if media_url:
                embed.set_image(url=media_url)
            embed.set_footer(text="Powered by Hugging Face Papers API")
            for guild_id, channel_id in guild_channels.items():
                channel = bot.get_channel(channel_id)
                if channel:
                    await channel.send(embed=embed)

if __name__ == "__main__":
    bot.run(DISCORD_KEY)
