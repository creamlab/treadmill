Microsoft Windows [version 10.0.18363.1440]
(c) 2019 Microsoft Corporation. Tous droits r‚serv‚s.

C:\Program Files\Sublime Text 3>git
'git' n'est pas reconnu en tant que commande interne
ou externe, un programme ex‚cutable ou un fichier de commandes.

C:\Program Files\Sublime Text 3>git
#############
## RESTART ##
#############
Microsoft Windows [version 10.0.18363.1440]
(c) 2019 Microsoft Corporation. Tous droits r‚serv‚s.

C:\Program Files\Sublime Text 3>git
usage: git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           [--super-prefix=<path>] [--config-env=<name>=<envvar>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone             Clone a repository into a new directory
   init              Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add               Add file contents to the index
   mv                Move or rename a file, a directory, or a symlink
   restore           Restore working tree files
   rm                Remove files from the working tree and from the index
   sparse-checkout   Initialize and modify the sparse-checkout

examine the history and state (see also: git help revisions)
   bisect            Use binary search to find the commit that introduced a bug
   diff              Show changes between commits, commit and working tree, etc
   grep              Print lines matching a pattern
   log               Show commit logs
   show              Show various types of objects
   status            Show the working tree status

grow, mark and tweak your common history
   branch            List, create, or delete branches
   commit            Record changes to the repository
   merge             Join two or more development histories together
   rebase            Reapply commits on top of another base tip
   reset             Reset current HEAD to the specified state
   switch            Switch branches
   tag               Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch             Download objects and refs from another repository
   pull              Fetch from and integrate with another repository or a local branch
   push              Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.

C:\Program Files\Sublime Text 3>git status
fatal: not a git repository (or any of the parent directories): .git

C:\Program Files\Sublime Text 3>E:

E:\>cd WORK/DO

E:\WORK\DO>cd [Quentin] tapis
Le chemin d'accŠs sp‚cifi‚ est introuvable.

E:\WORK\DO>ls
'ls' n'est pas reconnu en tant que commande interne
ou externe, un programme ex‚cutable ou un fichier de commandes.

E:\WORK\DO>dir
 Le volume dans le lecteur E s'appelle DATA
 Le num‚ro de s‚rie du volume est EAC1-F643

 R‚pertoire de E:\WORK\DO

20/11/2020  11:20    <DIR>          .
20/11/2020  11:20    <DIR>          ..
15/01/2020  18:31    <DIR>          2017
15/01/2020  19:04    <DIR>          2018
09/04/2021  10:07    <DIR>          2020
               0 fichier(s)                0 octets
               5 R‚p(s)  356ÿ155ÿ269ÿ120 octets libres

E:\WORK\DO>cd 2020

E:\WORK\DO\2020>cd [Quentin] tapis

E:\WORK\DO\2020\[Quentin] tapis>git init
Initialized empty Git repository in E:/WORK/DO/2020/[Quentin] tapis/.git/

E:\WORK\DO\2020\[Quentin] tapis>git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	leo walking/
	read_ni.py
	schema.png

nothing added to commit but untracked files present (use "git add" to track)

E:\WORK\DO\2020\[Quentin] tapis>git config --global user.name "JJ Aucouturier"

E:\WORK\DO\2020\[Quentin] tapis>git config --global user.email "aucouturier@gmail.com"

E:\WORK\DO\2020\[Quentin] tapis>git config --global color.ui auto

E:\WORK\DO\2020\[Quentin] tapis>git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	leo walking/
	read_ni.py
	schema.png

nothing added to commit but untracked files present (use "git add" to track)

E:\WORK\DO\2020\[Quentin] tapis>git remote add origin https://github.com/creamlab/treadmill.git

E:\WORK\DO\2020\[Quentin] tapis>git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	leo walking/
	read_ni.py
	schema.png

nothing added to commit but untracked files present (use "git add" to track)

E:\WORK\DO\2020\[Quentin] tapis>git add read_ni.py

E:\WORK\DO\2020\[Quentin] tapis>git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
	new file:   read_ni.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	leo walking/
	schema.png


E:\WORK\DO\2020\[Quentin] tapis>git commit -m "new file read_ni.py"
[master (root-commit) d7ff0d5] new file read_ni.py
 1 file changed, 194 insertions(+)
 create mode 100644 read_ni.py

E:\WORK\DO\2020\[Quentin] tapis>git push -u origin
fatal: The current branch master has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin master


E:\WORK\DO\2020\[Quentin] tapis>git push -u origin master

Exception non gérée : System.ComponentModel.Win32Exception: Handle de fenêtre non valide
   à MS.Win32.ManagedWndProcTracker.HookUpDefWindowProc(IntPtr hwnd)
   à MS.Win32.ManagedWndProcTracker.OnAppDomainProcessExit()
   à MS.Internal.ShutDownListener.HandleShutDown(Object sender, EventArgs e)

***Repl Killed***

#############
## RESTART ##
#############
Microsoft Windows [version 10.0.18363.1440]
(c) 2019 Microsoft Corporation. Tous droits r‚serv‚s.

C:\Program Files\Sublime Text 
Le chemin d'accŠs sp‚cifi‚ est introuvable.

C:\Program Files\Sublime Text 3>
C:\Program Files\Sublime Text 3>
C:\Program Files\Sublime Text 3>E:

E:\>cd WORK/DO/2020/[Quentin] tapis

E:\WORK\DO\2020\[Quentin] tapis>git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
	leo walking/
	schema.png

nothing added to commit but untracked files present (use "git add" to track)

E:\WORK\DO\2020\[Quentin] tapis>git add read_ni.py

E:\WORK\DO\2020\[Quentin] tapis>git push
fatal: The current branch master has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin master


E:\WORK\DO\2020\[Quentin] tapis>git push origin master
remote: 
remote: Create a pull request for 'master' on GitHub by visiting:        
remote:      https://github.com/creamlab/treadmill/pull/new/master        
remote: 
To https://github.com/creamlab/treadmill.git
 * [new branch]      master -> master

E:\WORK\DO\2020\[Quentin] tapis>git remote -v
origin	https://github.com/creamlab/treadmill.git (fetch)
origin	https://github.com/creamlab/treadmill.git (push)

E:\WORK\DO\2020\[Quentin] tapis>git branches -all 
git: 'branches' is not a git command. See 'git --help'.

E:\WORK\DO\2020\[Quentin] tapis>git branch -all
error: did you mean `--all` (with two dashes)?

E:\WORK\DO\2020\[Quentin] tapis>git branch --all
* master
  remotes/origin/master

E:\WORK\DO\2020\[Quentin] tapis>git push origin main
error: src refspec main does not match any
error: failed to push some refs to 'https://github.com/creamlab/treadmill.git'

E:\WORK\DO\2020\[Quentin] tapis>git branch -m master main

E:\WORK\DO\2020\[Quentin] tapis>git status
On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)
	leo walking/
	schema.png

