import discord, logging, json #importer la librairie discord.py
import colorama
import asyncio
import platform
import pylint.lint
from discord.ext.commands import Bot
from discord.ext import commands #importer des commandes spécifiques de la librairie
import os
from datetime import datetime
from profanity import profanity
from tinydb import TinyDB, Query
from tinydb.operations import delete,increment
from colorama import *
from random import randint

bot = commands.Bot(description='Help', command_prefix='*') #indiquez la description et le préfixe de votre bot (laissez les apostrophes)
db = TinyDB('data.json')
Users = Query()
bot.remove_command('help')

# Print the starting text
print('---------------')
print('Protothype')
print('---------------')
print('Starting Bot...')
# Setup basic logging for the bot
logging.basicConfig(level=logging.WARNING)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='à faire des pancakes|*help'))
    print('---------------------------')
    print("Le Bot est démarré et prêt!")
    
@bot.command()
async def botinfo(ctx):
    e = discord.Embed(title="Protothype", description="C'est moi !", color=0xeccd1c, timestamp=datetime.utcnow())
    e.set_thumbnail(url="https://cdn.discordapp.com/attachments/492745804671483925/507902257774329887/HypeSLogo.png")
    e.add_field(name='Version', value='Alpha 0.2')
    e.add_field(name='Librairies', value='Discord.py')
    e.add_field(name='Créateur', value='Anokino')
    e.add_field(name='Serveurs', value='hum, c\'est en cours...')
    e.add_field(name='Utilisateurs', value='Aussi en cours')
    e.add_field(name='Invite', value='goo.gl/nRghwcelienestscretNo')
    e.add_field(name='Discord', value='https://discord.gg/jUet6dfsg6')
    e.add_field(name='Date version finale 1', value='Non définie')
    e.add_field(name='Nombre actuel de commandes', value='bruh')
    e.set_footer(text="Codé par Anokino#0434")
    await ctx.send(embed=e)
    
@bot.command()
async def help(ctx):
    e = discord.Embed(description="Aide Protothype", title='*Catégories*', color=0xF47B67, timestamp=datetime.utcnow()) #titre, sous-titre, couleur de l'embed, tampon de date
    e.set_thumbnail(url="https://cdn.discordapp.com/attachments/492745804671483925/507902257774329887/HypeSLogo.png") #icone de l'embed
    e.add_field(name='`Info`', value='Infos sur le bot et quelques autres trucs') #titre de la case, sous-titre
    e.add_field(name='`Divers`', value='Toutes les commandes utiles')
    e.add_field(name='`Modération`', value='Commandes de modération')
    e.add_field(name='`Fun`', value='Les commandes pour s\'amuser !')
    e.set_footer(text='Tapez *help <category> pour voir toutes les commandes en détails') #sous-titre de l'embed
    if ctx.author.id == 305066808660983811 : #cette commande à laquelle vous n'aurez jamais accès :3
            e.add_field(name='`Administrateur`', value="Les commandes pour mon créateur !")
    await ctx.send(embed=e) #envoyer l'embed

@bot.command(aliases=['Info', 'Infos', 'INFO', 'INFOS']) #tous les "alias" souhaités pour la commande
async def helpinfo(ctx):
    e = discord.Embed(description="Aide Protothype™", title='*Infos*', color=0xF47B67, timestamp=datetime.utcnow()) #titre, sous-titre, couleur de l'embed, tampon de date
    e.set_thumbnail(url="https://cdn.discordapp.com/attachments/492745804671483925/507902257774329887/HypeSLogo.png") #icone de l'embed
    e.add_field(name='`botinfo`', value='Infos sur le bot') #titre de la case, sous-titre
    e.add_field(name='`serverinfo`', value='Infos sur le serveur')
    e.add_field(name='`invite`', value='Inviter le bot sur votre serveur')
    e.add_field(name='`commande`', value='Non plus !')
    e.set_footer(text='Tapez *help <category> pour voir toutes les commandes en détails') #sous-titre de l'embed
    if ctx.author.id == 305066808660983811 : #cette commande à laquelle vous n'aurez jamais accès :3
            e.add_field(name='`Administrateur`', value="Les commandes pour mon créateur !")
    await ctx.send(embed=e) #envoyer l'embed

@bot.command()
async def helpdivers(ctx):
    e = discord.Embed(description="Aide Protothype™", title='*Divers*', color=0xF47B67, timestamp=datetime.utcnow()) #titre, sous-titre, couleur de l'embed, tampon de date
    e.set_thumbnail(url="https://cdn.discordapp.com/attachments/492745804671483925/507902257774329887/HypeSLogo.png") #icone de l'embed
    e.add_field(name='`1`', value='1. 1') #titre de la case, sous-titre
    e.add_field(name='`2`', value='2. 1')
    e.add_field(name='`3`', value='3. 1')
    e.add_field(name='`4`', value='4. 1')
    e.set_footer(text='Tapez *help <category> pour voir toutes les commandes en détails') #sous-titre de l'embed
    if ctx.author.id == 305066808660983811 : #cette commande à laquelle vous n'aurez jamais accès :3
            e.add_field(name='`Administrateur`', value="Les commandes pour mon créateur !")
    await ctx.send(embed=e) #envoyer
 
