from configparser import ConfigParser

# Create a ConfigParser object.
config = ConfigParser()

# Read the .project config file.
config.read(filenames='.project_config')

# Get the values from the config file.
project_name = config['demo']['name']  # We get values as strings
project_version = config['demo']['version']

print(project_name, type(project_name))
print(project_version, type(project_version))
