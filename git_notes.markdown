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

    -   

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

-   Sync local repository with upstream
    ```
    git fetch upstream
    git merge upstream/master
    ```

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

Personal Access Tokens

-   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

-   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

-   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

-   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

-   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

-   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

-   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

-   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

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
