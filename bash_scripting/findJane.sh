

#!/bin/bash
> oldFiles.txt
files=$(grep " jane " ../data/list.txt | cut -d ' ' -f 3)
for file in $files; do
  file_path="..${file}"
  if [ -e $file_path ]; then
    realpath $file_path >> oldFiles.txt
  fi
done

