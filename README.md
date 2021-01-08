# Discord Bot for minecraft-sisters GCP minecraft server

Discord bot for initializing and stopping Google Cloud Compute Engine Minecraft Server Instance
Hosted on Heroku and written in Python

# To use: 
(This guide assumes you have a pre-existing minecraft server with auto start up and stop on instance intialization on the Google Cloud Compute Engine, if not, please check the docs for more info on how to set it up: https://cloud.google.com/solutions/gaming/minecraft-server)

1. Fork git repo. 
2. Change lines 11, 12, and 13 main.py to your own respective instance project name, zone and instance name. 
3. push changes to git
4. In heroku, set convig vars for your own discord token and server IP (naming the keys DISCORD_TOKEN and SERVER_IP respectively)
5. Add addtional config vars for Google Cloud Credentials. You have to download your credentials from Google Cloud Service Account page: https://cloud.google.com/docs/authentication/getting-started, follow guide here on how to do so ( creating service account), you shouldve downloaded a JSON file when done: 
      1 - Declare your env variables from in Heroku dashboard like :
      The GOOGLE_CREDENTIALS variable is the content of service account credential JSON file as is. The GOOGLE_APPLICATION_CREDENTIALS env variable in the string "google-                credentials.json"
      2 - Once variables are declared, add the builpack in heroku in the section below the config vars and pasting this link:
      https://github.com/gerywahyunugraha/heroku-google-application-credentials-buildpack
6. Make sure for !mc status to work, set enable_query to be true in the server properties file on your server. 
7. Deploy on heroku and it should work :)) 

# Commands:
!mcs start - to start minecraft server
!mcs status - display members online 
!mcs stop - stop minecraft server

enjoy, martin au-yeung. 
