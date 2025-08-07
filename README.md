# Braintrust-Project

This is the script for the take-home assesment portion of the interview. I wrote a simple Python script that pulls event data for all experiments/datasets in the specified project and outputs them as CSVs into individual folders to upload to support. The script requires the user to specify the Project ID that they want to pull data from as well as a valid API key that can be used for all necessary calls.

The script requires the use of the Pandas library to handle CSV output, so you'll need to install that first: 

```
pip install pandas
```

The script requires two arguments, the Project ID and your API Key. These are both passed as command arguments using the following formant:

```
python projectMain.py -p YOUR_PROJECT_ID -a YOUR_API_KEY
```

The arguments are as follows:

```
-p, --projectID : The project ID you want to pull data from
-a, --apiKey : The API key you are going to use with the script
```

I chose to use option arguments for the Project ID and API Key as I personally find that more readable for someone that isn't familiar with the script, as opposed to passing both as positional arguments. 
