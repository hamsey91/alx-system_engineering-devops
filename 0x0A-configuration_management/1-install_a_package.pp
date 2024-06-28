# Script to install Flask using Puppet

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip333',
}
