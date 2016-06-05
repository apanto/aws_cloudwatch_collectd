# aws_cloudwatch_collectd
collectd plugin for aws cloudwatch 

Requirements:

Boto3

Note: Collectd has a plugin uuid which when installed places a library uuid.so in /usr/lib64/collectd. Boto3 imports uuid which collides with the uuid library of the uuid plugin. Removing the plugin or simply renaming the file uuid.so solves this. 
