import platform
import subprocess
from pathlib import Path

OS = platform.system()

def open_folder(path):
    if OS == "Windows":
        subprocess.Popen(["explorer", str(path)])
    elif OS == "Darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])


def get_path():
    path = Path().home().joinpath('Downloads')
    path.mkdir(parents=True, exist_ok=True)
    return path


def ask_devid():
    banner = ["*"*55,]
    banner.append("System version is like this:\n")
    banner.append("    V4.02.R11.00000142.11001.131600.00000\n")
    banner.append("The important section of this string is this part:\n")
    banner.append("    --.--.---.00000142.-----.------.-----\n")
    banner.append("Use these 8 charachters or just last 3 (i.e 142) to search.")
    banner.append("If xmup found multiple results select appropriate one based on other part of version.\n")
    banner.append("*"*55)
    print('\n'.join(banner))
    while True:
        devid = input("\ndevid to search: ") or False
        if devid:
            return devid


def ask_download():
    answer = input("Continue to download? [y]: ") or 'y'
    if answer.lower() == 'y':
        return True
    else:
        return False

def show_info(result):
    lines = list()
    lines.append(f"DevID     : {result['DevID']}\n")
    lines.append(f"Name      : {result['FileName']}\n")
    lines.append(f"Size      : {human_readable(result['FileSize'])}\n")
    lines.append(f"Date      : {result['Date']}\n")    
    change_log = [ f"    {line}\n" for line in result['ChangeLog'].split('\n')]
    lines.append(f"Change Log:\n{''.join(change_log)}\n")
    info = ''.join(lines)
    print()
    print(info)
    return info

def human_readable(size):
    for unit in ['', 'K', 'M', 'G', 'T']:
        if size < 1024.0:
            return f"{size:03.2f} {unit}B"
        size = size / 1024.0

def select(results):
    if not results:
        return []
    else:
        print('[Select]')
        for i, res in enumerate(results):
            print(f"  {i} - {res['DevID']} - ({res['FileName']})")
        print(' '*2 + '...................')
        selected = get_user_choice(results)
    return [sel -1 for sel in selected]


def get_user_choice(results):
    mx = len(results)
    while True:
        if mx == 1:
            text = "Press Enter to select only result"
        else:
            text = "Enter a number or comma separated numbers for multiple choice.\nnumbers must be between (1-" + str(mx) + ")"

        print(' '*2 + text, end='')
        try:
            selected = input(' [1]: ') or '1'
            answer = filter_valid_choice(selected, mx)
            if answer:
                return answer
            else:
                raise IndexError
        except KeyboardInterrupt:
            print('\n'*2 + '[Exit] Terminated by user.' + '\n')
            exit()
        except IndexError:
            print("  Oops! not valid. try again:")

def filter_valid_choice(text, maximum):
    numbers = text.split(',')
    numbers = [int(n) for n in numbers if is_valid_integer(n)]
    return list(set([n for n in numbers if (0 < n < 1+maximum)]))

def is_valid_integer(i):
    try:
        int(i)
        return True
    except ValueError:
        return False

