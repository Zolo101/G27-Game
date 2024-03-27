from src.classes.SceneManager import Scene


def draw(manager, canvas, clock, frame, interaction):
    """ This gets run on every frame. """
    frame.set_canvas_background('rgb(100,5,25)')
    canvas.draw_text(
        'Harken ye to this saga, a chronicle most dire of one valorous soul whose mettle was tryed \'gainst legions of the unliving. ', (90, 160), 20, 'Yellow', 'sans-serif')
    canvas.draw_text(
        'In a realm belaboured by foul sorcery, where earth and stone took shape unnaturaled and cubistic, there roamed foul creatures ',
        (90, 200), 20, 'Yellow', 'sans-serif')
    canvas.draw_text(
        'noisome and vile, the shriven risen from restless graves. Ordgar was a stout-hearted man of simple means, content to till the ',
        (90, 240), 20, 'Yellow', 'sans-serif')
    canvas.draw_text(
        'loamy soil and reap its giving harvest. His plowlands lay bounded by sturdy ramparts of oaken timbers, the hard-won prizes of ',
        (90, 280), 20, 'Yellow', 'sans-serif')
    canvas.draw_text(
        'an honest life well-lived. Behind those stout palisades stood his humble cottage of wattle and thatch, welcoming abode to home',
        (90, 320), 20, 'Yellow', 'sans-serif')
    canvas.draw_text(
        'and hearth. But warding home this fateful morn, looking beyond his well-turned furrows, Ordgar\'s eye was caught by motion ',
        (90, 360), 20, 'Yellow', 'sans-serif')
    canvas.draw_text(
        'alien and unsettling - as the sickly light stretched across the fields, it revealed the horror of lifeless husks lurching from',
        (90, 400), 20, 'Yellow', 'sans-serif')
    canvas.draw_text(
        'prairie and from fen. Ordgar emerged from his battered holdfast, head bowed in reverent thanks for deliverance unforeseen. He',
        (90, 440), 20, 'Yellow', 'sans-serif')
    canvas.draw_text(
        'vowed that whatever sorcery had given rise to such abominations, it would find no easy purchase whilst a stout heart and valiant',
        (90, 480), 20, 'Yellow', 'sans-serif')
    canvas.draw_text(
        'arm remained to guard the lands. This day\'s trial, though dark, was but the first redoubt defended.',
        (90, 520), 20, 'Yellow', 'sans-serif')

    canvas.draw_text(
        'SURVIVE THE FIVE NIGHTS AND CONQUER!!!!!!!!!!!',
        (90, 650), 40, 'Yellow', 'sans-serif')

    canvas.draw_text('Press \' space \' to start game', (720, 760), 20, 'Yellow', 'sans-serif')
    canvas.draw_text('Press \' o \' to go back to welcome screen', (320, 760), 20, 'Yellow', 'sans-serif')

    if interaction.get_key("space"):
        manager.switch_scene("main")
    if interaction.get_key("o"):
        manager.switch_scene("welcome")


def tick(manager, clock, frame, interaction):
    pass


backstory = Scene("backstory", draw, tick)
