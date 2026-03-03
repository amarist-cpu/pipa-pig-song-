def on_button_pressed_a():
    music.play(music.tone_playable(784, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(659, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(523, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(587, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(392, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(392, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(494, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(587, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(698, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(659, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(523, music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(len("I am pippa pig "), music.beat(BeatFraction.WHOLE)),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.A, on_button_pressed_a)
