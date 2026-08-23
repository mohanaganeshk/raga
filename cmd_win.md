[![geeksforgeeks](https://media.geeksforgeeks.org/gfg-gg-logo.svg)](https://www.geeksforgeeks.org/)

![search icon](https://media.geeksforgeeks.org/auth-dashboard-uploads/Property=Light---Default.svg)

- Courses

- Tutorials

- Interview Prep


Switch to Dark Mode

Sign In

- [DSA](https://www.geeksforgeeks.org/dsa/dsa-tutorial-learn-data-structures-and-algorithms/)
- [Practice Problems](https://www.geeksforgeeks.org/explore)
- [C](https://www.geeksforgeeks.org/c/c-programming-language/)
- [C++](https://www.geeksforgeeks.org/cpp/c-plus-plus/)
- [Java](https://www.geeksforgeeks.org/java/java/)
- [Python](https://www.geeksforgeeks.org/python/python-programming-language-tutorial/)
- [JavaScript](https://www.geeksforgeeks.org/javascript/javascript-tutorial/)
- [Data Science](https://www.geeksforgeeks.org/data-science/data-science-for-beginners/)
- [Machine Learning](https://www.geeksforgeeks.org/machine-learning/machine-learning/)
- [Courses](https://www.geeksforgeeks.org/courses)
- [Linux](https://www.geeksforgeeks.org/linux-unix/linux-tutorial/)
- [DevOps](https://www.geeksforgeeks.org/devops/devops-tutorial/)
- [SQL](https://www.geeksforgeeks.org/sql/sql-tutorial/)
- [Web Development](https://www.geeksforgeeks.org/web-tech/web-technology/)

reCAPTCHA

Recaptcha requires verification.

protected by **reCAPTCHA**

# Essential CMD Commands for Windows Users

Last Updated : 12 Jan, 2026

The Windows Command Prompt (CMD) is a powerful tool that allows users to interact with their operating system through text-based commands.

## 1\. CMD Commands for Beginners

These commands are essential for users who are new to CMD and provide basic functionalities to help them navigate and perform simple tasks.

### **1\. View Directory '** **`dir`** **'**

- **Function**: Displays the contents of the current directory.
- **How to use**: Type **`dir`** and press Enter. Use **`dir /s`** to include subdirectories.
- **Use case**: Quickly view files and folders in your current location.

```
Syntax: dir
```

![dir](https://media.geeksforgeeks.org/wp-content/uploads/20250716114732776920/dir.webp)

### 2\. Change Directories 'cd'

- **Function**: Let's you navigate between folders.
- **How to use**: Type **`cd [folder_name]`** to move into a directory. Used `cd ..` to go up one level.
- **Use case**: Navigate to specific directories to manage files or execute commands

```
Syntax: cd [folder name]
```

![cd](https://media.geeksforgeeks.org/wp-content/uploads/20250716114917287785/cd.webp)

### 3\. Create a New Directory 'mkdir' or 'md'

- **Function**: Allows you to create a new directory
- **How to use**: Type **mkdir \[file\_name\]**\- Here the new directory name is GFG
- **Use case**: When you need a new directory for any separate work, you may create a new directory

```
Syntax: mkdir [GFG]
```

![mkdir](https://media.geeksforgeeks.org/wp-content/uploads/20250716115316718195/mkdir.webp)

### 4. Rename a File 'ren'

- **Function**: Helps in renaming any file or directory.
- **How to use**: Type **`ren`**`or` **`rename [old_name] [new_name]`** and press **Enter**.
- **Use case**: Discover new method of renaming file or any directory.

```
Syntax: ren xyz.txt newxyz.txt
```

![ren](https://media.geeksforgeeks.org/wp-content/uploads/20250716120008973626/ren.webp)

### 5\. Delete a File 'del'

- **Function**: Lets you to remove one or more files
- **How to use**: Type **del \[file\_name\]**\- This will erase the provided file name
- **Use case**: This function allows you to erase any file if you're unable to fetch

```
Syntax: del[file_name]
```

![del](https://media.geeksforgeeks.org/wp-content/uploads/20250716120326505338/del.webp)

### 6\. Close 'exit'

- **Function**: Closes the Command Prompt window.
- **How to use**: Type **`exit`** and press **Enter**.
- **Use case**: Ends your session with CMD.

```
Syntax: exit
```

![exit](https://media.geeksforgeeks.org/wp-content/uploads/20250716120418486381/exit.webp)

### 7\. Clear Screen 'cls'

- **Function**: Clears all text from the CMD window.
- **How to use**: Type **`cls`** and press **Enter**.
- **Use case**: Removes clutter after multiple commands

```
Syntax: cls
```

![cls](https://media.geeksforgeeks.org/wp-content/uploads/20250716120510380294/cls.webp)

### 8. View Available Command 'help'

- **Function**: Lists all available commands and their descriptions.
- **How to use**: Type **`help`** and press **Enter**.
- **Use case**: Discover new commands and learn their functions.

```
Syntax: help
```

![help](https://media.geeksforgeeks.org/wp-content/uploads/20250716120656298624/help.webp)time

### 9. Display or Set the System time 'time'

- **Function**: Lets you set the system time or display the current time.
- **How to use**: Type **`t`** **ime \[new\_time\]** and press **Enter**.
- **Use case**: Allows the user to set their system's time without additional navigation

```
Syntax: time [new_time]
```

![time](https://media.geeksforgeeks.org/wp-content/uploads/20250716121030009190/time.webp)

### 10. Copy Files 'copy'

- **Function**: Lists all available commands and their descriptions.
- **How to use**: Type **`c`** **opy \[source1\] \[destination2\]** and press **Enter**.
- **Use case**: Discover new commands and learn their functions.

```
Syntax: copy file.txt Backup\
```

![copy](https://media.geeksforgeeks.org/wp-content/uploads/20250716121228082165/copy.webp)

| **Command** | **Description** | **Syntax** | **Example** |
| --- | --- | --- | --- |
| `dir` | View the contents of a directory | `dir` | `dir C:\Users\Documents` |
| `cd` | Change the current working directory | `cd [directory_name]` | `cd Downloads` |
| `mkdir` | Create a new directory | `mkdir [directory_name]` | `mkdir NewProject` |
| `ren` | Rename a file | `ren [old_name] [new_name]` | `ren draft.txt final.txt` |
| `del` | Delete a file | `del [file_name]` | `del unwanted.txt` |
| `exit` | Close the Command Prompt | `exit` | `exit` |
| `cls` | Clear the Command Prompt screen | `cls` | `cls` |
| `help` | View available CMD commands and their descriptions | `help` | `help` |
| `time` | Display or set the system time | `time` | `time 14:30:00` |
| `copy` | Copy files from one location to another | `copy [source] [destination]` | `copy report.docx D:\Backup\` |

## 2\. CMD Commands for Experts

These commands are more advanced and suitable for users comfortable with troubleshooting and system management tasks.

### 1\. System File Checker 'sfc'

- **Function**: Scans and repairs corrupted system files.
- **How to use**: Type **`sfc /scannow`** in CMD (run as administrator).
- **Use case**: Fix system errors related to missing or corrupted files.

```
Syntax: sfc /scannow
```

![sfs](https://media.geeksforgeeks.org/wp-content/uploads/20250716122435580404/sfs.webp)

### 2\. Disk Error 'chkdsk'

- **Function**: Scans the hard drive for bad sectors and file system errors.
- **How to use**: Type **`chkdsk [drive letter]`**`: /f` (e.g., `chkdsk C: /f`) in CMD.
- **Use case**: Identify and fix disk issues.

```
Syntax: chkdsk C: /f
```

![chkdsk](https://media.geeksforgeeks.org/wp-content/uploads/20250716122305773316/chkdsk.webp)

### 3\. View Running Processor 'tasklist'

- **Function**: Displays all running processes and their details.
- **How to use**: Type **`tasklist`** to list processes. Use `tasklist /fi "imagename eq [process name]"` to filter.
- **Use case**: Identify resource-heavy or unresponsive processes.

```
Syntax: tasklist /fi "imagename eq [process name]
```

![task](https://media.geeksforgeeks.org/wp-content/uploads/20250716121937381983/task.webp)

### 4\. Restart 'shutdown'

- **Function**: Allows you to shut down or restart the computer via CMD.
- **How to use**:
  - Shutdown: `shutdown /s /f /t [seconds]`.
  - Restart: `shutdown /r /f /t [seconds]`.
- **Use case**: Automate shutdown or restart tasks

```
Syntax:
Shutdown: shutdown /s /f /t [seconds].
Restart: shutdown /r /f /t [seconds].
```

![shutdown](https://media.geeksforgeeks.org/wp-content/uploads/20250716123616473527/shutdown.webp)

### 5\. Network Statistics 'netstat'

- **Function**: Displays active connections and listening ports.
- **How to use**: Type **`netstat`** to view all active connections.
- **Use case**: Diagnose network-related issues or monitor network activity.

```
Syntax: netstat
```

![netstat](https://media.geeksforgeeks.org/wp-content/uploads/20250716122839372447/netstat.webp)

### 6\. Kill a Running Process 'taskkill'

- **Function**: Lets you terminate a process using its process ID (PID)
- **How to use**: Type **`t`** **askkill /\[PID\] /F** to terminate
- **Use case**: Can be helpful for terminating any dedicated PID.

Example (PID: 1124)

```
Syntax: taskkill /PID 11234 /F
```

![taskkill](https://media.geeksforgeeks.org/wp-content/uploads/20250716123133133007/taskkill.webp)

### 7\. View Saved Passwords 'netsh wlan show profiles'

- **Function**: Retrieve the password of a saved Wi-Fi network.
- **How to use**: Type **netsh wlan show profile name="WiFi-Name" key=clear**
- **Use case**: Discover new commands and learn their functions.

```
Example: netsh wlan show profile name="MyHomeWiFi" key=clear
```

![wifi](https://media.geeksforgeeks.org/wp-content/uploads/20250716123500345116/wifi.webp)

| **Command** | **Description** | **Syntax** | **Example** |
| --- | --- | --- | --- |
| `sfc` | System File Checker - Scans and repairs system files | `sfc /scannow` | `sfc /scannow` |
| `chkdsk` | Check Disk - Scans and fixes disk errors | `chkdsk [drive]: /f /r` | `chkdsk C: /f /r` |
| `tasklist` | View running processes | `tasklist` | `tasklist` |
| `shutdown` | Shutdown or restart the system | `shutdown /r /t [seconds]` | `shutdown /r /t 10` _(Restart in 10 seconds)_ |
| `netstat` | View network statistics and active connections | `netstat -a` | `netstat -an` _(Show all connections numerically)_ |
| `taskkill` | Kill a running process using its process ID (PID) | `taskkill /PID [PID] /F` | `taskkill /PID 4567 /F` _(Kill process with ID 4567)_ |
| `netsh wlan show profiles` | View saved Wi-Fi network names | `netsh wlan show profiles` | `netsh wlan show profiles` |

## 3\. CMD Commands for Utility

These commands are focused on specific tasks and utilities to enhance productivity and system performance.

### 1\. Network Configuration 'ipconfig'

- **Function**: Displays IP address, subnet mask, and gateway information.
- **How to use**:
  - Basic: Type **`ipconfig`**.
  - Detailed: Type `ipconfig /all`.
- **Use case**: Troubleshoot internet connectivity issues.

```
Syntax: ipconfig
```

![ip](https://media.geeksforgeeks.org/wp-content/uploads/20250716123838592426/ip.webp)

### 2\. Network Connectivity 'ping'

- **Function**: Sends packets to test communication with another device or website.
- **How to use**: Type **`ping`**`[destination]`
- **Use case**: Check if a device or website is reachable.

```
Syntax: ping geeksforgeeks.org
```

![ping](https://media.geeksforgeeks.org/wp-content/uploads/20250716124031706651/ping.webp)

### 3\. System Information 'systeminfo'

- **Function**: Displays detailed information about your computer.
- **How to use**: Type **`systeminfo`**.
- **Use case**: Quickly access system specifications for troubleshooting or reporting.

```
Syntax: systeminfo
```

![1](https://media.geeksforgeeks.org/wp-content/uploads/20250716124201283937/1.webp)

### 4\. Trace Route 'tracert'

- **Function**: Shows the path packets take to reach a specific destination.
- **How to use**: Type **`tracert`**`[destination]`
- **Use case**: Identify network bottlenecks or connectivity issues.

```
Syntax: tracert geeksforgeeks.org
```

![2](https://media.geeksforgeeks.org/wp-content/uploads/20250716124344068763/2.webp)

### 5\. Manage Drives 'diskpart'

- **Function**: Opens a command-line utility for managing disk partitions.
- **How to use**: Type **`diskpart`** to enter the disk management interface.
- **Use case**: Create, delete, or modify partitions on your drives.

```
Syntax: diskpart
```

![3](https://media.geeksforgeeks.org/wp-content/uploads/20250716124457613107/3.webp)

### 6. Delete a Directory 'rmdir'

- **Function**: Removes directory from the origin
- **How to use**: Type **rmdir \[directory\_name\]** and press **Enter**.
- **Use case**: Discover new commands and learn their functions.

**Example:** GFG - Directory name

```
Syntax: rmdir GFG
```

![4](https://media.geeksforgeeks.org/wp-content/uploads/20250716124713252940/4.webp)

### 7. View 'rmdir'

- **Function**: Removes directory from the origin
- **How to use**: Type **rmdir \[directory\_name\]** and press **Enter**.
- **Use case**: Discover new commands and learn their functions.

```
Example: GFG - Directory name
```

### 8. Manage User Account 'net user'

- **Function**: To list all the user accounts
- **How to use**: Type **net user** and press **Enter**.
- **Use case**: Discover new commands and learn their functions.

```
Syntax: net user username password /add
```

![5](https://media.geeksforgeeks.org/wp-content/uploads/20250716125122413174/5.webp)

### 9. View Startup Programs 'wmic startup get caption,command'

- **Function**: To check what programs launch on startup.
- **How to use**: Type **wmic startup get caption,command,** and press **Enter**.
- **Use case**: Discover new commands and learn their functions.

```
Syntax: wmic startup get caption,command
```

![6](https://media.geeksforgeeks.org/wp-content/uploads/20250716125419720027/6.webp)

| **Command** | **Description** | **Syntax** | **Example** |
| --- | --- | --- | --- |
| `ipconfig` | View network configuration, including IP address, subnet mask, and gateway | `ipconfig` | `ipconfig /all` _(Displays detailed network info)_ |
| `ping` | Test network connectivity by sending packets to a host | `ping [host or IP]` | `ping google.com` _(Check connection to Google)_ |
| `systeminfo` | Display detailed system information, including OS version, installed memory, and processor | `systeminfo` | `systeminfo` |
| `tracert` | Trace the route packets take to a network destination | `tracert [hostname or IP]` | `tracert google.com` _(View network path to Google)_ |
| `diskpart` | Manage disk partitions, including creating, formatting, and deleting partitions | `diskpart` | `diskpart → list disk → select disk 1 → create partition primary` |
| `rmdir` | Delete a directory (folder) | `rmdir [directory_name]` | `rmdir /s /q OldFolder` _(Delete a folder and its contents without confirmation)_ |
| `dir` | View contents of a directory | `dir` | `dir C:\Users\Documents` _(List files in a specific directory)_ |
| `net user` | Manage user accounts, including adding, modifying, or deleting users | `net user` | `net user John password123 /add` _(Create a new user account)_ |
| `wmic startup get caption,command` | View startup programs and their commands | `wmic startup get caption,command` | `wmic startup get caption,command` |

## 4\. CMD Commands for Troubleshooting

### 1\. File Comparison 'fc'

- **Function**: Compares two files and highlights differences.
- **How to use**: Type **`fc [file1] [file2]`** to compare files.
- **Use case**: Detect changes or errors in files

```
Syntax: fc 1 2
```

![13](https://media.geeksforgeeks.org/wp-content/uploads/20250716130958867409/13.webp)

### 2\. **Advanced Network Diagnostics** 'pathping'

- **Function**: Combines `ping` and `tracert` functionalities to provide detailed network path diagnostics.
- **How to use**: Type **`pathping`**`[destination]`
- **Use case**: Troubleshoot complex network issues.

```
Syntax: pathping geeksforgeeks.org
```

![14](https://media.geeksforgeeks.org/wp-content/uploads/20250716131125878693/14.webp)

### 3\. Registry Editor 'regedit'

- **Function**: Launches the Windows Registry Editor.
- **How to use**: Type **`regedit`** to open the registry.
- **Use case**: Modify registry keys for advanced configuration or troubleshooting.

```
Syntax: regedit
```

![15](https://media.geeksforgeeks.org/wp-content/uploads/20250716131236570855/15.webp)

### 4\. View MAC 'getmac'

- **Function**: Displays the MAC address of your network adapter.
- **How to use**: Type **`getmac`** to view the MAC address.
- **Use case**: Identify your device's hardware address for network configurations

```
Syntax: getmac
```

![16](https://media.geeksforgeeks.org/wp-content/uploads/20250716131337303992/16.webp)

### 5\. Power Configuration 'powercfg'

- **Function**: Displays and manages power settings.
- **How to use**: Type **`powercfg`**`/[option]`
- **Use case**: Optimize power usage and troubleshoot battery issues.

```
Syntax: powercfg /energy for a detailed power usage report
```

![17](https://media.geeksforgeeks.org/wp-content/uploads/20250716142253245682/17.webp)

### 6\. Enable Boot Manager 'bcdedit'

- **Function**: Used to modify boot configuration settings
- **How to use**: Type **`bcdedit`**`/ set current`
- **Use case**: Discover new commands and learn their functions.

```
Syntax: bcdedit /set {current} bootmenupolicy standard
```

![19](https://media.geeksforgeeks.org/wp-content/uploads/20250716142815078968/19.webp)

### 7. Format a Drive 'format'

- **Function**: To erase any specific drive.
- **How to use**: Type **format \[drive\]: /FS:NTFS** and press **Enter**.
- **Use case**: Discover new commands and learn their functions.

```
Syntax: format D: /FS:NTFS
```

![18](https://media.geeksforgeeks.org/wp-content/uploads/20250716142618242190/18.webp)

| **Command** | **Description** | **Syntax** | **Example** |
| --- | --- | --- | --- |
| `fc` | Compare two files and highlight differences | `fc [file1] [file2]` | `fc file1.txt file2.txt` _(Compare two text files)_ |
| `pathping` | Perform advanced network diagnostics with packet loss details | `pathping [destination]` | `pathping google.com` _(Analyze network route to Google)_ |
| `regedit` | Open the Windows Registry Editor (GUI) | `regedit` | `regedit` _(Opens the registry editor – use with caution!)_ |
| `getmac` | Display the MAC (Media Access Control) address of your network adapters | `getmac` | `getmac /v /fo list` _(View MAC addresses in detailed format)_ |
| `powercfg` | Manage and analyze power configurations | `powercfg /[option]` | `powercfg /batteryreport` _(Generate a battery usage report)_ |
| `bcdedit` | Enable, disable, or modify Windows Boot Configuration | `bcdedit /set {current} [option]` | `bcdedit /set {current} bootmenupolicy standard` _(Enable boot menu in Windows 10/11)_ |
| `format` | Format a drive (erase all data) | `format [drive]: /FS:[filesystem]` | `format D: /FS:NTFS` _(Format drive D: with NTFS file system)_ |

## 5\. CMD Commands for Students

Students can use these commands to manage files, perform simple calculations, and even help with tasks like coding and studying.

### 1\. Calculator 'calc'

- **Function**: Opens the Windows Calculator application.
- **How to use**: Type **`calc`** and press Enter.
- **Use case**: Quickly open the calculator for

```
Syntax: calc
```

![7](https://media.geeksforgeeks.org/wp-content/uploads/20250716125701945431/7.webp)

## 6\. CMD Commands for Programmers

Programmers often use CMD to automate tasks, compile code, and test network functionality. These commands can be especially useful for developers working in command-line environments.

### 1\. Compile Java Code 'javac'

- **Function**: Compiles Java source files into bytecode.
- **How to use**: Type `javac [file name].java` to compile Java code.
- **Use case**: Compile and test Java programs directly from the command line.

```
Syntax: javac
```

![8](https://media.geeksforgeeks.org/wp-content/uploads/20250716125810718050/8.webp)

### 2\. Version Control 'git'

- **Function**: Interacts with Git repositories from the command line.
- **How to use**: Type `git [command]`
- **Use case**: Manage version control, clone repositories, or push commits from the command line.

```
Syntax: git clone [repository URL]
```

![9](https://media.geeksforgeeks.org/wp-content/uploads/20250716125916140363/9.webp)

### 3\. Execute Python Script 'python'

- **Function**: Runs Python scripts in the command prompt.
- **How to use**: Type `python [script.py]` to execute a Python program.
- **Use case**: Test and run Python code directly in the command line.

```
Syntax: python [script.py]
```

![10](https://media.geeksforgeeks.org/wp-content/uploads/20250716130041826122/10.webp)

### 4\. Run Node.js Scripts 'node'

- **Function**: Executes Node.js scripts.
- **How to use**: Type `node [script.js]` to run a JavaScript file using Node.js.
- **Use case**: Run backend scripts and test JavaScript programs in the command line.

```
Syntax: node [script.js]
```

![11](https://media.geeksforgeeks.org/wp-content/uploads/20250716130205958320/11.webp)

### 5\. Node Package Manager 'npm'

- **Function**: Installs and manages JavaScript packages.
- **How to use**: Type `npm install [package]` to install a package.
- **Use case**: Manage dependencies and libraries in Node.js applications.

```
Syntax: npm install [package]
```

![12](https://media.geeksforgeeks.org/wp-content/uploads/20250716130340954002/12.webp)

| **Command** | **Description** | **Syntax** | **Example** |
| --- | --- | --- | --- |
| `javac` | Compile Java source code into bytecode (.class files) | `javac [filename].java` | `javac HelloWorld.java` _(Compile a Java file)_ |
| `git` | Version control system for tracking changes in files | `git [command]` | `git clone https://github.com/user/repo` _(Clone a repository)_ |
| `python` | Execute a Python script or enter interactive mode | `python [script.py]` | `python script.py` _(Run a Python script)_ |
| `node` | Execute JavaScript code using Node.js | `node [script.js]` | `node app.js` _(Run a Node.js script)_ |
| `npm` | Manage Node.js packages and dependencies | `npm [command]` | `npm install express` _(Install the Express.js package)_ |

## **7\. Bonus: CMD Tricks and Tips**

To make CMD usage even more efficient, here are some bonus tips:

### **1\. Save CMD Output to a File**

Use the **`>`** **operator** to save the output of a command to a text file.

### **2\. Open CMD in a Specific Directory**

Instead of navigating manually, you can directly open CMD in a folder by typing `cmd` in the File Explorer's address bar.

### **3\. Use** **`&&`** **for Multiple Commands**

You can run multiple commands sequentially:

```
ipconfig && ping google.com
```

![20](https://media.geeksforgeeks.org/wp-content/uploads/20250716143045708703/20.webp)

Comment

[![https://media.geeksforgeeks.org/auth/avatar.png](https://media.geeksforgeeks.org/auth/avatar.png)](https://www.geeksforgeeks.org/user/patelajeet/)

GeeksforGeeks

44

### Explore

How To

- [How to Recover Deleted Photos from WhatsApp3 min read](https://www.geeksforgeeks.org/websites-apps/recover-whatsapp-photo/)
- [How to Delete a Discord Server2 min read](https://www.geeksforgeeks.org/websites-apps/how-to-delete-discord-servers-step-by-step-guide/)
- [How to Fix “This Copy of Windows is Not Genuine” Error3 min read](https://www.geeksforgeeks.org/techtips/how-to-fix-this-copy-of-windows-is-not-genuine-error/)
- [How to Delete Discord Account1 min read](https://www.geeksforgeeks.org/websites-apps/how-to-delete-discord-account-a-complete-guide/)
- [Flowchart in Google Docs2 min read](https://www.geeksforgeeks.org/google-docs/flowchart-in-google-docs/)
- [How to Password Protect a Google Drive Folder: Comprehensive Guide7 min read](https://www.geeksforgeeks.org/websites-apps/how-to-password-protect-a-google-drive-folder-comprehensive-guide/)
- [How to Deploy a Replica Set in MongoDB4 min read](https://www.geeksforgeeks.org/mongodb/how-to-deploy-a-replica-set-in-mongodb/)

MAC

- [How to Find Your Mac Address3 min read](https://www.geeksforgeeks.org/computer-networks/how-to-find-your-mac-address/)
- [MAC Filtering in Computer Network3 min read](https://www.geeksforgeeks.org/computer-networks/mac-filtering-in-computer-network/)
- [How to validate MAC address using Regular Expression6 min read](https://www.geeksforgeeks.org/dsa/how-to-validate-mac-address-using-regular-expression/)
- [How to get the MAC Address in Kali Linux4 min read](https://www.geeksforgeeks.org/linux-unix/how-to-get-the-mac-address-10-different-methods-kali-linux/)
- [Extracting MAC address using Python3 min read](https://www.geeksforgeeks.org/python/extracting-mac-address-using-python/)

AI Tools

- [AI Tools List: 50+ Top Picks5 min read](https://www.geeksforgeeks.org/websites-apps/ai-tools-directory/)
- [10 Best AI Tools to Boost Productivity in 202514 min read](https://www.geeksforgeeks.org/blogs/10-best-ai-tools-to-boost-productivity/)
- [AI Testing Tools for Test Automation7 min read](https://www.geeksforgeeks.org/websites-apps/top-ai-testing-tools-for-test-automation/)
- [Top 20 Applications of Artificial Intelligence (AI) in 202513 min read](https://www.geeksforgeeks.org/blogs/applications-of-ai/)

Shortcut Key

- [Windows Keyboard Shortcuts A to Z with PDF (All Windows Versions)11 min read](https://www.geeksforgeeks.org/blogs/windows-keyboard-shortcuts-a-to-z-pdf/)
- [Mac Keyboard Shortcuts for All Mac Users (2025 Updated)9 min read](https://www.geeksforgeeks.org/blogs/10-mac-os-keyboard-shortcuts-that-you-should-know/)
- [Top 20 Excel Shortcuts That You Need To Know3 min read](https://www.geeksforgeeks.org/excel/top-20-excel-shortcuts-that-you-need-to-know/)
- [Microsoft Word Shortcut Keys7 min read](https://www.geeksforgeeks.org/ms-word/microsoft-word-shortcut-keys-command-list/)
- [Microsoft Office Keyboard Shortcuts5 min read](https://www.geeksforgeeks.org/websites-apps/microsoft-office-keyboard-shortcuts/)
- [General Keyboard Shortcuts For Visual Studio Code3 min read](https://www.geeksforgeeks.org/techtips/general-keyboard-shortcuts-for-visual-studio-code/)

Courses

- [Placement 360 Course2 min read](https://www.geeksforgeeks.org/courses/placement-360-cip-complete-tech-interview)
- [DSA and System Design Course2 min read](https://www.geeksforgeeks.org/courses/interviewe-101-data-structures-algorithm-system-design)
- [Generative AI Course2 min read](https://www.geeksforgeeks.org/courses/generative-ai-training-program)

![](https://www.geeksforgeeks.org/techtips/most-useful-cmd-commands-in-windows/)