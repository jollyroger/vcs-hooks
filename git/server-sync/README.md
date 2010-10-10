# Git post-receive hook for server synchronization

## Requirements
*   rsync
*   ssh (for remote synchronization)

## Configuration items:
*   <code>PROJECTNAME</code> --- custom name(used for creating temporary files, etc
*   <code>TARGETDIR</code> --- local or remote synchronization path
*   <code>REMOTE_USER</code> --- remote user to log in with
*   <code>TEMPDIR_PREFIX</code> --- temporary dir holding working copy on the
    VCS server
*   <code>REFNAME_PREFIX</code> --- default prefix (refs/heads for branches)
