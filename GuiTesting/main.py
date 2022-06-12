import dearpygui.dearpygui as dpg

# dpg.create_context()
# dpg.create_viewport(title='Custom Title', width=700, height=300)



# dpg.setup_dearpygui()
# dpg.show_viewport()
# dpg.start_dearpygui()
# dpg.destroy_context()



dpg.create_context()
dpg.create_viewport(title="dearPyGui Window", width=700, height=300)
dpg.setup_dearpygui()
dpg.show_viewport()

with dpg.window(label="Example Window") as window:
    dpg.add_text("Hello, world")
    dpg.add_button(label="Save")
    dpg.add_input_text(label="string", default_value="Quick brown fox")
    dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

dpg.set_primary_window(window, True)

dpg.start_dearpygui()
dpg.destroy_context()

print(inputer)