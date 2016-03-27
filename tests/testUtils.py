#!/usr/bin/env python

# LSST Data Management System
# Copyright 2014-2015 LSST Corporation.
#
# This product includes software developed by the
# LSST Project (http://www.lsst.org/).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the LSST License Statement and
# the GNU General Public License along with this program.  If not,
# see <http://www.lsstcorp.org/LegalNotices/>.

"""
This is a unittest for the Utils class.

@author  Jacek Becla, SLAC

"""

import ConfigParser
import os
import tempfile
import time
import unittest

import lsst.log as log
from lsst.db.testHelper import readCredentialFile


class TestUtils(unittest.TestCase):

    def testReadCredF(self):
        f, fN = tempfile.mkstemp(suffix=".cnf", text=True)
        f = open(fN, 'w')
        f.write("""
[mysql]
host = localhost
port = 3455
user = dummyX
password = 123a
socket = /tmp/my/socket.sock
""")
        f.close()
        dict = readCredentialFile(fN)
        self.assertEqual(dict["host"], "localhost")
        self.assertEqual(dict["port"], "3455")
        self.assertEqual(dict["user"], "dummyX")
        self.assertEqual(dict["passwd"], "123a")
        self.assertEqual(dict["unix_socket"], "/tmp/my/socket.sock")
        os.remove(fN)

####################################################################################


def main():
    unittest.main()

if __name__ == "__main__":
    main()
