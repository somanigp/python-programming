# Command to run : bash environment_variable.sh
# Use these commands in linux terminals. export - to set Env Variables in OS.
# NOTE: the values of these variables are strings
# key=value
export OPEN_WEATHER_API_KEY=783a52292572a6f5701e995dd9e56bdf;  # ; to end a sentence
export OPEN_WEATHER_URL=https://api.openweathermap.org/data/2.5/forecast;
export LATITUDE=21.152451;  # My location
export LONGITUDE=79.080559;
export TWILIO_ACCOUNT_SID=AC1262acc54d2d3ebe612f77dd7779a03b;
export TWILIO_AUTH_TOKEN=d315097f0253c75bbcd91ebc436e4c56;
#export LATITUDE=47.218372;
#export LONGITUDE=-1.553621;
python main.py

# NOTE: This below will be your linux command to execute for running the application with environment variables.
# export OPEN_WEATHER_API_KEY=783a52292572a6f5701e995dd9e56bdf; export OPEN_WEATHER_URL=https://api.openweathermap.org/data/2.5/forecast; export TWILIO_ACCOUNT_SID=AC1262acc54d2d3ebe612f77dd7779a03b; export TWILIO_AUTH_TOKEN=d315097f0253c75bbcd91ebc436e4c56; export LATITUDE=47.218372; export LONGITUDE=-1.553621; python main.py