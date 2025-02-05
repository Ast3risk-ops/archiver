import ezcord
import discord
import os
from datetime import datetime as dt
from dotenv import load_dotenv

load_dotenv()

website = (
    "https://caltrop.asterisk.lol"  # Will save a lot of time if the domain changes
)

embed = None
numembeds = 0
numfiles = 0

webhookurl = str(os.getenv("WEBHOOK_URL"))
intents = discord.Intents.default()
bot = ezcord.Bot(
    language="en", error_webhook_url=webhookurl, intents=intents, ready_event=None
)


@bot.event
async def on_ready():
    activity = discord.CustomActivity(name="🗃️ Archiving your messages")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    bot.add_view(DeleteBookmark())
    bot.ready(
        style=ezcord.ReadyEvent.default,
    )


class TagSet(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(timeout=None, *args, **kwargs)
        # Modal for tag input
        self.add_item(discord.ui.InputText(label="", required=False))

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()


class ColourModal(discord.ui.Modal):
    def __init__(self):
        super().__init__(title="Customizer")
        self.add_item(
            discord.ui.InputText(
                label="Colour (hex code)", placeholder="#FF5733", required=True
            )
        )

    async def callback(self, interaction: discord.Interaction):
        color_input = self.children[0].value

        # Validate the color input
        if not color_input.startswith("#") or len(color_input) != 7:
            await interaction.response.send_message(
                "Please enter a valid hex code (e.g., `#FF5733`).", ephemeral=True
            )

        # Update the global embed color
        global embed
        embed.color = int(color_input[1:], 16)

        # Edit the original message with the updated embed
        await interaction.response.edit_message(embed=embed)


class DeleteBookmark(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="", custom_id="delete", style=discord.ButtonStyle.secondary, emoji="🗑️"
    )
    async def button_callback(self, button, interaction):
        await interaction.response.defer()
        self.disable_all_items()
        await interaction.message.delete()
        global numembeds
        global numfiles
        if numembeds or numfiles != 0:
            channel = interaction.channel
            to_delete = int(numembeds + numfiles)
            messages = await channel.history(
                limit=to_delete, after=interaction.message.created_at
            ).flatten()
            for i in messages:
                await i.delete()

    @discord.ui.button(
        label="", custom_id="pin", style=discord.ButtonStyle.secondary, emoji="📌"
    )
    async def pin_callback(self, button, interaction):
        await interaction.message.pin()
        await interaction.response.defer()

    @discord.ui.button(
        label="",
        custom_id="move_to_bottom",
        style=discord.ButtonStyle.secondary,
        emoji="🔽",
    )
    async def button2_callback(self, button, interaction):
        for i in interaction.message.embeds:
            i.set_footer(
                text="🔼 Go back to the original message to view attachments and embeds."
            )
            await interaction.response.send_message(embed=i, view=DeleteBookmark())

    @discord.ui.button(
        label="", custom_id="customize", style=discord.ButtonStyle.secondary, emoji="🎨"
    )
    async def customizer(self, button, interaction):
        await interaction.response.send_modal(ColourModal())


class About(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        SiteButton = discord.ui.Button(
            label="Website",
            style=discord.ButtonStyle.url,
            url="https://archiver.asterisk.lol",
        )
        self.add_item(SiteButton)
        CodeButton = discord.ui.Button(
            label="Source Code",
            style=discord.ButtonStyle.url,
            url="https://github.com/Ast3risk-ops/archiver",
        )
        self.add_item(CodeButton)


@bot.slash_command(
    # This command can be used by guild members, but also by users anywhere if they install it
    integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    },
    name="help",
    description="How to use the bot",
)
async def help(ctx):
    context_img = discord.File("context.png", filename="context.png")
    embed = discord.Embed(
        title="Using Archiver",
        description="To use Archiver, simply right click or hold down on a message and go to **Apps > Archive Message**.",
        color=discord.Colour.from_rgb(255, 255, 255),
    )
    embed.set_image(url="attachment://context.png")
    await ctx.respond(embed=embed, file=context_img, ephemeral=True)


@bot.slash_command(
    # This command can be used by guild members, but also by users anywhere if they install it
    integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    },
    name="about",
    description="Links and stuff",
)
async def about(ctx):
    embed = discord.Embed(
        title="About",
        description=f"[**Archiver**]({website}) is a bot to archive Discord messages, developed by [**Asterisk**](https://asterisk.lol).",
        color=discord.Colour.from_rgb(255, 255, 255),
    )
    await ctx.respond(embed=embed, view=About(), ephemeral=True)


