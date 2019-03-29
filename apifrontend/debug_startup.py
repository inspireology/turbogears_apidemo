# debug entrypoint from https://stackoverflow.com/questions/18748300/turbogears-2-3-debug-through-eclipse
if __name__ == '__main__':
    from gearbox.main import GearBox
    gearbox = GearBox()
    gearbox.run(["serve", "--config=../development.ini"])
    #gearbox.run(["setup-app", "--config=development.ini"])
