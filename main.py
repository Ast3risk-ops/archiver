import ezcord
import discord
from discord.ext import tasks
import platform
import importlib.metadata
import os
from datetime import datetime as dt
from dotenv import load_dotenv
import aiohttp

load_dotenv()

website = (
    "https://caltrop.asterisk.lol"  # Will save a lot of time if the domain changes
)

embed = None
numembeds = 0
numfiles = 0

webhookurl = str(os.getenv("WEBHOOK_URL"))
topggtoken = str(os.getenv("TOPDOTGG_TOKEN"))
deltoken = str(os.getenv("DEL_TOKEN"))
intents = discord.Intents.default()
bot = ezcord.Bot(
    language="en", error_webhook_url=webhookurl, intents=intents, ready_event=None
)


def human_readable_size(size_in_bytes):
    """Convert bytes to a human-readable format."""
    if size_in_bytes < 1024:
        return f"{size_in_bytes} Bytes"
    elif size_in_bytes < 1024**2:
        return f"{size_in_bytes / 1024:.2f} KB"
    elif size_in_bytes < 1024**3:
        return f"{size_in_bytes / (1024 ** 2):.2f} MB"
    else:
        return f"{size_in_bytes / (1024 ** 3):.2f} GB"


def is_valid_hex_colour(colour):
    """Is this a hex code?"""
    return len(colour) == 7 and colour.startswith("#")


colour_list = {
    # Hex codes for all CSS named colours.
    "aliceblue": 0xF0F8FF,
    "antiquewhite": 0xFAEBD7,
    "aqua": 0x00FFFF,
    "aquamarine": 0x7FFFD4,
    "azure": 0xF0FFFF,
    "beige": 0xF5F5DC,
    "bisque": 0xFFE4C4,
    "black": 0x000000,
    "blanchedalmond": 0xFFEBCD,
    "blue": 0x0000FF,
    "blueviolet": 0x8A2BE2,
    "brown": 0xA52A2A,
    "burlywood": 0xDEB887,
    "cadetblue": 0x5F9EA0,
    "chartreuse": 0x7FFF00,
    "chocolate": 0xD2691E,
    "coral": 0xFF7F50,
    "cornflowerblue": 0x6495ED,
    "cornsilk": 0xFFF8DC,
    "crimson": 0xDC143C,
    "cyan": 0x00FFFF,
    "darkblue": 0x00008B,
    "darkcyan": 0x008B8B,
    "darkgoldenrod": 0xB8860B,
    "darkgrey": 0xA9A9A9,
    "darkgray": 0xA9A9A9,
    "darkgreen": 0x006400,
    "darkkhaki": 0xBDB76B,
    "darkmagenta": 0x8B008B,
    "darkolivegreen": 0x556B2F,
    "darkorange": 0xFF8C00,
    "darkorchid": 0x9932CC,
    "darkred": 0x8B0000,
    "darksalmon": 0xE9967A,
    "darkseagreen": 0x8FBC8F,
    "darkslateblue": 0x483D8B,
    "darkslategrey": 0x2F4F4F,
    "darkslategray": 0x2F4F4F,
    "darkturquoise": 0x00CED1,
    "darkviolet": 0x9400D3,
    "deeppink": 0xFF1493,
    "deepskyblue": 0x00BFFF,
    "dimgrey": 0x696969,
    "dimgray": 0x696969,
    "dodgerblue": 0x1E90FF,
    "firebrick": 0xB22222,
    "floralwhite": 0xFFFAF0,
    "forestgreen": 0x228B22,
    "fuchsia": 0xFF00FF,
    "gainsboro": 0xDCDCDC,
    "ghostwhite": 0xF8F8FF,
    "gold": 0xFFD700,
    "goldenrod": 0xDAA520,
    "gray": 0x808080,
    "grey": 0x808080,
    "green": 0x008000,
    "greenyellow": 0xADFF2F,
    "honeydew": 0xF0FFF0,
    "hotpink": 0xFF69B4,
    "indianred": 0xCD5C5C,
    "indigo": 0x4B0082,
    "ivory": 0xFFFFF0,
    "khaki": 0xF0E68C,
    "lavender": 0xE6E6FA,
    "lavenderblush": 0xFFF0F5,
    "lawngreen": 0x7CFC00,
    "lemonchiffon": 0xFFFACD,
    "lightblue": 0xADD8E6,
    "lightcoral": 0xF08080,
    "lightcyan": 0xE0FFFF,
    "lightgoldenrodyellow": 0xFAFAD2,
    "lightgrey": 0xD3D3D3,
    "lightgray": 0xD3D3D3,
    "lightgreen": 0x90EE90,
    "lightpink": 0xFFB6C1,
    "lightsalmon": 0xFFA07A,
    "lightseagreen": 0x20B2AA,
    "lightskyblue": 0x87CEFA,
    "lightslategrey": 0x778899,
    "lightslategray": 0x778899,
    "lightsteelblue": 0xB0C4DE,
    "lightyellow": 0xFFFFE0,
    "lime": 0x00FF00,
    "limegreen": 0x32CD32,
    "linen": 0xFAF0E6,
    "magenta": 0xFF00FF,
    "maroon": 0x800000,
    "mediumaquamarine": 0x66CDAA,
    "mediumblue": 0x0000CD,
    "mediumorchid": 0xBA55D3,
    "mediumpurple": 0x9370DB,
    "mediumseagreen": 0x3CB371,
    "mediumslateblue": 0x7B68EE,
    "mediumspringgreen": 0x00FA9A,
    "mediumturquoise": 0x48D1CC,
    "mediumvioletred": 0xC71585,
    "midnightblue": 0x191970,
    "mintcream": 0xF5FFFA,
    "mistyrose": 0xFFE4E1,
    "moccasin": 0xFFE4B5,
    "navajowhite": 0xFFDEAD,
    "navy": 0x000080,
    "oldlace": 0xFDF5E6,
    "olive": 0x808000,
    "olivedrab": 0x6B8E23,
    "orange": 0xFFA500,
    "orangered": 0xFF4500,
    "orchid": 0xDA70D6,
    "palegoldenrod": 0xEEE8AA,
    "palegreen": 0x98FB98,
    "paleturquoise": 0xAFEEEE,
    "palevioletred": 0xDB7093,
    "papayawhip": 0xFFEFD5,
    "peachpuff": 0xFFDAB9,
    "peru": 0xCD853F,
    "pink": 0xFFC0CB,
    "plum": 0xDDA0DD,
    "powderblue": 0xB0E0E6,
    "purple": 0x800080,
    "red": 0xFF0000,
    "rosybrown": 0xBC8F8F,
    "royalblue": 0x4169E1,
    "saddlebrown": 0x8B4513,
    "salmon": 0xFA8072,
    "sandybrown": 0xF4A460,
    "seagreen": 0x2E8B57,
    "seashell": 0xFFF5EE,
    "sienna": 0xA0522D,
    "silver": 0xC0C0C0,
    "skyblue": 0x87CEEB,
    "slateblue": 0x6A5ACD,
    "slategrey": 0x708090,
    "slategray": 0x708090,
    "snow": 0xFFFAFA,
    "springgreen": 0x00FF7F,
    "steelblue": 0x4682B4,
    "tan": 0xD2B48C,
    "teal": 0x008080,
    "thistle": 0xD8BFD8,
    "tomato": 0xFF6347,
    "turquoise": 0x40E0D0,
    "violet": 0xEE82EE,
    "wheat": 0xF5DEB3,
    "white": 0xFFFFFF,
    "whitesmoke": 0xF5F5F5,
    "yellow": 0xFFFF00,
    "yellowgreen": 0x9ACD32,
}


