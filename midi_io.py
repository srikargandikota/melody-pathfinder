from music21 import stream, note, tempo, meter, instrument

def melody_to_midi(notes, bpm=96, out_path="melody.mid"):
    s = stream.Stream()
    s.append(tempo.MetronomeMark(number=bpm))
    s.append(meter.TimeSignature('4/4'))
    s.append(instrument.Piano())
    for n in notes:
        s.append(note.Note(n, quarterLength=1.0))
    s.write('midi', fp=out_path)
    return out_path
