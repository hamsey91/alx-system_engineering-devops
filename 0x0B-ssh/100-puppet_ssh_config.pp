#!/usr/bin/env bash
# Script that use puppet to change config

file { '/etc/ssh/ssh_config':
	ensure  => present,
content => "
	# SSH client configuration
	Host *
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
  	",
}
