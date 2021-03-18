[Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)

## Important shell/terminal commands

```
# To make a directory
$ mkdir <directory_name_no_spaces>

# list directories, -la parameters show hidden files and permissions
$ ls -la

# remove file
$ rm <ABSOLUTE FILE_PATH OR NAME>

# remove directory (folder)
$ rm -r <ABSOLUTE Dir_PATH OR NAME>
```
## Strings

### F-strings
for when you want to mix variables with strings

example:

```
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
```

### Important string methods

.title() will capatilize the first character of each letter in string

```
title()
full_name.title()
# Ada Lovelace
```