from nicegui import ui

with ui.tabs() as tabs:
 ui.tab("Home", icon="home")
 ui.tab("About me", icon="info")
with ui.tab_panels(tabs, value='Home'):
    with ui.tab_panel('Home'):
     ui.label("Welcome to iPig's Website").style("font-size: 30px")
    with ui.tab_panel('About me'):
     ui.label("About me").style("font-size: 30px")
     ui.label("I'm iPig, a new programmer from Taiwan. I'm currently learning Python.")
     ui.icon("discord", size="30px").style("display: inline-block; margin-right: 5px;")
     ui.label("iPig#9689").style("display: inline-block; font-size: 17px;")
     ui.button("YouTube Channel", on_click=lambda: ui.open("https://youtube.com/@ipigtaiwan")).style("display: block;").props("color=red")
     ui.button("Discord Server",on_click=lambda: ui.open("https://discord.gg/Px4wHz9GrW")).style("display: block; margin-top: 10px; ")
     ui.button("Monkeytype profile", on_click=lambda: ui.open("https://monkeytype.com/profile/iPig")).style("display: block; margin-top: 10px;").props("color=blue")

ui.run(title="iPig's Website", favicon="roblox pig.jpg")