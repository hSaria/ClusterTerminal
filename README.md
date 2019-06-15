ClusterTerminal (`cterm`) forwards all keystrokes from a master window to multiple slave windows. Use `cterm` as a method for performing ad hoc tasks, not as a substitute for automation frameworks.

# Installation

    pip3 install cterm

ClusterTerminal uses the built-in Terminal application of macOS.

# Usage

The most common use case is controlling multiple SSH sessions simultaneously, like:

    cterm ssh host1 host2

You might want to set up an alias in your `~/.bash_profile`, like `alias cssh="cterm ssh"` and then just call it using `cssh host1 host2`. You don't have to, but it'll save you some time.
