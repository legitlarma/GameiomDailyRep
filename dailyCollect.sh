currDirExe="$(pwd)/Gameiom-Daily-Report-previous-day.py"
echo -n "Enter Gameiom Username: " 
read username
read -s -p "Enter Password: " password
echo "\n"
exec python3 ${currDirExe} $username $password &
echo "\n"
#open on start up
