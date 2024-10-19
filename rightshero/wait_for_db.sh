#!/bin/sh
echo "try"
while ! mysqladmin ping -h"db" --silent; do
    echo "Waiting for database connection..."
    sleep 2
done
echo "I am out"
