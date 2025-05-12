import os
import shutil
import tempfile
from pathlib import Path

def delete_temp_files(folder_path, count_logs=False):
    deleted_files = 0
    failed_files = 0
    log_files_deleted = 0

    for root, dirs, files in os.walk(folder_path, topdown=False):
        for name in files:
            file_path = os.path.join(root, name)
            try:
                if count_logs and file_path.lower().endswith(".log"):
                    log_files_deleted += 1
                os.remove(file_path)
                deleted_files += 1
            except Exception:
                failed_files += 1

        for name in dirs:
            dir_path = os.path.join(root, name)
            try:
                shutil.rmtree(dir_path, ignore_errors=True)
            except Exception:
                failed_files += 1

    return deleted_files, failed_files, log_files_deleted if count_logs else None

def main():
    # Directories to clean
    temp_dirs = [
        tempfile.gettempdir(),                          # Default user temp
        os.environ.get("TEMP", ""),                     # %TEMP%
        os.environ.get("TMP", ""),                      # %TMP%
        r"C:\Windows\Temp",                             # System-wide temp
        str(Path.home() / "AppData" / "Local" / "Temp") # Redundant safety
    ]

    # Filter out invalid or non-existent paths
    temp_dirs = list(set(filter(os.path.isdir, temp_dirs)))

    total_deleted = 0
    total_failed = 0

    for temp_dir in temp_dirs:
        print(f"\n🧹 Cleaning: {temp_dir}")
        if temp_dir.lower() == r"c:\windows\temp":
            deleted, failed, log_deleted = delete_temp_files(temp_dir, count_logs=True)
            print(f" - .log files deleted: {log_deleted}")
        else:
            deleted, failed, _ = delete_temp_files(temp_dir)

        print(f" - Total files/folders deleted: {deleted}")
        if failed:
            print(f" - Failed to delete: {failed} items")

        total_deleted += deleted
        total_failed += failed

    print(f"\n✅ Full Cleanup Complete.")
    print(f"   🔸 Total deleted: {total_deleted}")
    print(f"   🔸 Total failed: {total_failed}")

if __name__ == "__main__":
    main()