# choosem

`choosem` is a [choose] based picker and launcher for macos.
Currently these functionalities are available:

* Insert select character from character dictionaries
* Focus [Yabai] program
* Launch programs

# install

for python 3.6+:
```
$ pip install --user choosem 
...
$ choosem --help
Usage: choosem [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  insert  insert character into active window
  yabai   control yabai windows manager
```

## Known issues

`insert` command might stop working, for this accessibility permission needs to be disabled and then enabled again.

[choose]: https://github.com/chipsenkbeil/choose


