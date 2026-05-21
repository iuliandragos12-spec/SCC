#!/bin/sh
echo "Activare venv:"
. .venv/bin/activate

echo "Configurare variabila de mediu FLASK_APP"
export FLASK_APP=masini

echo "Start server pe portul 5011..."
exec flask run -h 0.0.0.0 -p 5011
