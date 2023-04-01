# Automations
Scripts that I create to automate tasks I come across when I would rather spend an hour coding than an 40 minutes doing it.
## Tables of Contents
1. [Description of `remove_md5_from_filename.py`](https://github.com/ally-petitt/Automations#description-of-remove_md5_from_filenamepy)
2. [Description of `remove-old-files.sh`](https://github.com/ally-petitt/Automations#description-of-remove-old-filessh)


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


