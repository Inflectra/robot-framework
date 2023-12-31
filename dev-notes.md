# How to setup and distribute plugin

## Environment setup
- install python 3.6+
- install pip
- update pip as required
- install robotframework `pip install robotframework`
- install twine for distribution `pip install twine`

## Running the sample
- Make sure the spira url and login/password are correct in the spira.cfg file
- Use either of these two commands, depending on whether you want to test running with a specific output folder/filename
- run `python robot_spira_integration.py`
- run `python robot_spira_integration.py Output.xml`

## Distribute code
- double check the version is correct in setup.py
- delete any files in the dist folder
- run `python -m pip install --upgrade build`
- run `python -m build`
- run `python -m twine upload dist/*`
- at the prompt for the username type __TOKEN__
- for the password paste the API key that is stored with the login information for https://pypi.org/
- if the above credentials do not work you can try the standard username and password for https://pypi.org/

# Useful links
https://packaging.python.org/tutorials/packaging-projects/

# Other information
To create an xunit XML file (not needed for Spira integration, but useful for other tools)
`rebot -R --xunit xunit.xml output*.xml`