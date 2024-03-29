Command line tool for managing docker-containers
================================================

.. image:: https://readthedocs.org/projects/docker-manager/badge/?version=latest
    :target: https://docker-manager.readthedocs.org/en/latest/?badge=latest


Description
-----------
docker-manager is a tool similar to docker-compose but it handles a few additional things like
nginx config for proxying/clustering webservices and handling basic auth. And it's also adding hosts entries for each container.

Installation
------------

Since docker-manager is using python3 by default, you better upgrade.

After successful installation of python3 and pip for pyhton3, run the following command to install or upgrade docker-manager:

.. code:: console

    pip3 install --user --upgrade docker-manager

If you are on mac osx and your local python folder isn't in your PATH variable you might add it to $PATH or symlink it in /usr/local/bin with sudo.

**Max OSX**

.. code:: console

    sudo ln -s /home/<username>/.local/bin/docker-container /usr/local/bin/
    sudo ln -s /home/<username>/.local/bin/docker-image /usr/local/bin/
    sudo ln -s /home/<username>/.local/bin/docker-watcher /usr/local/bin/
    sudo ln -s /home/<username>/.local/bin/docker-bridge /usr/local/bin/

The same applies to linux, however, the path is different. (On usual Distributions this is in $PATH already)

.. code:: console

    sudo ln -s /home/<username>/.local/bin/docker-container /usr/local/bin/
    sudo ln -s /home/<username>/.local/bin/docker-image /usr/local/bin/
    sudo ln -s /home/<username>/.local/bin/docker-watcher /usr/local/bin/
    sudo ln -s /home/<username>/.local/bin/docker-bridge /usr/local/bin/

Argument Completion
-------------------

docker-manager supports argument completion, to activate this feature in linux run:

.. code:: console

    sudo activate-global-python-argcomplete3

Under OSX it isn't that simple unfortunately. Global completion requires bash support for complete -D, which was introduced in bash 4.2. On OS X or older Linux systems, you will need to update bash to use this feature. Check the version of the running copy of bash with echo $BASH_VERSION. On OS X, install bash via Homebrew (brew install bash), add /usr/local/bin/bash to /etc/shells, and run chsh to change your shell.
Afterwards you might be able to also just run:

.. code:: console

    sudo activate-global-python-argcomplete3

Usage
-----

tbd


Known Issues
------------

If you discover any bugs, feel free to create an issue on GitHub fork
and send us a pull request.

`Issues List`_.


Authors
-------

-  Claudio Walser (https://github.com/claudio-walser)


Contributing
------------
Please use git-cd for contributing, it matches my workflow best.

1. Fork it
2. Create your feature branch (``git cd start my-new-feature``)
3. Commit your changes (``git commit -am 'Add some feature'``)
4. Push to the branch (``git push origin feature/my-new-feature``)
5. Create new Pull Request (``git cd review my-new-feature``)


License
-------

Apache License 2.0 see
https://github.com/claudio-walser/python-docker-manager/blob/master/LICENSE

.. _Issues List: https://github.com/claudio-walser/python-docker-manager/issues
