#!/bin/sh

if [ -d "../venv" ]
then
    VENVDIR="../venv"
    source "${VENVDIR}/bin/activate"
fi

./run.py --host 0.0.0.0 --port=5000

