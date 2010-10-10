# Git post-receive hook for server synchronization

## Requirements

*   rsync
*   ssh client (for remote synchronization)

## Configuration items:

*   `PROJECTNAME` --- custom name(used for creating temporary files,
    etc
*   `TARGETDIR` --- local or remote synchronization path
*   `REMOTE_USER` --- remote user to log in with
*   `TEMPDIR_PREFIX` --- temporary dir holding working copy on the
    VCS server
*   `REFNAME_PREFIX` --- default prefix (refs/heads for branches)

Currently this hook supports updating up to 3 local/remote servers with the
same directory and the same login for all servers. However It can be extended
in future to support arbitrary list of servers.

There are special variables to set up a repository for each server/envioronment:

*   `DEVELOPMENT_REFNAME`, `DEVELOPMENT_SERVER` --- branch name and server name
    used to synchronize development environment
*   `TESTING_REFNAME`, `TESTING_SERVER` --- same variables for testing
    environment
*   `PRODUCTION_REFNAME`, `PRODUCTION_SERVER` --- same variables for testing
    environment
