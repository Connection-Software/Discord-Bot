import discord
from discord.ext import commands
from PyDictionary import PyDictionary

class Dictionary(commands.Cog):
    """Commands related to dictionaries! Use `.cs help Dictionary` to know more!"""
    
    def __init__(self, client):
        self.client = client

    # ---------------------------------------------------

    # Gives you the definition(s) of the word
    @commands.command(aliases=["def"])
    async def definition(self, ctx, *, word):
        """Get the meaning of any word, phrase or sentence. Usage: `.cs definition (word)`"""
        
        meanings = PyDictionary(word.lower()).getMeanings()

        embed = discord.Embed(title=word.capitalize(), url=f"https://dictionary.com/browse/{word.lower()}", color=0x1479d2)

        for part_of_speech, meanings_list in meanings[word.lower()].items():
            meaning_string = ""

            for meaning in meanings_list:
                meaning_string += f"{meaning};\n"

            embed.add_field(name=part_of_speech, value=meaning_string)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Dictionary(client))
