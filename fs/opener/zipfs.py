# coding: utf-8
"""`ZipFS` opener definition.
"""

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from .base import Opener

class ZipOpener(Opener):
    """`ZipFS` opener.
    """
    
    protocols = ['zip']

    def open_fs(self, fs_url, parse_result, writeable, create, cwd):
        from ..zipfs import ZipFS
        zip_fs = ZipFS(
            parse_result.resource,
            write=create
        )
        return zip_fs
