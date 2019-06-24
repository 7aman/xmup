from xmup import firmwares
from xmup import inout


def main():
    devid = inout.ask_devid()
    db = firmwares.get_all()
    found = firmwares.search(devid, db)
    selected = inout.select(found)
    if selected:
        path = inout.get_path()
        for item in selected:
            result = firmwares.check(found[item])
            info = inout.show_info(result)
            if inout.ask_download():
                firmwares.download(result, path, info)
        inout.open_folder(path)
    else:
        print('nothing to display.')
        exit()

if __name__ == "__main__":
    main()

