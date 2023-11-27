# Git and GitHub

## Git

-   Configuration: git config \--local

### Repository

-   project folder in which changes are tracked by git

-   contains .git file (?)
    
-   can be locally stored or hosted on GitHub
    
-   git init

-   Stages

    -   Modified (green) - \> Staging -\> Commit(snapshot at that
        particular point)

    -   Commit =\> take everything from staging area and make a
        "save-point"

-   Creating a repository -- git init

-   Staging files

    -   git status

    -   Add to staging: git add \<file\> (Add everything to staging: git
        add . )

    -   Remove from staging: git rm --cached \<file\>

    -   Adding files to the staging area allows us to review the code
        before committing it (an extra blanket of security)

    -   allows to have separate commits for separate changes

-   Commit

    -   git commit -m "\<descriptive message of what the commit is
        about\>"

    -   To view commit history: git log (OR) git log \--oneline

    -   To get a graph of commits do `git log --graph --decorate  --oneline --all`  

-   Uploading to GitHub from a local repository

    -   <https://docs.github.com/en/get-started/importing-your-projects-to-github/importing-source-code-to-github/adding-locally-hosted-code-to-github>

    -   Note: git push \--set-upstream origin master

    -   Using personal access tokens
        (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) --
        <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token>

-   Changing remote repository

    -   git remote set-url origin \<NEW_URL\> && git remote -v

    -   <https://docs.github.com/en/get-started/getting-started-with-git/managing-remote-repositories>

-   Rename branch

    -   git branch -m \<old_name\> \<new_name\>

    -   <https://stackoverflow.com/questions/6591213/how-do-i-rename-a-local-git-branch>

-   Switch branch

    -   git checkout new_branch (?)

-   refusing to merge unrelated histories --
    <https://stackoverflow.com/questions/37937984/git-refusing-to-merge-unrelated-histories-on-rebase>

-   git clone vs. git init

-   git pull vs. git fetch

-   \--set-upstream / \--set-upstream-to:
    <https://stackoverflow.com/questions/18031946/what-does-set-upstream-do>

-   checkout

-   origin vs. upstream --
    <https://stackoverflow.com/questions/9257533/what-is-the-difference-between-origin-and-upstream-on-github>

-   Different branch names in local and remote repository --
    https://stackoverflow.com/questions/19154302/git-push-to-specific-branch

> git push origin localBranch:remoteBranch

-   Renaming a branch --
    <https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-branches-in-your-repository/renaming-a-branch>

-   Make a new branch

    -   git checkout -b branch-name

-   Using git with Jupyter Notebook/ Colab

    -   <https://blog.reviewnb.com/jupyter-version-control/>

    -   <https://colab.research.google.com/github/googlecolab/colabtools/blob/master/notebooks/colab-github-demo.ipynb#scrollTo=8QAWNjizy_3O>

-   Remove origin: git remote rm origin

-   Remove version tracking: rm -rf .git

-   Searching for issuses

    -   https://docs.github.com/en/search-github/searching-on-github/searching-issues-and-pull-requests

-   Creating pull requests

    -   <https://youtu.be/8A4TsoXJOs8>

    -   Linking a PR to an issue --
        <https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue>

    -   

-   Commit messages

    -   <https://www.conventionalcommits.org/en/v1.0.0/>

## Merging
-   Scenario 1: When the local repository is ahead of the remote by some commits
    and the remote also has commits that were *not* pulled by the local *before*
    it made those commits.
    ```
    // before merge
    * LOCAL ORIGIN HEAD
    *
    *
    | REMOTE ORIGIN HEAD
    |/
    *
    *

    // after merge
    * LOCAL ORIGIN HEAD
     \
    * |
    * |
    | REMOTE ORIGIN HEAD
    |/
    *
    *
    // the merge itself is a separate commit, but that is not shown here.
    ```

-   Sync local repository with upstream
    ```
    git fetch upstream
    git merge upstream/master
    ```
-   `HEAD`
-   Stash
-   Merge
-   Rebase
-   Reset
-   Revert
-   Modifying/ reverting commits
    -   Undo previous commit
    ```
    git reset HEAD~
    # make necessary changes and commit again
    ```
    -   Checkout file to previous state and amend commit
    ```
    git checkout HEAD~ file.txt
    git commit --amend
    ```
    -   Hard 'delete' commits
    `git reset --hard [commit_id_start]..[commit_id_end]`
    -   [Source 1](https://remarkablemark.org/blog/2017/09/19/revert-file-after-commit/), [2](https://stackoverflow.com/questions/4114095/how-do-i-revert-a-git-repository-to-a-previous-commit)

### Pulling a change from multiple branches
- `git cherry-pick [commit-id]`
  - In case of conflict, resolve conflict and do `git commit --no-verify`
  - [Reference](https://stackoverflow.com/questions/65224262/how-do-you-git-cherry-pick-continue-with-no-verify)

### `git mergetool`
- Refer [here](https://gist.github.com/karenyyng/f19ff75c60f18b4b8149) for a
  detailed description on using `mergetool`
- **Note**: Once `mergetool` is opened, do not quit until the conflicts are
  resolved.

### `git difftool`
- `git difftool --tool=nvimdiff <filename>` to view differences between the previous commit and the current state of the file
- Not applicable for staged files (works only for tracked, modified files)
- [nvimdiff docs](https://neovim.io/doc/user/diff.html)

### `git config`
- Used to define variables used by various git commands
- `git config --local diff.tool nvimdiff`

**Pushing from a local repository branch (master) to a (my) GitHub
repository (set as remote origin) branch (main)**

![](media/image1.png){width="6.6930555555555555in"
height="5.330555555555556in"}

Remeber when you want to **upload your local git repositiory to GitHub**

(Source:
<https://www.theserverside.com/video/How-to-use-the-git-remote-add-origin-command-to-push-remotely>
)

![](media/image2.png){width="5.416666666666667in"
height="2.8541666666666665in"}

Rebasing

-   "There isn't anything to compare" -- [git - Github Pull Request:
   There isn\'t anything to compare - Stack
   Overflow](https://stackoverflow.com/questions/53844405/github-pull-request-there-isnt-anything-to-compare)

-   "You are currently editing a commit" -- [git - How to get rid of
   \"You are currently editing a commit\"? - Stack
   Overflow](https://stackoverflow.com/questions/31252363/how-to-get-rid-of-you-are-currently-editing-a-commit)

## Stash
- `git stash list`
- `git stash push -m "Stash message"` to save a stash with message 
- `git stash push -m "particular_files_only" /path/to/file` to stash only specific files
- `git stash pop` to pop the (topmost) stash and apply the changes
- `git stash drop stash@{n}` to drop a specific stash
- `git stash show` to show files in the topmost stash

Meilisearch

\--master-key BuDML6SBIbVeGPiute8gisixsBDMHGOxxCF_uLqnl5M

Libreoffice

-   New "stuff"

    -   gerrit

    -   logerrit

    -   ssh (ed25519)

-   EasyHacks --
    <https://wiki.documentfoundation.org/Development/EasyHacks>

    -   Look at all links under \`Getting Started\`

-   Generating SSH key --
    <https://www.mediawiki.org/wiki/SSH_keys#Generating_a_new_SSH_key>

> (See \~/.ssh)

-   Errors

    -   Missing Change-ID in commit message --
        <https://stackoverflow.com/questions/8845658/gerrit-error-when-change-id-in-commit-messages-are-missing>

## References
- [Charles Duan - Guide](https://www.cduan.com/technical/git/)
