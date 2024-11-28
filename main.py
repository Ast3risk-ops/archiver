import ezcord
import discord
import os
from dotenv import load_dotenv
load_dotenv()

webhookurl = str(os.getenv("WEBHOOK_URL"))

bot = ezcord.Bot(language="en", error_webhook_url=webhookurl)

@bot.message_command(
    # This command can be used by guild members, but also by users anywhere if they install it
    integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    },
   name="Bookmark Message"
)
async def bookmark(
    ctx,
    message: discord.Message
):
    # Emojis used are MDI icons
    await ctx.respond(f"🔖 Bookmarked!", ephemeral=True)
    embed = discord.Embed(title="<:mdibookmark:1311457777834528768> Bookmark", description=f"{message.content}", timestamp=message.created_at, color=discord.Colour.random())
    embed.add_field(name="<:mdiaccount:1311490376091045989> Author", value=f"<@{message.author.id}>", inline=True)
    embed.add_field(name="<:mdilinkvariant:1311490590747267082> Link", value=f"{message.jump_url}", inline=True)
    embed.add_field(name="<:mdicodetags:1311506780332752977> ID", value=f"`{message.id}`", inline=True)
    embed.set_thumbnail(url=f"{message.author.avatar.url}")
    await ctx.user.send(embed=embed)
    # Gets the links of any attachments and sends them after the embed
    for i in message.attachments:
        await ctx.user.send(i)

class TagSet(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # Modal for tag input
        self.add_item(discord.ui.InputText(label=Tag(s)))
@bot.message_command(
    # This command can be used by guild members, but also by users anywhere if they install it
    integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    },
   name="Bookmark Message With Tag"
)
async def bookmark_tag(
    ctx,
    message: discord.Message
):
    
    modal = TagSet(title="Tag(s) to save with")
    await ctx.send_modal(modal)
    await modal.wait() # Wait for the modal to finish
    await ctx.respond(f"🔖 Bookmarked!", ephemeral=True)
    embed = discord.Embed(title="<:mdibookmark:1311457777834528768> Bookmark", description=f"{message.content}", timestamp=message.created_at, color=discord.Colour.random())
    embed.add_field(name="<:mdiaccount:1311490376091045989> Author", value=f"<@{message.author.id}>", inline=True)
    embed.add_field(name="<:mdilinkvariant:1311490590747267082> Link", value=f"{message.jump_url}", inline=True)
    embed.add_field(name="<:mdicodetags:1311506780332752977> ID", value=f"`{message.id}`", inline=True)
    embed.add_field(name="<:mditag:1311505882047189012> Tags", value=f"{modal.children[0].value}", inline=True)
    embed.set_thumbnail(url=f"{message.author.avatar.url}")
    await ctx.user.send(embed=embed)
    for i in message.attachments:
        await ctx.user.send(i)


if __name__ == "__main__":
    bot.run(str(os.getenv('TOKEN'))) # run the bot with the token
