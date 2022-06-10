import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=300)
inst1_id = dpg.generate_uuid()
inst2_id = dpg.generate_uuid()

with dpg.window(label="Instrument Calc"):
    dpg.add_text("Welcome to the Instrument Calculator")
    dpg.add_input_text(label="Instrument 1", width=200, tag=inst1_id)
    dpg.add_button(label="Save")
    dpg.add_input_text(label="Instrument 2", width=200, tag=inst2_id)
    dpg.add_button(label="Save")
    
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()