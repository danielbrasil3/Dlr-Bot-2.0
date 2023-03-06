import discord
from discord.ext import commands
import os
import sqlite3
import datetime
import schedule
import time
from config import TOKEN


# Constantes
CHANNEL_FOTOS_ID = 1082388924485349477
CHANNEL_FOTOSV_ID = 1082388961617510430

# Conexão com o banco de dados
with sqlite3.connect("main.sqlite") as conn:
    cursor = conn.cursor()  
    



class View1(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        url = "https://www.instagram.com/the_dlr_team/"
        bt1 = discord.ui.Button(label="📱- Instagram", style=discord.ButtonStyle.link, url=url)
        self.add_item(bt1)

async def buscar_foto_mais_votada():
    # aqui você pode colocar o código que busca a foto mais votada
    week_ago = datetime.datetime.now() - datetime.timedelta(days=1)
    cursor.execute("SELECT url, author, content, votos FROM main WHERE data_envio > ?", (week_ago,))
    results = cursor.fetchall()
    if results:

        most_voted = max(results, key=lambda x: x[3])  # Procura a foto mais votada

        if most_voted is not None:
                
            url, author, content, votos = most_voted
            embed = discord.Embed(
                title='🏆 Foto mais votada na última semana 🏆',
                description='Foto de {0}\nJogo: {1}\n\n**Votos:** {2}'.format(author, content, votos),
                color=0xFF0000  # Vermelho
            )
            embed.set_image(url=url)
            embed.set_footer(text='Envie sua foto e participe também.')

            embedfs=discord.Embed(title='📷 - Fotos da Semana - 📷',
            description = '**Como Participar:**\n⠀⠀⠀Compartilhe uma imagem 📷 de veículos 🚗 🏍️ 🚚 como **carros, motos, caminhões, etc**, dos jogos **Asseto Corsa, Live For Speed, Euro Truck, etc**.\n\n⠀⠀⠀Inclua o nome do jogo na postagem 🎮, por exemplo:**\nLive for Speed\nFoto...\n**\n⠀⠀⠀Uma **votação** 🗳️ será iniciada para todos os participantes escolherem a **melhor imagem** 💯.\n⠀⠀⠀A imagem **mais votada** será compartilhada em nosso Instagram 📱, com **créditos ao autor** 🙌.\n\n**Regras 📜:**\n⠀⠀⠀As imagens devem ser de jogos 🕹️ e **não devem ser da vida real** 🚫.\n⠀⠀⠀A imagem deve ser de **sua autoria** 💻.\n⠀⠀⠀Edições e reshaders são **permitidos** 🎨.\n⠀⠀⠀**Ao compartilhar a imagem neste canal 💬, você autoriza a equipe a publicá-la em nosso Instagram** 📱.\n⠀⠀⠀Cada participante pode compartilhar apenas **uma** imagem por semana 📅.\n⠀⠀⠀O vencedor da semana será **anunciado a cada domingo** 📢 e o processo será reiniciado 🔄.',
            color = 16711792
            )
            embedfs.set_author(name= "Dlr Management", icon_url= "https://cdn.discordapp.com/attachments/848679590930284565/1059616717799694458/image.png")
            embedfs.set_footer(text = "Sugestão de DennerM")

            view1 = View1()
            channel = bot.get_channel(CHANNEL_FOTOSV_ID)
            channell = bot.get_channel(CHANNEL_FOTOS_ID)
            await channell.purge()
            await channell.send(embed=embedfs, view=view1)
            await channel.send(embed=embed)
            cursor.execute("DELETE FROM main")
            cursor.execute("DELETE FROM votes")
            conn.commit()
            
    else:
            print("Nenhuma foto encontrada.")
    

# agenda a tarefa para executar todo domingo às 12:00
schedule.every().wednesday.at("13:00").do(buscar_foto_mais_votada)

while True:
    # verifica se há tarefas agendadas para serem executadas
    schedule.run_pending()
    # aguarda 1 segundo antes de verificar novamente
    time.sleep(1)

# Classe que define a view do bot
class View(discord.ui.View):
    
    def __init__(self):
        super().__init__(timeout=None)
        
    # Função que é chamada ao clicar no botão
    @discord.ui.button(label="Votar", style=discord.ButtonStyle.green, emoji="✅", custom_id='persistent_view:green')
    async def green_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        

        # Consultar o banco de dados para obter informações sobre a mensagem e a votação atual
        cursor.execute("SELECT id_user, url, author, content, votos FROM main WHERE message_id = ?", (interaction.message.id,))
        result = cursor.fetchone()
        
        if result is not None:
            id_user, url, author, content, votos = result
        else:
            await interaction.response.defer()
            await interaction.followup.send(content="A mensagem não foi encontrada no banco de dados!", ephemeral=True)
            return

        
        cursor.execute("SELECT * FROM votes WHERE message_id = ? AND user_id = ?", (interaction.message.id, interaction.user.id))
        resultt = cursor.fetchone()
        if resultt is not None:
            await interaction.response.defer()
            await interaction.followup.send(content="Você já votou nesta foto!", ephemeral=True)
        else:
            # Inserir o voto do usuário na tabela "votes"
            cursor.execute("INSERT INTO votes (message_id, user_id) VALUES (?, ?)", (interaction.message.id, interaction.user.id))
            conn.commit()
            votos += 1 
            
            sql = ("UPDATE main SET votos = ? WHERE message_id = ?")
            val = (votos, interaction.message.id)
                
            cursor.execute(sql, val)
            conn.commit()
            
        

        embed3 = discord.Embed(title='📸  Nova Foto Enviada  📸, Votos {}'.format(votos), 
            description=f'Foto de {author}\nJogo: {content}', color=0xFF0000)
        embed3 = discord.Embed(
                    title='📸 Nova Foto Enviada 📸',
                    description='Foto de {0}\nJogo: {1}\n\n**Votos:** {2}'.format(author, content, votos),
                    color=0xFF0000  # Vermelho
                )
        embed3.set_image(url=url)
        embed3.set_footer(text='Envie sua foto e participe também.')
        if interaction.response.is_done():
            return
        else:
            await interaction.response.edit_message(embed=embed3, view=View())

        

class MeuBot(commands.Bot):

    def __init__(self):
        super().__init__(
            command_prefix='d!',
            intents= discord.Intents.all(),
            application_id = 850050516943372348
            
        )
        

        
    

    
    async def setup_hook(self):
        
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):


                try:
                    await bot.load_extension(f"cogs.{filename[:-3]}")
                    print(f"Loaded {filename}")
                except Exception as e:
                    print(f"Failed to load {filename}")
                    print(f"[ERROR] {e}")
                 
                await bot.tree.sync(guild = discord.Object(id = 848678305745862676))
        
                    

    
    
    conn.commit()
    async def on_ready(self):
        print(f"Logged in as {self.user.name} ({self.user.id})")
        print("----------------------")
        print(f"Current servers:")
        for guild in self.guilds:
            print(f"{guild.name} (id: {guild.id})")
        print("----------------------")
        print(f"Total members: {len(self.users)}")
        print("----------------------")

        self.add_view(View1())
        self.add_view(View())

    async def on_message(self, message):
        if message.channel.id == CHANNEL_FOTOS_ID and message.attachments:
            if message.content:
                
                attachment = message.attachments[0]
                global url
                url = attachment.url
                # Você pode fazer o que quiser com a URL aqui, como salvar a imagem em seu disco ou enviá-la para outro canal.
                agora = datetime.datetime.now()
                data_envio = agora.strftime("%Y-%m-%d %H:%M:%S")
                men = message.author
                
                view = View()
                
                embedf = discord.Embed(
                    title='📸 Nova Foto Enviada 📸',
                    description='Foto de {0.mention}\nJogo: {1}\n\n**Votos:** 0'.format(message.author, message.content),
                    color=0xFF0000  # Vermelho
                )
                embedf.set_image(url=url)
                embedf.set_footer(text='Envie sua foto e participe também.')
                channel = message.channel
                
                vote_message = await message.channel.send(embed=embedf, view=view)
                cursor.execute(f"SELECT votos FROM main WHERE message_id = {message.id}")
                result = cursor.fetchone()
                if result is None:
                    sql = ("INSERT INTO main(message_id, votos, id_user, url, content, author, data_envio) VALUES(?,?,?,?,?,?,?)")
                    val = (vote_message.id, 0, None, url, message.content, men.mention, data_envio)
                    
                cursor.execute(sql, val)
                conn.commit()
                await message.delete()
            else:
                embede=discord.Embed(title='🚫 - Sem Nome do jogo. 🚫',
                description = 'Ao enviar a foto precisa do **nome do jogo** do qual foi tirada a foto,\nTente novamente colocando o nome do jogo no texto conforme mostra na imagem:',
                color = 16711680
                )
                embede.set_image(url="https://cdn.discordapp.com/attachments/972164561165779009/1072938801338519632/image.png")
                await message.author.send(embed=embede)
                await message.delete()
        await bot.process_commands(message)

"""
CREATE TABLE main (
    message_id TEXT,
    votos      INTEGER,
    id_user    TEXT,
    url        TEXT,
    content    TEXT,
    author     TEXT
);

CREATE TABLE votes (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    message_id INTEGER NOT NULL,
    user_id    INTEGER NOT NULL
);
"""
bot = MeuBot()
bot.run(TOKEN)