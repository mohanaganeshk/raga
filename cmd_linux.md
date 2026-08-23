---
title: "60 essential Linux commands with syntax & examples"
author: "Aris Sentika"
date: "2026-05-06T09:31:57.000Z"
publisher: "Hostinger"
lang: "en"
description: "Master 60 essential Linux commands with syntax, options, examples, and troubleshooting tips. Covers file operations, networking, system monitoring, and more."
url: "https://www.hostinger.com/in/tutorials/linux-commands"
word_count: 6434
reading_time: "25 min read"
---

## Table of Contents

- [Top 60 Linux commands](#top-60-linux-commands)
- [Linux commands cheat sheet](#linux-commands-cheat-sheet)
- [1. ls command](#1-ls-command)
- [2. pwd command](#2-pwd-command)
- [3. cd command](#3-cd-command)
- [4. mkdir command](#4-mkdir-command)
- [5. rmdir command](#5-rmdir-command)
- [6. rm command](#6-rm-command)
- [7. cp command](#7-cp-command)
- [8. mv command](#8-mv-command)
- [9. touch command](#9-touch-command)
- [10. file command](#10-file-command)
- [11. zip and unzip commands](#11-zip-and-unzip-commands)
- [12. tar command](#12-tar-command)
- [13. nano, vi, and jed command](#13-nano-vi-and-jed-command)
- [14. cat command](#14-cat-command)
- [15. grep command](#15-grep-command)
- [16. sed command](#16-sed-command)
- [17. head command](#17-head-command)
- [18. tail command](#18-tail-command)
- [19. awk command](#19-awk-command)
- [20. sort command](#20-sort-command)
- [21. cut command](#21-cut-command)
- [22. diff command](#22-diff-command)
- [23. tee command](#23-tee-command)
- [24. locate command](#24-locate-command)
- [25. find command](#25-find-command)
- [26. sudo command](#26-sudo-command)
- [27. su and whoami commands](#27-su-and-whoami-commands)
- [28. chmod command](#28-chmod-command)
- [29. chown command](#29-chown-command)
- [30. useradd, passwd, and userdel command](#30-useradd-passwd-and-userdel-command)
- [31. df command](#31-df-command)
- [32. du command](#32-du-command)
- [33. top command](#33-top-command)
- [34. htop command](#34-htop-command)
- [35. ps command](#35-ps-command)
- [36. uname command](#36-uname-command)
- [37. hostname command](#37-hostname-command)
- [38. time command](#38-time-command)
- [39. systemctl command](#39-systemctl-command)
- [40. watch command](#40-watch-command)
- [41. jobs command](#41-jobs-command)
- [42. kill command](#42-kill-command)
- [43. shutdown command](#43-shutdown-command)
- [44. ping command](#44-ping-command)
- [45. wget command](#45-wget-command)
- [46. cURL command](#46-curl-command)
- [47. scp command](#47-scp-command)
- [48. rsync command](#48-rsync-command)
- [49. ip command](#49-ip-command)
- [50. netstat command](#50-netstat-command)
- [51. traceroute command](#51-traceroute-command)
- [52. nslookup command](#52-nslookup-command)
- [53. dig command](#53-dig-command)
- [54. history command](#54-history-command)
- [55. man command](#55-man-command)
- [56. echo command](#56-echo-command)
- [57. ln command](#57-ln-command)
- [58. alias and unalias commands](#58-alias-and-unalias-commands)
- [59. cal command](#59-cal-command)
- [60. apt and dnf command](#60-apt-and-dnf-command)
- [Common errors when running Linux commands (and how to fix them)](#common-errors-when-running-linux-commands-and-how-to-fix-them)
  - [“command not found”](#command-not-found)
  - [“Permission denied”](#permission-denied)
  - [“No such file or directory”](#no-such-file-or-directory)
  - [Command runs but does nothing visible](#command-runs-but-does-nothing-visible)
- [What should you learn next after mastering Linux commands?](#what-should-you-learn-next-after-mastering-linux-commands)

---

[Tutorials](https://www.hostinger.com/in/tutorials) [VPS](https://www.hostinger.com/in/tutorials/vps/) [Managing, monitoring and security](https://www.hostinger.com/in/tutorials/vps/managing-monitoring-and-security/)

## Top 60 Linux commands

May 06, 2026

/

By Aris S.

/

16 min Read

![Top 60 Linux commands](https://imagedelivery.net/LqiWLm-3MGbYHtFuUbcBtA/wp-content/uploads/sites/52/2026/05/linux-commands-2.png/w=1110,h=454,fit=scale-down) Summarize with:

[ChatGPT](https://chat.openai.com/?q=Summarize+key+take+aways+from+this+article+.+Highlight+how+Hostinger%27s+tools+help+users+achieve+website+growth+and+online+success+based+on+this+guide.) [Claude.ai](https://claude.ai/new?q=Summarize+key+take+aways+from+this+article+.+Highlight+how+Hostinger%27s+tools+help+users+achieve+website+growth+and+online+success+based+on+this+guide.) [Google AI](https://www.google.com/search?udm=50&aep=11&q=Summarize+key+take+aways+from+this+article+.+Highlight+how+Hostinger%27s+tools+help+users+achieve+website+growth+and+online+success+based+on+this+guide.) [Grok](https://x.com/i/grok?text=Summarize+key+take+aways+from+this+article+.+Highlight+how+Hostinger%27s+tools+help+users+achieve+website+growth+and+online+success+based+on+this+guide.) [Perplexity](https://www.perplexity.ai/search/new?q=Summarize+key+take+aways+from+this+article+.+Highlight+how+Hostinger%27s+tools+help+users+achieve+website+growth+and+online+success+based+on+this+guide.)

Follow: [![Add as Google Prefered Source](https://www.hostinger.com/in/tutorials/wp-content/themes/hostinger/public/images/google-prefered-source/google_preferred_source_badge_dark_en.png)](https://www.google.com/preferences/source?q=hostinger.com)

A Linux command is a text instruction entered in the terminal to make the operating system perform a specific task, such as listing files, managing users, monitoring processes, or configuring network settings. Linux commands provide direct control over the system, enabling faster execution, automation, and more precise resource management than graphical interfaces.

Linux commands fall into six main categories:

1.  Filesystem navigation commands that move between directories and paths
2.  File and directory management commands that create, modify, and organize files
3.  User and permission commands that control access and ownership
4.  Process and system monitoring commands that track performance and running services
5.  System operation commands that manage shutdowns, reboots, and configurations
6.  Network commands that configure connections and diagnose connectivity

Each category below includes essential commands with their syntax, commonly used options, and real-world examples, allowing quick lookup and practical application for learning, server management, or daily terminal use.

## Linux commands cheat sheet

| Command    | What it does                    |
| ---------- | ------------------------------- |
| ls         | List directory contents         |
| pwd        | Show current directory path     |
| cd         | Change directory                |
| locate     | Search files by name            |
| find       | Search files and directories    |
| mkdir      | Create a directory              |
| rmdir      | Remove an empty directory       |
| rm         | Delete files or directories     |
| cp         | Copy files or directories       |
| mv         | Move or rename files            |
| touch      | Create an empty file            |
| file       | Show file type                  |
| zip        | Compress files into ZIP archive |
| unzip      | Extract ZIP archive             |
| tar        | Archive files and directories   |
| nano       | Edit files with Nano            |
| vi         | Edit files with Vi              |
| jed        | Edit files with Jed             |
| cat        | Display file content            |
| grep       | Search text patterns in files   |
| sed        | Replace or modify text patterns |
| head       | Show first lines of a file      |
| tail       | Show last lines of a file       |
| awk        | Process and analyze text        |
| sort       | Sort file content               |
| cut        | Extract sections of text        |
| diff       | Compare two files               |
| tee        | Output to terminal and file     |
| sudo       | Run command as administrator    |
| su         | Switch user account             |
| whoami     | Show current user               |
| chmod      | Change file permissions         |
| chown      | Change file ownership           |
| useradd    | Create new user                 |
| userdel    | Delete user account             |
| passwd     | Set or change password          |
| df         | Show disk space usage           |
| du         | Show directory size             |
| top        | Display running processes       |
| htop       | Interactive process viewer      |
| ps         | Show process snapshot           |
| uname      | Show system information         |
| hostname   | Show or set hostname            |
| time       | Measure command execution time  |
| systemctl  | Manage system services          |
| watch      | Run command repeatedly          |
| jobs       | List shell background jobs      |
| kill       | Terminate a process             |
| shutdown   | Shut down or restart system     |
| ping       | Test network connectivity       |
| wget       | Download files from the web     |
| curl       | Transfer data via URL           |
| scp        | Copy files over SSH             |
| rsync      | Sync files between systems      |
| ip         | Manage network settings         |
| netstat    | Show network connections        |
| traceroute | Trace network packet path       |
| nslookup   | Query DNS records               |
| dig        | Detailed DNS lookup             |
| history    | Show command history            |
| man        | Show command manual             |
| echo       | Print text to terminal          |
| ln         | Create file links               |
| alias      | Create command shortcut         |
| unalias    | Remove command shortcut         |
| cal        | Display calendar                |
| apt        | Manage packages (Debian-based)  |
| dnf        | Manage packages (RHEL-based)    |

![](https://imagedelivery.net/LqiWLm-3MGbYHtFuUbcBtA/wp-content/uploads/sites/2/2023/02/VPS-hosting-banner.png/w=1024,h=1024,fit=scale-down)

Tutorials VPS Managing, monitoring and security

## 1. ls command

The [`ls` command](https://www.hostinger.com/in/tutorials/ls-command/) displays files and directories within a specified location.

Syntax:

```
ls [options] [directory_or_path]
```

Common options:\
• `-a` → shows hidden files, including those starting with a dot (`.`)\
• `-l` → displays a detailed list with permissions, ownership, size, and timestamps

Example:

```
ls -Ra /path/to/dir
```

Lists all files and subdirectories recursively inside `/path/to/dir`, including hidden files, allowing you to inspect the full directory structure.

## 2. pwd command

The `pwd` command prints the full path of the current working directory.

Syntax:

```
pwd [options]
```

Common options:\
• `-L` → prints the logical path using symbolic links or environment shortcuts\
• `-P` → prints the physical path by resolving all symbolic links

Example:

```
pwd -P
```

Displays the exact directory path without symbolic links, helping verify the actual location of the current working directory.

## 3. cd command

The `cd` command changes the current working directory to a specified location.

Syntax:

```
cd [path_or_directory]
```

Common options: *(no options available for this command)*

Common shortcuts:\
• `cd` → moves to the current user’s home directory\
• `cd ..` → moves one directory up\
• `cd -` → returns to the previous directory

Example:

```
cd /var/www/html
```

Changes the current directory to `/var/www/html`, allowing you to access and manage files in that location.

## 4. mkdir command

The `mkdir` command creates one or more directories at a specified location.

Syntax:

```
mkdir [options] directory_name1 directory_name2
```

Common options:\
• `-m` → sets custom permissions for the new directory (e.g., `-m 755`)\
• `-p` → creates parent directories as needed and avoids errors if they already exist

Example:

```
mkdir -p /path/to/target_folder/new_folder
```

Creates the directory `/path/to/target_folder/new_folder`, including any missing parent directories, allowing you to build nested folder structures in one command.

## 5. rmdir command

The `mkdir` command creates one or more directories at a specified location.

Syntax:

```
mkdir [options] directory_name1 directory_name2
```

Common options:\
• `-m` → sets custom permissions for the new directory (e.g., `-m 755`)\
• `-p` → creates parent directories as needed and avoids errors if they already exist

Example:

```
mkdir -p /path/to/target_folder/new_folder
```

Creates the directory `/path/to/target_folder/new_folder`, including any missing parent directories, allowing you to build nested folder structures in one command.

## 6. rm command

The `rm` command removes files or directories from the file system.

Syntax:

```
rm [options] file1 file2
```

Common options:\
• `-r` → removes directories and their contents recursively\
• `-f` → forces deletion without confirmation prompts\
• `-i` → prompts for confirmation before each removal

Example:

```
rm -rf folder-name
```

Deletes the directory `folder-name` and all its contents recursively without confirmation, which is useful for cleanup tasks but requires caution to avoid accidental data loss.

## 7. cp command

The `cp` command copies files or directories from one location to another.

Syntax:

```
cp [options] source_file target_path
```

Common options:\
• `-R` → copies directories and their contents recursively\
• `-i` → prompts before overwriting existing files\
• `-v` → displays detailed output of the copy process

Example:

```
cp -R /path/to/folder /target/path/to/folder_copy
```

Copies the directory `/path/to/folder` and all its contents to `/target/path/to/folder_copy`, preserving the structure for backup or duplication tasks.

## 8. mv command

The `mv` command moves or [renames files and directories](https://www.hostinger.com/in/tutorials/how-to-rename-files-in-linux/).

Syntax:

```
mv [options] source target
```

Common options:\
• `-i` → prompts before overwriting existing files\
• `-v` → displays detailed output of the move operation\
• `-n` → prevents overwriting existing files

Example:

```
mv /original/path/file1.txt /new/file/directory/
```

Moves `file1.txt` from `/original/path/` to `/new/file/directory/`, allowing you to reorganize files or relocate them to a different folder.

## 9. touch command

The [`touch` command](https://www.hostinger.com/in/tutorials/linux-touch-command/) creates a new empty file or updates the timestamp of an existing file.

Syntax:

```
touch [options] [path_and_file_name]
```

Common options:\
• `-c` → avoids creating a file if it does not exist\
• `-t` → sets a specific timestamp for the file\
• `-a` → updates only the access time

Example:

```
touch file.txt
```

Creates an empty file named `file.txt` in the current directory, allowing you to quickly generate placeholder or configuration files.

## 10. file command

The [`file` command](https://www.hostinger.com/in/tutorials/linux-file-command/) identifies the type of a file based on its content.

Syntax:

```
file [file_name]
```

Common options:\
• `-k` → displays additional information about the file type\
• `-i` → shows the MIME type of the file\
• `-L` → follows [symbolic links](https://www.hostinger.com/in/tutorials/how-to-create-symbolic-links-in-linux/) and reports the actual file type

Example:

```
file hostinger_sym.txt
```

Displays the actual file type that `hostinger_sym.txt` points to, which helps verify symbolic links or detect unknown file formats.

## 11. zip and unzip commands

The `zip` command compresses files or directories into a ZIP archive, while the `unzip` command [extracts files from a ZIP archive](https://www.hostinger.com/in/tutorials/how-to-unzip-files-linux/).

Syntax:

```
zip [options] zip_file_name file1 file2
unzip [options] zip_file_name
```

Common options:\
• `-r` (zip) → compresses directories recursively\
• `-e` (zip) → encrypts the archive with a password\
• `-l` (unzip) → lists contents of the archive without extracting\
• `-d` (unzip) → extracts files to a specified directory

Example:

```
zip -r archive.zip /path/to/folder && unzip archive.zip
```

Creates a compressed archive `archive.zip` from `/path/to/folder` and then extracts its contents into the current directory, allowing you to bundle and restore files efficiently.

## 12. tar command

The [`tar` command](https://www.hostinger.com/in/tutorials/linux-tar-command-with-examples/) creates, extracts, and manages archive files that bundle multiple files or directories.

Syntax:

```
tar [options] tar_file_name file1 file2
```

Common options:\
• `-c` → creates a new archive\
• `-x` → extracts files from an archive\
• `-f` → specifies the archive file name\
• `-z` → compresses or decompresses using gzip

Example:

```
tar -czf archive.tar.gz file1.txt file2.txt
```

Creates a compressed archive `archive.tar.gz` containing `file1.txt` and `file2.txt`, allowing you to bundle and reduce file size in a single command.

## 13. nano, vi, and jed command

The `nano`, `vi`, and `jed` commands open and edit text files directly in the terminal.

Syntax:

```
nano file_name
vi file_name
jed file_name
```

Common options: *(no commonly used options required for basic file editing)*

Example:

```
nano file.txt
```

Opens `file.txt` in the Nano text editor, allowing you to create or modify file content directly from the terminal.

## 14. cat command

The [`cat` command](https://www.hostinger.com/in/tutorials/linux-cat-command/) displays, combines, or creates files by reading and writing file content.

Syntax:

```
cat [options] file_name
```

Common options:\
• `-n` → displays line numbers alongside file content\
• `-b` → displays line numbers for non-empty lines only\
• `-s` → suppresses repeated empty lines

Example:

```
cat file1.txt file2.txt > target.txt
```

Combines the contents of `file1.txt` and `file2.txt` into `target.txt`, allowing you to merge multiple files into a single output file.

## 15. grep command

The [`grep` command](https://www.hostinger.com/in/tutorials/grep-command-in-linux/) searches for specific patterns or keywords within files or command output.

Syntax:

```
grep [options] keyword [file]
```

Common options:\
• `-i` → performs a case-insensitive search\
• `-r` → searches recursively through directories\
• `-n` → displays line numbers with matching results

Example:

```
ls | grep "file.txt"
```

Filters the output of the `ls` command to show only entries that match `file.txt`, allowing you to quickly locate specific items in a list.

## 16. sed command

The [`sed` command](https://www.hostinger.com/in/tutorials/linux-sed-command/) searches, replaces, and transforms text within files or input streams.

Syntax:

```
sed [options] 's/pattern/replacement/' file
```

Common options:\
• `-i` → edits files in place without creating a new output\
• `-n` → suppresses automatic output (used with explicit print commands)\
• `-e` → allows multiple editing expressions

Example:

```
sed 's/red/blue/' colors.txt
```

Replaces the first occurrence of `red` with `blue` in each line of `colors.txt`, allowing quick text modifications without opening a file manually.

## 17. head command

The `head` command displays the first lines or bytes of a file or command output.

Syntax:

```
head [options] file_name
```

Common options:\
• `-n` → specifies the number of lines to display\
• `-c` → specifies the number of bytes to display

Example:

```
head -n 5 file.txt
```

Displays the first five lines of `file.txt`, allowing you to quickly preview the beginning of a file without opening it fully.

## 18. tail command

The [`tail` command](https://www.hostinger.com/in/tutorials/how-to-use-tail-command/) displays the last lines or bytes of a file or command output.

Syntax:

```
tail [options] file_name
```

Common options:\
• `-n` → specifies the number of lines to display\
• `-c` → specifies the number of bytes to display\
• `-f` → follows the file in real time as new lines are added

Example:

```
ping -c 10 8.8.8.8 | tail -n 5
```

Displays the last five lines of the `ping` command output, allowing you to focus on the most recent results or summaries.

## 19. awk command

The [`awk` command](https://www.hostinger.com/in/tutorials/awk-command/) processes and analyzes text by applying patterns and actions to structured data.

Syntax:

```
awk 'pattern {action}' input_file
```

Common options:\
• `-F` → specifies a custom field separator\
• `-v` → assigns variables for use within the command\
• `-f` → reads the `awk` program from a file

Example:

```
awk -F':' '{ total += $2; students[$1] = $2 } END { average = total / length(students); for (student in students) if (students[student] > average) print student }' score.txt
```

Calculates the average value from `score.txt` and prints the names of entries with values above the average, allowing you to perform data analysis directly in the terminal.

## 20. sort command

The `sort` command arranges lines of text in a file or input stream in a specified order.

Syntax:

```
sort [options] [file_name]
```

Common options:\
• `-r` → sorts in reverse order\
• `-n` → sorts numerically instead of alphabetically\
• `-k` → sorts based on a specific column or field

Example:

```
sort -n file.txt
```

Sorts the contents of `file.txt` numerically and prints the result to the terminal without modifying the original file.

## 21. cut command

The [`cut` command](https://www.hostinger.com/in/tutorials/linux-cut-command/) extracts specific sections of text from each line of a file or input stream.

Syntax:

```
cut [options] file
```

Common options:\
• `-f` → selects specific fields (columns)\
• `-d` → specifies a delimiter to separate fields\
• `-c` → extracts specific character positions\
• `-b` → extracts specific byte ranges

Example:

```
cut -d',' -f3-5 list.txt
```

Extracts the third to fifth fields from each line in `list.txt` using a comma as the delimiter, allowing you to isolate structured data from files like CSVs.

## 22. diff command

The `diff` command compares two files and displays the differences between them.

Syntax:

```
diff [options] file_name1 file_name2
```

Common options:\
• `-c` → displays differences in context format with surrounding lines\
• `-u` → shows unified output format (commonly used for patches)\
• `-i` → ignores differences in letter case

Example:

```
diff -c 1.txt 2.txt
```

Displays the differences between `1.txt` and `2.txt` with surrounding context, making it easier to understand changes between file versions.

## 23. tee command

The [`tee` command](https://www.hostinger.com/in/tutorials/linux-tee-command-with-examples/) writes command output to both the terminal and a file simultaneously.

Syntax:

```
command | tee [options] file_name
```

Common options:\
• `-a` → appends output to the file instead of overwriting it\
• `-i` → ignores interrupt signals (useful in pipelines)

Example:

```
ping 8.8.8.8 | tee -a test_network.txt
```

Appends the output of the `ping` command to `test_network.txt` while displaying it in the terminal, allowing you to monitor and save results at the same time.

## 24. locate command

The [`locate` command](https://www.hostinger.com/in/tutorials/how-to-use-find-and-locate-commands-in-linux/) searches for files by name using a prebuilt system database.

Syntax:

```
locate [options] keyword
```

Common options:\
• `-i` → performs a case-insensitive search\
• `-r` → searches using a regular expression\
• `-n` → limits the number of results displayed

Example:

```
locate -i filename.txt
```

Searches for all files matching `filename.txt` regardless of case, returning results quickly based on the system’s file index.

## 25. find command

The `find` command searches for files and directories in a specified path based on conditions.

Syntax:

```
find [path] [options] expression
```

Common options:\
• `-name` → searches for items by name\
• `-type f` → limits results to files\
• `-type d` → limits results to directories

Example:

```
find /path/to/folder -type f -name "file.txt"
```

Searches for a file named `file.txt` within `/path/to/folder`, returning matches in real time based on the specified criteria.

## 26. sudo command

The [`sudo` command](https://www.hostinger.com/in/tutorials/sudo-and-the-sudoers-file/) runs a command with elevated (administrator) privileges.

Syntax:

```
sudo [options] command
```

Common options:\
• `-u` → runs the command as a specified user\
• `-i` → starts a shell with root privileges\
• `-l` → lists allowed commands for the current user

Example:

```
sudo nano file.txt
```

Opens `file.txt` in the Nano editor with administrator privileges, allowing you to modify system-level files that require elevated access.

## 27. su and whoami commands

The `su` command switches the current user to another user account, while the `whoami` command displays the currently logged-in user.

Syntax:

```
su [options] [username]
whoami
```

Common options:\
• `-` → starts a login shell for the target user\
• `-c` → runs a single command as the specified user

Example:

```
su - root
```

Switches to the root user and starts a login shell, allowing you to execute commands with full system privileges.

## 28. chmod command

The [`chmod` command](https://www.hostinger.com/in/tutorials/how-to-change-linux-permissions-and-owners/) changes file and directory permissions for users, groups, and others.

Syntax:

```
chmod [options] permissions file_or_directory
```

Common options:\
• `-R` → applies changes recursively to directories and their contents\
• `-v` → displays a message for each processed file\
• `-c` → reports only when a change is made

Example:

```
chmod 744 file1.txt
```

Sets permissions for `file1.txt` so the owner can read, write, and execute, while others can only read, allowing controlled access to the file.

## 29. chown command

The [`chown` command](https://www.hostinger.com/in/tutorials/linux-chown-command/) changes the ownership of files and directories.

Syntax:

```
chown [options] owner:group file1 file2
```

Common options:\
• `-R` → applies ownership changes recursively\
• `-v` → displays a message for each processed file\
• `-c` → reports only when a change is made

Example:

```
chown admin-vps:developers file1.txt
```

Sets `admin-vps` as the owner and `developers` as the group for `file1.txt`, allowing proper access control and file management.

## 30. useradd, passwd, and userdel command

The `useradd` command creates a new user account, the [`passwd` command](https://www.hostinger.com/in/tutorials/how-to-change-password-in-linux/) sets or updates a user’s password, and the `userdel` command removes a user account.

Syntax:

```
useradd [options] username
passwd username
userdel [options] username
```

Common options:\
• `-m` (useradd) → creates a home directory for the user\
• `-r` (userdel) → removes the user’s home directory and files\
• `-l` (passwd) → locks a user account

Example:

```
sudo useradd -m newuser && sudo passwd newuser
```

Creates a new user `newuser` with a home directory and sets a password, allowing the account to log in and use the system.

## 31. df command

The [`df` command](https://www.hostinger.com/in/tutorials/how-to-check-disk-space-in-linux/) displays disk space usage for file systems.

Syntax:

```
df [options] [file_system]
```

Common options:\
• `-h` → shows output in human-readable format (KB, MB, GB)\
• `-T` → displays the file system type\
• `-a` → includes all file systems, including empty ones

Example:

```
df -h
```

Displays disk usage for all mounted file systems in a human-readable format, helping you quickly assess available and used storage space.

## 32. du command

The **du** command checks the size of a directory and its content.

Syntax:

```
du [directory]
```

The command will check your working directory if you don’t specify a path or folder. By default, it breaks down each subfolder’s disk usage, but you can add the **-s** option to summarize the total usage in one output.

You can also use the **-M** option to change the information from **KB** to **MB**.

## 33. top command

The `top` command displays real-time information about running processes and system resource usage.

Syntax:

```
top [options]
```

Common options:\
• `-p` → monitors a specific process by its ID (PID)\
• `-d` → sets the delay between screen updates\
• `-u` → shows processes for a specific user

Example:

```
top -u root
```

Displays real-time resource usage for processes owned by the `root` user, helping you monitor system performance and identify resource-heavy tasks.

## 34. htop command

The [`htop` command](https://www.hostinger.com/in/tutorials/how-to-list-processes-in-linux/) displays and manages running processes in an interactive interface.

Syntax:

```
htop [options]
```

Common options:\
• `-d` → sets the update interval\
• `-u` → shows processes for a specific user\
• `--tree` → displays processes in a hierarchical tree view

Example:

```
htop
```

Opens an interactive process viewer that shows CPU and memory usage, allowing you to navigate, filter, and manage processes in real time.

## 35. ps command

The `ps` command displays a snapshot of currently running processes.

Syntax:

```
ps [options]
```

Common options:\
• `-A` → shows all running processes\
• `-u` → displays processes for a specific user\
• `-r` → lists only running processes

Example:

```
ps -A
```

Displays all active processes on the system at a specific moment, allowing you to inspect process IDs, statuses, and resource usage.

## 36. uname command

The `uname` command displays system information such as the kernel, architecture, and operating system.

Syntax:

```
uname [options]
```

Common options:\
• `-a` → displays all available system information\
• `-r` → shows the kernel release version\
• `-m` → displays the machine hardware architecture

Example:

```
uname -a
```

Displays complete system information, including kernel version and architecture, helping you identify your Linux environment.

## 37. hostname command

The `hostname` command displays or sets the system’s hostname.

Syntax:

```
hostname [options]
```

Common options:\
• `-i` → displays the IP address of the host\
• `-a` → shows the hostname alias\
• `-A` → displays the fully qualified domain name (FQDN)

Example:

```
hostname -A
```

Displays the system’s fully qualified domain name, helping identify the server within a network or domain.

## 38. time command

The [`time` command](https://www.hostinger.com/in/tutorials/linux-time-command/) measures how long a command or script takes to execute.

Syntax:

```
time command
```

Common options: *(no commonly used options required for basic usage)*

Example:

```
time ls -la
```

Measures how long the `ls -la` command takes to run, providing execution time details such as real, user, and system time.

## 39. systemctl command

The **systemctl** command manages services in your Linux system.

Syntax:

```
systemctl subcommand [service_name][options]
```

The subcommands represent your task, like listing, restarting, terminating, or enabling the services. For example, we will [list Linux services](https://www.hostinger.com/in/tutorials/manage-and-list-services-in-linux/) using this:

```
sudo systemctl list-unit-files --type service --all
```

Note that this command might not work with older distributions since they use another service manager.

## 40. watch command

The [`watch` command](https://www.hostinger.com/in/tutorials/linux-watch-command/) runs a command repeatedly at specified intervals and displays the updated output.

Syntax:

```
watch [options] command
```

Common options:\
• `-n` → sets the interval in seconds between executions\
• `-d` → highlights changes between updates

Example:

```
watch -n 5 netstat
```

Runs the `netstat` command every five seconds and updates the output, allowing you to monitor changes in network activity over time.

## 41. jobs command

The `jobs` command lists background and suspended jobs in the current shell session.

Syntax:

```
jobs [options] [job_id]
```

Common options:\
• `-l` → displays job IDs along with process IDs\
• `-n` → shows only jobs that have changed status\
• `-p` → lists only process IDs

Example:

```
jobs -l
```

Displays all jobs in the current shell with their process IDs, allowing you to monitor and manage background tasks.

## 42. kill command

The [`kill` command](https://www.hostinger.com/in/tutorials/how-to-kill-a-process-in-linux/) sends a signal to terminate or control a process by its process ID (PID).

Syntax:

```
kill [signal] process_id
```

Common options:\
• `-15` → sends the default SIGTERM signal for graceful termination\
• `-9` → sends SIGKILL to forcefully terminate a process\
• `-l` → lists all available signals

Example:

```
kill -9 1234
```

Forcefully terminates the process with ID `1234`, which is useful when a program becomes unresponsive.

## 43. shutdown command

The [`shutdown` command](https://www.hostinger.com/in/tutorials/linux-shutdown-command/) powers off or restarts the system at a specified time.

Syntax:

```
shutdown [options] [time] [message]
```

Common options:\
• `-r` → restarts the system instead of shutting it down\
• `-h` → halts or powers off the system\
• `-c` → cancels a scheduled shutdown

Example:

```
shutdown -r +5
```

Schedules a system restart in five minutes, allowing users to prepare before the system goes offline.

## 44. ping command

The [`ping` command](https://www.hostinger.com/in/tutorials/linux-ping-command-with-examples/) sends network packets to a target host and measures the response time.

Syntax:

```
ping [options] [hostname_or_ip]
```

Common options:\
• `-c` → specifies the number of packets to send\
• `-i` → sets the interval between packets\
• `-s` → defines the packet size

Example:

```
ping -c 15 -i 2 google.com
```

Sends 15 packets to `google.com` at two-second intervals, allowing you to test connectivity and measure network latency.

## 45. wget command

The [`wget` command](https://www.hostinger.com/in/tutorials/wget-command-examples/) downloads files from the internet using HTTP, HTTPS, or FTP protocols.

Syntax:

```
wget [options] [url]
```

Common options:\
• `-O` → saves the file with a custom name\
• `-c` → resumes a partially downloaded file\
• `-q` → runs in quiet mode without output

Example:

```
wget https://wordpress.org/latest.zip
```

Downloads the file from the specified URL to the current directory, allowing you to retrieve remote resources directly from the terminal.

## 46. cURL command

The [`curl` command](https://www.hostinger.com/in/tutorials/curl-command/) transfers data to or from a server using a specified URL.

Syntax:

```
curl [options] url
```

Common options:\
• `-O` → downloads a file and saves it with its original name\
• `-o` → saves the file with a custom name\
• `-X` → specifies the HTTP method (GET, POST, PUT, DELETE)

Example:

```
curl -X GET https://api.example.com/endpoint
```

Sends a GET request to the specified API endpoint and returns the response, allowing you to test APIs or retrieve remote data directly from the terminal.

## 47. scp command

The [`scp` command](https://www.hostinger.com/in/tutorials/linux-scp-command/) securely copies files and directories between local and remote systems over SSH.

Syntax:

```
scp [options] source destination
```

Common options:\
• `-P` → specifies a custom SSH port\
• `-r` → copies directories recursively\
• `-C` → enables compression during transfer

Example:

```
scp file1.txt root@185.185.185.185:/path/to/folder
```

Copies `file1.txt` from the local machine to the remote server at `/path/to/folder`, allowing secure file transfer between systems.

## 48. rsync command

The [`rsync` command](https://www.hostinger.com/in/tutorials/how-to-use-rsync/) synchronizes files and directories between locations while minimizing data transfer.

Syntax:

```
rsync [options] source destination
```

Common options:\
• `-a` → preserves file attributes (permissions, timestamps, symbolic links)\
• `-z` → compresses data during transfer\
• `-v` → displays detailed transfer output

Example:

```
rsync -avz /path/to/local/folder/ vps-user@185.185.185.185:/path/to/remote/folder/
```

Synchronizes the local folder with the remote directory while preserving attributes and compressing data, resulting in faster, more efficient transfers.

## 49. ip command

The `ip` command displays and manages network interfaces, addresses, and routing.

Syntax:

```
ip [options] object command
```

Common options:\
• `address` → manages and displays IP addresses\
• `link` → manages network interfaces\
• `route` → displays or modifies routing tables

Example:

```
ip address show
```

Displays all network interfaces and their assigned IP addresses, helping you inspect and troubleshoot network configuration.

## 50. netstat command

The [`netstat` command](https://www.hostinger.com/in/tutorials/netstat-command/) displays network connections, routing tables, and interface statistics.

Syntax:

```
netstat [options]
```

Common options:\
• `-a` → shows all connections, including listening sockets\
• `-t` → displays TCP connections\
• `-u` → displays UDP connections\
• `-r` → shows routing tables

Example:

```
netstat -tuln
```

Displays all listening TCP and UDP ports, helping you identify active network services and open ports.

## 51. traceroute command

The [`traceroute` command](https://www.hostinger.com/in/tutorials/traceroute-command/) tracks the path packets take to reach a destination host.

Syntax:

```
traceroute [options] destination
```

Common options:\
• `-m` → sets the maximum number of hops\
• `-n` → disables DNS resolution for faster output\
• `-w` → sets the timeout in seconds for each response

Example:

```
traceroute google.com
```

Displays each hop between your system and `google.com`, helping you identify network delays or routing issues.

## 52. nslookup command

The `nslookup` command queries [DNS](https://www.hostinger.com/in/tutorials/what-is-dns/) servers to retrieve domain or IP address information.

Syntax:

```
nslookup [options] domain_or_ip [dns_server]
```

Common options:\
• `-type=` → specifies the DNS record type (e.g., A, MX, TXT)\
• `-retry=` → sets the number of query retries\
• `-port=` → uses a specific DNS server port

Example:

```
nslookup -type=MX example.com
```

Retrieves the mail exchange (MX) records for `example.com`, helping you inspect DNS configuration and troubleshoot domain-related issues.

## 53. dig command

The [`dig` command](https://www.hostinger.com/in/tutorials/linux-dig-command/) queries DNS records and provides detailed information about a domain or IP address.

Syntax:

```
dig [options] [server] [type] name_or_ip
```

Common options:\
• `-x` → performs a reverse DNS lookup\
• `+short` → displays a concise output\
• `@server` → queries a specific DNS server

Example:

```
dig MX domain.com
```

Retrieves the mail exchange (MX) records for `domain.com`, helping you analyze DNS configuration and troubleshoot domain resolution issues.

## 54. history command

The `history` command displays a list of previously executed commands in the current shell session.

Syntax:

```
history [options]
```

Common options:\
• `-c` → clears the command history\
• `-r` → reads the history file and appends it to the current session\
• `-d` → deletes a specific entry by its ID

Example:

```
!145
```

Re-executes the command with ID `145` from the history list, allowing you to quickly repeat previously used commands.

## 55. man command

The `man` command displays the manual page for a specified command.

Syntax:

```
man [options] [section_number] command_name
```

Common options:\
• `-k` → searches manuals for keywords\
• `-f` → displays a short description of a command\
• `-a` → shows all available manual pages for a command

Example:

```
man 3 ls
```

Displays the section 3 manual page for `ls`, allowing you to access detailed documentation for specific command categories.

## 56. echo command

The `echo` command outputs text or variables to the terminal or a file.

Syntax:

```
echo [options] [text]
```

Common options:\
• `-n` → removes the trailing newline from output\
• `-e` → enables interpretation of escape sequences (e.g., `n`, `t`)

Example:

```
echo "Hello World" > file.txt
```

Writes `Hello World` to `file.txt`, allowing you to create or overwrite files with custom text output.

## 57. ln command

The `ln` command creates links between files, including symbolic (soft) and hard links.

Syntax:

```
ln [options] source target
```

Common options:\
• `-s` → creates a symbolic (soft) link\
• `-f` → forces creation by overwriting existing files\
• `-v` → displays detailed output of the operation

Example:

```
ln -s target.txt shortcut.txt
```

Creates a symbolic link named `shortcut.txt` that points to `target.txt`, allowing you to access the file using an alternative path.

## 58. alias and unalias commands

The [`alias` command](https://www.hostinger.com/in/tutorials/linux-alias-command/) creates a shortcut for a command, while the `unalias` command removes an existing alias.

Syntax:

```
alias name='command'
unalias name
```

Common options:\
• *(no commonly used options required for basic usage)*

Example:

```
alias k='kill'
```

Creates an alias `k` for the `kill` command, allowing you to run `kill` using a shorter keyword.

## 59. cal command

The `cal` command displays a calendar for a specified month or year.

Syntax:

```
cal [options] [month] 2026
```

Common options:\
• `-3` → displays the previous, current, and next month\
• `-y` → shows the entire year\
• `-m` → displays Monday as the first day of the week

Example:

```
cal -3
```

Displays the previous, current, and next month, allowing you to view nearby dates at a glance.

## 60. apt and dnf command

The `apt` command manages packages on Debian-based systems, while the `dnf` command manages packages on Red Hat-based systems.

Syntax:

```
apt [options] subcommand
dnf [options] subcommand
```

Common options:\
• `install` → installs a package\
• `remove` → removes a package\
• `update` → updates package lists\
• `upgrade` → upgrades installed packages

Example:

```
sudo apt install vim
```

Installs the `vim` text editor using the APT package manager, allowing you to add new software to the system.

## Common errors when running Linux commands (and how to fix them)

When running Linux commands, errors often occur due to incorrect syntax, missing permissions, or invalid file paths. Understanding these common issues helps you quickly identify the cause and apply the correct fix without interrupting your workflow.

### “command not found”

This error means the shell cannot locate the command you entered. It usually occurs for one of three reasons:

- The package is not installed. Install it using your package manager (for example, `sudo apt install <package>` on Debian/Ubuntu or `sudo dnf install <package>` on RHEL-based systems).
- The command is not in your PATH. Check its location with `which <command>`. If it exists outside your PATH, add its directory:\
  `export PATH=$PATH:/path/to/dir`
- The command contains a typo. Linux is case-sensitive, so `LS` and `ls` are treated as different commands. Verify spelling and capitalization.

### “Permission denied”

This error indicates that your user account lacks the required permissions to run a command or access a file.

- Run the command with elevated privileges:\
  `sudo <command>`
- Modify file permissions if needed:\
  `chmod +x file.sh` → makes a script executable\
  `chmod 644 file.txt` → sets read/write for owner and read-only for others
- If ownership is the issue, update it:\
  `chown <user>:<group> <file>`

### “No such file or directory”

This error means the specified file or path does not exist from your current location.

- Check your current directory:\
  `pwd`
- List available files:\
  `ls`
- Verify the path and filename for typos. Linux uses forward slashes (`/`) and is case-sensitive, so even small differences will break the command.

### Command runs but does nothing visible

Some Linux commands do not produce output when they succeed. This behavior is intentional.

- Commands like `touch`, `cp`, or `mv` return silently if successful
- Verify the result manually using:\
  `ls`, `cat`, or similar commands
- To see detailed output, use verbose flags where available:\
  `cp -v`, `rm -v`

## What should you learn next after mastering Linux commands?

Mastering Linux commands enables you to efficiently manage a remote [virtual private server platform](https://www.hostinger.com/in/vps-hosting) from the terminal. While these utilities are sufficient by themselves, learning [how to write Bash scripts](https://www.hostinger.com/in/tutorials/bash-scripting-tutorial/) will further improve your workflow, given the benefits:

- **Automation and efficiency**. A Bash script combines multiple commands into a single executable file, allowing you to automate multi-step tasks using a single execution.
- **Consistency and reduced human error.** Commands in a Bash script always run and behave consistently across executions, which significantly reduces human error.
- **Reusability**. Developers can easily copy and transport Bash scripts to different UNIX operating systems, making it easy to replicate tasks in other environments.

Given its importance, learning how to create a Bash script is the natural next step for aspiring system administrators after mastering various Linux commands.

**All of the tutorial content on this website is subject to [Hostinger's rigorous editorial standards and values.](https://www.hostinger.com/tutorials/editorial-standards-and-values)**

![Author](https://secure.gravatar.com/avatar/26f8a510b4fd4b5697699e6663e7f698f1881d65a8f6de774a4f6cb76a9965e5?s=96&d=mm&r=g) The author

Aris Sentika

[![Add as Google Prefered Source](https://www.hostinger.com/in/tutorials/wp-content/themes/hostinger/public/images/google-prefered-source/google_preferred_source_badge_dark_en.png)](https://www.google.com/preferences/source?q=hostinger.com)

Aris is a Content Writer specializing in Linux and WordPress development. He has a passion for networking, front-end web development, and server administration. By combining his IT and writing experience, Aris creates content that helps people easily understand complex technical topics to start their online journey. Follow him on [LinkedIn](https://www.linkedin.com/in/aris-sentika).

[More from Aris Sentika](https://www.hostinger.com/in/tutorials/author/aris/)

Hosting[Web hosting](https://www.hostinger.com/in/web-hosting) [Hosting for WordPress](https://www.hostinger.com/in/wordpress-hosting) [VPS hosting](https://www.hostinger.com/in/vps-hosting) [Self-hosted n8n](https://www.hostinger.com/in/self-hosted-n8n) [Business email](https://www.hostinger.com/in/business-email) [Cloud hosting](https://www.hostinger.com/in/cloud-hosting) [Hosting for WooCommerce](https://www.hostinger.com/in/woocommerce-hosting) [Hosting for agencies](https://www.hostinger.com/in/pro) [Minecraft hosting](https://www.hostinger.com/in/vps/minecraft-hosting) [Hermes Agent VPS](https://www.hostinger.com/in/applications/hermes-agent) [OpenClaw](https://www.hostinger.com/in/ai-automation-apps) [Paperclip VPS](https://www.hostinger.com/in/applications/paperclip) [Google Workspace](https://www.hostinger.com/in/google-workspace) [Cheap Web Hosting](https://www.hostinger.com/in/cheap-web-hosting)

Domain[Domains](https://www.hostinger.com/in/domain-name-search) [Buy a domain](https://www.hostinger.com/in/domains) [Cheap domains](https://www.hostinger.com/in/cheap-domain) [Free Domain Name](https://www.hostinger.com/in/free-domain) [WHOIS Lookup](https://www.hostinger.com/in/whois) [Free SSL certificate](https://www.hostinger.com/in/free-ssl-certificate) [Domain transfer](https://www.hostinger.com/in/domain-transfer) [Domain Extensions](https://www.hostinger.com/in/tld) [.fr domain](https://www.hostinger.com/in/tld/fr-domain) [Personal domain name](https://www.hostinger.com/in/personal-domain-name) [Premium domains](https://www.hostinger.com/in/premium-domains)

Tools[AI Builder](https://www.hostinger.com/in/ai-builder) [Website Builder](https://www.hostinger.com/in/website-builder) [AI Website Builder](https://www.hostinger.com/in/ai-website-builder) [Ecommerce Website Builder](https://www.hostinger.com/in/ecommerce-website) [Templates](https://www.hostinger.com/in/templates) [Domain Name Generator](https://www.hostinger.com/in/domain-name-generator) [Print on Demand](https://www.hostinger.com/in/print-on-demand) [Link in bio](https://www.hostinger.com/in/link-in-bio) [Business Name Generator](https://www.hostinger.com/in/business-name-generator) [AI Newsletter Generator](https://www.hostinger.com/in/ai-email-generator) [AI Logo Generator](https://www.hostinger.com/in/logo-maker) [Migrate to Hostinger](https://www.hostinger.com/in/website-migration) [Hostinger API](https://developers.hostinger.com/)

Information[Pricing](https://www.hostinger.com/in/pricing) [Hostinger Reviews](https://www.hostinger.com/in/reviews) [Affiliate program](https://www.hostinger.com/in/affiliates) [Educational partnership](https://www.hostinger.com/in/educational-partnership) [Referral program](https://www.hostinger.com/in/referral-program) [Agency directory](https://www.hostinger.com/in/agency-directory) [Roadmap](https://roadmap.hostinger.com/) [Terms of migration](https://www.hostinger.com/) [System status](https://statuspage.hostinger.com/) [Trust center](https://trust.hostinger.com/) [Sitemap](https://www.hostinger.com/in/sitemap) [EntityMap](https://www.hostinger.com/entitymap.html)

Company[About Hostinger](https://www.hostinger.com/in/about) [Our technology](https://www.hostinger.com/in/technology) [Career](https://www.hostinger.com/career) [Blog](https://www.hostinger.com/blog/) [Student discount](https://www.hostinger.com/in/student-discount) [Sustainability](https://www.hostinger.com/sustainability) [Hostinger Group International](https://hgis-group.lu/)

Support[Tutorials](https://www.hostinger.com/in/tutorials/) [Knowledge Base](https://www.hostinger.com/support) [Hostinger Academy](https://www.youtube.com/HostingerIndia) [Contact us](https://www.hostinger.com/in/contacts) [Report Online Abuse](https://www.hostinger.com/in/report-abuse)

[linkedin](https://www.linkedin.com/company/hostinger)[facebook](https://www.facebook.com/Hostinger)[instagram](https://www.instagram.com/hostinger_global)[twitter](https://x.com/Hostinger)[youtube](https://www.youtube.com/@Hostinger)[reddit](https://www.reddit.com/r/Hostinger/)[tiktok](https://www.tiktok.com/@hostingeracademy)[discord](https://discord.gg/Zp2FteMUea)

[NPRD request policy](https://www.hostinger.com/in/legal/non-public-registrant-data-request-policy) [Privacy policy](https://www.hostinger.com/in/legal/privacy-policy) [Refund policy](https://www.hostinger.com/in/legal/refund-policy) [Terms of service](https://www.hostinger.com/in/legal/universal-terms-of-service-agreement) [Registrar information](https://www.hostinger.com/in/legal/registrar-information)

![visa](https://www.hostinger.com/cdn-cgi/imagedelivery/LqiWLm-3MGbYHtFuUbcBtA/eea0da37-b667-4d93-3e73-ce63b3b81400/w=1280,sharpen=1)![mastercard](https://www.hostinger.com/cdn-cgi/imagedelivery/LqiWLm-3MGbYHtFuUbcBtA/8c07a3ee-6954-4b35-f511-ae9011dbfd00/w=1280,sharpen=1)![discover](https://www.hostinger.com/cdn-cgi/imagedelivery/LqiWLm-3MGbYHtFuUbcBtA/49823ad9-8a1e-43f7-8d84-0de15a627700/w=1280,sharpen=1)![dinersclub](https://www.hostinger.com/cdn-cgi/imagedelivery/LqiWLm-3MGbYHtFuUbcBtA/eaeabe9a-6e9d-4f74-4411-be32b5a81700/w=1280,sharpen=1)![rupay](https://www.hostinger.com/cdn-cgi/imagedelivery/LqiWLm-3MGbYHtFuUbcBtA/0dad6858-9c10-40d1-7258-0b606f111e00/w=1280,sharpen=1)[and more](https://www.hostinger.com/in/payment-methods)

© 2004-2026 Hostinger - Premium Web Hosting, Cloud, VPS, AI Website Builder & Domain Registration Services.

Prices are listed without GST