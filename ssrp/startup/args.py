from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('ra', 'reauth', help="Get a new credential tokens for Slack or Spotify")
    parser.add_argument('rasp', 'reauth-spotify', help="Get new access and refresh tokens for Spotify only")
    parser.add_argument('rasl', 'reauth-slack', help="Get a new workspace token for Slack only")
    