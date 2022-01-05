# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
import discord
from discord import Member
from discord.ext import commands


import database


class cherryfaq(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	shorthelp ='Show the answer on a FAQ item. For more info, write #help faq'
	longhelp = "Show the answer from a FAQ item.\nTo see a full list of all the FAQ items, write #list"
	@commands.command(pass_context=True, name='faq', help=longhelp, brief=shorthelp)
	async def faq(self, ctx, key="none"):
		answer = database.read(key, "faq.json")
		if answer != "KeyNotFound":
			await ctx.send(answer)
		else:
			await ctx.send("Could not find the question in the archive.")


	shorthelp = 'Add a FAQ item. for more info, write #help add'
	longhelp = 'To add a question you need to add a keyword to find it back, as well as the actual answer.\nWrite both the keyword as the answer between double quotes so the system knows which part is the keyword and which is the answer.\nFor example: #add "Question" "This is the answer on the question"'
	@commands.command(pass_context=True, name='add', help=longhelp, brief=shorthelp)
	async def add(self, ctx, key="none", value="none"):
		
		database.write(key, value, "faq.json")
		await ctx.send("Your question is added to the list. To request the answer, you can write #faq " + key)


	shorthelp ='Show the list of FAQ items. For more info, write #help list'
	longhelp = "This command will show you all the FAQ items in this bot. If you want to show the answer of 1 of the FAQ items, write #faq followed by 1 of the items from the list."
	@commands.command(pass_context=True, name='list', help=longhelp, brief=shorthelp)
	async def list(self, ctx):
		list = database.list("faq.json")
		if list:
			keys = "The following keys are available: ["
			for key in list.keys():
				keys += key + ","
			keys = keys.rstrip(keys[-1])
			keys += "]"

			await ctx.send(keys)
		else:
			await ctx.send("There are no FAQ items")


def setup(bot):
    bot.add_cog(cherryfaq(bot))