nothing added to commit but untracked files present (use "git add" to track)

E:\WORK\DO\2020\[Quentin] tapis>git branch --all
* main
  remotes/origin/master

E:\WORK\DO\2020\[Quentin] tapis>git push -u origin main 
To https://github.com/creamlab/treadmill.git
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'https://github.com/creamlab/treadmill.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

E:\WORK\DO\2020\[Quentin] tapis>git pull
From https://github.com/creamlab/treadmill
 * [new branch]      main       -> origin/main
There is no tracking information for the current branch.
Please specify which branch you want to merge with.
See git-pull(1) for details.

    git pull <remote> <branch>

If you wish to set tracking information for this branch you can do so with:

    git branch --set-upstream-to=origin/<branch> main


E:\WORK\DO\2020\[Quentin] tapis>git push -u origin main
To https://github.com/creamlab/treadmill.git
 ! [rejected]        main -> main (non-fast-forward)
error: failed to push some refs to 'https://github.com/creamlab/treadmill.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

E:\WORK\DO\2020\[Quentin] tapis>git push -u origin main main
error: dst ref refs/heads/main receives from more than one src
error: failed to push some refs to 'https://github.com/creamlab/treadmill.git'

E:\WORK\DO\2020\[Quentin] tapis>git push origin --delete master
To https://github.com/creamlab/treadmill.git
 - [deleted]         master

