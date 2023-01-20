#!/bin/bash

services=("rabbit mysql mongodb" "notification auth converter gateway")

for group in ${services[@]};
do
	for service in $group
	do
		kubectl delete -f ./src/$service/manifests/
	done
done