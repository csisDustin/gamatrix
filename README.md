# Gamatrix

![Build Status Badge](https://github.com/d3r3kk/gamatrix/workflows/CI/badge.svg)

An app to help you and your Steam friends determine what game to play.

## Contents

- [Quick Setup](#quick-setup-for-the-mildly-impatient)
- [Prerequisites](#prerequisites)
- [Preparation](#preparation)
- [How to Run](#how-to-run)
- [How to Contribute](#how-to-contribute)

---

## Quick Setup for the Mildly Impatient

> _Step #1:_

```bash
git clone https://github.com/d3r3kk/gamatrix
cd gamatrix
# get key here: https://steamcommunity.com/dev/
echo "my_personal_steam_web_api_key" > .user_steam_api_dev_keyapikey
```

> _Step #2:_

```bash
poetry install
```

> _Step #3:_

```bash
pytest # This is optional, if you are going to do some development...
python -m gamatrix
```

---

## Prerequisites

- Python 3.8 or higher installed (see [Python.org for downloads](https://www.python.org/downloads/)).
- [Poetry](https://python-poetry.org/)
- The Git client installed on your system and accessible via PATH.
- A Steam account, and at least one friend! (go to [Steam online to sign up](https://steampowered.com/)).
- A Steam Web API Key (see [Steam community Web API Page for details](https://steamcommunity.com/dev/apikey)).

## How to Run

### Running during development

Once you are all setup and have the [prerequisites](#prerequisites) installed, you can
now run the application.

1. Open your shell of choice.
1. Navigate to the `gamatrix` folder. (Note this is the root-folder you cloned to in
Git, **_not_** the `gamatrix/gamatrix` folder within the repo).
1. Run the application with the `--help` flag to see what options/commands are available.
    - `poetry run python -m gamatrix --help`
1. Run the application.
    - Show off all your connected friends:
    - `poetry run python -m gamatrix friends`

### Running in production

TBD

> Note: At the time of writing we aren't yet publishing packages to PyPI.

### A Note About Cache

The application tries to minimize the amount of times it will reach out to the game
client service. To achieve this, the results from the basic queries about friends and
games are cached between runs. The caches are stored under the users home directory,
under a folder called `.gamatrix/cache`. The files located there can be removed at any
time, and can be ignored during runtime by using the `--force` command line option.

Users can look through these cache files using Python, as they are simply _pickled
objects_ with a fairly basic schema.

### Examples

Show friends:

`python -m gamatrix --user=<username> --passwd='<password>' friends`

Compare games with `friend 1` and `friend_2`:

`python -m gamatrix --user=<username> --passwd='<password>' compare --friend="<friend 1>" --friend=<friend_2>`

## How to Contribute

Quick setup steps...

1. Clone the repo.

    - `git clone https://github.com/d3r3kk/gamatrix`

1. Setup your local environment with Poetry

    - `poetry install`

1. **Important**: Ensure tests all run and pass before you start!

    - `poetry run pytest`

1. Create your own feature branch off of master.

    - `git checkout -b my_feature master`

1. Do your work.
1. Ensure tests pass.

    - `poetry run pytest`

1. Push your feature branch.

    - `git push --set-upstream origin my_feature`

1. Create a PR against `main` via Github.

---

> NOTE: If you need to update dependencies...

Please don't update the `pyproject.toml` file directly. Add your package requirement using
poetry's `poetry add <pkg_name>` functionality instead. Use
`poetry add <pkg_name> --dev` for dev-only requirements. Use `poetry update` to update the
versions of packages being used.

---

## Code of Conduct

Basic Premise: _Be excellent to each other_.

In general, this means that everyone is expected to be **open**, **considerate**, and
**respectful**, of others no matter what their perspective is within this project.

## Troubleshooting

### Windows Problems

---

**Issue:** The C++ Build Tools aren't available.

Error message occurs during `python -m pip install -r requirements.txt` stage.

Error message ends with:
`"distutils.errors.DistutilsPlatformError: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": https://visualstudio.microsoft.com/downloads/"`

**Solution:** Install the Microsoft build tools by installing the Visual Studio Community Edition from the link provided. Be certain to install the `MSVC v[VER] - VS 20xx C++ x64/x86 build tools (vMAJ.MIN)` are selected in "Individual Components" within the Visual Studio installer. You can install the "Desktop development with C++" workload to ensure you get everything. Alternatively, install only the "C++ Build Tools" workload for the latest Visual Studio (currently [you can find them for Visual Studio 2019 here](https://visualstudio.microsoft.com/downloads/#build-tools-for-visual-studio-2019)).

---

**Issue:** The Powershell `Activate.ps1` script raises permissions errors.

Error message occurs during activation of the Python environment `.venv\Scripts\Activate.ps1`.

Error message is:

```pwsh
.\.venv\Scripts\Activate.ps1 : File C:\path\to\gamatrix\.venv\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this system. For more information, see about_Execution_Policies at https://go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:1
+ .\.venv\Scripts\Activate.ps1
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
+ CategoryInfo          : SecurityError: (:) [], PSSecurityException
+ FullyQualifiedErrorId : UnauthorizedAccess
```

**Solution:** The Powershell access is set to something _less than_ `RemoteSigned`. Change the execution
policy to `RemoteSigned`.

```pwsh
 Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
 ```

---
