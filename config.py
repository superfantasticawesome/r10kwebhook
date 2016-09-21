import os


SECRET_KEY = os.environ.get('SECRET_KEY') or 'bdgasfj'
R10K = os.environ.get('R10K') or '/opt/puppetlabs/puppet/bin/r10k'
R10K_CONF = os.environ.get('R10K_CONF') or '/etc/puppetlabs/r10k/r10k.yaml'
