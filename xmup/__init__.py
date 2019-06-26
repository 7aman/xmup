from xmup import firmwares
from xmup import inout


def main():
    devid = inout.ask_devid()
    db = firmwares.get_all()
    found = firmwares.search(devid, db)
    selected = inout.select(found)
    if selected:
        path = inout.get_path()
        open_after = False
        for item in selected:
            result = firmwares.check(found[item])
            info = inout.show_info(result)
            if inout.ask_download():
                firmwares.download(result, path, info)
                open_after = True
        inout.open_folder(path, open_after)
    else:
        print('nothing to display.')
    input('\nPress any key to exit ....')
    exit()

if __name__ == "__main__":
    main()

