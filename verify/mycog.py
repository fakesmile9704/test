from redbot.core import commands
from redbot.core.bot import Red
import discord

class ButtonsView(discord.ui.View):
    def __init__(self, role: discord.Role) -> None:
        super().__init__()
        self.role = role

    @discord.ui.button(label="S2020" , custom_id="emote_1")
    async def button_1_callback(self, interaction: discord.Interaction, item: discord.ui.Button):
        await interaction.response.edit_message(content="Wrong answer try again!", embed=None, view=None)

    @discord.ui.button(label="SSS2020" , custom_id="emote_2")
    async def button_2_callback(self, interaction: discord.Interaction, item: discord.ui.Button):
        member = interaction.user
        guild = interaction.guild
        
        if self.role in member.roles:
            await interaction.response.edit_message(content="You are already verified!", embed=None, view=None)
        else:
            await member.add_roles(self.role)
            await interaction.response.edit_message(content="You are verifed successfully!", embed=None, view=None)

    @discord.ui.button(label="SS2020" , custom_id="emote_3")
    async def button_3_callback(self, interaction: discord.Interaction, item: discord.ui.Button):
        await interaction.response.edit_message(content="Wrong answer try again!", embed=None, view=None)

    @discord.ui.button(label="2020SSS", custom_id="emote_4")
    async def button_4_callback(self, interaction: discord.Interaction, item: discord.ui.Button):
        await interaction.response.edit_message(content="Wrong answer try again!", embed=None, view=None)

class MyView(discord.ui.View):
    def __init__(self, channel: discord.TextChannel, role: discord.Role) -> None:
        super().__init__(timeout=None)
        self.channel = channel
        self.role = role

    @discord.ui.button(label="Verify",style=discord.ButtonStyle.green,emoji="<:yess:1020703229891330099>",custom_id="verify")
    async def button_callback(self, interaction: discord.Interaction, item: discord.ui.Button):
        button_embed: discord.Embed = discord.Embed(title="Verifying . . . ",description="You are about to verify yourself if you read the rules click on the right emote to get verified",color=0x2b2d31)
        await interaction.response.send_message(embed=button_embed, view=ButtonsView(self.role), ephemeral=True)

class MyyCog(commands.Cog):
    """My custom cog."""

    def __init__(self, bot: Red) -> None:
        self.bot: Red = bot

    async def cog_load(self) -> None:
        pass

    @commands.admin_or_permissions(administrator=True)
    @commands.hybrid_command()
    async def verify(self, ctx: commands.Context, channel: discord.TextChannel, role: discord.Role):
        embed: discord.Embed = discord.Embed(title="Verification",description="**Read the rules and click on the button below that says Verify to gain access**",color=0x2b2d31)
        embed.set_image(url="https://media.tenor.com/yG0BZ-wew-sAAAAC/verify-discord.gif")
        await channel.send(embed=embed, view=MyView(channel, role))
