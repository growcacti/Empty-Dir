# Empty-Dir
Remove empty directories and send a report
 Directory Checker – Empty Folder GUI Manager

A Python GUI tool built with Tkinter that allows users to scan, omit, delete, and restore empty folders from a selected directory. It includes progress tracking, report saving, undo functionality, and multi-directory selection, all packed into a clean, interactive interface.
🎯 Key Features

    ✅ Scan for Empty Folders
    Recursively identifies all empty folders inside a selected directory and lists them.

    ❌ Delete Selected or All Empty Folders
    Choose to delete specific empty folders or remove all with a single click.

    🚫 Omit Selected Folders
    Mark folders you want to keep and prevent accidental deletion.

    🔁 Undo Deletions
    Instantly recreate deleted folders if you need to undo the operation.

    📝 Save Report
    Export a detailed scan and deletion report to a text file.

    📊 Progress Bar & Status Display
    Visual feedback for scanning and deletion processes.

    🔒 Safe Operation
    Folders are only removed if they are empty and not omitted.

🧱 Application Layout

    Buttons

        Check Directories: Starts scan for empty folders.

        Delete Selected Directories: Removes selected folders from the list.

        Delete All Empty Directories: Deletes all found empty folders (except omitted ones).

        Omit Selected Directory: Marks selected folders to skip during deletion.

        Save Report: Saves the text output to a .txt file.

        Undo Deletions: Recreates deleted folders.

    Text Widget

        Shows logs and status messages during operations.

    Listbox

        Displays found empty directories. Allows multi-selection.

    Progress Bar

        Indicates scanning or deletion progress.

    Status Label

        Shows the current operation status (e.g., "Scanning...", "Deletion Completed").

🖥️ Example Workflow

    Click Check Directories → Select a folder.

    View empty directories in the listbox and log window.
 Directory Checker – Empty Folder GUI Manager

A Python GUI tool built with Tkinter that allows users to scan, omit, delete, and restore empty folders from a selected directory. It includes progress tracking, report saving, undo functionality, and multi-directory selection, all packed into a clean, interactive interface.
🎯 Key Features

    ✅ Scan for Empty Folders
    Recursively identifies all empty folders inside a selected directory and lists them.

    ❌ Delete Selected or All Empty Folders
    Choose to delete specific empty folders or remove all with a single click.

    🚫 Omit Selected Folders
    Mark folders you want to keep and prevent accidental deletion.

    🔁 Undo Deletions
    Instantly recreate deleted folders if you need to undo the operation.

    📝 Save Report
    Export a detailed scan and deletion report to a text file.

    📊 Progress Bar & Status Display
    Visual feedback for scanning and deletion processes.

    🔒 Safe Operation
    Folders are only removed if they are empty and not omitted.

🧱 Application Layout

    Buttons

        Check Directories: Starts scan for empty folders.

        Delete Selected Directories: Removes selected folders from the list.

        Delete All Empty Directories: Deletes all found empty folders (except omitted ones).

        Omit Selected Directory: Marks selected folders to skip during deletion.

        Save Report: Saves the text output to a .txt file.

        Undo Deletions: Recreates deleted folders.

    Text Widget

        Shows logs and status messages during operations.

    Listbox

        Displays found empty directories. Allows multi-selection.

    Progress Bar

        Indicates scanning or deletion progress.

    Status Label

        Shows the current operation status (e.g., "Scanning...", "Deletion Completed").

🖥️ Example Workflow

    Click Check Directories → Select a folder.

    View empty directories in the listbox and log window.

    Select specific folders to delete or omit.

    Click Delete Selected Directories or Delete All Empty Directories.

    Optionally Undo deletions or Save the report.

📦 Requirements

    Python 3.x

    Tkinter (comes built-in with standard Python installations)

▶️ How to Run

python directory_checker.py

    Note: Replace directory_checker.py with the filename of your script.

🛡️ Safety Tips

    Only empty directories are deleted — folders with files remain untouched.

    Omitted folders are never deleted.

    Undo only recreates deleted folder paths, not their contents.

Let me know if you'd like a version of this README in markdown format or an installable .exe/.deb version setup for users!
    Select specific folders to delete or omit.

    Click Delete Selected Directories or Delete All Empty Directories.

    Optionally Undo deletions or Save the report.

📦 Requirements

    Python 3.x

    Tkinter (comes built-in with standard Python installations)

▶️ How to Run

python directory_checker.py

    Note: Replace directory_checker.py with the filename of your script.

🛡️ Safety Tips

    Only empty directories are deleted — folders with files remain untouched.

    Omitted folders are never deleted.

    Undo only recreates deleted folder paths, not their contents.
