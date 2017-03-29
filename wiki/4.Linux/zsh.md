## Configure
### Starts up files

- `/etc/zshenv`
- `~/.zshenv`
- IF the shell is a login shell, `/etc/zprofile` and `~/.zprofile`
- IF the shell is interactive, `/etc/zshrc` and `~/.zshrc`
- IF the shell is a login shell, `/etc/zlogin` and `~/.zlogin`

### Logging out

`/etc/zlogout` is read, and then `ZDOTDIR/.zlogout`

### Two terms

A **login** shell is generally one that is spawned at login time. (IE, by either /bin/login or some other daemon that handles incoming connections). If you telnet, rlogin, rsh, or ssh to a host, chances are you have a login shell.
An **interactive** shell is one in which prompts are displayed and the user types in commands to the shell. (IE, a tty is associated with the shell)

For example, if I run the command

    ssh SOME_HOST some_command

I will be running (presumably) a non-interactive program called `some_command`. This means that zsh will not be an interactive shell, and ignore the corresponding files. Zsh should, however, be a login shell, and read the appropriate files.

### Zsh options

- Over 100 options.
- case-insensitive.
- underscores are ignored. `SOME_OPTION` == `SOMEOPTION`

1. `setopt OPTION_NAME` <--- Turn an option on
1. `unsetopt OPTION_NAME` <--- Turn an option off
1. `setopt NO_OPTION_NAME` <--- Turen an option off too!

### Zsh Prompts (提示符)

- primary: contained in the shell variable `PROMPT`, also known as `PS1`
- IF `PROMPT_SUBST` is on: the prompts are first subjected to parameter expansion, command substitution, and arithmetic expansion, before actually displays them.

#### Customize

- Over 40 special escape sequences to control information
- current time, date, host info, current directory, etc...

### Watching for other users
#### Events

- The user who logged in/out: use their username
- The host where the user was connected from: use `@` followed by the remote hostname
- The line(tty) that the user was connected on: use `%` followed by the line name(ie, pts/186)

#### Telling zsh to look for events

    watch=all
    watch=$USERNAME
    watch=(event1 event2 ... eventN)

#### Obtaining the report

Setting `LOGCHECK` to interger `n` will cause zsh to report monitored events every `n` seconds.(default 60)

Then run `log` at any time.


## Conveniences
### Aliases

Every token in the input is checked to see if there is an alias defined for it. If there is, the token will be replaced by the alias value IF:

- The token is in command position OR
- The alias is global (See below) OR
- The previous word on the line was an alias whose value ended in a space.

#### Using

The formal syntax of the zsh alias builtin is:

    alias [ -gmrL ] [ name[=value] ... ]

- The `-r` argument tells the alias command to operate on regular aliases.
- The `-g` argument tells the alias command to operate on global aliases.
- Without either the r or g flags, alias operates on both types.

For each name with no value, zsh will print the name and what it is aliased to.

With no arguments at all, `alias` prints the values of ALL defined aliases

With the `-L` argument, the output from alias is suitable to cut-and-paste into your startup scripts.

To define one or more aliases, simply enter

    alias name1=value1 name2=value2 ... nameX=valueX

For each name with a corresponding value, zsh defines an alias with that value.

#### Global aliases

zsh lets you use aliases even if they are not the first word on the command line. These kinds of aliases are called global aliases.

    alias -g

#### List aliases that match pattern

    alias -m

#### Disable or delete aliases

- delete: `unalias foo`
- temporarily disable: `disable -a foo`
- enable back: `enable -a foo`

#### Use the origin command

`=ftp` or `\ftp`.


### Command `cd`

`cd` == `chdir`

#### First form

- `cd`: `cd ${HOME}`
- `cd NEW_DIR`: Place you in the directory called `NEW_DIR`
- `cd -`: `cd ${OLDPWD}`

zsh adds some usefull functionality:

First, if zsh doesn't find `NEW_DIR` in the current directory (and `NEW_DIR` isn't an absolute path), zsh looks at the shell variable cdpath. It looks for a subdirectory `NEW_DIR` in each directory of cdpath. If zsh sees `NEW_DIR`, it goes there.

Furthermore, you can store the FULL pathname of directory in a shell variable.

    XDIR=/usr/lib/X11
    cd XDIR # without the "$"

XDIR is a **named directory**

#### Second form

    cd OLD NEW

and zsh replaced any occurance of `OLD` in the current directory with `NEW`, and then cd's into it.

#### Third form

Pull an entry from the direcotry stack.

    cd +n
    cd -n

`dirs -v` to see the direcotry stack.

#### Arguments

