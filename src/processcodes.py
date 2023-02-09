from controller import controller
import time

codes = ['5HD9TY', '5HD86H', '6HUJ56', '53NKH3', '294NMB', '528HBB', '584HJF', 'AAB123', 'ACK646', 'AUJ261', 'BBR334', 'BDC866', 'BDE289', 'BENGH8', 'BHH538', 'BKJ462', 'BKJ857', 'BKL123', 'BNL435', 'BOBA00', 'BRJ437', 'BVH785', 'BVNJ84', 'BWK887', 'BYU785', 'BYY492', 'CBR954', 'CCH677', 'CDT859', 'CGF754', 'CLZ738', 'DBH897', 'DDD748', 'DFY111', 'DHV940', 'DHY782', 'DQY857', 'DRK328', 'DRX444', 'DVY683', 'ECU428', 'EMP666', 'ERF893', 'EUK421', 'EVILR2', 'EWK785', 'EXP912', 'FBM152', 'FBM834', 'GAR945', 'GGF539', 
'GHL978', 'GHR673', 'GIJ989', 'GUA850', 'HBF899', 'HDD733', 'HHD647', 'HHY697', 'HJH848', 'HJI667', 'HJU848', 'HJY732', 'HS9K44', 'HUT845', 'HVT573', 'HWY633', 'HYR849', 'INT729', 'JHU423', 'JJU782', 'JKD867', 'JKJ589', 'JNK8J4', 'KAU532', 'KIT766', 'KJU233', 'KLA621', 'KLG412', 'KLJ897', 'KLP412', 'KPF958', 'LUM521', 'MMN372', 'MUN486', 'MZY419', 'NBN431', 'NBU753', 'NJK912', 'NJK995', 'NMP499', 'NNB674', 'NNM784', 'NUJ866', 'NVU859', 'PER894', 'PLK689', 'PLL967', 'PMN576', 'PMN904', 'PPP555', 'PRX482', 'PUL966', 'QQY843', 'QRN714', 'QYD793', 'R2D222', 'RTD428', 'SLM768', 'SMA293', 'SPRGNK', 'TFI888', 'THE931', 'THY432', 'TTY463', 'UUU875', 'VBJ322', 'VCT533', 'VVV429', 'VXZ3K2', 'VXZ123', 'VXZ193', 'VYY985', 'XCT333', 
'XXD447', 'XXY99G', 'YUF634', 'YYR778', 'YZFR1K', 'ZZR636']

code_order = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
code_order_reverse = '9876543210ZYXWVUTSRQPONMLKJIHGFEDCBA'

def process_codes(gamepad, fps=60, verbose=False):
    delay = gamepad.get_delay()
    time.sleep(5)
    gamepad.a_button(20)
    time.sleep(5)
    last_code = 'AAAAAA'
    for code in codes:
        char_pos = 0
        for char in code:
            hold_time, reverse, index = get_hold_time(char, char_pos, last_code, fps, delay)
            if verbose:
                print(f"Code: {code} Character: {char} Hold Time: {hold_time} Character Pos: {char_pos} Last Code: {last_code} Reverse: {reverse} Order Index: {index} Delay: {delay}")
            send_input(hold_time, reverse, char_pos, gamepad)
            char_pos += 1
        last_code = code
        
        

def get_hold_time(char, char_pos, last_code, fps, delay):
    
    modified_code_order = code_order.split(last_code[char_pos])
    modified_code_order = last_code[char_pos] + modified_code_order[1]  + modified_code_order[0]
    modified_code_order_reverse = code_order_reverse.split(last_code[char_pos])
    modified_code_order_reverse = last_code[char_pos] + modified_code_order_reverse[1]  + modified_code_order_reverse[0]
    
    if modified_code_order.index(char) <= modified_code_order_reverse.index(char):
        best_order = modified_code_order 
        reverse = False
    else: 
        best_order = modified_code_order_reverse
        reverse = True
    
    if best_order.index(char) == 0:
        return 0, False, best_order.index(char)
    else: 
        #print(best_order, str(best_order.index(char)))
        return ((8/fps) * best_order.index(char) * 1000) - delay, reverse, best_order.index(char)

def send_input(hold_time, reverse, char_pos, gamepad):
    gamepad.down(hold_time) if reverse else gamepad.up(hold_time)
    gamepad.right(20)

    if char_pos == 5: 
        gamepad.a_button(20)
        gamepad.left(1000)

    time.sleep(10/60)

if __name__ == '__main__':
    import time
    gamepad = controller()
    time.sleep(15)
    process_codes(gamepad, 60, True)

