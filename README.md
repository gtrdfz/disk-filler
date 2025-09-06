# DiskFiller 🔒  

A simple script to fill up storage space (HDD, SSD, external drive, USB stick, etc.) with random files.

I created this tool to help remove sensitive data from disks after a quick format.

The program creates filler files until no free space is left. You can stop the program (Ctrl+C) at any time. The generated files can later be deleted if you want to free the space again.

## ✨ Features

- 🛑 **Safe for existing data**: does not delete or overwrite already present files.  
- ⏸️ **Interruptible**: you can stop the process at any time.  
- ▶️ **Resumable**: restart the tool and it will continue filling the remaining space.  
- 🔀 **Multi-drive support**: you can fill **several disks at the same time**.  

## 🚀 Usage

1. Open the `diskfiller.py` file.
2. Update it with the drive letters of the storage devices you want to fill.
   - Example: D and F 
3. Save the file and run the script:

```bash
python diskfiller.py
```

