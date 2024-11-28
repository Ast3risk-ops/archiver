import ezcord
import discord
import os
from dotenv import load_dotenv
load_dotenv()

webhookurl = str(os.getenv("WEBHOOK_URL"))

bot = ezcord.Bot(language="en", error_webhook_url=webhookurl)

class TagSet(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        # Modal for tag input
        self.add_item(discord.ui.InputText(label="", required=False))
class DeleteBookmark(discord.ui.View):
    @discord.ui.button(label="", style=discord.ButtonStyle.secondary, emoji="🗑️")
    async def button_callback(self, button, interaction):
        await self.message.delete()
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
    await modal.wait() # Wait for the modal to finish
    embed = discord.Embed(title="<:mdiarchive:1311542586745294868> Archived Message", description=f"{message.content}", timestamp=message.created_at, color=discord.Colour.random())
    embed.add_field(name="<:mdiaccount:1311490376091045989> Author", value=f"<@{message.author.id}>", inline=True)
    embed.add_field(name="<:mdilinkvariant:1311490590747267082> Link", value=f"{message.jump_url}", inline=True)
    embed.add_field(name="<:mdicodetags:1311506780332752977> ID", value=f"`{message.id}`", inline=True)
    embed.add_field(name="<:mditag:1311505882047189012> Tags", value=f"{modal.children[0].value}", inline=True)
    embed.add_field(name="<:mdicalendar:1311544097240121384> Send Date", value="", inline=False)
    embed.set_thumbnail(url=f"{message.author.avatar.url}")
    await ctx.user.send(embed=embed, view=DeleteBookmark())
    for i in message.attachments:
        await ctx.user.send(i)


if __name__ == "__main__":
    bot.run(str(os.getenv('TOKEN'))) # run the bot with the token