@tasks.loop(hours=1)
async def periodic_update():
    await update_server_count()
    await update_server_count_2()


@bot.event
async def on_ready():
    activity = discord.CustomActivity(name="🗃️ Archiving messages")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    bot.add_view(DeleteBookmark())
    bot.ready(
        style=ezcord.ReadyEvent.default,
    )
    await update_server_count()
    await update_server_count_2()
    periodic_update.start()


async def update_server_count():
    # Get the number of servers the bot is in
    server_count = int(len(bot.guilds))
    global topggtoken
    # Prepare the headers and data for the POST request
    headers = {"Authorization": topggtoken, "Content-Type": "application/json"}
    data = {"server_count": server_count}
    async with aiohttp.ClientSession() as session:
        async with session.post(
            f"https://top.gg/api/bots/1311438512045949029/stats",
            headers=headers,
            json=data,
        ) as response:
            if response.status != 200:
                print(
                    f"Failed to update server count (Top.gg): {response.status} - {await response.text()}"
                )


async def update_server_count_2():
    # Get the number of servers the bot is in
    server_count2 = int(len(bot.guilds))
    global deltoken
    # Prepare the headers and data for the POST request
    headers = {"Authorization": deltoken, "Content-Type": "application/json"}
    data = {"guildCount": server_count2}
    async with aiohttp.ClientSession() as session:
        async with session.post(
            f"https://api.discordextremelist.xyz/v2/bot/1311438512045949029/stats",
            headers=headers,
            json=data,
        ) as response:
            if response.status != 200:
                print(
                    f"Failed to update server count (DEL): {response.status} - {await response.text()}"
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
                label="Embed Colour",
                placeholder="Colour name (lightgreen) or hex code (#90ee90)",
                required=True,
            )
        )

    async def callback(self, interaction: discord.Interaction):
        colour_input = self.children[0].value.strip()
        if is_valid_hex_colour(colour_input):
            colour = int(colour_input[1:], 16)  # Convert hex to int
        else:
            # Check if the input is a named color
            colour = colour_list.get(colour_input.lower())
            if colour is None:
                # Send an error message if the colour is invalid
                await interaction.response.send_message(
                    content=f"⛔ `{colour_input}` is not a valid colour! (try its hex code instead?)\n\nConsult the list of [CSS named colours](<https://www.w3.org/TR/css-color-4/#named-colors>) if you don't know the name of your colour.",
                    ephemeral=True,
                )
                return  # Exit the callback

        # Update the global embed color
        embed = interaction.message.embeds[0].copy()
        embed.color = colour

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
        label="", custom_id="edit_tag", style=discord.ButtonStyle.secondary, emoji="✏️"
    )
    async def edit_tag_callback(self, button, interaction):
        await interaction.response.send_modal(EditTagModal())

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


