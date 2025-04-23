import ezcord
import discord
import os
from datetime import datetime as dt
from dotenv import load_dotenv

load_dotenv()

website = (
    "https://caltrop.asterisk.lol"  # Will save a lot of time if the domain changes
)

numembeds = 0
numfiles = 0
embed = None

webhookurl = str(os.getenv("WEBHOOK_URL"))
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
    return len(colour) == 7 and colour.startswith('#')


colour_list = {
  # Hex codes for all CSS named colours.
  "aliceblue": 0xf0f8ff,
  "antiquewhite": 0xfaebd7,
  "aqua": 0x00ffff,
  "aquamarine": 0x7fffd4,
  "azure": 0xf0ffff,
  "beige": 0xf5f5dc,
  "bisque": 0xffe4c4,
  "black": 0x000000,
  "blanchedalmond": 0xffebcd,
  "blue": 0x0000ff,
  "blueviolet": 0x8a2be2,
  "brown": 0xa52a2a,
  "burlywood": 0xdeb887,
  "cadetblue": 0x5f9ea0,
  "chartreuse": 0x7fff00,
  "chocolate": 0xd2691e,
  "coral": 0xff7f50,
  "cornflowerblue": 0x6495ed,
  "cornsilk": 0xfff8dc,
  "crimson": 0xdc143c,
  "cyan": 0x00ffff,
  "darkblue": 0x00008b,
  "darkcyan": 0x008b8b,
  "darkgoldenrod": 0xb8860b,
  "darkgrey": 0xa9a9a9,
  "darkgray": 0xa9a9a9,
  "darkgreen": 0x006400,
  "darkkhaki": 0xbdb76b,
  "darkmagenta": 0x8b008b,
  "darkolivegreen": 0x556b2f,
  "darkorange": 0xff8c00,
  "darkorchid": 0x9932cc,
  "darkred": 0x8b0000,
  "darksalmon": 0xe9967a,
  "darkseagreen": 0x8fbc8f,
  "darkslateblue": 0x483d8b,
  "darkslategrey": 0x2f4f4f,
  "darkslategray": 0x2f4f4f,
  "darkturquoise": 0x00ced1,
  "darkviolet": 0x9400d3,
  "deeppink": 0xff1493,
  "deepskyblue": 0x00bfff,
  "dimgrey": 0x696969,
  "dimgray": 0x696969,
  "dodgerblue": 0x1e90ff,
  "firebrick": 0xb22222,
  "floralwhite": 0xfffaf0,
  "forestgreen": 0x228b22,
  "fuchsia": 0xff00ff,
  "gainsboro": 0xdcdcdc,
  "ghostwhite": 0xf8f8ff,
  "gold": 0xffd700,
  "goldenrod": 0xdaa520,
  "gray": 0x808080,
  "grey": 0x808080,
  "green": 0x008000,
  "greenyellow": 0xadff2f,
  "honeydew": 0xf0fff0,
  "hotpink": 0xff69b4,
  "indianred": 0xcd5c5c,
  "indigo": 0x4b0082,
  "ivory": 0xfffff0,
  "khaki": 0xf0e68c,
  "lavender": 0xe6e6fa,
  "lavenderblush": 0xfff0f5,
  "lawngreen": 0x7cfc00,
  "lemonchiffon": 0xfffacd,
  "lightblue": 0xadd8e6,
  "lightcoral": 0xf08080,
  "lightcyan": 0xe0ffff,
  "lightgoldenrodyellow": 0xfafad2,
  "lightgrey": 0xd3d3d3,
  "lightgray": 0xd3d3d3,
  "lightgreen": 0x90ee90,
  "lightpink": 0xffb6c1,
  "lightsalmon": 0xffa07a,
  "lightseagreen": 0x20b2aa,
  "lightskyblue": 0x87cefa,
  "lightslategrey": 0x778899,
  "lightslategray": 0x778899,
  "lightsteelblue": 0xb0c4de,
  "lightyellow": 0xffffe0,
  "lime": 0x00ff00,
  "limegreen": 0x32cd32,
  "linen": 0xfaf0e6,
  "magenta": 0xff00ff,
  "maroon": 0x800000,
  "mediumaquamarine": 0x66cdaa,
  "mediumblue": 0x0000cd,
  "mediumorchid": 0xba55d3,
  "mediumpurple": 0x9370db,
  "mediumseagreen": 0x3cb371,
  "mediumslateblue": 0x7b68ee,
  "mediumspringgreen": 0x00fa9a,
  "mediumturquoise": 0x48d1cc,
  "mediumvioletred": 0xc71585,
  "midnightblue": 0x191970,
  "mintcream": 0xf5fffa,
  "mistyrose": 0xffe4e1,
  "moccasin": 0xffe4b5,
  "navajowhite": 0xffdead,
  "navy": 0x000080,
  "oldlace": 0xfdf5e6,
  "olive": 0x808000,
  "olivedrab": 0x6b8e23,
  "orange": 0xffa500,
  "orangered": 0xff4500,
  "orchid": 0xda70d6,
  "palegoldenrod": 0xeee8aa,
  "palegreen": 0x98fb98,
  "paleturquoise": 0xafeeee,
  "palevioletred": 0xdb7093,
  "papayawhip": 0xffefd5,
  "peachpuff": 0xffdab9,
  "peru": 0xcd853f,
  "pink": 0xffc0cb,
  "plum": 0xdda0dd,
  "powderblue": 0xb0e0e6,
  "purple": 0x800080,
  "red": 0xff0000,
  "rosybrown": 0xbc8f8f,
  "royalblue": 0x4169e1,
  "saddlebrown": 0x8b4513,
  "salmon": 0xfa8072,
  "sandybrown": 0xf4a460,
  "seagreen": 0x2e8b57,
  "seashell": 0xfff5ee,
  "sienna": 0xa0522d,
  "silver": 0xc0c0c0,
  "skyblue": 0x87ceeb,
  "slateblue": 0x6a5acd,
  "slategrey": 0x708090,
  "slategray": 0x708090,
  "snow": 0xfffafa,
  "springgreen": 0x00ff7f,
  "steelblue": 0x4682b4,
  "tan": 0xd2b48c,
  "teal": 0x008080,
  "thistle": 0xd8bfd8,
  "tomato": 0xff6347,
  "turquoise": 0x40e0d0,
  "violet": 0xee82ee,
  "wheat": 0xf5deb3,
  "white": 0xffffff,
  "whitesmoke": 0xf5f5f5,
  "yellow": 0xffff00,
  "yellowgreen": 0x9acd32
}

