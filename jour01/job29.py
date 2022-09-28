def arrondi_note(note):
    nb_notes = len(note)
    note_arr = []
    for i in range(nb_notes):
        if note[i] > 40:
            reste = note[i] % 5
            if reste >= 3:
                note_arr.append((note[i]// 5 + 1)*5)
            else:
                note_arr.append(note[i])
        else:
            note_arr.append(note[i])
    print(note_arr)
arrondi_note([32 , 40 , 82 , 83])