#!/usr/bin/env python3
from sys import exit
from test.ftp_test import FTPTest
from test.base_test import FTP
from misc.wget_file import WgetFile

"""
    This test ensures that Wget can download files from FTP Server
"""
TEST_NAME = "FTP Downloads"
########## File Definitions ######################################
File1 = "Beyond the fog lies clarity"

# Define directory structure by creating WgetFile object.
# Here URL path is /Foo/Bar/File1
# hence creating Foo and Bar directories
# Make the flag isdir=True and add parent 


Foo = WgetFile("Foo", parent="/", isdir=True)
Bar = WgetFile("Bar", parent="Foo", isdir=True)

A_File = WgetFile("File1", File1, parent="Bar")

WGET_OPTIONS = " -S "
WGET_URLS = [["/Foo/Bar/File1"]]

Files = [[A_File, Foo, Bar]]

Servers = [FTP]

ExpectedReturnCode = 0
ExpectedDownloadedFiles = [A_File]

######### Pre and Post Test Hooks ################################
pre_test = {
    "ServerFiles"     : Files
}
test_options = {
    "WgetCommands"    : WGET_OPTIONS,
    "Urls"            : WGET_URLS
}
post_test = {
    "ExpectedFiles"   : ExpectedDownloadedFiles,
    "ExpectedRetCode" : ExpectedReturnCode
}

err = FTPTest(
              name=TEST_NAME,
              pre_hook=pre_test,
              test_params=test_options,
              post_hook=post_test,
              protocols=Servers
).begin()

exit(err)
