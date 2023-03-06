import discord
from discord import app_commands
from discord.ext import commands
bot = commands.Bot(command_prefix=",", intents=discord.Intents.all())
TEAM_ROLE = 972164560058482764
GUILD_ID = 972164559915847810
TICKET_CHANNEL = 972164562486972436 
CATEGORY_ID = 972164562486972441 
TICKET_MOD_ROLE_ID = 972164560058482764


class selec1(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="Reportar Bug",  emoji="🛠"),
            discord.SelectOption(label="Fazer uma denúncia",  emoji="🚨"),
            discord.SelectOption(label="Apelar uma punição",  emoji="🙇🏽‍♂️"),
            discord.SelectOption(label="Enviar uma sugestão",  emoji="💡"),
            discord.SelectOption(label="Tirar duvidas",  emoji="🙋🏽"),
            discord.SelectOption(label="Outros",  emoji="🔎")
            ]
        super().__init__(placeholder="O que precisa?",max_values=1,min_values=1,options=options)

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Reportar Bug":
            embedbug=discord.Embed(title='❗️Reportar bug ❗️',
                description = '**Escolha de qual serviço deseja reportar o bug.**',
                color = 0xff0000
                )
            for channel in interaction.guild.text_channels:
                if f"{interaction.user.id}" in channel.name:
                    await interaction.response.send_message(ephemeral=True,content=f"Você já tem um atendimento em andamento!")
                    return
                
            ticket_mod_role = interaction.guild.get_role(
                972164560058482764
            )
            overwrites = {
                interaction.guild.default_role: discord.PermissionOverwrite(view_channel=False),
                interaction.user: discord.PermissionOverwrite(view_channel=True),
                interaction.guild.me: discord.PermissionOverwrite(view_channel=True),
                ticket_mod_role: discord.PermissionOverwrite(view_channel=True),
            }
            ticket = await interaction.guild.create_text_channel(name=f"Ticket {interaction.user.id} ", overwrites=overwrites) 
                    
                    

            await interaction.response.send_message(ephemeral=True,content=f"Criei um ticket para você! {ticket.mention}")
                    
            await ticket.send(embed=embedbug, view=reportar1())
            
            

        elif self.values[0] == "Fazer uma denúncia":
            embedden=discord.Embed(title='📢  Denunciar  📢',
        description = f"{interaction.user.mention}\n**Escolha de qual serviço deseja fazer a denuncia.**",
        color = 0xff5200
        )
            for channel in interaction.guild.text_channels:
                if f"{interaction.user.id}" in channel.name:
                    await interaction.response.send_message(ephemeral=True,content=f"Você já tem um atendimento em andamento!")
                    return
            
            ticket_mod_role = interaction.guild.get_role(
                972164560058482764
            )
            overwrites = {
                interaction.guild.default_role: discord.PermissionOverwrite(view_channel=False),
                interaction.user: discord.PermissionOverwrite(view_channel=True),
                interaction.guild.me: discord.PermissionOverwrite(view_channel=True),
                ticket_mod_role: discord.PermissionOverwrite(view_channel=True),
            }
            ticket = await interaction.guild.create_text_channel(name=f"Ticket {interaction.user.id} ", overwrites=overwrites) 
            
            

            await interaction.response.send_message(ephemeral=True,content=f"Criei um ticket para você! {ticket.mention}")

            await ticket.send(embed=embedden, view=denunciar1())

        elif self.values[0] == "Apelar uma punição":
            embedunb=discord.Embed(title='📌 Pedido de unban 📌',
        description = '**Escolha de qual serviço deseja fazer a apelação.**',
        color = 0x000aff
        )
            for channel in interaction.guild.text_channels:
                if f"{interaction.user.id}" in channel.name:
                    await interaction.response.send_message(ephemeral=True,content=f"Você já tem um atendimento em andamento!")
                    return
            
            ticket_mod_role = interaction.guild.get_role(
                972164560058482764
            )
            overwrites = {
                interaction.guild.default_role: discord.PermissionOverwrite(view_channel=False),
                interaction.user: discord.PermissionOverwrite(view_channel=True),
                interaction.guild.me: discord.PermissionOverwrite(view_channel=True),
                ticket_mod_role: discord.PermissionOverwrite(view_channel=True),
            }
            ticket = await interaction.guild.create_text_channel(name=f"Ticket {interaction.user.id} ", overwrites=overwrites) 
            
            

            await interaction.response.send_message(ephemeral=True,content=f"Criei um ticket para você! {ticket.mention}")

            await ticket.send(embed=embedunb, view=unban1())

        elif self.values[0] == "Enviar uma sugestão":
            embedsug=discord.Embed(title='💡 Sugestão 💡',
        description = '**Escolha de qual serviço deseja fazer a sugestão.**',
        color = 0x00ffff
        )
            for channel in interaction.guild.text_channels:
                if f"{interaction.user.id}" in channel.name:
                    await interaction.response.send_message(ephemeral=True,content=f"Você já tem um atendimento em andamento!")
                    return
            
            ticket_mod_role = interaction.guild.get_role(
                972164560058482764
            )
            overwrites = {
                interaction.guild.default_role: discord.PermissionOverwrite(view_channel=False),
                interaction.user: discord.PermissionOverwrite(view_channel=True),
                interaction.guild.me: discord.PermissionOverwrite(view_channel=True),
                ticket_mod_role: discord.PermissionOverwrite(view_channel=True),
            }
            ticket = await interaction.guild.create_text_channel(name=f"Ticket {interaction.user.id} ", overwrites=overwrites) 
            
            

            await interaction.response.send_message(ephemeral=True,content=f"Criei um ticket para você! {ticket.mention}")

            await ticket.send(embed=embedsug, view=sugestao1())

        elif self.values[0] == "Tirar duvidas":
            embedduv=discord.Embed(title='❓ Duvidas ❓',
        description = '**Escolha de qual serviço você tem duvida.**',
        color = 0xff00c2
        )
            for channel in interaction.guild.text_channels:
                if f"{interaction.user.id}" in channel.name:
                    await interaction.response.send_message(ephemeral=True,content=f"Você já tem um atendimento em andamento!")
                    return
            
            ticket_mod_role = interaction.guild.get_role(
                972164560058482764
            )
            overwrites = {
                interaction.guild.default_role: discord.PermissionOverwrite(view_channel=False),
                interaction.user: discord.PermissionOverwrite(view_channel=True),
                interaction.guild.me: discord.PermissionOverwrite(view_channel=True),
                ticket_mod_role: discord.PermissionOverwrite(view_channel=True),
            }
            ticket = await interaction.guild.create_text_channel(name=f"Ticket {interaction.user.id} ", overwrites=overwrites) 
            
            

            await interaction.response.send_message(ephemeral=True,content=f"Criei um ticket para você! {ticket.mention}")

            await ticket.send(embed=embedduv, view=duvida1())

        elif self.values[0] == "Outros":
            embedout=discord.Embed(title='💬 Outros 💬',
        description = '**Foi aberto um ticket normal em **',
        color = 0xe0ff00
        )
            for channel in interaction.guild.text_channels:
                if f"{interaction.user.id}" in channel.name:
                    await interaction.response.send_message(ephemeral=True,content=f"Você já tem um atendimento em andamento!")
                    return
            
            ticket_mod_role = interaction.guild.get_role(
                972164560058482764
            )
            overwrites = {
                interaction.guild.default_role: discord.PermissionOverwrite(view_channel=False),
                interaction.user: discord.PermissionOverwrite(view_channel=True),
                interaction.guild.me: discord.PermissionOverwrite(view_channel=True),
                ticket_mod_role: discord.PermissionOverwrite(view_channel=True),
            }
            ticket = await interaction.guild.create_text_channel(name=f"Ticket {interaction.user.id} ", overwrites=overwrites) 
            
            

            await interaction.response.send_message(ephemeral=True,content=f"Criei um ticket para você! {ticket.mention}")

            await ticket.send(embed=embedout)

        

