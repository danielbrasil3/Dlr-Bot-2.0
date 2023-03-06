import discord
from discord import app_commands
from discord.ext import commands
from discord.app_commands import Choice













class Select(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="Homem",  emoji="🧑🏼"),
            discord.SelectOption(label="Mulher",  emoji="👱🏼‍♀️"),
            discord.SelectOption(label="Não binario",  emoji="🌈")
            ]
        super().__init__(placeholder="⚧ Escolha seu genero ⚧",max_values=1,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction,):
        cargo_home = interaction.guild.get_role(972164559961980986)
        cargo_mulher = interaction.guild.get_role(972164559961980985)
        cargonao_binario = interaction.guild.get_role(972164559961980984)
        if self.values == ["Homem"]:
            await interaction.user.add_roles(cargo_home)
            await interaction.user.remove_roles(cargo_mulher)
            await interaction.user.remove_roles(cargonao_binario)

        elif self.values == ["Mulher"]:
            await interaction.user.add_roles(cargo_mulher)
            await interaction.user.remove_roles(cargo_home)
            await interaction.user.remove_roles(cargonao_binario)

        else:
            await interaction.user.add_roles(cargonao_binario)
            await interaction.user.remove_roles(cargo_home)
            await interaction.user.remove_roles(cargo_mulher)
        
        await interaction.response.defer()

