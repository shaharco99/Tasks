#!/bin/bash
# Update every Jenkins plugin that has an update available, then safe-restart.
# Usage: JENKINS_URL=http://<host>:<port>/ JENKINS_AUTH=user:api-token ./jenkins_update.sh
set -euo pipefail
: "${JENKINS_URL:?set JENKINS_URL}"
: "${JENKINS_AUTH:?set JENKINS_AUTH (user:api-token)}"

curl -fsS "${JENKINS_URL}jnlpJars/jenkins-cli.jar" --output /opt/jenkins-cli.jar
cli() { java -jar /opt/jenkins-cli.jar -s "$JENKINS_URL" -auth "$JENKINS_AUTH" "$@"; }

UPDATE_LIST=$(cli list-plugins | grep -e ')$' | awk '{ print $1 }')
if [ -n "${UPDATE_LIST}" ]; then
    echo "Updating Jenkins plugins: ${UPDATE_LIST}"
    # shellcheck disable=SC2086 # one argument per plugin
    cli install-plugin ${UPDATE_LIST}
    cli safe-restart
fi
