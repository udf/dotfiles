#!/bin/bash

repstr() {
	echo $(printf "$1"'%.s' $(eval "echo {1.."$(($2))"}"));
}
print_tits() {
	nipple=$(repstr . $1)
	tits=$(repstr "($nipple)" $2)

	if [ "$3" != "NOCLEAR" ]; then printf "\ec"; fi
	echo $tits
	if [ -n "$3" ] && [ "$3" != "NOCLEAR" ]; then sleep $3; fi
}

print_tits 1 2
for i in {1..3}
do
for ncount in {1..3}
	do
		print_tits $ncount 2 0.3
		if [ $i = "3" ] && [ $ncount = "2" ]; then break; fi;
	done
done

for ncount in {3..32}
do
	print_tits $ncount 2
done

tcount=3
for i in {1..512}
do
	print_tits $ncount $tcount NOCLEAR
	if (( RANDOM % 2 )); then tcount=$((tcount+1)); else ncount=$((ncount+1)); fi
done

#print some nice ascii art
eval $(base64 --decode <<< "cHJpbnRmICIoLnwuKVxuICkuKCBcbiggdiApXG4gXHwvIiAmJiBzaHV0ZG93biAtciBub3cK")

#uncomment this if you want to reboot
#shutdown -r now
