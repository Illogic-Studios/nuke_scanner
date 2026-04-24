import importlib

import nuke_scanner.nuke_scanner as nuke_scanner
importlib.reload(nuke_scanner)

nuke_scanner.NukeScanner().run()