All forms of the cd builtin can take a few arguments:
- cd -s DIR   Don't cd into DIR if DIR's path contains symlinks
- cd -P DIR   Resolve all symlinks to their true values before changing to DIR
- cd -L DIR   Symlinks are followed, ignoring the `CHASE_LINKS` option)

Note: Turning on the shell option `CHASE_LINKS` is the same as the `-P` argument to cd.

### Directory stack

Zsh has an internal directory stack. This is a facility that can help you manage working in many different direcotries throughout your **zsh login session**.

- `pushd`: place onto the direcotry stack
- `popd`: get and remove one from the stack top

#### Command `dirs`

    dirs -v  # view the contents of the stack
    dirs dir1 dir2 ... dirN  # rebuild the stack, staring with the rightmost dirN, and push $PWD on the top

#### `popd`, `pushd`

TODO

#### Filename Expansion and the Directory Stack

Zsh offers a nice way to reference the directory stack quickly in your daily work. The description below is taken directly from the man page:

- A `~` followed by a number is replaced by the directory at that position in the directory stack.
- `~0` is equivalent to `~+`, and `~1` is the top of the stack.
- `~+` followed by a number is replaced by the directory at that position in the directory stack.
- `~+0` is equivalent to `~+`, and `~+1` is the top of the stack.
- `~-` followed by a number is replaced by the directory that many positions from the bottom of the stack.
- `~-0` is the bottom of the stack.
- The `PUSHD_MINUS` option exchanges the effects of `~+` and `~-` where they are followed by a number.


### Brace Expansion

Brace expansion is a convenient feature that allows you to generate lists of items quickly on the command line.

    echo str{xx,yy,zz}
    echo logfile.1610{01..31}.log

## Programing Zsh
### Parameters

- names: can be any sequence of alpha-numeric characters and underscores. (There are a few special cases, namely * , @ , # , ? , - , $ , and !)
- values: the pieces of information that variables store.
- Values in zsh can be one of three types: strings, integers, or arrays.

**Assigning values**

    name=value
    name=(value1 value2 ... valueN) # array parameter
    unset PARAMETER_NAME # delete parameter

**Scope**

- Shell functions delimit scope for shell parameters.
- If you assign a value to a variable that doesn't exist, the variable gets created in the outermost scope.
- If a variable X goes out of scope, it gets deleted. (Just like in C).

**Positional parameters**

- start with the number 0
- can go past 9. So $11 is the 11th argument.
- contain all the positional parameters: `&`, `*`, `argv`

#### Array Parameters

    array_name=(value1 value2 ... valueN)
    set -A array_name value1 value2 .. valueN

##### Single element subscripts

subscripts are used to select one of more individual items from an array. zsh's mechanism for subscripting into arrays is so powerful, it can be considered superior to many programming languages.

The index are start from 1.

    some_array[expr]
    ARGV[-2]

##### Obtaining Multiple Consecutive Elements

    some_array[expr1,expr2]

This returns elements (in `some_array`) starting from expr1, up to and including expr2.

Again, the expressions are evaluated to integers before being used, and negative numbers are used in the same way as descibed above.

Subscripts can be included with variable names inside curly braces...

    ${friends[2,5]}

##### Replacing Portions of Arrays

    > veg=(lettuce carrot celery tomato onion)
    > echo $veg
    lettuce carrot celery tomato onion
    > veg[4]=(pepper radish)
    > echo $veg
    lettuce carrot celery pepper radish onion

##### Subscripting Strings

This item is not quite related to arrays, but it's too useful to pass up.

#### Sbscript flags

TODO

#### Parameter expansion

TODO

### Filename generation

TODO

#### Modifiers

TODO

#### Filename qualifiers

TODO


## Programmable completion

>Before proceeding, keep the zshcompctl man page in mind.

Completion refers to zsh's ability to finish your command lines for you. It comes in many forms. By default, the < TAB > key is bound to a completion command in zsh.

Filenames are the default item to complete on. In zsh, ANYTHING can be completed, including:

- Filenames
- Filesystems paths
- builtin commands
- external commands
- aliases
- shell functions
- reserved words
- global aliases
- disabled hash table elements
- shell options
- shell parameter names
- environment variables
- named directories
- key bindings
- running jobs
- suspended jobs
- user names
- anything else you can imagine - you can program it yourself easily.


## Links

- [Zsh Workshop: Table of Contents](https://www-s.acm.illinois.edu/workshops/zsh/toc.html)
- [A User's Guide to the Z-Shell](http://zsh.sourceforge.net/Guide/zshguide.html)
- [zsh: Table of Contents](http://zsh.sourceforge.net/Doc/Release/zsh_toc.html)

## QQ chat group

By the way, I created a QQ chat group to discuss "Using Zsh": 481187270

Zsh 爱好者交流群: 481187270