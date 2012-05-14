#!/usr/bin/env python
# Este arquivo faz parte do Pasteall

import os
import os.path
import commands

from distutils.core import setup
from distutils.core import Command
from distutils.command.install import install
from distutils.command.install_data import install_data

setup(
	name = "Pasteall",
	description = "Um monitor de clipboard simples e funcional.",
	author = "Lara Maia",
	author_email = "lara@craft.net.br",
	url = "http://github.com/mrk3004/Pasteall/",
	license = "GNU GPL v3",
	version = "0.0.2",
	scripts = ["pasteall"])