E:\WORK\DO\2020\[Quentin] tapis>git push -u origin main main
error: dst ref refs/heads/main receives from more than one src
error: failed to push some refs to 'https://github.com/creamlab/treadmill.git'

E:\WORK\DO\2020\[Quentin] tapis>git push -u origin main
To https://github.com/creamlab/treadmill.git
 ! [rejected]        main -> main (non-fast-forward)
error: failed to push some refs to 'https://github.com/creamlab/treadmill.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

E:\WORK\DO\2020\[Quentin] tapis>git pull
There is no tracking information for the current branch.
Please specify which branch you want to merge with.
See git-pull(1) for details.

    git pull <remote> <branch>

If you wish to set tracking information for this branch you can do so with:

    git branch --set-upstream-to=origin/<branch> main


E:\WORK\DO\2020\[Quentin] tapis>git pull main main
fatal: 'main' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.

E:\WORK\DO\2020\[Quentin] tapis>git pull origin/main main
fatal: 'origin/main' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.

E:\WORK\DO\2020\[Quentin] tapis>git pull origin main
From https://github.com/creamlab/treadmill
 * branch            main       -> FETCH_HEAD
fatal: refusing to merge unrelated histories

E:\WORK\DO\2020\[Quentin] tapis>git fetch origin main
From https://github.com/creamlab/treadmill
 * branch            main       -> FETCH_HEAD

E:\WORK\DO\2020\[Quentin] tapis>git merge origin main
merge: origin - not something we can merge

E:\WORK\DO\2020\[Quentin] tapis>git merge main
Already up to date.

E:\WORK\DO\2020\[Quentin] tapis>git status
On branch main
Untracked files:
  (use "git add <file>..." to include in what will be committed)
	leo walking/
	schema.png

nothing added to commit but untracked files present (use "git add" to track)

E:\WORK\DO\2020\[Quentin] tapis>git show commit
fatal: ambiguous argument 'commit': unknown revision or path not in the working tree.
Use '--' to separate paths from revisions, like this:
'git <command> [<revision>...] -- [<file>...]'

E:\WORK\DO\2020\[Quentin] tapis>git log
commit d7ff0d55e459c5e7533d362b1b39fa401943c715
Author: JJ Aucouturier <aucouturier@gmail.com>
Date:   Fri Apr 9 10:39:56 2021 +0200

    new file read_ni.py

E:\WORK\DO\2020\[Quentin] tapis>git branch --set-upstream-to=origin/main main
Branch 'main' set up to track remote branch 'main' from 'origin'.

E:\WORK\DO\2020\[Quentin] tapis>
E:\WORK\DO\2020\[Quentin] tapis>git pull
fatal: refusing to merge unrelated histories

E:\WORK\DO\2020\[Quentin] tapis>git clone https://github.com/creamlab/treadmill.git
Cloning into 'treadmill'...

E:\WORK\DO\2020\[Quentin] tapis>git add read_ni.py

E:\WORK\DO\2020\[Quentin] tapis>git status
On branch main
Your branch and 'origin/main' have diverged,
and have 1 and 1 different commits each, respectively.
  (use "git pull" to merge the remote branch into yours)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	deleted:    read_ni.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	leo walking/
	schema.png
	treadmill/


E:\WORK\DO\2020\[Quentin] tapis>git pull
fatal: refusing to merge unrelated histories

E:\WORK\DO\2020\[Quentin] tapis>git commit -m "added read_ni.py"
[main b1ef66b] added read_ni.py
 1 file changed, 194 deletions(-)
 delete mode 100644 read_ni.py

