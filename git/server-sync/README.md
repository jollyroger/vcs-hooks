# Git post-receive hook for server deployment

This hook performes local and remote deployment on per-branch basis

## Requirements

  * rsync
  * ssh client (for remote deployment)

## Configuration items

Configuration options are stored in `.git/config` file per branch. Script uses
`git-config` to get the values for each branch.

  * `branch.<branch_name>.deploy-dir` --- the directory where branch will be
    deployed to
  * `branch.<branch_name>.deploy-server` --- remote server name (optional)
  * `branch.<branch_name>.deploy-user` --- remote user name (optional)

While validating the values the following rules are applied:

  * at least `deploy-dir` must be set if you want the branch to be deployed
  * if no `deploy-server` specified then local deployment assumed
  * if no `deploy-user` specified then current user assumed. Only used for
    remote deployment

## Default deployment settings

It is posible to set deployemnt settings for all branches at once and override
them if needed as well as disable deployment for specific branches.

To set up a default deployment method one uses the same approach as before,
except the following git-config options are set:

  * `branch.deploy-dir` --- the directory where branch will be deployed to
  * `branch.deploy-server` --- remote server name
  * `branch.deploy-user` --- remote user name

While validating the values the following rules are applied:

  * `-` is invalid value for any paramenter and disables deployment for specific
    branch

## Deploy arguments expansion

In most cases it is desirable to have set ome part of the variable that will
expand for every branch using some substitution method. It is possible to
expand the variables using a thirdparty script or a function available on the
repository server (for example a script under $PATH). This script should read
the refname via STDIN and write only one line - the result of the expansion.

One can enable such expansion using `branch.deploy-dir-func` and similar
`-func` git-config variables.

## Examples

### Case 1. Local deployment

Sample configuration might look like this:

    [branch "local-deploy"]
        deploy-dir = /path/to/dir

In this case deployment wil be performed locally. Don't forget to check
permissions on the target directory.

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

### Case 3. Multiple branches deployment

    [branch]
        deploy-server = example.com
        deploy-user = user
        deploy-dir-func = multibranch deploy/branches
    [branch "master"]
        deploy-dir = deploy/production
    [branch "stable"]
        deploy-dir = 
    [branch "nondeploy"]
        deploy-dir = -

In this case we'll have all branches deployed to the directory of the same name
under `~/deploy/branches`, nondeploy branch won't be deployed at all and
master branch will be deployed to a custom directory `~/deploy/production`

The multibranch function is defined inside the hook itself since it is the most
simple and usefull one.
