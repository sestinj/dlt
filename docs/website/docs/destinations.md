---
sidebar_position: 8
---

# Destinations

**`dlt` supports three destinations (more coming soon)**
- [Google BigQuery](./destinations#google-bigquery)
- [Postgres](./destinations#postgres)
- [Amazon Redshift](./destinations#amazon-redshift)

Learn how to set up each of the supported destinations below.

## Google BigQuery

**1. Initalize a project with a pipeline that loads to BigQuery by running**
```
dlt init chess bigquery
```

**2. Install the necessary dependencies for BigQuery by running**
```
pip install -r requirements.txt
```

**3. Log in to or create a Google Cloud account**

Sign up for or log in to the [Google Cloud Platform](https://console.cloud.google.com/) in your web browser.

**4. Create a new Google Cloud project**

After arriving at the [Google Cloud console welcome page](https://console.cloud.google.com/welcome), click the
project selector in the top left, then click the `New Project` button, and finally click the `Create` button
after naming the project whatever you would like.

**5. Create a service account and grant BigQuery permissions**

You will then need to [create a service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts#creating). After clicking the `Go to Create service account` button
on the linked docs page, select the project you just created and name the service account whatever you would like.

Click the `Continue` button and grant the following roles, so that `dlt` can create schemas and load data:
- *BigQuery Data Editor*
- *BigQuery Job User*
- *BigQuery Read Session User*

You don't need to grant users access to this service account at this time, so click the `Done` button.

**6. Download the service account JSON**

In the service accounts table page that you are redirected to after clicking `Done` as instructed above,
select the three dots under the `Actions` column for the service account you just created and 
select `Manage keys`. 

This will take you to page where you can click the `Add key` button, then the `Create new key` button, 
and finally the `Create` button, keeping the preselected `JSON` option.

A `JSON` file that includes your service account private key will then be downloaded.

**7. Update your `dlt` credentials file with your service account info**

Open your `dlt` credentials file:
```
open .dlt/secrets.toml
```

Replace the `project_id`, `private_key`, and `client_email` with the values from the downloaded `JSON` file:
```
[destination.bigquery.credentials]

location = "US"
project_id = "project_id" # please set me up!
private_key = "private_key" # please set me up!
client_email = "client_email" # please set me up!
```

## Postgres

**1. Initalize a project with a pipeline that loads to Postgres by running**
```
dlt init chess postgres
```

**2. Install the necessary dependencies for Postgres by running**
```
pip install -r requirements.txt
```

**3. Create a new database after setting up a Postgres instance and `psql` / query editor by running**
```
CREATE DATABASE dlt_data;
```

Add `dlt_data` database to `.dlt/secrets.toml`.

**4. Create a new user by running**
```
CREATE USER loader WITH PASSWORD '<password>';
```

Add `loader` user and `<password>` password to `.dlt/secrets.toml`.

**5. Give the `loader` user owner permissions by running**
```
ALTER DATABASE dlt_data OWNER TO loader;
```

It is possible to set more restrctive permissions (e.g. give user access to a specific schema).

**6. Your `.dlt/secrets.toml` should now look like**
```
[destination.postgres.credentials]

database = "dlt_data"
username = "loader"
password = "<password>" # replace with your password
host = "localhost" # or the IP address location of your database
port = 5432
connect_timeout = 15
```

## Amazon Redshift

**1. Initalize a project with a pipeline that loads to Redshift by running**
```
dlt init chess redshift
```

**2. Install the necessary dependencies for Redshift by running**
```
pip install -r requirements.txt
```

**3. Edit the `dlt` credentials file with your info**
```
open .dlt/secrets.toml
```