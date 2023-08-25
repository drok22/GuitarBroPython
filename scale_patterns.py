CHROMATIC_SCALE = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]


def minor_scale_pattern(key):
    '''Minor Scale Pattern - whole, half, whole, whole, half, whole, whole'''
    scale_pattern = []
    next_step = key

    # add the root note
    scale_pattern.append(next_step)

    for step in range(1, 7):
        if step == 2 or step == 5:
            next_step = find_next_interval(1, next_step)
        else:
            next_step = find_next_interval(2, next_step)
        scale_pattern.append(next_step)

    return scale_pattern


def major_scale_pattern(key):
    '''Major Scale Pattern - whole, whole, half, whole, whole, whole, half'''
    scale_pattern = []
    next_step = key

    # add the root note
    scale_pattern.append(next_step)

    for step in range(1, 7):
        if step == 3 or step == 7:
            next_step = find_next_interval(1, next_step)
        else:
            next_step = find_next_interval(2, next_step)
        scale_pattern.append(next_step)

    return scale_pattern


def pentatonic_pattern(key, is_major):
    '''Creates a pentatonic scale for a given key'''
    if is_major:
        return major_pentatonic_pattern(key)
    else:
        return minor_pentatonic_pattern(key)


def minor_pentatonic_pattern(key):
    '''Minor Pentatonic Pattern - 3,2,2,3 (semitones)'''
    scale_pattern = []
    next_step = key

    # add the root note
    scale_pattern.append(next_step)

    for step in range(1, 5):
        if step == 2 or step == 3:
            next_step = find_next_interval(2, next_step)
        else:
            next_step = find_next_interval(3, next_step)

        scale_pattern.append(next_step)

    return scale_pattern


def major_pentatonic_pattern(key):
    '''Major Pentatonic Pattern - 2,2,3,2 (semitones)'''
    scale_pattern = []
    next_step = key

    # add the root note
    scale_pattern.append(next_step)

    for step in range(1, 5):
        if step == 3:
            next_step = find_next_interval(3, next_step)
        else:
            next_step = find_next_interval(2, next_step)

        scale_pattern.append(next_step)

    return scale_pattern


def blues_pattern(key, is_major):
    '''Creates a blues scale for a given key'''
    if is_major:
        return major_blues_pattern(key)
    else:
        return minor_blues_pattern(key)


def minor_blues_pattern(key):
    '''Minor Blues Pattern - 3,2,1,1,3 (semitones)'''
    scale_pattern = []
    next_step = key

    # add the root note
    scale_pattern.append(next_step)

    for step in range(1, 6):
        if step == 3 or step == 4:
            next_step = find_next_interval(1, next_step)
        elif step == 2:
            next_step = find_next_interval(2, next_step)
        else:
            next_step = find_next_interval(3, next_step)

        scale_pattern.append(next_step)

    return scale_pattern


def major_blues_pattern(key):
    '''Major Blues Pattern - 2,1,1,3,2 (semitones)'''
    scale_pattern = []
    next_step = key

    # add the root note
    scale_pattern.append(next_step)

    for step in range(1, 6):
        if step == 2 or step == 3:
            next_step = find_next_interval(1, next_step)
        elif step == 1 or step == 5:
            next_step = find_next_interval(2, next_step)
        else:
            next_step = find_next_interval(3, next_step)

        scale_pattern.append(next_step)

    return scale_pattern


def update_scale_pattern(scale_name, key, is_major):
    pass


def find_next_interval(interval, note):
    ''' take the indicated number of steps forward in the chromatic scale
    then, safety check to stay in bounds of CHROMATIC_SCALE. Return result'''

    index = CHROMATIC_SCALE.index(note) + interval

    if index >= 12:
        index -= 12

    next_step = CHROMATIC_SCALE[index]

    return next_step


def find_third(note):
    return find_next_interval(3, note)


def find_fourth(note):
    return find_next_interval(4, note)


def find_fifth(note):
    return find_next_interval(5, note)


def find_sixth(note):
    return find_next_interval(6, note)


def find_seventh(note):
    return find_next_interval(7, note)
