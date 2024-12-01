import ezcord
import discord
import os
from datetime import datetime as dt
from dotenv import load_dotenv
load_dotenv()

website = "https://caltrop.asterisk.lol" # Will save a lot of time if the domain changes

embed = None

webhookurl = str(os.getenv("WEBHOOK_URL"))
intents = discord.Intents.default()
bot = ezcord.Bot(language="en", error_webhook_url=webhookurl, intents=intents)

class TagSet(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(title="Message Tag(s)")
        # Modal for tag input
        self.add_item(discord.ui.InputText(label="", required=False))
        return
class ColourModal(discord.ui.Modal):
    def __init__(self):
        super().__init__(title="Customizer")

        self.add_item(discord.ui.InputText(label="Colour (hex code)", placeholder="#FF5733", required=True))

    async def callback(self, interaction: discord.Interaction):
        color_input = self.children[0].value

        # Validate the color input
        if not color_input.startswith("#") or len(color_input) != 7:
            await interaction.response.send_message("Please enter a valid hex code (e.g., `#FF5733`).", ephemeral=True)
            return

        # Update the global embed color
        global embed
        embed.color = int(color_input[1:], 16)

        # Edit the original message with the updated embed
        await interaction.response.edit_message(embed=embed)
        return
class DeleteBookmark(discord.ui.View):
    @discord.ui.button(label="", style=discord.ButtonStyle.secondary, emoji="🗑️")
    async def button_callback(self, button, interaction):
        self.disable_all_items()
        await interaction.message.delete()
        return
    @discord.ui.button(label="", style=discord.ButtonStyle.secondary, emoji="📌")
    async def pin_callback(self, button, interaction):
        await interaction.message.pin()
        return
    @discord.ui.button(label="", style=discord.ButtonStyle.secondary, emoji="⬇️")
    async def button2_callback(self, button, interaction):
        for i in interaction.message.embeds:
            i.set_footer(text="Go back to the original message to view attachments and embeds.")
            await interaction.message.reply(embed=i, view=DeleteBookmark())
        for i in interaction.message.attachments:
            await interaction.message.reply(i)
        return
    @discord.ui.button(label="", style=discord.ButtonStyle.secondary, emoji="🎨")
    async def customizer(self, button, interaction):
        await interaction.response.send_modal(ColourModal())
        return
class About(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        SiteButton = discord.ui.Button(label='Website', style=discord.ButtonStyle.url, url='https://archiver.asterisk.lol')
        self.add_item(SiteButton)
        CodeButton = discord.ui.Button(label='Source Code', style=discord.ButtonStyle.url, url='https://github.com/Ast3risk-ops/archiver')
        self.add_item(CodeButton)

@bot.slash_command(
    # This command can be used by guild members, but also by users anywhere if they install it
    integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    },
   name="help",
   description="How to use the bot"
)
async def help(ctx):
    context_img = discord.File("context.png", filename="context.png")
    embed = discord.Embed(title="Using Archiver", description="To use Archiver, simply right click or hold down on a message and go to **Apps > Archive Message**.", color=discord.Colour.from_rgb(255, 255, 255))
    embed.set_image(url="attachment://context.png")
    await ctx.respond(embed=embed, file=context_img, ephemeral=True)

@bot.slash_command(
    # This command can be used by guild members, but also by users anywhere if they install it
    integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    },
   name="about",
   description="Links and stuff"
)
async def about(ctx):
    embed = discord.Embed(title="About", description=f"[**Archiver**]({website}) is a bot to archive Discord messages, developed by [**Asterisk**](https://asterisk.lol).", color=discord.Colour.from_rgb(255, 255, 255))
    await ctx.respond(embed=embed, view=About(), ephemeral=True)

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
    modal = TagSet()
    await ctx.send_modal(modal)
    await modal.wait() # Wait for the modal to be submitted before archiving
    reactionlist = [] # Empty list of reactions to use later
    for i in message.reactions:
        count = i.count # Number of times reacted
        formatted_emoji = str(i.emoji)
        reactionlist.append(f"{count}x {formatted_emoji} ")
    global embed
    embed = discord.Embed(title=f"📅 Archived Message On {discord.utils.format_dt(dt.now(), 'f')} ({discord.utils.format_dt(dt.now(), 'R')})", description=f"-------\n\n{message.content}\n\n--------", color=discord.Colour.random())
    embed.add_field(name="\n\n", value=", ".join(reactionlist), inline=False)
    embed.add_field(name="👤 Author", value=f"<@{message.author.id}>", inline=True)
    embed.add_field(name="🔗 Link", value=f"{message.jump_url}", inline=True)
    embed.add_field(name="🪪 ID", value=f"`{message.id}`", inline=True)
    if message.embeds:
        numembeds = len(message.embeds) # Number of embeds
        embed.add_field(name="🔲 Embeds", value=f"{numembeds}", inline=True)
    embed.add_field(name="📅 Send Date", value=f"{discord.utils.format_dt(message.created_at, 'F')}", inline=True)
    embed.add_field(name="🔖 Tags", value=f"{modal.children[0].value}", inline=True)
    if message.author.avatar:
        embed.set_thumbnail(url=f"{message.author.avatar.url}")
    await ctx.user.send(embed=embed, view=DeleteBookmark())
    for i in message.attachments:
        await ctx.user.send(i)
    if message.stickers:
        stickers = []
        for i in message.stickers:
            format = f'[{i.name}]({i.url})'
            stickers.append(format)
            await ctx.user.send(' '.join(stickers))
    if message.embeds:
        for i in message.embeds:
            await ctx.user.send(embed=i)


if __name__ == "__main__":
    bot.run(str(os.getenv('TOKEN'))) # run the bot with the token
