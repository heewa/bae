Emoji for the shell – use emoji as Environment Variables using the same names that Github, Slack, and many others use. Check the [Emoji Cheat Sheet](http://emoji-cheat-sheet.com).

## Installing

### Bash

Drop the emoji file somewhere:

```bash
curl 'https://raw.githubusercontent.com/heewa/bae/master/emoji_vars.sh' > ~/.emoji_vars.sh
```

And include it in your `~/.profile` (preferably) or `~/.bashrc`:

```bash
if [ -e ~/.emoji_vars.sh ]; then
    source ~/.emoji_vars.sh
fi
```

### Fish

Drop the emoji file somewhere:

```bash
curl 'https://raw.githubusercontent.com/heewa/bae/master/emoji_vars.fish' > ~/.emoji_vars.fish
```

And include it in your `fish.config`:

```bash
if test -f $HOME/.emoji_vars.fish
    source $HOME/.emoji_vars.fish
end
```

## Using

```bash
$ echo $E_STARS $E_TELESCOPE $E_MONKEY $E_EAR_OF_RICE
🌠 🔭 🐒 🌾

$ echo $E_FIRE $E_FIRE $E_FIRE $E_FIRE $E_FIRE $E_DOG $E_FIRE $E_FIRE this is fine
🔥 🔥 🔥 🔥 🔥 🐶 🔥 🔥 this is fine

$ do-something && echo $E_THUMBSUP || echo $E_THUMBSDOWN
👍

$ git commit -a -m "Fix race condition $E_TADA"
[master 687c204] Fix race condition 🎉
 1 file changed, 1 insertion(+), 1 deletion(-)
```

