# Git post-receive hook for server deployment

This hook performes local and remote deployment on per-branch basis

## Requirements

*   rsync
*   ssh client (for remote deployment)

## Configuration items

Configuration options are stored in `.git/config` file per branch. Script uses
`git-config` to get the values for each branch.

*   `branch.<branch_name>.deploy-dir` --- the directory where branch will be
    deployed to
*   `branch.<branch_name>.deploy-server` --- remote server name (optional)
*   `branch.<branch_name>.deploy-user` --- remote user name (optional)

While validating the values the following rules are applied:

*   at least `deploy-dir` must be set if you want the branch to be deployed
*   if no `deploy-server` specified then local deployment assumed
*   if no `deploy-user` specified then current user assumed. Only used for
    remote deployment

## Examples

### Case 1. Local deployment

Sample configuration might look like this:

    [branch "local-deploy"]
        deploy-dir = /path/to/dir

In this case deployment wil be performed locally. Don't forget to check rights
on a target directory.

You also can deploy as another user using `localhost` as a remote server
described in the next case.

### Case 2. Remote deployment

Configuration file will be as follows:

    [branch "remote-deploy"]
        deploy-server = example.com
        deploy-dir = /path/to/dir

Note that you will need to set up a passwordless SSH access to the remote
server using SSH keys.

It is possible to specify the remote user with `deploy-user` option:

    [branch "remote-deploy"]
        deploy-server = example.com
        deploy-dir = /path/to/dir
        deploy-user = user
