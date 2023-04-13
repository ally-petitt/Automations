# Automations
Scripts that I create to automate tasks I come across when I would rather spend an hour coding than an 40 minutes doing it.
## Tables of Contents
1. [Description of `exploit_libc.py`](https://github.com/ally-petitt/Automations#description-of-exploit_libcpy)
2. [Description of `remove_md5_from_filename.py`](https://github.com/ally-petitt/Automations#description-of-remove_md5_from_filenamepy)
3. [Description of `remove-old-files.sh`](https://github.com/ally-petitt/Automations#description-of-remove-old-filessh)
4. [Description of `install-security-updates.sh`](https://github.com/ally-petitt/Automations#description-of-install-security-updatessh)
5. [Description of `find_rip_offset.py`](https://github.com/ally-petitt/Automations#description-of-find_rip_offsetpy)

## Description of `exploit_libc.py`
Finds the RIP offset of an executable binary just like `find_rip_offset.py`, but continues to use that value in order to get a shell through the `system()` function in libc.so.6 with PIE, Canary and NX enabled. It does this by leaking the memory address of `scanf` when the `gets` function is called and using its offset in the `libc.so.6` file in order to calculate the base address of the `libc.so.6` file. Then, it uses the offset of the `system` function from the base address in order to call it with the parameter `/bin/sh`, which was located in memory and written to the RDI ([see x86 calling conventions](https://en.wikipedia.org/wiki/X86_calling_conventions) to understand why I overwrote the RDI to pass a parameter). The result is that the server hosting the vulnerable binary runs `system('/bin/sh')` that you use to get remote code execution through your interactive shell.

### Help Menu
```
$ python3 ./exploit_libc.py --help                                                     2 ⨯
usage: exploit_libc [-h] -f FILENAME -p PAYLOAD_SIZE

options:
  -h, --help            show this help message and exit
  -f FILENAME, --filename FILENAME
                        name of the executable file that you want to find the offset of
  -p PAYLOAD_SIZE, --payload-size PAYLOAD_SIZE
                        size of the payload to use to find the offset (must be enough to cause a segmentation fault
                        in the program)

         This program finds the address of libc.so.6 in the running binary
         and uses it, along with a "pop RDI" instruction in order to get a shell.

```

## Description of `remove_md5_from_filename.py`
This Python script removes the MD5 hash added by Notion to each file when you go to export you notes. The typical file name format would be "[YOUR FOLDER/FILE] [MD5 HASH].[EXT]". An example of this is from my OSCP Notes repo when MSSQL.md had the name "MSSQL 3ccca60abe454be8bee82e97c920a60a.md" after being exported.

For this script to run, just replace the parameter of the function to be the base folder. From there, the MD5 hash will be removed recursivley from all the files and folders while retaining file extensions.

Note: this might not work if you have a .git folder in the the folder. You can either modifiy the code to work or move the folder to a temporary location, run the script, and replace it. The first option is reccommended.
```python remove_md5_from_filename.py```

## Description of `remove-old-files.sh`
This Bash script deletes files that haven't been accessed in a certain number of days. It is assumed that the OS running this script is Debian-based, but if it isn't, then it can be easily modified to work for your OS.
```
./clear-old-files.sh <YOUR_DIRECTORY> <DAYS_SINCE_ACCESSED>

# this example will delete the files in "/home/ally/awesome-dir" that haven't been
# accessed in 60 days or more
./clear-old-files.sh /home/ally/awesome-dir 60 
```
### Example output
![Image of the output when the program is in use](./photos/clear-old-files.png)


## Description of `install-security-updates.sh`
This bash script will automatically install security updates on Debain-based operating systems through the apt package manager. As such, root or sudo privileges are required. It uses 3 methods of installing the security updates to ensure that minimal packages were missed by the end.

```
chmod +x install-security-updates.sh
./install-security-updates.sh
```

## Description of `find_rip_offset.py`
This python script was created to automate the process of finding the RIP offset when attempting to overflow a 64-bit buffer in a vulnerable binary. It utilizes pwntools to create a process running the executable and interacts with it using a de Bruijn sequence to calculate the offset.

### Example Usage
```
$ python ./find_rip_offset.py -f ./binary_to_overflow -p 200
[+] Starting local process './binary_to_overflow': pid 104267
[*] Process './binary_to_overflow' stopped with exit code -11 (SIGSEGV) (pid 104267)
[+] Parsing corefile...: Done
[*] '/home/ally/my/path/core.104267'
    Arch:      amd64-64-little
    RIP:       0x400770
    RSP:       0x7fff33c05f58
    Exe:       '/home/ally/my/path/binary_to_overflow' (0x400000)
    Fault:     0x6261616b6261616a
[*] RIP offset is 136

```



