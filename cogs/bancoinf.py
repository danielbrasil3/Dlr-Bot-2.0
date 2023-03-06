import discord
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice
import sqlite3
import csv

"""class View(discord.ui.View):
    def __init__(self, *, timeout=1000000000000000000000):
        super().__init__(timeout=timeout)
        url = "https://www.instagram.com/the_dlr_team/"
        bt1 = discord.ui.Button(label="📱- Instagram", style=discord.ButtonStyle.link, url=url)
        self.add_item(bt1)"""
    
class bancoinf(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(
        name = "database",
        description = "ver a database"
    )
    
    async def database(
        self,
        interaction: discord.Interaction,
        action: str = None,
    ):
        
        
        # Conexão com o banco de dados
        conn = sqlite3.connect("main.sqlite")
        cursor = conn.cursor()
        
        
        if not action:
            return await interaction.response.send_message("Você precisa escolher uma ação! Use `!database delete` para excluir todas as linhas do banco de dados ou `!database view` para ver todas as linhas.")
        
        if action == "delete":
            cursor.execute("DELETE FROM main")
            cursor.execute("DELETE FROM votes")
            conn.commit()
            return await interaction.response.send_message("Todas as linhas foram excluídas do banco de dados.")
        
        if action == "view":
            # salva as linhas em um arquivo CSV
            with open("database.txt", mode="w", encoding="utf-8") as file:
                writer = csv.writer(file, delimiter='\t')
                writer.writerow(['message_id', 'votos', 'id_user', 'url', 'content', 'author'])
                cursor.execute("SELECT * FROM main")
                rows = cursor.fetchall()
                for row in rows:
                    writer.writerow(row)
                if not rows:
                    return await interaction.response.send_message("Não há linhas no banco de dados.")

            # envia o arquivo de texto para o usuário
            with open("database.txt", mode="rb") as file:
                return await interaction.response.send_message(file=discord.File(file, "database.txt"))
            
                
            
                
            
            
            
            
        
        # Caso a ação escolhida seja inválida
        return await interaction.response.send_message("Ação inválida! Use `!database delete` para excluir todas as linhas do banco de dados ou `!database view` para ver todas as linhas.")
    
            
    
    
    

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        bancoinf(bot),
        guilds = [discord.Object(id = 848678305745862676)]
    )