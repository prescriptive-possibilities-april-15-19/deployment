/bin/bash
$name = $1
$name .= .zip
zip $name application.py requirements.txt *.pickle script.py