E:\WORK\DO\2020\[Quentin] tapis>git push
To https://github.com/creamlab/treadmill.git
 ! [rejected]        main -> main (non-fast-forward)
error: failed to push some refs to 'https://github.com/creamlab/treadmill.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

E:\WORK\DO\2020\[Quentin] tapis>git status
On branch main
Your branch and 'origin/main' have diverged,
and have 2 and 1 different commits each, respectively.
  (use "git pull" to merge the remote branch into yours)

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	leo walking/
	schema.png
	treadmill/

nothing added to commit but untracked files present (use "git add" to track)

E:\WORK\DO\2020\[Quentin] tapis>git branch add-first-file

E:\WORK\DO\2020\[Quentin] tapis>git add read_ni.py
fatal: pathspec 'read_ni.py' did not match any files

E:\WORK\DO\2020\[Quentin] tapis>cd treadmill

E:\WORK\DO\2020\[Quentin] tapis\treadmill>git add read_ni.py

E:\WORK\DO\2020\[Quentin] tapis\treadmill>git commit -m "added first file"
[main f229252] added first file
 1 file changed, 194 insertions(+)
 create mode 100644 read_ni.py

E:\WORK\DO\2020\[Quentin] tapis\treadmill>git push -u origin add-first-file
error: src refspec add-first-file does not match any
error: failed to push some refs to 'https://github.com/creamlab/treadmill.git'

E:\WORK\DO\2020\[Quentin] tapis\treadmill>git checkout add-first-file
error: pathspec 'add-first-file' did not match any file(s) known to git

E:\WORK\DO\2020\[Quentin] tapis\treadmill>git branch -all
error: did you mean `--all` (with two dashes)?

E:\WORK\DO\2020\[Quentin] tapis\treadmill>git branch --all
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/main

E:\WORK\DO\2020\[Quentin] tapis\treadmill>git branch add-first-file

E:\WORK\DO\2020\[Quentin] tapis\treadmill>
E:\WORK\DO\2020\[Quentin] tapis\treadmill>git checkout add-first-file
Switched to branch 'add-first-file'

E:\WORK\DO\2020\[Quentin] tapis\treadmill>git add read_ni.py

E:\WORK\DO\2020\[Quentin] tapis\treadmill>git commit -m "added first file"
On branch add-first-file
nothing to commit, working tree clean

E:\WORK\DO\2020\[Quentin] tapis\treadmill>git push -u origin add-first-file
remote: 
remote: Create a pull request for 'add-first-file' on GitHub by visiting:        
remote:      https://github.com/creamlab/treadmill/pull/new/add-first-file        
remote: 
Branch 'add-first-file' set up to track remote branch 'add-first-file' from 'origin'.
To https://github.com/creamlab/treadmill.git
 * [new branch]      add-first-file -> add-first-file

E:\WORK\DO\2020\[Quentin] tapis\treadmill>git merge --help

E:\WORK\DO\2020\[Quentin] tapis\treadmill>git checkout main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)
Switched to branch 'main'

E:\WORK\DO\2020\[Quentin] tapis\treadmill>git merge add-first-file
Already up to date.

E:\WORK\DO\2020\[Quentin] tapis\treadmill>git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

E:\WORK\DO\2020\[Quentin] tapis\treadmill>git push -u origin
Branch 'main' set up to track remote branch 'main' from 'origin'.
To https://github.com/creamlab/treadmill.git
   edf2d06..f229252  main -> main

E:\WORK\DO\2020\[Quentin] tapis\treadmill>git branch -d add-first-file
Deleted branch add-first-file (was f229252).

