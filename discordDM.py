import discord
import asyncio
import datetime
import openpyxl
from openpyxl.reader.excel import load_workbook
from openpyxl import load_workbook,workbook
from Dtime import Uptime
import os
client = discord.Client()
Uptime.uptimeset()
token = "ODIwMjEwODQxOTAzMzAwNjE4.YEx23w.poCBECdBy70mWX7VAt2AQRLxWJE"


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
    sibal = {"씨부럴","씨부랄","시부럴","시부랄","시\발","씨\발","시벌탱","씨벌탱","씨-","씨*","씨&","씨^","씨%","씨$","씨#","씨@","씨!","시-","시*","시&","시^","시%","시$","시#","시@","시!","씨0","씨9","씨8","씨7","씨6","씨5","씨4","씨3","씨2","시0","시9","시8","시7","시6","시5","시4","시3","시2","쓰발","싶팔","십팔","십발","씹","싸발","야발","싯팔","씻팔", "시부", "씨부", "씨||||", "시||||", "ㅅ||||", "ㅆ||||", "씨||", "시||", "ㅆ||", "ㅅ||","씨이","시이","시발","시벌", "tlqkf", "ㅅㅂ","ㅆㅂ","ㅆ1","ㅆ2","ㅆ12","씨바","씨발","씨벌","씨12","씨1", "ㅅ1ㅂ", "ㅅ12ㅂ", "쉬", "쒸","쉬1", "ㅅ1", "쉬12", "ㅅ12", "시바","시1", "ㅅ ㅂ", "ㅅ  ㅂ", "ㅅ   ㅂ", "ㅅ    ㅂ", "ㅅ     ㅂ"}
    for i in sibal:
        if i in message.content:
            await message.delete()
            print(f"{message.author}님의 욕설 | ID=1")
            await message.channel.send(f"<@{message.author.id}> 님의 욕설사용이 적발되었습니다. 욕설 ID=1")

    crazy = {"미친", "미쳤", "미춋", "도라이", "또라이", "미춌","병신","븅신","등신","지랄","죠랄","염병","젠장"}
    for i in crazy:
        if i in message.content:
            await message.delete()
            print(f"{message.author}님의 욕설 | ID=2")
            await message.channel.send(f"<@{message.author.id}>님의 욕설사용이 적발되었습니다. 욕설 ID=2")

    puppy = {"개색", "개새", "새끼", "새꺄", "개같"}
    for i in puppy:
        if i in message.content:
            await message.delete()
            print(f"{message.author}님의 욕설 | ID=3")
            await message.channel.send(f"<@{message.author.id}>님의 욕설사용이 적발되었습니다. 욕설 ID=3")

    jot = {"좆", "ㅈ같"}
    for i in jot:
        if i in message.content:
            await message.delete()
            print(f"{message.author}님의 욕설 | ID=4")
            await message.delete()
            await message.channel.send(f"<@{message.author.id}>님의 욕설사용이 적발되었습니다. 욕설 ID=4")
 
    die = {"죽어","뒤져","뒤짐","죽음","쥬금","주금","뒤질","죽고","뒤지","죽을","죽 어","뒤 져","뒤 짐","죽 음","쥬 금","주 금","뒤 질","죽 고","뒤 지","죽 을","죽  어","뒤  져","뒤  짐","죽  음","쥬  금","주  금","뒤  질","죽  고","뒤  지","죽  을", "뒤1","죽1"}
    for i in die:
        if i in message.content:
            print(f"{message.author}님의 욕설 | ID=5")
            await message.channel.send(f"<@{message.author.id}>님의 욕설사용이 적발되었습니다 . 욕설 ID=5")

    susik = {"존나","졸라","쥰내","쥰나"}
    for i in susik:
        if i in message.content:
            await message.delete()
            print(f"{message.author}님의 욕설 | ID=6")
            await message.channel.send(f"<@{message.author.id}>님의 욕설사용이 적발되었습니다. 욕설 ID=6")
    
    Team = {"유니언","Union","스네","스카이네트워크","skynetwork"}
    for i in Team:
        if i in message.content:
            await message.delete()
            await message.channel.send("그말하면 밴임!!. <@787181025876377620> 참고!! ID=7")
            print(f"{message.author}님이 금지된 팀 언급!")
            
    sex = {'섹스','쎅스','쎅쓰','색스','쌕스','쌕쓰','색쓰','섹쓰','sex','세엑스','쎄엑스','세엑쓰','쎄엑쓰','세엑스으','쎄엑스으','세엑쓰으',"쎄엑쓰으"}
    for i in sex:
        if i in messaage.content:
            await message.delete()
            await message.channel.send(f"<@{message.author.id}>님의 욕설사용이 적발되었습니다. 욕설 ID=8")
            
client.run(token)