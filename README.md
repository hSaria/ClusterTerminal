ClusterTerminal (`cterm`) forwards all keystrokes from a master window to multiple slave windows. Use `cterm` as a method for performing ad hoc tasks, not as a substitute for automation frameworks.

> This is mostly just something I wanted to do out of fun; plenty of similar solutions out there, `tmux` being a very popular one.

![alt text](https://github.com/hSaria/ClusterTerminal/raw/master/.github/ssh_example.gif "Example output")

# Installation

    pip3 install cterm

ClusterTerminal uses the built-in Terminal application of macOS.

# Usage

The most common use case is controlling multiple SSH sessions simultaneously:

    cterm ssh host1 host2

## Tips

You might want to set up an alias for cluster ssh in your `~/.bash_profile`. For instance, `alias cssh="cterm ssh"`, and then call it using `cssh host1 host2`.

In an alias, you can save your normal settings, like `alias cssh="cterm --screen 2 ssh"` to change the default screen.

If you specify the same argument twice, the last instance is the one used. This is useful since you may want to overwrite part of your alias, but not all of it. For example, the following will use screen 1:

    cterm ssh host1 host2 --screen 2 --screen 1

# Limitations

The window must be completely opaque as the scripting capabilities of Terminal ignore the alpha component.
