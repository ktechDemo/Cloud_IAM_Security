import boto3

# Create a CloudTrail client
client = boto3.client('cloudtrail')

# Fetch the last 10 events
events = client.lookup_events(MaxResults=10)['Events']

# Loop through the events and print out relevant info
for e in events:
    print(f"Event: {e['EventName']}, User: {e.get('Username', 'N/A')}, Time: {e['EventTime']}")
