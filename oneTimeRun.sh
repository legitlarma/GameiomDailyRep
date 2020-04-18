currDirExe="$(pwd)/Gameiom-Daily-Report-oneTimeRun.py"
echo -n "Enter Gameiom Username: " 
read username
read -s -p "Enter Password: " password
python3 ${currDirExe} $username $password
