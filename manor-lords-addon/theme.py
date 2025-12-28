import dearpygui.dearpygui as dpg

TRACKED_RESOURCES = {
    'Ale': {
        'color': [205, 177, 154]
    },
    'Approval': {
        'color': [68, 124, 51]
    },
    'Berries': {
        'color': [139, 97, 223]
    },
    'Clay': {
        'color': [255, 187, 178]
    },
    'Eggs': {
        'color': [225, 210, 184]
    },
    'Firewood': {
        'color': [190, 140, 76]
    },
    'Hides': {
        'color': [163, 128, 104]
    },
    'Iron Ore': {
        'color': [175, 58, 69]
    },
    'Leather': {
        'color': [85, 54, 38]
    },
    'Meat': {
        'color': [178, 80, 78]
    },
    'Planks': {
        'color': [220, 142, 91]
    },
    'Regional Wealth': {
        'color': [188, 174, 154]
    },
    'Roof Tiles': {
        'color': [225, 138, 0]
    },
    'Stone': {
        'color': [126, 124, 126]
    },
    'Timber': {
        'color': [72, 36, 35]
    },
    'Vegetables': {
        'color': [241, 160, 125]
    },
}

def setupGlobalAllRules():
    baseColor = [48, 55, 78]
    tileColor = [18, 23, 42]
    gridColor = [92, 92, 92]
    textColor = [195, 195, 195]

    # Frame + bgs
    dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 10, category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvPlotCol_FrameBg, tileColor, category=dpg.mvThemeCat_Plots)
    dpg.add_theme_color(dpg.mvPlotCol_PlotBg, tileColor, category=dpg.mvThemeCat_Plots)
    dpg.add_theme_color(dpg.mvThemeCol_FrameBg, tileColor, category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_WindowBg, baseColor, category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_ChildBg, tileColor, category=dpg.mvThemeCat_Core)
    dpg.add_theme_style(dpg.mvStyleVar_ChildRounding, 10, category=dpg.mvThemeCat_Core)

    # Axis styling
    dpg.add_theme_color(dpg.mvPlotCol_PlotBorder, baseColor, category=dpg.mvThemeCat_Plots)

    # Font
    dpg.set_global_font_scale(1.2)
    dpg.add_theme_color(dpg.mvThemeCol_Text, textColor, category=dpg.mvThemeCat_Core)

    # Grid
    dpg.add_theme_style(dpg.mvPlotStyleVar_MinorGridSize, 3, category=dpg.mvThemeCat_Plots)
    dpg.add_theme_color(dpg.mvPlotCol_XAxisGrid, gridColor, category=dpg.mvThemeCat_Plots)
    dpg.add_theme_color(dpg.mvPlotCol_YAxisGrid, gridColor, category=dpg.mvThemeCat_Plots)

    # Line + Marker
    dpg.add_theme_color(dpg.mvPlotCol_Line, (150, 255, 0), category=dpg.mvThemeCat_Plots)
    # dpg.add_theme_style(dpg.mvPlotStyleVar_Marker, dpg.mvPlotMarker_Circle, category=dpg.mvThemeCat_Plots)
    # dpg.add_theme_color(dpg.mvPlotCol_MarkerOutline, tileColor, dpg.mvPlotMarker_Circle, category=dpg.mvThemeCat_Plots)
    # dpg.add_theme_style(dpg.mvPlotStyleVar_MarkerSize, 4, dpg.mvPlotMarker_Circle, category=dpg.mvThemeCat_Plots)
    dpg.add_theme_style(dpg.mvPlotStyleVar_LineWeight, 4, dpg.mvPlotMarker_Circle, category=dpg.mvThemeCat_Plots)

def setupButtonStyling():
    dpg.add_theme_color(dpg.mvThemeCol_Button, (0, 0, 0, 0))
    dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (0, 0, 0, 0))
    dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (0, 0, 0, 0))

def setupTextures():
    # Setup icons for all resources
    for resource in TRACKED_RESOURCES:
        iconPath = f"./assets/{resource}.png"
        width, height, channels, imgData = dpg.load_image(iconPath)

        dpg.add_static_texture(width=width, height=height, default_value=imgData, tag=f"{resource}_icon")

def setupResourceTheme(label: str):
    with dpg.theme(tag=label):
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvPlotCol_Line, TRACKED_RESOURCES[label]['color'], category=dpg.mvThemeCat_Plots)