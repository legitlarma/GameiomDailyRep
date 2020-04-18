currDirExe="$(pwd)/Gameiom-Daily-Report-previous-day.py"
echo "${currDirExe}"
exec nohup python3 ${currDirExe} &
#open on start up
