import requests
from discord import Embed, File
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType

token = ""

client = commands.Bot(command_prefix='+')
client.remove_command('help')

@client.command()
async def help(ctx):
    embed = Embed(title="All Commands", description="Cooldown every 1 Min.")
    embed.add_field(name="+help", value="Displays all available commands", inline=False)
    embed.add_field(name="+http", value="Sends fresh HTTP proxy list", inline=False)
    embed.add_field(name="+https", value="Sends fresh HTTPS proxy list", inline=False)
    embed.add_field(name="+socks4", value="Sends fresh Socks4 proxy list", inline=False)
    embed.add_field(name="+socks5", value="Sends fresh Socks5 proxy list", inline=False)
    embed.add_field(name="+all", value="Sends fresh HTTP, HTTPS, Socks4 and Socks5 proxy list", inline=False)
    await ctx.send(embed=embed)

@client.command()
@cooldown(1, 60, BucketType.user)
async def http(ctx):
    f = open("Data/http-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=5000')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.send(file=File("Data/http-proxies.txt"))

@client.command()
@cooldown(1, 60, BucketType.user)
async def https(ctx):
    f = open("Data/https-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&timeout=5000')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.send(file=File("Data/https-proxies.txt"))

@client.command()
@cooldown(1, 60, BucketType.user)
async def socks4(ctx):
    f = open("Data/socks4-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=5000')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.send(file=File("Data/socks4-proxies.txt"))

@client.command()
@cooldown(1, 60, BucketType.user)
async def socks5(ctx):
    f = open("Data/socks5-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=5000')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.send(file=File("Data/socks5-proxies.txt"))

@client.command()
@cooldown(1, 60, BucketType.user)
async def all(ctx):
    f = open("Data/all-proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=all&timeout=5000')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        f.write((p)+"\n")
    await ctx.send(file=File("Data/all-proxies.txt"))

client.run(token)