@bot.event
async def on_ready():
    activity = discord.CustomActivity(name="🗃️ Archiving messages")
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
                label="Embed Colour", placeholder="Colour name (white) or hex code (#FFFFFF)", required=True
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
                    ephemeral=True
                )
                return  # Exit the callback

        # Update the global embed color
        global embed
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
        global embed
        embed = interaction.message.embeds[0].copy()
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
            title=f"🗃️ Archived Message On {discord.utils.format_dt(dt.now(), 'f')} ({discord.utils.format_dt(dt.now(), 'R')})",
            description=f"-------\n\n{message.content}\n\n--------",
            color=discord.Colour.random(),
        )
    else:
        embed = discord.Embed(
            title=f"🗃️ Archived Message On {discord.utils.format_dt(dt.now(), 'f')} ({discord.utils.format_dt(dt.now(), 'R')})",
            color=discord.Colour.random(),
        )
    if message.poll:
        embed.description = (
            f"\n**📊 Poll**\n-------\n❓ {message.poll.question.text}\n\n"
        )
        answertext = []
        for i in message.poll.answers:
            answerf = f"{i.id}. [{i.emoji}] {i.text} \n"
            answertext.append(answerf)
        embed.add_field(name="", value="".join(answertext), inline=False)
    embed.add_field(name="\n\n", value=", ".join(reactionlist), inline=False)
    embed.add_field(
        name="👤 Author",
        value=f"`{message.author.name}` (<@{message.author.id}>)",
        inline=True,
    )
    embed.add_field(name="🔗 Link", value=f"{message.jump_url}", inline=True)
    embed.add_field(name="🪪 ID", value=f"{message.id}", inline=True)
    if message.guild:
        embed.add_field(name="🏰 Guild", value=f"{message.guild.id}", inline=True)
    else:
        embed.add_field(name="🏰 Guild", value=f"DM", inline=True)
    if message.embeds:
        global numembeds
        numembeds = len(message.embeds)  # Number of embeds
        embed.add_field(name="🔲 Embeds", value=f"{numembeds}", inline=True)
    if message.attachments:
        global numfiles
        numfiles = len(message.attachments)
        embed.add_field(name="📸 Attachments", value=f"{numfiles}", inline=True)

    embed.add_field(
        name="📅 Send Date",
        value=f"{discord.utils.format_dt(message.created_at, 'F')}",
        inline=True,
    )
    if modal.children[0].value:
        embed.add_field(name="🔖 Tags", value=f"{modal.children[0].value}", inline=True)
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