@bot.command()
async def helpmoderation(ctx):
    e = discord.Embed(description="Aide Protothype™", title='*Modération*', color=0xF47B67, timestamp=datetime.utcnow()) #titre, sous-titre, couleur de l'embed, tampon de date
    e.set_thumbnail(url="https://cdn.discordapp.com/attachments/492745804671483925/507902257774329887/HypeSLogo.png") #icone de l'embed
    e.add_field(name='`1`', value='1. 1') #titre de la case, sous-titre
    e.add_field(name='`2`', value='2. 1')
    e.add_field(name='`3`', value='3. 1')
    e.add_field(name='`4`', value='4. 1')
    e.set_footer(text='Tapez *help <category> pour voir toutes les commandes en détails') #sous-titre de l'embed
    if ctx.author.id == 305066808660983811 : #cette commande à laquelle vous n'aurez jamais accès :3
            e.add_field(name='`Administrateur`', value="Les commandes pour mon créateur !")
    await ctx.send(embed=e) #envoyer 

@bot.command()
async def helpfun(ctx):
    e = discord.Embed(description="Aide Protothype™", title='*Fun*', color=0xF47B67, timestamp=datetime.utcnow()) #titre, sous-titre, couleur de l'embed, tampon de date
    e.set_thumbnail(url="https://cdn.discordapp.com/attachments/492745804671483925/507902257774329887/HypeSLogo.png") #icone de l'embed
    e.add_field(name='`1`', value='1. 1') #titre de la case, sous-titre
    e.add_field(name='`2`', value='2. 1')
    e.add_field(name='`3`', value='3. 1')
    e.add_field(name='`4`', value='4. 1')
    e.set_footer(text='Tapez *help <category> pour voir toutes les commandes en détails') #sous-titre de l'embed
    if ctx.author.id == 305066808660983811 : #cette commande à laquelle vous n'aurez jamais accès :3
            e.add_field(name='`Administrateur`', value="Les commandes pour mon créateur !")
    await ctx.send(embed=e) #envoyer
 
@bot.command()
async def helpadmin(ctx):
    e = discord.Embed(description="Aide Protothype™", title='*Administrateur*', color=0xF47B67, timestamp=datetime.utcnow()) #titre, sous-titre, couleur de l'embed, tampon de date
    e.set_thumbnail(url="https://cdn.discordapp.com/attachments/492745804671483925/507902257774329887/HypeSLogo.png") #icone de l'embe
    if ctx.author.id == 305066808660983811 : #cette commande à laquelle vous n'aurez jamais accès :3
            e.add_field(name='`Administrateur`', value="Les commandes pour mon créateur !")
            e.set_footer(text="Codé par Anokino#0434")
    await ctx.send(embed=e) #envoyer
    
@bot.command()
async def ping(ctx): #nom de la commande
    """Renvoie 'Pong !'""" #description de la commande (affichée dans le message d'aide)
    await ctx.send("**Pong !**") #réponse du bot
     # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(f'`Latence : {latency}`')

@bot.command()
async def say(ctx, *, text):
    await ctx.send(text)    

@bot.command()
async def autodestruction(ctx):
    await ctx.send('3')    
    await ctx.send('2')   
    await ctx.send('1')   
    await ctx.send('Autodestruction')   


@bot.command()
async def konamicode(ctx):
    rnd = randint(0, 9999999999999999)
    await ctx.send(rnd)  

@bot.command(pass_context=True)
async def roles(ctx):
    """Displays all of the roles with their ids"""
    roles = ctx.guild.roles
    embed=discord.Embed(title="Roles", description=f"Serveur : {ctx.guild}", color=0xce0005, timestamp=datetime.utcnow())
    embed.set_thumbnail(url = ctx.guild.icon_url)
    for role in roles:
        embed.add_field(name=f"Role : {role.name}", value=f"ID : {role.id}", inline=False)
        embed.set_footer(text="Codé par Anokino#0434")
    await ctx.send(embed=embed)
    
@bot.command()
async def serverinfo(ctx):
    e = discord.Embed(title=f"Serveur : {ctx.guild}", description="Infos", color=0xeccd1c, timestamp=datetime.utcnow())
    e.set_thumbnail(url= ctx.guild.icon_url)
    e.add_field(name='Propriétaire', value= ctx.guild.owner)
    e.add_field(name='Region', value= ctx.guild.region)
    e.add_field(name='Securité', value= ctx.guild.verification_level)
    e.add_field(name='Invitation', value='En cours')
    e.add_field(name='Utilisateurs', value='Aussi en cours')
    e.add_field(name='No', value='No')
    e.add_field(name='No', value='No')
    e.add_field(name='No', value='No')
    e.add_field(name='No', value='No')
    e.set_footer(text="Codé par Anokino#0434")
    await ctx.send(embed=e)

