#
# Copyright (c) 2018 Red Hat, Inc.
#
# This software is licensed to you under the GNU General Public License,
# version 3 (GPLv3). There is NO WARRANTY for this software, express or
# implied, including the implied warranties of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. You should have received a copy of GPLv3
# along with this software; if not, see
# https://www.gnu.org/licenses/gpl-3.0.txt.
#

"""Exceptions used by network scan."""


class NetworkCancelException(Exception):
    """Exception for Network Cancel interrupt."""

    pass


class NetworkPauseException(Exception):
    """Exception for Network Pause interrupt."""

    pass


class ScannerException(Exception):
    """Exception for issues detected during scans."""

    def __init__(self, message=""):
        """Exception for issues detected during scans.

        :param message: An error message describing the problem encountered
        during scan.
        """
        self.message = "Scan task failed.  Error: {}".format(message)
        super().__init__(self.message)