class sugestao1(discord.ui.View):
    def __init__(self, *, timeout=1000000000000000000000):
        super().__init__(timeout=timeout)
    @discord.ui.button(label="Bot",style=discord.ButtonStyle.gray,emoji="🤖") # or .primary
    async def gray1_button(self,button:discord.ui.Button,interaction:discord.Interaction):
        button.disabled=True
        await interaction.response.edit_message(view=self)
    @discord.ui.button(label="Servidor discord",style=discord.ButtonStyle.gray,emoji="💻") # or .secondary/.grey
    async def gray2_button(self,button:discord.ui.Button,interaction:discord.Interaction):
        button.disabled=True
        await interaction.response.edit_message(view=self)
    @discord.ui.button(label="Servidor lfs",style=discord.ButtonStyle.gray,emoji="🏎") # or .success
    async def gray3_button(self,button:discord.ui.Button,interaction:discord.Interaction):
        button.disabled=True
        await interaction.response.edit_message(view=self)
    @discord.ui.button(label="Fechar",style=discord.ButtonStyle.red,emoji="❌") # or .success
    async def red_button(self,button:discord.ui.Button,interaction:discord.Interaction):
        await interaction.guild.delete_text_channel()
   
class reportar1(discord.ui.View):
    def __init__(self, *, timeout=1000000000000000000000):
        super().__init__(timeout=timeout)
    @discord.ui.button(label="Bot Bug",style=discord.ButtonStyle.gray,emoji="⚙️") # or .primary
    async def gray1_button(self,button:discord.ui.Button,interaction:discord.Interaction):
        button.disabled=True
        await interaction.response.edit_message(view=self)
    @discord.ui.button(label="Servidor discord",style=discord.ButtonStyle.gray,emoji="🚨") # or .secondary/.grey
    async def gray2_button(self,button:discord.ui.Button,interaction:discord.Interaction):
        button.disabled=True
        await interaction.response.edit_message(view=self)
    @discord.ui.button(label="Servidor lfs",style=discord.ButtonStyle.gray,emoji="🏎") # or .success
    async def gray3_button(self,button:discord.ui.Button,interaction:discord.Interaction):
        button.disabled=True
        await interaction.response.edit_message(view=self)
    @discord.ui.button(label="Fechar",style=discord.ButtonStyle.red,emoji="❌") # or .success
    async def red_button(self,button:discord.ui.Button,interaction:discord.Interaction):
        await interaction.guild.channel.delete()

