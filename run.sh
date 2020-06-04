#!/usr/bin/env sh
RUNMODE="${1:-app}"

echo "Start calculator service"

if [ "${RUNMODE}" = "app" ]; then
    exec python -m calc_app.app
elif [ "${RUNMODE}" = "test" ]; then
    pytest "./tests"
else
    exec "$@"
fi
