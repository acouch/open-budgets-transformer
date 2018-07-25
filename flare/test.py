import sys
import yaml

gov = sys.argv[1]

govs = yaml.load(open('./config.yml'))

print govs

print govs[gov]

