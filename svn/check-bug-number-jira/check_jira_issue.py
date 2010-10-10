#!/usr/bin/python
# -*- coding: utf8 -*-
# Script checks wether issue exists in JIRA Bugtracking system
#
# SYNOPSIS:
#       check_jira_issue.py -U <URL> -u <user> -p <password> issue [ [issue2] ... ]
#
# ARGUMENTS:
#       -U <URL>
#               URL to JIRA XML-RPC API, for example https://jira.example.com/rpc/xmlrpc
#
#       -u user
#               username to bind with
#
#       -p password
#               password for the username account
#
#       issue
#               code name of the issue in JIRA bugtracking system, which contains the 
#               project name part and issue number separated with a dash "-" symbol.

import sys
import getopt
import xmlrpclib

class JiraChecker:
        "JiraChecker checks wether issues exist in JIRA"

        token = ""

        def __init__(self,serverURL,user,password):
                self.server = xmlrpclib.ServerProxy(serverURL)
                self.user = user
                self.password = password

        
        def login(self):
                "Log to JIRA RPC Server with predefined credentials"
                self.token = self.server.jira1.login(self.user, self.password)

        def check(self,issueList):
                "Checks the list of issues for predefined criteria. Returns list of failed bugs"
                if len(issueList) == 0:
                        return False

                result = []

                for issue in issueList:
                        try:
                                jiraIssue = self.server.jira1.getIssue(self.token,issue)
                                if jiraIssue['assignee'] != committer:
                                        result.append(issue + ":\tYou are not assignee")
                        except xmlrpclib.Fault, err:
                                result.append(issue + ":\tNo such issue")
                return result;


        def logout(self):
                "Logs out from JIRA RPC Server"
                if self.token <> "":
                        try:
                                self.server.jira1.logout(self.token)
                        except xmlrpclib.Fault, err:
                                sys.stderr.write("Caught exception %d : %s" % (err.faultCode, err.faultString))
                        finally:
                                self.token = ""

        
optlist,issues = getopt.getopt(sys.argv[1:],"U:u:p:h:c:")

for option,argument in optlist:
        if option == "-U":
                serverURL = argument
        elif option == "-u":
                user = argument
        elif option == "-p":
                password = argument
        elif option == "-c":
                committer = argument
        else:
                print "Unknown option \"%s\"" % option
                sys.exit(1)

if not len(issues):
        sys.stderr.write("Please, specify the issue name to commit for.")
        sys.exit(1)

if not len(committer):
        sys.stderr.write("Please,specify the person who committed changes.")
        sys.exit(1)

checker = JiraChecker(serverURL, user, password)
try:
        checker.login()
        result = checker.check(issues)
        checker.logout()
except xmlrpclib.Fault, err:
        sys.stderr.write("Caught exception %d : %s" % (err.faultCode, err.faultString))
        sys.exit(1)

errCount = len(result)
if errCount:
        sys.stderr.write("Cannot accept commit. The following errors occured:\n%s" % "\n".join(result))

sys.exit(errCount)