class denunciar1(discord.ui.View):
    def __init__(self, *, timeout=1000000000000000000000):
        super().__init__(timeout=timeout)
    @discord.ui.button(label="Servidor discord",style=discord.ButtonStyle.gray,emoji="💻") # or .secondary/.grey
    async def gray1_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        embedden1=discord.Embed(title='💻  Denunciar/Discord  💻',
        description = f"{interaction.user.mention}.\n\n**Me fale o nome do individuo (De quem esta sendo denunciado).**",
        color = 0xff0000
        )
        
        await interaction.response.delete_original_message()
        await interaction.response.send_message(embed=embedden1)
    @discord.ui.button(label="Servidor lfs",style=discord.ButtonStyle.green,emoji="🏎") # or .success
    async def gray2_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        embedden2=discord.Embed(title='🏎  Denunciar/Live for Speed  🏎',
        description = f"{interaction.user.mention}.\n\n**Me fale o USUARIO do individuo (De quem esta sendo denunciado).**\nObs: Nick não e usuario",
        color = 0xffc200
        )
        
        await interaction.response.delete_message()
        await interaction.response.send_message(embed=embedden2)
    @discord.ui.button(label="Fechar",style=discord.ButtonStyle.red,emoji="❌") # or .success
    async def red_button(self,button:discord.ui.Button,interaction:discord.Interaction):
        await interaction.guild.channel.delete()
        
   
class unban1(discord.ui.View):
    def __init__(self, *, timeout=1000000000000000000000):
        super().__init__(timeout=timeout)
    @discord.ui.button(label="Bot Bug",style=discord.ButtonStyle.gray,emoji="⚙️") # or .primary
    async def gray1_button(self,button:discord.ui.Button,interaction:discord.Interaction):
        button.disabled=True
        await interaction.response.edit_message(view=self)
    @discord.ui.button(label="Servidor discord",style=discord.ButtonStyle.gray,emoji="🚨") # or .secondary/.grey
    async def gray2_button(self,button:discord.ui.Button,interaction:discord.Interaction):
        button.disabled=True
        await interaction.response.edit_message(view=self)
    @discord.ui.button(label="Servidor lfs",style=discord.ButtonStyle.gray,emoji="🏎") # or .success
    async def gray3_button(self,button:discord.ui.Button,interaction:discord.Interaction):
        button.disabled=True
        await interaction.response.edit_message(view=self)
    @discord.ui.button(label="Fechar",style=discord.ButtonStyle.red,emoji="❌") # or .success
    async def red_button(self,button:discord.ui.Button,interaction:discord.Interaction):
        await interaction.guild.channel.delete()

class duvida1(discord.ui.View):
    def __init__(self, *, timeout=1000000000000000000000):
        super().__init__(timeout=timeout)
    @discord.ui.button(label="Bot Bug",style=discord.ButtonStyle.gray,emoji="⚙️") # or .primary
    async def gray1_button(self,button:discord.ui.Button,interaction:discord.Interaction):
        button.disabled=True
        await interaction.response.edit_message(view=self)
    @discord.ui.button(label="Servidor discord",style=discord.ButtonStyle.gray,emoji="🚨") # or .secondary/.grey
    async def gray2_button(self,button:discord.ui.Button,interaction:discord.Interaction):
        button.disabled=True
        await interaction.response.edit_message(view=self)
    @discord.ui.button(label="Servidor lfs",style=discord.ButtonStyle.gray,emoji="🏎") # or .success
    async def gray3_button(self,button:discord.ui.Button,interaction:discord.Interaction):
        button.disabled=True
        await interaction.response.edit_message(view=self)
    @discord.ui.button(label="Fechar",style=discord.ButtonStyle.red,emoji="❌") # or .success
    async def red_button(self,button:discord.ui.Button,interaction:discord.Interaction):
        await interaction.guild.channel.delete()

class SelectView2(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(selec1())
class ticket1(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

        global guild
        guild = self.bot.get_guild(GUILD_ID)
    @app_commands.command(
        name = "ticket",
        description = "Crie uma messagem de ticket (Somente adms)"
    )
    
    async def ticket1(
        self,
        interaction: discord.Interaction
        ):
        embedtick=discord.Embed(title='📩 Central de Tickets da Dlr 📩',
        description = '❗️ **Precisa de ajuda? use o menu abaixo** ❗️\n\n👉 Se não tiver o que você procura escolha **outros**. 👈🏽\n\n👊🏽 Desde já agradeço por entrar com contato com nossa equipe.',
        color = 0x7a00ff
        )
        embedtick.set_footer(text = "Dlr Management 👨🏽‍💻")
        await interaction.response.defer()
        await interaction.followup.send(embed=embedtick, view=SelectView2())
        
    
    
    

async def setup(bot: commands.Bot) -> None:
    
    await bot.add_cog(
        
        ticket1(bot),
        guilds = [discord.Object(id = 972164559915847810)],
        
        
    )