import dearpygui.dearpygui as dpg
from graphe import graphe
dpg.create_context()

slider_ids = []

with dpg.window(label="Exemple"):
    # Création de plusieurs sliders
    slider_ids.append(dpg.add_slider_int(label="nombre de personnes", default_value=20, max_value=50))
    slider_ids.append(dpg.add_slider_float(label="Slider 2", default_value=0.5, max_value=1.0))
    slider_ids.append(dpg.add_slider_float(label="Slider 3", default_value=0.8, max_value=1.0))
    
    def start_callback():
        valeurs = [dpg.get_value(s) for s in slider_ids]
        print("Valeurs des sliders au Start :", valeurs)
    
    dpg.add_button(label="Start", callback=start_callback)

dpg.create_viewport(title='Demo', width=400, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()


slider_ids[0]