class EditTagModal(discord.ui.Modal):
    def __init__(self):
        super().__init__(title="Edit Tag(s)")
        self.add_item(
            discord.ui.InputText(
                label="",
                placeholder="Enter new tag(s), leave this empty to remove all tags",
                required=False,
            )
        )

    async def callback(self, interaction: discord.Interaction):
        embed = interaction.message.embeds[0].copy()
        new_tag = self.children[0].value.strip()
        fields = []
        tag_found = False
        for field in embed.fields:
            if field.name == "<:mditag:1311505882047189012> Tags":
                tag_found = True
                if new_tag:
                    fields.append(
                        discord.EmbedField(
                            name="<:mditag:1311505882047189012> Tags",
                            value=new_tag,
                            inline=True,
                        )
                    )
                # If new_tag is empty, skip adding this field (removes it)
            else:
                fields.append(field)
        # If no tag field was found and new_tag is not empty, add it
        if not tag_found and new_tag:
            fields.append(
                discord.EmbedField(
                    name="<:mditag:1311505882047189012> Tags",
                    value=new_tag,
                    inline=True,
                )
            )
        embed.clear_fields()
        for field in fields:
            embed.add_field(name=field.name, value=field.value, inline=field.inline)
        await interaction.response.edit_message(embed=embed, view=DeleteBookmark())


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
    app_info = await bot.application_info()
    owner = app_info.owner
    if hasattr(owner, "members"):  # It's a Team
        member_names = ", ".join([str(member) for member in owner.members])
        managed_by = f"\n\nThis instance is managed by {member_names}"
    else:
        managed_by = f"\n\nThis instance is managed by <@{owner.id}>"
    embed = discord.Embed(
        title="About",
        description=f"[**Archiver**]({website}) is a bot to archive Discord messages, developed by [**Asterisk**](https://asterisk.lol).{managed_by}",
        color=discord.Colour.from_rgb(255, 255, 255),
    )
    python_version = platform.python_version()
    try:
        pycord_version = importlib.metadata.version("py-cord")
    except importlib.metadata.PackageNotFoundError:
        pycord_version = "?"
    try:
        ezcord_version = importlib.metadata.version("ezcord")
    except importlib.metadata.PackageNotFoundError:
        ezcord_version = "?"
    embed.set_thumbnail(url=ezcord.utils.avatar(f"{bot.application_id}"))
    embed.add_field(
        name="<:mdichesscastle:1314056466516283413> Servers",
        value=int(len(bot.guilds)),
        inline=True,
    )
    embed.add_field(
        name="<:mdiaccount:1311490376091045989> Users", value="?", inline=True
    )
    embed.add_field(
        name="<:mdiserver:1383097147288846356> Host",
        value=f"{platform.system()} {platform.release()}",
        inline=True,
    )
    embed.add_field(
        name="<:mdilanguagepython:1383097357884854433> Python",
        value=python_version,
        inline=True,
    )
    embed.add_field(
        name="<:mdibookshelf:1383097558112669716> Libraries",
        value=f"[Pycord](https://pycord.dev) {pycord_version} w/ [ezcord](https://ezcord.rtfd.io) {ezcord_version}",
        inline=True,
    )
    await ctx.respond(embed=embed, view=About(), ephemeral=True)


@bot.slash_command(
    integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    },
    name="ping",
    description="Pong! Check Discord API latency",
)
async def ping(ctx):
    await ctx.respond(
        f"🏓 Pong! Discord API latency is **{round(bot.latency * 1000)}ms**",
        ephemeral=True,
    )


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
            name="<:mdichesscastle:1314056466516283413> Guild", value="DM", inline=True
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
            f"☹️ I can't DM you! Please enable DMs for this server or [install me as a user app](<https://discord.com/oauth2/authorize?client_id={bot.application_id}&integration_type=1&scope=applications.commands>) and try again.",
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
            try:
                await ctx.user.send(file=discord.File(path))
            except discord.HTTPException as e:
                if e.status == 413:
                    filesize = human_readable_size(i.size)
                    await ctx.respond(
                        content=f"<@{ctx.user.id}> ⚠️ Attachment `{i.filename}` is too large to re-upload ({filesize}). The URL for this attachment will be saved instead (this expires).",
                        ephemeral=True,
                    )
                    await ctx.user.send(content=i.url)
                    os.remove(path)
                else:
                    await ctx.respond(
                        content=f"<@{ctx.user.id}> ⛔ Error while re-uploading attachment `{i.filename}`: \n\n```\n{e}\n```",
                        ephemeral=True,
                    )
                    os.remove(path)
            else:
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
