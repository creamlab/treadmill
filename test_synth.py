from synthesizer import Player, Synthesizer, Waveform


player = Player()
player.open_stream()
synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
# # Play A4
player.play_wave(synthesizer.generate_constant_wave(440.0, 3.0))

# Play C major
chord = ["C2", "D4", "G3"]
player.play_wave(synthesizer.generate_chord(chord, 3.0))

# You can also specify frequencies to play just intonation
# chord = [440.0, 500.0, 700.0]
# player.play_wave(synthesizer.generate_chord(chord, 3.0))