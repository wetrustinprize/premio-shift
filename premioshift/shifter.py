from string import ascii_lowercase as alpha_lower, ascii_uppercase as alpha_upper

"""
Returns a encrypted or decrypted message.

Arguments:
    message (str): The message to use
    key (str): The key to use

kwargs:
    shift_to (int): Will shift to this location, requires: cur_shift
    cur_pos (int): The current shift location
    shift (int): Will shift this amount

Return:
    str: The final message
"""
def shift_message(message: str, key: str, **kwargs) -> str:

    # Shift to information
    cur_pos = kwargs.get("cur_pos", 0)
    shift_to = kwargs.get("shift_to", cur_pos)

    # Shift information
    shift = (shift_to - cur_pos) + kwargs.get("shift", 0)

    # Key information
    key_shifts = key_to_shifts(key)
    key_index = 0

    # Shift
    final_message = ""

    for char in message:
        shift_char = key_shifts[key_index] * shift
        final_char = char

        if char.isnumeric():
            # gets the last number in (char + shift_char)
            final_char = str(int(char)+shift_char)[-1]
        elif char.isalpha():
            # gets information
            char_upper = char.isupper()

            # gets the index
            char_index = alpha_lower.index(char.lower())

            char_index += shift_char

            # gets the correct index
            while abs(char_index) > len(alpha_lower)-1:
                if char_index > 0:
                    char_index -= len(alpha_lower)
                else:
                    char_index += len(alpha_lower)
            
            final_char = alpha_upper[char_index] if char_upper else alpha_lower[char_index]

        # Append
        final_message += final_char

        # Change key index
        key_index = 0 if key_index+1 > len(key_shifts)-1 else key_index+1
    
    return final_message

"""
Returns the key as a list of shifts.

Arguments:
    key (str): The key to convert

Return:
    [int]: Array with the shift for each char
"""
def key_to_shifts(key: str) -> [int]:
    shifts = []

    for char in key:
        if char.isnumeric():
            shifts.append(int(char))
        elif char.isalpha():
            shift = (alpha_upper.index(char) if char.isupper() else alpha_lower.index(char)) + 1

            shifts.append(shift)
        else:
            continue

    return shifts