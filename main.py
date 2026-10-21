def on_button_pressed_a():
    basic.show_leds("""
        . # # # .
        # . . . #
        # . . . #
        . # # # .
        # . . . .
        """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    basic.show_icon(IconNames.ANGRY)
    music._play_default_background(music.built_in_playable_melody(Melodies.CHASE),
        music.PlaybackMode.IN_BACKGROUND)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_touched():
    basic.show_icon(IconNames.HAPPY)
    music._play_default_background(music.built_in_playable_melody(Melodies.JUMP_UP),
        music.PlaybackMode.IN_BACKGROUND)
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

def on_sound_loud():
    basic.show_icon(IconNames.SAD)
    music._play_default_background(music.built_in_playable_melody(Melodies.BADDY),
        music.PlaybackMode.IN_BACKGROUND)
input.on_sound(DetectedSound.LOUD, on_sound_loud)

def on_button_pressed_b():
    basic.show_icon(IconNames.NO)
    music._play_default_background(music.built_in_playable_melody(Melodies.JUMP_DOWN),
        music.PlaybackMode.IN_BACKGROUND)
input.on_button_pressed(Button.B, on_button_pressed_b)