@commands.has_permissions(kick_members=True)
@bot.command(pass_context=True)
async def clear(ctx, msglimit : int):
    try:
        deleted = await ctx.channel.purge(limit=msglimit)
        await ctx.send("J'ai supprimé **{}** messages".format(len(deleted)))
    except:
        e = discord.Embed(title="__Erreur :__", color=0xeccd1c, timestamp=datetime.utcnow())
        e.set_thumbnail(url="https://cdn.discordapp.com/attachments/399581255961804821/511145934982217738/error.png")
        e.add_field(name="**Permissions Insuffisantes**", value="­­ ")
        e.set_footer(text="Codé par Anokino#0434")
        await ctx.send(embed=e)

@bot.command()
async def test(ctx):
    await ctx.send("**Le bot est connecté et opérationnel**")
@bot.command()
async def invite(ctx):
    await ctx.send("**Tu peux m'inviter grâce à ce lien :** https://goo.gl/nRghwcelienestscretNo") #lien d' invitation : https://goo.gl/nghwNo
    
@bot.command()
async def salons(ctx):
    channels = bot.get_all_channels
    await ctx.send(channels)

@bot.command()
async def user(ctx, *, member: discord.Member = None):
    if member is None:
        member = ctx.message.author
        embed = discord.Embed(color = 0xF47B67)
        embed.set_thumbnail(url = member.avatar_url)
        embed.add_field(name="ID utilisateur:", value=member.id, inline=True)
        embed.add_field(name="Nom d'utilisateur:", value=member, inline=True)
        embed.add_field(name="Bot:", value=member.bot, inline=True)
        embed.add_field(name="Création du compte:", value=member.created_at, inline=True)
        embed.add_field(name="Pseudo:", value=member.display_name, inline=True)
        embed.set_footer(text="Codé par Anokino#0434")
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(color = 0xF47B67)
        embed.set_thumbnail(url = member.avatar_url)
        embed.add_field(name="ID utilisateur:", value=member.id, inline=True)
        embed.add_field(name="Nom d'utilisateur:", value=member, inline=True)
        embed.add_field(name="Bot:", value=member.bot, inline=True)
        embed.add_field(name="Création du compte:", value=member.created_at, inline=True)
        embed.add_field(name="Pseudo:", value=member.display_name, inline=True)
        embed.set_footer(text="Codé par Anokino#0434")
        await ctx.send(embed=embed)
    print(Fore.CYAN + "Command Successfully Executed |\n       Command Ran In:[" + ctx.message.server.id + "]\n       User:[" + ctx.message.author.id + "]\n       Channel:[" + ctx.message.channel.id + "]") 

@bot.command()
async def avatar268(ctx, *, member: discord.Member = None):
    embed = discord.Embed(color = 0xF47B67)
    embed.add_field(name="Avatar de:", value=member)
    embed.add_field(name="Image :", value=member.avatar_url)
    await ctx.send(embed=embed)

@bot.command()
async def avatar(ctx, *, member: discord.Member = None):
    e = discord.Embed(description="Image de profil de {}".format(member.name), title='Avatar', color=0xF47B67, timestamp=datetime.utcnow())
    e.set_image(url=member.avatar_url)
    e.set_footer(text="Codé par Anokino#0434")
    await ctx.send(embed=e)

@bot.command()
async def embed(ctx, *, text):
    e = discord.Embed(color=0xF47B67, timestamp=datetime.utcnow()) 
    e.add_field(name='Message Embed', value=text)
    e.set_footer(text=f'Demandé par {ctx.author.name}:')
    await ctx.send(embed=e)

@bot.command()
async def ami(ctx, member: discord.Member):
    rnd = randint(0, 100)
    await ctx.send(f'{ctx.author.name}, tu as {rnd}% d\'être un bon ami avec {member.name}')

@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick2(ctx, member: discord.Member):
        if ctx.message.author.server_permissions.kick_members:
            await bot.delete_message(ctx.message)
            await bot.kick(member)
            await ctx.send(member + " a été kick")        
        else: 
            await ctx.send("Tu n'as pas la permission de kick les membres.")

@commands.has_permissions(kick_members=True)
@bot.command()
async def kick(ctx, member: discord.Member):
    try:
        await member.kick()
        await ctx.send('{} a bien été exclu !'.format(member))
    except Exception as e:
        print(e.args)
        await ctx.send("Nom d'utilisateur incorrect !")

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member):
        if ctx.message.author.server_permissions.kick_members:
            await bot.delete_message(ctx.message)
            await bot.ban(member)
            await bot.say(member + " a été banni.")        
        else: 
            await    bot.say("Tu n'as pas la permission de bannir les membres.")

bot.run(bot.run(os.environ['NTA3OTI2OTc4NTYxODM1MDIw.Dr31-Q.SrHFTaeBXYtWYOG3aCyU4JM31J0'])) #Lancer le bot. Remplacez token par votre token et laissez les apostrophes

    
