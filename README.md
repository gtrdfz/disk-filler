# DiskFiller 🔒  

A simple script to fill up storage space (HDD, SSD, external drive, USB stick, etc.) with files full of **zeros**.

The program creates filler files until no free space is left.

You can stop the program (Ctrl+C) at any time.

The generated files can later be deleted if you want to free the space again.

---

## ✨ Features

- 🟢 **Simple data sanitization**: creates files filled with `0x00` until free space is consumed.  
- 🛑 **Safe for existing data**: does not delete or overwrite already present files.  
- ⏸️ **Interruptible**: you can stop the process at any time.  
- ▶️ **Resumable**: restart the tool and it will continue filling the remaining space.  
- 💽 **Wide compatibility**: works on any writable storage device (HDD, SSD, USB drive, external disk, etc.).  
---

## 🚀 Usage

1. Open the `diskfiller.py` file.
2. Update it with the drive letters of the storage devices you want to fill.
   - Example: D and F 
3. Save the file and run the script:

```bash
python diskfiller.py
```

