import time
from threading import Thread
import dearpygui.dearpygui as dpg

from dataParser import transformDataForChart
from theme import setupButtonStyling, setupGlobalAllRules, setupResourceTheme, setupTextures

viewportWidth = 1000
viewportHeight = 800
buttonsWrapperWidth = 200
chartWrapperWidth = viewportWidth - buttonsWrapperWidth - 50
chartWrapperHeight = viewportHeight - 50
chartWidth = chartWrapperWidth
chartHeight = chartWrapperHeight
titleBarDrag = False

dpg.create_context()

# Theme setup
with dpg.theme(tag="global_theme") as global_theme:
    with dpg.theme_component(dpg.mvAll):
        setupGlobalAllRules()

    with dpg.theme_component(dpg.mvButton):
        setupButtonStyling()

# Texture setup
with dpg.texture_registry():
    setupTextures()

def exit():
    dpg.destroy_context()

def updateChartData():
    while True:
        xData, yData = transformDataForChart()

        for resource in yData:
            dpg.configure_item(f"{resource}-series", x=xData, y=yData[resource])

            newBtnLabel = f"{resource} {int(yData[resource][len(yData[resource]) - 1])}"
            dpg.configure_item(f"{resource}-btn", label=newBtnLabel)

        time.sleep(6)

dpg.bind_theme(global_theme)

viewport = dpg.create_viewport(
    title="Manor Lords Economy",
    width=viewportWidth,
    height=viewportHeight,
    decorated=False,
    resizable=False,
    always_on_top=True
)
dpg.setup_dearpygui()

with dpg.window(
    label="Manor Lords Economy",
    no_collapse=True,
    no_move=True,
    no_resize=True,
    on_close=exit,
    # no_title_bar=True,
    width=viewportWidth
):
    xData, yData = transformDataForChart()
    chartWindow = dpg.add_child_window(tag="chart_wrapper", width=chartWrapperWidth, height=chartWrapperHeight, border=False, pos=[buttonsWrapperWidth + 30, 30])
    buttonsWindow = dpg.add_child_window(tag="buttons_wrapper", before=chartWindow, width=buttonsWrapperWidth, border=False, no_scrollbar=True)

    # Generate buttons
    for resource in yData:
        buttonWindow = dpg.add_child_window(tag=f"button_{resource}_wrapper", parent=buttonsWindow, border=False, height=60)
        btnLabel = f"{resource} {int(yData[resource][len(yData[resource]) - 1])}"
        btn = dpg.add_button(label=btnLabel, parent=buttonWindow, tag=f"{resource}-btn", height=60, pos=[60, -5])
        dpg.add_image(f"{resource}_icon", before=btn, width=55, height=50)

    # Create plot
    with dpg.plot(
        label="Line Series",
        height=chartHeight,
        width=chartWidth,
        no_menus=True,
        no_title=True,
        tag="plot",
        anti_aliased=True,
        parent=chartWindow,
        use_local_time=True
    ):
        dpg.add_plot_axis(dpg.mvXAxis, label="Time", tag="x_axis", time=True)
        dpg.add_plot_axis(dpg.mvYAxis, tag="y_axis")

        for resource in yData:
            line = dpg.add_line_series(xData, yData[resource], label=resource, parent="y_axis", tag=f"{resource}-series")
            setupResourceTheme(resource)
            dpg.bind_item_theme(line, resource)

        thread = Thread(target=updateChartData)
        thread.start()

def onMouseMove(sender,data):
    global titleBarDrag

    if dpg.is_mouse_button_down(0):
        y = data[1]

        if -10 <= y <=25:
            titleBarDrag = True
        else:
            titleBarDrag = False

def setupWindowPosition(sender, data):
    global titleBarDrag
    
    if titleBarDrag:
        pos = dpg.get_viewport_pos()
        x = data[1]
        y = data[2]
        final_x = pos[0] + x
        final_y = pos[1] + y

        dpg.configure_viewport(viewport, x_pos=final_x, y_pos=final_y)

with dpg.handler_registry():
    dpg.add_mouse_move_handler(callback=onMouseMove)
    dpg.add_mouse_drag_handler(button=0, callback=setupWindowPosition)

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()