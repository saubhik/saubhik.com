### Linux commands for survival

##### Change read-only partition to read/write
Today all of a sudden, I could not delete my trash. Figured out that my SDHC card became read-only.
Even though the hardware toggle switch was not in `Lock` mode. Might have been due to some kernel
updates I guess.

```commandline
mount -v | grep "^/" | awk '{print "\nPartition identifier: " $1  "\n Mountpoint: "  $3}'
```

Used this to find the partition identifier and the mountpoint. Then used this:

```commandline
sudo mount --options remount,rw <partition_identifier> <mountpoint>
```
Things became fine again.


##### 
