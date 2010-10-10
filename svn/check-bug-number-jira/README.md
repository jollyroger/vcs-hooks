# SVN pre-commit hook which check bug info in JIRA

## Requirements

*   Allow to connect to JIRA by XML-RPC
*   Python to run the actual check

## Configuration items:

*    `JIRA_KEY` --- The JIRA project's key
*    `JIRA_XMLRPC` --- JIRA XML-RPC URL to connect to
*    `JIRA_USER` --- JIRA username to bind with
*    `JIRA_PASSWORD` --- JIRA user's password

Currently following checks are performed:

*    Bug exists 
*    Committing user is assigned to the bug
