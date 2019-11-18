"""Test the games command."""

import docopt  # type: ignore

import steamingpile.commands as spcmd

from . import utils


class TestGamesCommand:

    cfg = utils.Config()

    def test_get_games_command(self):
        """Ensure get_command returns a proper games command instance."""
        games_cmd, _ = spcmd.get_command("games", self.cfg)
        assert games_cmd
        assert isinstance(games_cmd, spcmd.Games)

    def test_games_command_fails_with_incorrect_parameters(self):
        """Games command elegantly handles incorrect parameters."""
        games_cmd, args = spcmd.get_command("games --something-not-there", self.cfg)
        assert games_cmd
        cli = utils.NoneClientProvider()
        try:
            games_cmd.run(args, cli)
            assert "Argument parsing for games command did not recognize bad input." == ""
        except docopt.DocoptExit as e:
            assert "games" in e.usage.lower()
            assert "--force" in e.usage.lower()

    def test_get_games_for_friend(self):
        """Ensure we can get a game for a friend."""
        friends_list = utils.get_friends(count=1, name_prefix="Fren_")
        games_cmd, args = spcmd.get_command(f"games --friend={friends_list[0].name}", self.cfg)
        cli_provider = utils.SettableClientProvider()
        cli_provider.set_friends = friends_list
        friends_games = utils.get_games(1)
        cli_provider.set_games = friends_games
        output = games_cmd.run(args, cli_provider)

        assert cli_provider.get_games_forced is False
        assert any(friends_games[0].name in s for s in output)

    def test_get_games_for_friend_with_space_in_name(self):
        """Ensure we can get a game for a friend."""
        friends_list = utils.get_friends(count=1, name_prefix="Space in name ")
        games_cmd, args = spcmd.get_command(f"games --friend='{friends_list[0].name}'", self.cfg)
        cli_provider = utils.SettableClientProvider()
        cli_provider.set_friends = friends_list
        friends_games = utils.get_games(1)
        cli_provider.set_games = friends_games
        output = games_cmd.run(args, cli_provider)

        assert cli_provider.get_games_forced is False
        assert any(friends_games[0].name in s for s in output)

    def test_get_games_for_friend_is_forced(self):
        """Ensure we can get a game for a friend."""
        friends_list = utils.get_friends(count=1)
        games_cmd, args = spcmd.get_command(f"games --friend={friends_list[0].name} --force", self.cfg)
        cli_provider = utils.SettableClientProvider()
        cli_provider.set_friends = friends_list
        friends_games = utils.get_games(1)
        cli_provider.set_games = friends_games
        output = games_cmd.run(args, cli_provider)

        assert cli_provider.get_games_forced is True
        assert any(friends_games[0].name in s for s in output)
