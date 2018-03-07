Coding new features
-------------------

1. Start a new issue: `(!) Issues on GitHub <https://github.com/msparapa/beluga/issues>`_

    a. :code:`git pull` Make sure you have the latest copy of **master**.

    b. :code:`git checkout -b I# master` Create the **I#** branch locally based upon the **master** branch.

    c. :code:`git push -u origin I#` Create the branch on the server.

2. Write code and push commits:

    a. Each commit message should begin with :code:`Ref ##` to reference the issue number (i.e. :code:`Ref #1` to reference issue #1)

    b. :code:`git push` Push latest commits to the server.

3. End a task: (from **master**)

    a. :code:`git checkout master` Set **master** as the working branch locally.

    b. :code:`git branch -D I#` Delete **I#** locally. You no longer need it because everything is pushed to the server.

    c. :code:`git merge --no-ff origin/I#` Merge the task into **master** and preserving branch history. All changes in **master** will show up as a single commit keeping the log simpler. The complete commit history will be preserved in **I#**.

    d. :code:`git push` Push any changes to **master** to the server.

    e. :code:`git push origin :I#` Delete **I#** from the server. It will still remain in the history along with every individual commit to it that was pushed, but it won't be cluttering up the workspace.
