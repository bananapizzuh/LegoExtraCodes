import time, pydirectinput
from utility import wait

code_order = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
code_order_reverse = "9876543210ZYXWVUTSRQPONMLKJIHGFEDCBA"


def process_codes(start_delay, codes, verbose=False):
    time.sleep(int(start_delay))
    start = time.time()
    last_code = "AAAAAA"
    for code in codes:
        char_pos = 0
        for char in code:
            reverse, index = get_hold_time(char, char_pos, last_code)
            if verbose:
                print(
                    f"Code: {code} Character: {char} Character Pos: {char_pos} Last Code: {last_code} Reverse: {reverse} Order Index: {index} "
                )
            send_input(index, reverse, char_pos)
            char_pos += 1
        last_code = code
    print(f"Elasped time: {time.time() - start}")


def get_hold_time(char, char_pos, last_code):
    modified_code_order = code_order.split(last_code[char_pos])
    modified_code_order = (
        last_code[char_pos] + modified_code_order[1] + modified_code_order[0]
    )
    modified_code_order_reverse = code_order_reverse.split(last_code[char_pos])
    modified_code_order_reverse = (
        last_code[char_pos]
        + modified_code_order_reverse[1]
        + modified_code_order_reverse[0]
    )

    if modified_code_order.index(char) <= modified_code_order_reverse.index(char):
        best_order = modified_code_order
        reverse = False
    else:
        best_order = modified_code_order_reverse
        reverse = True

    if best_order.index(char) == 0:
        return False, best_order.index(char)
    else:
        # print(best_order, str(best_order.index(char)))
        return reverse, best_order.index(char)


def send_input(index, reverse, char_pos):
    if reverse:
        for i in range(index):
            pydirectinput.press("s")
    else:
        for i in range(index):
            pydirectinput.press("w")
    pydirectinput.press("d")
    if char_pos == 5:
        pydirectinput.press("u")
        pydirectinput.keyDown("a")
        wait(1000)
        pydirectinput.keyUp("a")

    time.sleep(10 / 60)


if __name__ == "__main__":
    import time

    time.sleep(15)
    process_codes(True)
