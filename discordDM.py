import discord
import asyncio
import datetime
import openpyxl
from openpyxl.reader.excel import load_workbook
from openpyxl import load_workbook,workbook
from Dtime import Uptime
import os

@client.event
async def on_ready():
    print(client.user.name)
    print(client.user.id)
    print('로그인 완료')
    print("="*50)
    play = discord.Game("DPLY호스팅 문의 받는 중")
    await client.change_presence(status=discord.Status.online, activity=play)

@client.event
async def on_message(message):
    if message.guild is None:
        if message.author.bot:
            return
        else:
            embed = discord.Embed(title=(f"``{message.author}``님의 메세지 입니다"), color=0x00ff13, timestamp=message.created_at)
            embed.add_field(name="문의 내용", value=f"``{message.content}``", inline=True)
            embed.set_footer(text=f"!답변 <@{message.author.id}> 을 통해 답변이 가능합니다.")
            await client.get_channel(820482259966361621).send(embed=embed)
    #디엠을 받는 코드
    if message.content.startswith('!답변'):
        if message.author.guild_permissions.manage_messages:
            msg = message.content[26:]
            embed = discord.Embed(title=f"STAFF **{message.author}**님의 답장", color=0x00ff13)
            embed.add_field(name="**답변 내용**", value=f"``{msg}``")
            await message.mentions[0].send(embed=embed)
            embed = discord.Embed(title=f"**{message.mentions[0]}** 님에게 답변이 성공적으로 전달되었습니다", color=0x00ff13)
            await message.channel.send(embed=embed)
        else:
            await message.channel.send("당신은 권한이 없습니다!")
            return
    #리포트
    if message.content.startswith("!리포트"):
        msg = message.content[28:]
        embed = discord.Embed(title=f"새 리포트!")
        embed.add_field(name="리포트", value=f"``{message.content}``", inline=True)
        await client.get_channel(822484207678259270).send(embed=embed)
        await message.channel.send("리포트가 성공적으로 전송되었습니당!")

    #리붓
    if message.content.startswith("!리붓"):
        if message.author.guild_permissions.manage_messages:
            print(f"봇을 리붓합니다 리붓진행자:{message.author}")
            await message.channel.send(f"<@{message.author.id}> 님이 리붓 프로세스 시작")
            os.startfile('DMbotRB.cmd')
            os.system('taskkill.exe /f /im python.exe')
            print(50 * "-")
            return 0
            pass
        else:
            await message.channel.send("당신은 권한이 없습니다")
            return
    #업타임
    if message.content == "!업타임":
        uptime = str(Uptime.uptime()).split(":")
        hours = uptime [0]
        minutes = uptime [1]
        seconds = uptime [2].split(".")[0]
        await message.channel.send(f"봇이 {hours}시간 {minutes}분 {seconds}초 동안 일하고있어요!")
        print(message.author, "님이 봇 업타임 조회")

    #프로필
    if message.content.startswith("!프로필"):
        await message.channel.send(f"{message.author.avatar_url}")

    #청소   
    if message.content.startswith("!청소"):
        number = int(message.content.split(" ")[1])
        print(message.author, "님이 메세지", number, "개 삭제")
        await message.delete()  
        await message.channel.purge(limit=number)
        await message.channel.send(f"{number}개의 메세지가 삭제되었습니다.")

    #욕감지(Beta)
 
client.run(token)