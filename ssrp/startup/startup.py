import webbrowser, os, json
from getpass import getpass
from colorama import Fore as f
from ssrp.utils.colors import *

DEFAULT_CONFIG = {
    "spotify_auth_token": "NONE",
    "spotify_refresh_token": "NONE",
    "slack_workspaces": [],
    "update_interval": 5,
    "format": "song - artist | [album]"
}
CONFIG_DIR = os.path.realpath(os.path.expanduser("~") + "/.ssrp/")
CONFIG_FILE = os.path.realpath(os.path.expanduser("~") + "/.ssrp/config.json")

def check_config():
    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)
    if not os.path.exists(CONFIG_FILE):
        setup_wizard()
        
def setup_wizard():
    tprompt = "> "
    info("Press ENTER to login to Spotify/Slack to Get Started or Ctrl+C to Quit!")
    try:
        getpass("")
    except KeyboardInterrupt:
        print("Quitting")
        exit()
    webbrowser.open_new_tab("https://ssrp.maxbridgland.com/authorize")
    spot_at = None
    spot_re = None
    slack_at = []
    while True:
        prompt("Please Enter The Spotify Auth Token Displayed on The Page When Done:")
        spot_at = input(tprompt)
        info("You Input: " + spot_at)
        prompt("Is this correct? Y\\n")
        ans = input(tprompt)
        if ans.lower() == "y":
            break
        else:
            pass
    while True:
        prompt("Please Enter The Spotify Refresh Token Displayed on The Page When Done:")
        spot_re = input(tprompt)
        info("You Input: " + spot_re)
        prompt("Is this correct? Y\\n")
        ans1 = input(tprompt)
        if ans1.lower() == "y":
            break
        else:
            pass
    while True:
        prompt("Please Enter The Slack Auth Token Displayed on The Page When Done:")
        slack_ans = input(tprompt)
        info("You Input: " + slack_ans)
        prompt("Is this correct? Y\\n")
        ans2 = input(tprompt)
        if ans2.lower() == "y":
            slack_at.append(slack_ans.strip())
            break
        else:
            pass
    finished = False
    while not finished:
        prompt("Would you like to add more workspaces for Slack? Y\\n")
        ans3 = input(tprompt)
        if ans3.lower() == "y":
            while True:
                warning("You must login to your other workspace FIRST!")
                getpass("Press ENTER to Continue")
                webbrowser.open_new_tab("https://slack.com/oauth/authorize?scope=users:write&client_id=1014188996113.1014189480129")
                prompt("Please Enter The Slack Auth Token Displayed on The Page When Done:")
                slack_ans = input(tprompt)
                info("You Input: " + slack_ans)
                prompt("Is this correct? Y\\n")
                ans2 = input(tprompt)
                if ans2.lower() == "y":
                    slack_at.append(slack_ans)
                    break
                else:
                    pass
        elif ans3.lower() == "n":
            finished = True
        else:
            warning("Unknown Answer. Please Choose Y or N!")
    if spot_re and spot_at and slack_at:
        info("Creating Configuration File...")
        with open(CONFIG_FILE, "w+") as cf:
            config = DEFAULT_CONFIG
            config['spotify_auth_token'] = spot_at.strip()
            config['spotify_refresh_token'] = spot_re.strip()
            config['slack_workspaces'] = slack_at
            json.dump(config, cf, indent=4)
        info("Finished Creating Config File...")
    else:
        error("Something Went Wrong or You Didn't Fill In An Answer, Please Try Again!")