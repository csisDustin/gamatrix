import docopt  # type: ignore
from importlib.metadata import PackageNotFoundError, version

import gamatrix.appmain as appmain
import gamatrix.config as appcfg
import gamatrix.doc as appdoc

if __name__ == "__main__":
    try:
        ver = version("gamatrix")
    except PackageNotFoundError:
        # running in dev, no distribution installed in this environment
        ver = "0.0.0-dev"

    opt = docopt.docopt(appdoc.__doc__, version=ver, options_first=True)

    conf = appcfg.GamatrixConfig(opt)
    if conf.api_key() == "":
        raise RuntimeError(
            "No personal API key found. Please see help (--help) for information."
        )

    sp = appmain.Gamatrix(conf)
    sp.run()
