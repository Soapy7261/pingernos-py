from re import match
from discord.ext import commands, bridge
from discord import Embed
from mcstatus import JavaServer
from utils import Utils
class CheckIP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bridge.bridge_command(aliases=["checkserverip", "check"], description="Checks if an Aternos-IP is free to use.")
    async def checkip(self, ctx, address = None):
        if address is None:
            return await ctx.respond("Please provide a Aternos server ip!\nExample: example.aternos.me")
        if not match(r"^(\w+)(?:\.aternos\.me)?$", address):
            return await ctx.respond(f"`{address}`is not a valid Aternos server IP or name.")
        if address.count(".") > 2:
            return await ctx.respond("Please provide a valid Aternos server ip!\nExample: example.aternos.me")
        nip = address.split(".")[0]
        if len(nip) > 20:
            return await ctx.respond("Aternos IPs can only be 20 characters long, please try a shorter one. Yours is " + str(len(nip)) + " characters long.")
        if len(nip) < 4:
            return await ctx.respond("Aternos IPs must be at least 4 characters long, please try a longer one. Yours is " + str(len(nip)) + " characters long.")
        #async with ctx.typing():
        await ctx.defer()
        embed = Embed()
        server = await JavaServer.async_lookup(address)
        stat = await server.async_status()
        if stat.version.name == "⚠ Error":
            embed.description=f"**{nip}.aternos.me** is free to use!\nTo use it as your server address, head to **[the options of your server](https://aternos.org/options)**"
            embed.colour = Utils.Colors.green
        else:
            embed.description=f"**{nip}.aternos.me** is already taken!"
            embed.colour = Utils.Colors.red
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(CheckIP(bot))
