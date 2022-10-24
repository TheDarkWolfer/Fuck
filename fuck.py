import glob, os, argparse, sys, time
parser = argparse.ArgumentParser()
parser.add_argument("file_extension", help="specify the file extension to be deleted")
args = parser.parse_args()
if args.file_extension[0] != ".":
    print("Invalid file extension")
    sys.exit(0)
file_extension = args.file_extension
file_list = glob.glob("*"+file_extension)
print(f'starting deletion of {len(file_list)} files')
deleted_files_count = 0
print(f"Welcome to Lou's fuck-up cleaner ! It will automatically delete all files of extension {file_extension} in no time !")
for file in glob.glob("*" + file_extension):
    os.remove(file)
    print(f'deleted {file} now {deleted_files_count} files deleted out of {len(file_list)}',end="\r")
    deleted_files_count += 1
    time.sleep(0.001)
print(f"Done ! {deleted_files_count} files deleted out of {len(file_list)}")
time.sleep(1)
os.system("cls")