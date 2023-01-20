#!/bin/bash

services=("rabbit mysql mongodb" "notification auth converter gateway")

for group in ${services[@]};
do
	for service in $group
	do
		kubectl apply -f ./src/$service/manifests/
	done
	sleep 5
done

minikube addons enable ingress
sudo -- sh -c "echo 127.0.0.1       mp3converter.com >> /etc/hosts"
