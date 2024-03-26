##!/usr/bin/pup
# Script that use  Puppt to install flask
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
