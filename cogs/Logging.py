import discord
from discord.ext import commands

class Logging(commands.Cog):
    """Maintain server logs! There are no commands under this cog."""
    def __init__(self, client):
        self.client = client

    # ---------------------------------------------------

    # Logs when a message is edited
    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if not before.author.bot:

            embed = discord.Embed(
                title="Edited Message",
                description=before.channel.mention,
                color=0xbd8306,
            )

            embed.add_field(name="Before", value=before.content, inline=True)
            embed.add_field(name="After", value=after.content, inline=True)

            text = f"Author: {before.author.mention}\nTime: {before.created_at.strftime('%d-%m-%y at %H:%M')}\nEdited at: {after.edited_at.strftime('%d-%m-%y at %H:%M')}\nMessage URL: {before.jump_url}\nMessage ID: {before.id}"
            embed.add_field(name="Info", value=text, inline=False)

            await self.client.logs_channel.send(embed=embed)

    # ---------------------------------------------------

    # Logs when a message is deleted
    @commands.Cog.listener()
    async def on_message_delete(self, before):
        if before.author.id != self.client.user.id or before.author.bot:
            embed = discord.Embed(
                title="Deleted Message",
                description=before.channel.mention,
                color=0x852c2a,
            )
            embed.add_field(
                name="Message", value=before.content, inline=True
            )
            text = f"Author: {before.author.mention}\nTime: {before.created_at.strftime('%d-%m-%y at %H:%M')}\nMessage ID: {before.id}"
            embed.add_field(name="Info", value=text, inline=False)
            await self.client.logs_channel.send(embed=embed)
    
def setup(client):
    client.add_cog(Logging(client))
