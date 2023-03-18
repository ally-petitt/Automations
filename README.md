# Automations
Scripts that I create to automate tasks I come across when I would rather spend an hour coding than an 40 minutes doing it.

## remove_md5_from_filename.py Description
This Python script removes the MD5 hash added by Notion to each file when you go to export you notes. The typical file name format would be "[YOUR FOLDER/FILE] [MD5 HASH].[EXT]". An example of this is from my OSCP Notes repo when MSSQL.md had the name "MSSQL 3ccca60abe454be8bee82e97c920a60a.md" after being exported.

For this script to run, just replace the parameter of the function to be the base folder. From there, the MD5 hash will be removed recursivley from all the files and folders while retaining file extensions.

Note: this might not work if you have a .git folder in the the folder. You can either modifiy the code to work or move the folder to a temporary location, run the script, and replace it. The first option is reccommended.
```python remove_md5_from_filename.py```
