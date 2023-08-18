Go to the BaseSpace developer portal.
Click on the "Create an App" button.
Enter a name for your app and click on the "Create App" button.
Click on the "Credentials" tab.
Click on the "Generate Token" button.
Copy the token and save it in a secure location.


#Run the following lines to set necessary environment variables
export BASESPACE_CLIENT_ID=<REPLACE_ME>
export BASESPACE_CLIENT_SECRET=<REPLACE_ME>
export BASESPACE_BEARER_TOKEN=<REPLACE_ME>

curl -v -d "response_type=device_code" -d "client_id=$BASESPACE_CLIENT_ID" -d "scope=browse global" https://api.basespace.illumina.com/v1pre3/oauthv2/deviceauthorization

curl -H "Authorization: Bearer $BASESPACE_BEARER_TOKEN" -v -d "response_type=device_code" -d "scope=browse global" https://api.basespace.illumina.com/v1pre3/projects

curl -H "Authorization: Bearer $BASESPACE_BEARER_TOKEN" \
-v \
-d "response_type=device_code" \
-d "scope=browse global" \
-d '{
    "name": "My Project"
  }' \
https://api.basespace.illumina.com/v2/projects

curl -H "Authorization: Bearer 9824fd6870fc422b9696b98bbfedb346" -v -d "response_type=device_code" -d "scope=browse global" https://api.basespace.illumina.com/v2/applications

curl -H "Authorization: Bearer $BASESPACE_BEARER_TOKEN" \
-v \
 -H "Content-Type: application/json" \
  -d '{
    "name": "My Project"
  }' \
  https://api.basespace.illumina.com/v2/projects
 
 