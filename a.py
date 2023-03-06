class View(discord.ui.View):
    
    def __init__(self):
        super().__init__(timeout=None)
        
    
    @discord.ui.button(label="Votar", style=discord.ButtonStyle.green, emoji="✅", custom_id='persistent_view:green')
    async def green_button(self,interaction:discord.Interaction, button:discord.ui.Button):
        

        # Consultar o banco de dados para obter informações sobre a mensagem e a votação atual
        cursor.execute("SELECT id_user, url, author, content, votos FROM main WHERE message_id = ?", (interaction.message.id,))
        result = cursor.fetchone()
        
        if result is not None:
            id_user, url, author, content, votos = result
        else:
            await interaction.response.defer()
            await interaction.followup.send(content="A mensagem não foi encontrada no banco de dados!", ephemeral=True)
            return

        if id_user is not None:
            if id_user == interaction.user.id:

                # A mensagem já foi votada pelo usuário
                await interaction.response.defer()
                await interaction.followup.send(content="Você já votou nesta foto!", ephemeral=True)
            else:
                
                votos += 1 
            
                sql = ("UPDATE main SET id_user = id_user || ?, votos = ? WHERE message_id = ?")
                val = (interaction.user.id, votos, interaction.message.id)
                
                cursor.execute(sql, val)
                conn.commit()
        else:
            
            # A mensagem ainda não foi votada pelo usuário
            idu = str(interaction.user.id)
            votos += 1 
            
            sql = ("UPDATE main SET id_user = ?, votos = ? WHERE message_id = ?")
            val = (idu, votos, interaction.message.id)
            
            cursor.execute(sql, val)
            conn.commit()

        embed3 = discord.Embed(title='📸  Nova Foto Enviada  📸, Votos {}'.format(votos), 
            description=f'Foto de {author}\nJogo: {content}', color=3407616)
        embed3.set_image(url=url)
        if interaction.response.is_done():
            return
        else:
            await interaction.response.edit_message(embed=embed3, view=View())