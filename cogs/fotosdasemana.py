import discord
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice
class View(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        url = "https://www.instagram.com/the_dlr_team/"
        bt1 = discord.ui.Button(label="📱- Instagram", style=discord.ButtonStyle.link, url=url)
        self.add_item(bt1)
    
class fotossemana(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(
        name = "habilitarfs",
        description = "para habilitar fotos semana"
    )
    
    async def fotossemana(
        self,
        interaction: discord.Interaction,
    ):
        view = View()
        
        embedfs=discord.Embed(title='📷 - Fotos da Semana - 📷',
        description = '**Como Participar:**\n⠀⠀⠀Compartilhe uma imagem 📷 de veículos 🚗 🏍️ 🚚 como **carros, motos, caminhões, etc**, dos jogos **Asseto Corsa, Live For Speed, Euro Truck, etc**.\n\n⠀⠀⠀Inclua o nome do jogo na postagem 🎮, por exemplo:**\nLive for Speed\nFoto...\n**\n⠀⠀⠀Uma **votação** 🗳️ será iniciada para todos os participantes escolherem a **melhor imagem** 💯.\n⠀⠀⠀A imagem **mais votada** será compartilhada em nosso Instagram 📱, com **créditos ao autor** 🙌.\n\n**Regras 📜:**\n⠀⠀⠀As imagens devem ser de jogos 🕹️ e **não devem ser da vida real** 🚫.\n⠀⠀⠀A imagem deve ser de **sua autoria** 💻.\n⠀⠀⠀Edições e reshaders são **permitidos** 🎨.\n⠀⠀⠀**Ao compartilhar a imagem neste canal 💬, você autoriza a equipe a publicá-la em nosso Instagram** 📱.\n⠀⠀⠀Cada participante pode compartilhar apenas **uma** imagem por semana 📅.\n⠀⠀⠀O vencedor da semana será **anunciado a cada domingo** 📢 e o processo será reiniciado 🔄.',
        color = 16711792
        )
        embedfs.set_author(name= "Dlr Management", icon_url= "https://cdn.discordapp.com/attachments/848679590930284565/1059616717799694458/image.png")
        embedfs.set_footer(text = "Sugestão de DennerM")
        await interaction.response.defer()
        await interaction.followup.send(embed=embedfs, view=view)
    
            
    
    
    

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        fotossemana(bot),
        guilds = [discord.Object(id = 848678305745862676)]
    )