E:\WORK\DO\2020\[Quentin] tapis\treadmill>git pull -u origin
error: unknown switch `u'
usage: git pull [<options>] [<repository> [<refspec>...]]

    -v, --verbose         be more verbose
    -q, --quiet           be more quiet
    --progress            force progress reporting
    --recurse-submodules[=<on-demand>]
                          control for recursive fetching of submodules

Options related to merging
    -r, --rebase[=(false|true|merges|preserve|interactive)]
                          incorporate changes by rebasing rather than merging
    -n                    do not show a diffstat at the end of the merge
    --stat                show a diffstat at the end of the merge
    --log[=<n>]           add (at most <n>) entries from shortlog to merge commit message
    --signoff[=...]       add a Signed-off-by trailer
    --squash              create a single commit instead of doing a merge
    --commit              perform a commit if the merge succeeds (default)
    --edit                edit message before committing
    --cleanup <mode>      how to strip spaces and #comments from message
    --ff                  allow fast-forward
    --ff-only             abort if fast-forward is not possible
    --verify-signatures   verify that the named commit has a valid GPG signature
    --autostash           automatically stash/stash pop before and after
    -s, --strategy <strategy>
                          merge strategy to use
    -X, --strategy-option <option=value>
                          option for selected merge strategy
    -S, --gpg-sign[=<key-id>]
                          GPG sign commit
    --allow-unrelated-histories
                          allow merging unrelated histories

Options related to fetching
    --all                 fetch from all remotes
    -a, --append          append to .git/FETCH_HEAD instead of overwriting
    --upload-pack <path>  path to upload pack on remote end
    -f, --force           force overwrite of local branch
    -t, --tags            fetch all tags and associated objects
    -p, --prune           prune remote-tracking branches no longer on remote
    -j, --jobs[=<n>]      number of submodules pulled in parallel
    --dry-run             dry run
    -k, --keep            keep downloaded pack
    --depth <depth>       deepen history of shallow clone
    --shallow-since <time>
                          deepen history of shallow repository based on time
    --shallow-exclude <revision>
                          deepen history of shallow clone, excluding rev
    --deepen <n>          deepen history of shallow clone
    --unshallow           convert to a complete repository
    --update-shallow      accept refs that update .git/shallow
    --refmap <refmap>     specify fetch refmap
    -o, --server-option <server-specific>
                          option to transmit
    -4, --ipv4            use IPv4 addresses only
    -6, --ipv6            use IPv6 addresses only
    --negotiation-tip <revision>
                          report that we have only objects reachable from this object
    --show-forced-updates
                          check for forced-updates on all updated branches
    --set-upstream        set upstream for git pull/fetch


E:\WORK\DO\2020\[Quentin] tapis\treadmill>git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

E:\WORK\DO\2020\[Quentin] tapis\treadmill>git pull
Already up to date.

E:\WORK\DO\2020\[Quentin] tapis\treadmill>git branch add-start-control

E:\WORK\DO\2020\[Quentin] tapis\treadmill>git checkout add-start-control
Switched to branch 'add-start-control'

E:\WORK\DO\2020\[Quentin] tapis\treadmill>pip install tkinter
ERROR: Could not find a version that satisfies the requirement tkinter (from versions: none)
ERROR: No matching distribution found for tkinter
WARNING: You are using pip version 20.2.3; however, version 21.0.1 is available.
You should consider upgrading via the 'c:\users\aucouturier\appdata\local\programs\python\python36\python.exe -m pip install --upgrade pip' command.

E:\WORK\DO\2020\[Quentin] tapis\treadmill>git status
On branch add-start-control
Untracked files:
  (use "git add <file>..." to include in what will be committed)
	timer.py

nothing added to commit but untracked files present (use "git add" to track)

E:\WORK\DO\2020\[Quentin] tapis\treadmill>git checkout main
Your branch is up to date with 'origin/main'.
Switched to branch 'main'

E:\WORK\DO\2020\[Quentin] tapis\treadmill>git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	timer.py

nothing added to commit but untracked files present (use "git add" to track)

E:\WORK\DO\2020\[Quentin] tapis\treadmill>git checkout add-start-control
Switched to branch 'add-start-control'

E:\WORK\DO\2020\[Quentin] tapis\treadmill>git reflog
f229252 HEAD@{0}: checkout: moving from main to add-start-control
f229252 HEAD@{1}: checkout: moving from add-start-control to main
f229252 HEAD@{2}: checkout: moving from main to add-start-control
f229252 HEAD@{3}: checkout: moving from add-first-file to main
f229252 HEAD@{4}: checkout: moving from main to add-first-file
f229252 HEAD@{5}: commit: added first file
edf2d06 HEAD@{6}: clone: from https://github.com/creamlab/treadmill.git

E:\WORK\DO\2020\[Quentin] tapis\treadmill>git pull 
From https://github.com/creamlab/treadmill
   f229252..14bb35b  main       -> origin/main
There is no tracking information for the current branch.
Please specify which branch you want to merge with.
See git-pull(1) for details.

    git pull <remote> <branch>

If you wish to set tracking information for this branch you can do so with:

    git branch --set-upstream-to=origin/<branch> add-start-control


E:\WORK\DO\2020\[Quentin] tapis\treadmill>git checkout main
Your branch is behind 'origin/main' by 1 commit, and can be fast-forwarded.
  (use "git pull" to update your local branch)
Switched to branch 'main'

E:\WORK\DO\2020\[Quentin] tapis\treadmill>git pull
Updating f229252..14bb35b
Fast-forward
 read_ni.py | 268 +++++++++++++++++--------------------------------------------
 1 file changed, 74 insertions(+), 194 deletions(-)

E:\WORK\DO\2020\[Quentin] tapis\treadmill>git pull
From https://github.com/creamlab/treadmill
   14bb35b..b43f688  main       -> origin/main
Updating 14bb35b..b43f688
Fast-forward
 read_ni.py | 297 ++++++++++++++++++++++++++++++++++++++++++++++---------------
 1 file changed, 223 insertions(+), 74 deletions(-)

E:\WORK\DO\2020\[Quentin] tapis\treadmill>git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   read_ni.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	timer.py

no changes added to commit (use "git add" and/or "git commit -a")

E:\WORK\DO\2020\[Quentin] tapis\treadmill>git add read_ni.py 

E:\WORK\DO\2020\[Quentin] tapis\treadmill>git commit -m "Removed useless cong_read_task function"
[main f3a17eb] Removed useless cong_read_task function
 1 file changed, 4 insertions(+), 7 deletions(-)

E:\WORK\DO\2020\[Quentin] tapis\treadmill>git push -u origin
Branch 'main' set up to track remote branch 'main' from 'origin'.
To https://github.com/creamlab/treadmill.git
   b43f688..f3a17eb  main -> main

E:\WORK\DO\2020\[Quentin] tapis\treadmill>git status
#############
## RESTART ##
#############
Microsoft Windows [version 10.0.18363.1440]
(c) 2019 Microsoft Corporation. Tous droits r‚serv‚s.

C:\Program Files\Sublime Text 3>E
'E' n'est pas reconnu en tant que commande interne
ou externe, un programme ex‚cutable ou un fichier de commandes.

C:\Program Files\Sublime Text 3>E:

E:\>cd WORK/DO/2020/[Quentin] tapis

E:\WORK\DO\2020\[Quentin] tapis>cd treadmill

E:\WORK\DO\2020\[Quentin] tapis\treadmill>git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	timer.py

nothing added to commit but untracked files present (use "git add" to track)

E:\WORK\DO\2020\[Quentin] tapis\treadmill>git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	timer.py

nothing added to commit but untracked files present (use "git add" to track)

E:\WORK\DO\2020\[Quentin] tapis\treadmill>git pull
From https://github.com/creamlab/treadmill
   f3a17eb..6528a91  main       -> origin/main
Updating f3a17eb..6528a91
Fast-forward
 Launcher.py           | 42 +++++++++++++++++++++++++
 module_acquisition.py | 86 +++++++++++++++++++++++++++++++++++++++++++++++++++
 2 files changed, 128 insertions(+)
 create mode 100644 Launcher.py
 create mode 100644 module_acquisition.py

E:\WORK\DO\2020\[Quentin] tapis\treadmill>git