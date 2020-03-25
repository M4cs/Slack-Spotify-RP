from ssrp.startup import startup
from ssrp.api import API
from ssrp.utils.colors import prompt
import os, time

def main():
    startup.check_config()
    api = API(os.path.realpath(os.path.expanduser("~") + "/.ssrp/config.json"))
    running = True
    try:
        while running:
            api.set_now_playing()
            time.sleep(api.update_interval)
    except KeyboardInterrupt:
        prompt("Quitting... Unsetting Status")
        api.unset_status()
        exit()
    
if __name__ == "__main__":
    main()