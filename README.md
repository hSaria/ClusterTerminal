ClusterTerminal (`cterm`) forwards all keystrokes from a master window to multiple slave windows. Use `cterm` as a method for performing ad hoc tasks, not as a substitute for automation frameworks.

> This is mostly just something I wanted to do out of fun; plenty of similar solutions out there, `tmux` being a very popular one.

![alt text](https://github.com/hSaria/ClusterTerminal/raw/master/.github/ssh_example.gif "Example output")

# Installation

    pip3 install cterm

ClusterTerminal uses the built-in Terminal application of macOS.

# Usage

The most common use case is controlling multiple SSH sessions simultaneously:

    cterm ssh host1 host2

In addition to the master window, the above will create two slaves windows, like so:

    ssh host1
    ssh host2

## Command Arguments

If you want to pass arguments to the command, include it as part of the command. Beware of character escaping where necessary. For example:

    cterm "ssh -l \"some user\"" host1 host2

which will expand to:

    ssh -l "some user" host1
    ssh -l "some user" host2

> You could've also used `cterm "ssh -l 'some user'" host1 host2` to get the same outcome; I only escaped quotes to demo purposes.

## Item Arguments

Similar to a command, you can pass per-item arguments (again, beware of character escaping):

    cterm ssh "\-p 1022 host1" "\-p 2022 host2"

which will expand to:

    ssh -p 1022 host1
    ssh -p 2022 host2

# Tips

You might want to set up an alias for cluster ssh in your `~/.bash_profile`. For instance, `alias cssh="cterm ssh"`, and then call it using `cssh host1 host2`.

In an alias, you can save your normal settings, like `alias cssh="cterm --screen 2 ssh"` to change the default screen.

If you specify the same argument twice, the last instance is the one used. This is useful since you may want to overwrite part of your alias, but not all of it. For example, the following will use screen 1:

    cterm ssh host1 host2 --screen 2 --screen 1

# Limitations

The window must be completely opaque as the scripting capabilities of Terminal ignore the alpha component.
