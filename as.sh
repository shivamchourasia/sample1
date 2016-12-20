#echo give any number
#read var
#if [ "$var" -ge "2" ]
#	 then
 for File in /home/asm/temp1/temp2/*
  do
  echo ${File##*/}
  #var=${File##*/}
 find ${File##*/} -mtime +1 -type f -delete
   echo "hello"
 done
#fi