import ezcord
import discord
import os
from datetime import datetime as dt
from dotenv import load_dotenv
load_dotenv()

webhookurl = str(os.getenv("WEBHOOK_URL"))
intents = discord.Intents.default()
bot = ezcord.Bot(language="en", error_webhook_url=webhookurl, intents=intents)

class TagSet(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # Modal for tag input
        self.add_item(discord.ui.InputText(label="", required=False))
class DeleteBookmark(discord.ui.View):
    @discord.ui.button(label="", style=discord.ButtonStyle.secondary, emoji="🗑️")
    async def button_callback(self, button, interaction):
        self.disable_all_items()
        await interaction.message.delete()
    @discord.ui.button(label="", style=discord.ButtonStyle.secondary, emoji="📌")
    async def pin_callback(self, button, interaction):
        await interaction.message.pin()
    @discord.ui.button(label="", style=discord.ButtonStyle.secondary, emoji="⬇️")
    async def button2_callback(self, button, interaction):
        for i in interaction.message.embeds:
            i.set_footer(text="Go back to the original message to view attachments and embeds.")
            await interaction.message.reply(embed=i, view=DeleteBookmark())
        for i in interaction.message.attachments:
            await interaction.message.reply(i)
@bot.message_command(
    # This command can be used by guild members, but also by users anywhere if they install it
    integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    },
   name="Archive Message"
)
async def bookmark_tag(
    ctx,
    message: discord.Message
):
    modal = TagSet(title="Message Tag(s)")
    await ctx.send_modal(modal)
    await modal.wait() # Wait for the modal to be submitted before archiving
    reactionlist = [] # Empty list of reactions to use later
    for i in message.reactions:
        count = i.count # Number of times reacted
        formatted_emoji = str(i.emoji)
        reactionlist.append(f"{count}x {formatted_emoji} ")
    embed = discord.Embed(title=f"<:mdiarchive:1311542586745294868> Archived Message On {discord.utils.format_dt(dt.now(), 'f')} ({discord.utils.format_dt(dt.now(), 'R')})", description=f"{message.content}", color=discord.Colour.random())
    embed.add_field(name="\n", value=", ".join(reactionlist), inline=False)
    embed.add_field(name="<:mdiaccount:1311490376091045989> Author", value=f"<@{message.author.id}>", inline=True)
    embed.add_field(name="<:mdilinkvariant:1311490590747267082> Link", value=f"{message.jump_url}", inline=True)
    embed.add_field(name="<:mdicodetags:1311506780332752977> ID", value=f"`{message.id}`", inline=True)
    if message.embeds:
        numembeds = len(message.embeds) # Number of embeds
        embed.add_field(name="<:mdicardtext:1311825458480021596> Embeds", value=f"{numembeds}", inline=True)
    embed.add_field(name="<:mditag:1311505882047189012> Tags", value=f"{modal.children[0].value}", inline=True)
    embed.add_field(name="<:mdicalendar:1311544097240121384> Send Date", value=f"{discord.utils.format_dt(message.created_at, 'F')}", inline=False)
    embed.set_thumbnail(url=f"{message.author.avatar.url}")
    await ctx.user.send(embed=embed, view=DeleteBookmark())
    for i in message.attachments:
        await ctx.user.send(i)
    if message.embeds:
        for i in message.embeds:
            await ctx.user.send(embed=i)


if __name__ == "__main__":
    bot.run(str(os.getenv('TOKEN'))) # run the bot with the token
