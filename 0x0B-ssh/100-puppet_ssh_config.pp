#!/usr/bin/env bash
# Script that use puppet to change config.

file { 	'ect/ssh/ssh_cofig':
	 ensure => present,

content =>"

	#SSH client configuration
	host*
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
	",

}