@bot.message_command(
    # This command can be used by guild members, but also by users anywhere if they install it
    integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    },
    name="Archive Message",
)
async def bookmark_tag(ctx, message: discord.Message):
    modal = TagSet(title="Message Tag(s)")
    await ctx.send_modal(modal)
    await modal.wait()  # Wait for the modal to be submitted before archiving
    reactionlist = []  # Empty list of reactions to use later
    for i in message.reactions:
        count = i.count  # Number of times reacted
        formatted_emoji = str(i.emoji)
        reactionlist.append(f"{count}x {formatted_emoji} ")
    global embed
    if message.content:
        embed = discord.Embed(
            title=f"<:mdiarchive:1311542586745294868> Archived Message On {discord.utils.format_dt(dt.now(), 'f')} ({discord.utils.format_dt(dt.now(), 'R')})",
            description=f"-------\n\n{message.content}\n\n--------",
            color=discord.Colour.random(),
        )
    else:
        embed = discord.Embed(
            title=f"<:mdiarchive:1311542586745294868> Archived Message On {discord.utils.format_dt(dt.now(), 'f')} ({discord.utils.format_dt(dt.now(), 'R')})",
            color=discord.Colour.random(),
        )
    if message.poll:
        embed.description = f"\n**<:mdigraphbar:1316204402025173042> Poll**\n-------\n<:mdichatquestion:1316204302364315659> {message.poll.question.text}\n\n"
        answertext = []
        for i in message.poll.answers:
            answerf = f"{i.id}. [{i.emoji}] {i.text} \n"
            answertext.append(answerf)
        embed.add_field(name="", value="".join(answertext), inline=False)
    embed.add_field(name="\n\n", value=", ".join(reactionlist), inline=False)
    embed.add_field(
        name="<:mdiaccount:1311490376091045989> Author",
        value=f"`{message.author.name}` (<@{message.author.id}>)",
        inline=True,
    )
    embed.add_field(
        name="<:mdilinkvariant:1311490590747267082> Link",
        value=f"{message.jump_url}",
        inline=True,
    )
    embed.add_field(
        name="<:mdicodetags:1311506780332752977> ID",
        value=f"{message.id}",
        inline=True,
    )
    if message.guild:
        embed.add_field(
            name="<:mdichesscastle:1314056466516283413> Guild",
            value=f"{message.guild.id}",
            inline=True,
        )
    else:
        embed.add_field(
            name="<:mdichesscastle:1314056466516283413> Guild", value=f"DM", inline=True
        )
    if message.embeds:
        global numembeds
        numembeds = len(message.embeds)  # Number of embeds
        embed.add_field(
            name="<:mdicardtext:1311825458480021596> Embeds",
            value=f"{numembeds}",
            inline=True,
        )
    if message.attachments:
        global numfiles
        numfiles = len(message.attachments)
        embed.add_field(
            name="<:mdifiledownload:1322695880637284514> Attachments",
            value=f"{numfiles}",
            inline=True,
        )
    embed.add_field(
        name="<:mdicalendar:1311544097240121384> Send Date",
        value=f"{discord.utils.format_dt(message.created_at, 'F')}",
        inline=True,
    )
    if modal.children[0].value:
        embed.add_field(
            name="<:mditag:1311505882047189012> Tags",
            value=f"{modal.children[0].value}",
            inline=True,
        )
    embed.set_thumbnail(url=ezcord.utils.avatar(f"{message.author.id}"))
    try:
        await ctx.user.send(embed=embed, view=DeleteBookmark())
    except discord.Forbidden:
        await ctx.respond(
            "☹️ I can't DM you! Please enable DMs for this server or [install me as a user app](<https://discord.com/oauth2/authorize?client_id=1311438512045949029&integration_type=1&scope=applications.commands>) and try again.",
            ephemeral=True,
        )
    except discord.HTTPException:
        await ctx.respond(
            "☹️ I can't DM you! (Unknown HTTP exception, please contact my developer if the issue persists)",
            ephemeral=True,
        )
    else:
        for i in message.attachments:
            path = f"./{i.filename}"
            await i.save(path)
            await ctx.user.send(file=discord.File(path))
            os.remove(path)
        if message.stickers:
            stickers = []
            for i in message.stickers:
                format = f"[{i.name}]({i.url})"
                stickers.append(format)
                await ctx.user.send(" ".join(stickers))
        if message.embeds:
            for i in message.embeds:
                await ctx.user.send(embed=i)


if __name__ == "__main__":
    bot.run(str(os.getenv("TOKEN")))  # run the bot with the token
