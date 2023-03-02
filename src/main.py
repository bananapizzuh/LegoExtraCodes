import rich_click as click
from utility import *
from processcodes import process_codes

games, codes = load_games()[3], load_games()[1]


@click.command()
@click.option(
    "-g",
    "--game",
    type=click.Choice(games),
    help="What game you would like to put codes into.",
)
@click.option(
    "-w",
    "--wait",
    type=int,
    default=15,
    help="How long you want to wait until the codes process.",
)
@click.option("-v", "--verbose", is_flag=True, default=False)
def main(game, wait, verbose):
    if game == None:
        import gui

        return
    print(list(games.keys()).index(game))
    update()
    process_codes(wait, codes[list(games.keys()).index(game)], verbose)


if __name__ == "__main__":
    main()
