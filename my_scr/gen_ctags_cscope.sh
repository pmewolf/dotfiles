#! /bin/bash

TARGET='./cscope.files'

if [ -z ${1} ]; then
    echo "Please enter database directory"
    exit 1
fi

if [ -s ${TARGET} ]; then
    cat /dev/null > ${TARGET}
fi

#for dir in $@
#do
#    if [ ${dir} != ${1} ]; then
#        find ${1}/${dir} -name "*.[hc]" -print >> ${TARGET}
#    fi
#done

find ${1} -name "*.[hc]" -print >> ${TARGET}
/usr/bin/cscope -Rbq -i cscope.files
ctags -R --exclude=.svn