class Select1(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="-18",  emoji="🔞"),
            discord.SelectOption(label="+18",  emoji="🍺")
            
            ]
        super().__init__(placeholder="🔞 Escolha sua idade 🍺",max_values=1,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        cargo_maior = interaction.guild.get_role(972164559982981253)
        cargo_menor = interaction.guild.get_role(972164559982981252)
        if self.values == ["-18"]:
            await interaction.user.add_roles(cargo_menor)
            await interaction.user.remove_roles(cargo_maior)
        else:
            await interaction.user.add_roles(cargo_maior)
            await interaction.user.remove_roles(cargo_menor)
        
        await interaction.response.defer()

class Select2(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="Pc",  emoji="💻"),
            discord.SelectOption(label="Celular",  emoji="📱")
            
            ]
        super().__init__(placeholder="💻 Escolha sua plataforma 📱",max_values=2,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        cargo_pc = interaction.guild.get_role(972164559982981251)
        cargo_cell = interaction.guild.get_role(972164559961980988)
        
        
        if self.values == ["Pc"]:
            await interaction.user.add_roles(cargo_pc)
            await interaction.user.remove_roles(cargo_cell)
        elif self.values == ["Celular"]:
            await interaction.user.add_roles(cargo_cell)
            await interaction.user.remove_roles(cargo_pc)
        else:
            await interaction.user.add_roles(cargo_pc)
            await interaction.user.add_roles(cargo_cell)
        
        await interaction.response.defer()

class Select3(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="Conteudo lfs",  emoji="🛻"),
            discord.SelectOption(label="Comunidade",  emoji="💬"),
            discord.SelectOption(label="Outros jogos",  emoji="🎮")
            ]
        super().__init__(placeholder="🎮 Escolha oque deseja ver 🌐",max_values=3,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        cargo_clfs = interaction.guild.get_role(972164560003944485)
        cargo_comu = interaction.guild.get_role(972164559941017685)
        cargo_out = interaction.guild.get_role(972164560003944486)
        
        if self.values == ["Conteudo lfs"] + ["Comunidade"]:
            
            await interaction.user.add_roles(cargo_clfs)
            await interaction.user.add_roles(cargo_comu)
            await interaction.user.remove_roles(cargo_out)
            
        elif self.values == ["Comunidade"] + ["Conteudo lfs"]:
            
            await interaction.user.add_roles(cargo_clfs)
            await interaction.user.add_roles(cargo_comu)
            await interaction.user.remove_roles(cargo_out)
            
        elif self.values == ["Outros jogos"] + ["Comunidade"]:

            await interaction.user.add_roles(cargo_out)
            await interaction.user.add_roles(cargo_comu)
            await interaction.user.remove_roles(cargo_clfs)
            
        elif self.values == ["Comunidade"] + ["Outros jogos"]:
            
            await interaction.user.add_roles(cargo_out)
            await interaction.user.add_roles(cargo_comu)
            await interaction.user.remove_roles(cargo_clfs)

        elif self.values == ["Conteudo lfs"] + ["Outros jogos"]:
            
            await interaction.user.add_roles(cargo_clfs)
            await interaction.user.add_roles(cargo_out)
            await interaction.user.remove_roles(cargo_comu)

        elif self.values == ["Outros jogos"] + ["Conteudo lfs"]:
            
            await interaction.user.add_roles(cargo_clfs)
            await interaction.user.add_roles(cargo_out)
            await interaction.user.remove_roles(cargo_comu)

        else:
            if self.values == ["Conteudo lfs"]:
                await interaction.user.add_roles(cargo_clfs)
                await interaction.user.remove_roles(cargo_comu)
                await interaction.user.remove_roles(cargo_out)
            elif self.values == ["Comunidade"]:
                await interaction.user.add_roles(cargo_comu)
                await interaction.user.remove_roles(cargo_out)
                await interaction.user.remove_roles(cargo_clfs)

            elif self.values == ["Outros jogos"]:
                await interaction.user.add_roles(cargo_out)
                await interaction.user.remove_roles(cargo_comu)
                await interaction.user.remove_roles(cargo_clfs)
            else:
                await interaction.user.add_roles(cargo_out)
                await interaction.user.add_roles(cargo_comu)
                await interaction.user.add_roles(cargo_clfs)
        
        
        
        await interaction.response.defer()
class Select4(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="Comunidade ping",  emoji="📢"),
            discord.SelectOption(label="LFS ping",  emoji="🚘"),
            discord.SelectOption(label="Parcerias ping",  emoji="👊🏾"),
            discord.SelectOption(label="Sorteios ping",  emoji="🎁")
            ]
        super().__init__(placeholder="⚠️ Escolha onde quer ser notificado 🔔",max_values=4,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        cargo_comup = interaction.guild.get_role(972164559961980982)
        cargo_lfsp = interaction.guild.get_role(972164559961980981)
        cargo_pp = interaction.guild.get_role(972164559961980979)
        cargo_sp = interaction.guild.get_role(972164559961980983)
        
        if self.values == ["Parcerias ping", "Comunidade ping", "LFS ping"] or self.values == ["Parcerias ping", "LFS ping", "Comunidade ping"] or self.values == ["LFS ping", "Comunidade ping", "Parcerias ping"] or self.values == ["LFS ping", "Parcerias ping", "Comunidade ping"] or self.values == ["Comunidade ping", "LFS ping", "Parcerias ping"] or self.values == ["Comunidade ping", "Parcerias ping", "LFS ping"]:
            
            await interaction.user.add_roles(cargo_lfsp)
            await interaction.user.add_roles(cargo_comup)
            await interaction.user.add_roles(cargo_pp)
            await interaction.user.remove_roles(cargo_sp)
            
        elif self.values == ["Sorteios ping", "Comunidade ping", "LFS ping"] or self.values == ["Sorteios ping", "LFS ping", "Comunidade ping"] or self.values == ["LFS ping", "Comunidade ping", "Sorteios ping"] or self.values == ["LFS ping", "Sorteios ping", "Comunidade ping"] or self.values == ["Comunidade ping", "LFS ping", "Sorteios ping"] or self.values == ["Comunidade ping", "Sorteios ping", "LFS ping"]:
            
            await interaction.user.add_roles(cargo_lfsp)
            await interaction.user.add_roles(cargo_comup)
            await interaction.user.add_roles(cargo_sp)
            await interaction.user.remove_roles(cargo_pp)

        elif self.values == ["Parcerias ping", "Comunidade ping", "Sorteios ping"] or self.values == ["Parcerias ping", "Sorteios ping", "Comunidade ping"] or self.values == ["Sorteios ping", "Comunidade ping", "Parcerias ping"] or self.values == ["Sorteios ping", "Parcerias ping", "Comunidade ping"] or self.values == ["Comunidade ping", "Sorteios ping", "Parcerias ping"] or self.values == ["Comunidade ping", "Parcerias ping", "Sorteios ping"]:
            
            await interaction.user.add_roles(cargo_sp)
            await interaction.user.add_roles(cargo_comup)
            await interaction.user.add_roles(cargo_pp)
            await interaction.user.remove_roles(cargo_lfsp)

        elif self.values == ["Parcerias ping", "Sorteios ping", "LFS ping"] or self.values == ["Parcerias ping", "LFS ping", "Sorteios ping"] or self.values == ["LFS ping", "Sorteios ping", "Parcerias ping"] or self.values == ["LFS ping", "Parcerias ping", "Sorteios ping"] or self.values == ["Sorteios ping", "LFS ping", "Parcerias ping"] or self.values == ["Sorteios ping", "Parcerias ping", "LFS ping"]:
            
            await interaction.user.add_roles(cargo_lfsp)
            await interaction.user.add_roles(cargo_sp)
            await interaction.user.add_roles(cargo_pp)
            await interaction.user.remove_roles(cargo_comup)

        else:
            if self.values == ["Comunidade ping", "LFS ping"] or self.values == ["LFS ping", "Comunidade ping"]:
                await interaction.user.add_roles(cargo_lfsp)
                await interaction.user.add_roles(cargo_comup)
                await interaction.user.remove_roles(cargo_pp)
                await interaction.user.remove_roles(cargo_sp)
            elif self.values == ["Comunidade ping", "Parcerias ping"] or self.values == ["Parcerias ping", "Comunidade ping"]:
                await interaction.user.add_roles(cargo_pp)
                await interaction.user.add_roles(cargo_comup)
                await interaction.user.remove_roles(cargo_lfsp)
                await interaction.user.remove_roles(cargo_sp)
            elif self.values == ["Comunidade ping", "Sorteios ping"] or self.values == ["Sorteios ping", "Comunidade ping"]:
                await interaction.user.add_roles(cargo_sp)
                await interaction.user.add_roles(cargo_comup)
                await interaction.user.remove_roles(cargo_lfsp)
                await interaction.user.remove_roles(cargo_pp)
            elif self.values == ["LFS ping", "Sorteios ping"] or self.values == ["Sorteios ping", "LFS ping"]:
                await interaction.user.add_roles(cargo_sp)
                await interaction.user.add_roles(cargo_lfsp)
                await interaction.user.remove_roles(cargo_comup)
                await interaction.user.remove_roles(cargo_pp)
            elif self.values == ["LFS ping", "Parcerias ping"] or self.values == ["Parcerias ping", "LFS ping"]:
                await interaction.user.add_roles(cargo_pp)
                await interaction.user.add_roles(cargo_lfsp)
                await interaction.user.remove_roles(cargo_comup)
                await interaction.user.remove_roles(cargo_sp)
            elif self.values == ["Sorteios ping", "Parcerias ping"] or self.values == ["Parcerias ping", "Sorteios ping"]:
                await interaction.user.add_roles(cargo_pp)
                await interaction.user.add_roles(cargo_sp)
                await interaction.user.remove_roles(cargo_comup)
                await interaction.user.remove_roles(cargo_lfsp)
            else:
                if self.values == ["Sorteios ping"]:
                    await interaction.user.add_roles(cargo_sp)
                    await interaction.user.remove_roles(cargo_comup)
                    await interaction.user.remove_roles(cargo_lfsp)
                    await interaction.user.remove_roles(cargo_pp)
                elif self.values == ["Parcerias ping"]:
                    await interaction.user.add_roles(cargo_pp)
                    await interaction.user.remove_roles(cargo_comup)
                    await interaction.user.remove_roles(cargo_lfsp)
                    await interaction.user.remove_roles(cargo_sp)
                elif self.values == ["LFS ping"]:
                    await interaction.user.add_roles(cargo_lfsp)
                    await interaction.user.remove_roles(cargo_comup)
                    await interaction.user.remove_roles(cargo_sp)
                    await interaction.user.remove_roles(cargo_pp)
                elif self.values == ["Comunidade ping"]:
                    await interaction.user.add_roles(cargo_comup)
                    await interaction.user.remove_roles(cargo_sp)
                    await interaction.user.remove_roles(cargo_pp)
                    await interaction.user.remove_roles(cargo_lfsp)
                else:
                    await interaction.user.add_roles(cargo_comup)
                    await interaction.user.add_roles(cargo_lfsp)
                    await interaction.user.add_roles(cargo_pp)
                    await interaction.user.add_roles(cargo_sp)
        await interaction.response.send_message(content=f"**Registro completo, Obrigado!**",ephemeral=True)

class SelectView(discord.ui.View):
    def __init__(self, *, timeout = None):
        super().__init__(timeout=timeout)
        self.add_item(Select())



class SelectView1(discord.ui.View):
    def __init__(self, *, timeout = None):
        super().__init__(timeout=timeout)
        self.add_item(Select1())

class SelectView2(discord.ui.View):
    def __init__(self, *, timeout = None):
        super().__init__(timeout=timeout)
        self.add_item(Select2())

class SelectView3(discord.ui.View):
    def __init__(self, *, timeout = None):
        super().__init__(timeout=timeout)
        self.add_item(Select3())

class SelectView4(discord.ui.View):
    def __init__(self, *, timeout = None):
        super().__init__(timeout=timeout)
        self.add_item(Select4())


    
class registro(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot



    @app_commands.command(
        name = "registro",
        description = "registro"
    )
    
    @app_commands.checks.has_any_role(972164560058482764, "👑 |CHEFE DLR" )

    async def registro1(
        self,
        interaction: discord.Interaction
        ):
        embedgenero=discord.Embed(title='⚧ | Registro/Gênero | ⚧',
        description = 'Escolha o seu gênero utilizando o menu abaixo',
        color = 0x7a00ff)

        embedidade=discord.Embed(title='🔞 | Registro/Idade | 🍺',
        description = 'Escolha o sua Idade utilizando o menu abaixo',
        color = 0xff0000)

        embedplataforma=discord.Embed(title='💻 | Registro/Plataforma | 📱',
        description = 'Escolha a sua Plataforma utilizando o menu abaixo',
        color = 0x00adff)

        embedacesso=discord.Embed(title='🎮 | Registro/Acesso | 🌐',
        description = 'Escolha o acesso de que você deseja ter',
        color = 0x00ffeb)

        embednotify=discord.Embed(title='⚠️ | Registro/Notificação | 🔔',
        description = 'Escolha de que você quer ser notificado',
        color = 0xff0070)
        await interaction.response.defer()
        await interaction.followup.send(embed = embedgenero, view=SelectView())
        await interaction.followup.send(embed = embedidade, view=SelectView1())
        await interaction.followup.send(embed = embedplataforma, view=SelectView2())
        await interaction.followup.send(embed = embedacesso, view=SelectView3())
        await interaction.followup.send(embed = embednotify, view=SelectView4())
        
        
    
    @registro1.error
    async def registro1Error(self, interaction : discord.Interaction, error : app_commands.AppCommandError):
        if isinstance(error, app_commands.MissingRole):
            await interaction.response.send_message("Você não tem permissão para isso", ephemeral = True)
    

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        registro(bot),
        guilds = [discord.Object(id = 972164559915847810)]
    )