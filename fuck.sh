files=$(ls)
ext=$1
for file in $files
do
    if [[ $file == *.$ext ]]
    then
        rm $file
    fi
done