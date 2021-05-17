# does not validate the input with if statement
def Search(clips, search):
    try:
        matched_indexes = []
        i = 0
        length = len(clips)

        while i < length:
            if search == clips[i]:
                matched_indexes.append(i)
            i += 1

        # print(f'{search} is present in list at indexes {matched_indexes}')
        return matched_indexes
    except:
        return -1