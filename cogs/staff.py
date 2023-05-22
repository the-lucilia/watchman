import discord
from discord.ext import commands


class dev(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    # load/reload/unload commands stolen shamelessly from Aav (again) :D
    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, *, cog: str):
        """Loads a cog"""
        try:
            await self.bot.load_extension(f"cogs.{cog}")
            await ctx.send(f"Loaded cog: {cog}")
            print(f"Loaded Cog: {cog}")
        except Exception as e:
            await ctx.send(f"Error: {e}")
            print(f"Error: {e}")

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, *, cog: str):
        """Unloads a cog"""
        try:
            await self.bot.unload_extension(f"cogs.{cog}")
            await ctx.send(f"Unloaded cog: {cog}")
            print(f"Unloaded Cog: {cog}")
        except Exception as e:
            await ctx.send(f"Error: {e}")
            print(f"Error: {e}")

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, *, cog: str):
        """Reloads a cog"""
        try:
            await self.bot.reload_extension(f"cogs.{cog}")
            await ctx.send(f"Reloaded cog: {cog}")
            print(f"Reloaded Cog: {cog}")
        except Exception as e:
            await ctx.send(f"Error: {e}")
            print(f"Error: {e}")

    # Shut down command | Credit to Dharman and Bhavyadeep Yadav on StackOverflow
    # (https://stackoverflow.com/a/66839279)
    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        """Shuts the bot down"""
        shutdown_embed = discord.Embed(
            title="Shutting Down",
            description="I am now shutting down. Farewell my friends!",
            color=0x8EE6DD,
        )
        await ctx.channel.send(embed=shutdown_embed)
        await self.bot.close()


async def setup(bot):
    await bot.add_cog(dev(bot))
