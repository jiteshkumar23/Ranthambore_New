from human_mouse import MouseController

# Initialize globally or within a class if preferred
mouse = MouseController()

def human_click(location, speed=1.0):
    if isinstance(location, tuple) and len(location) >= 2:
        x, y = location[0], location[1]
    elif hasattr(location, 'x') and hasattr(location, 'y'):
        x, y = location.x, location.y
    else:
        raise ValueError("Invalid location format")

    mouse.move(x, y, speed_factor=speed)
    mouse.perform_click(x, y)