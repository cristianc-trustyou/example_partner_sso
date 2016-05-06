# TrustYou Partner B2B App Integration Example

This script shows an example of how to use the TY Partner B2B App.

<br />

#### Users are able to do the following operations:

 * Generate signed url that allows to access the Partner App from TrustYou.

<br/><br/>


## TABLE OF CONTENTS

  * [Synopsis](#synopsis).
  * [Environment](#environment).
  * [Requirements](#requirements).
  * [Configuration](#configuration).
  * [Example Call](#example-call).

<br/><br/>


## SYNOPSIS

```
$ python test_client.py --consumer_id=test_client --host_url=https://analytics.trustyou.com/kayak/ --hotel_id=42907d1a-91ea-4b43-bc40-8cc54cd92abf --user_name=kayak_test_1
```

<br/><br/>


## ENVIRONMENT

Install virtualenv if not already installed, for example:

```
$ sudo apt install virtualenv
```

Clone repository:

```
$ git clone [REPOSITORY_URL]
```

Execute the following in the directory from where you executed the clone:

```
$ cd example_partner_sso
$ virtualenv venv
```

Activate the newly created virtual environment:

```
$ . venv/bin/activate
```

<br/><br/>


## REQUIREMENTS

Install Python dependencies from the `requirements.txt` file:

```
$ pip install -r requirements.txt
```

<br/><br/>


## CONFIGURATION

Expected SSH keys in the "key_store" folder:

 * priv_<consumer_id>.pem: private key of consumer, needed for the signed url generation
 * pub_<consumer_id>.pem: public key of consumer, needed for the signed url verification, not used by the example

<br/><br/>


## EXAMPLE CALL

In order to perform an example call for the Kayak Partner B2B App having the following properties:

 * consumer_id: its important the consumer_id in the ssh private key name, for example: "priv_test_client.pem" corresponds to "test_client" consumer_id
 * host_url: standard url of the app
 * hotel_id: the id of the hotel
 * user_name: the user name from the caller system

```
python test_client.py --consumer_id=test_client --host_url=https://analytics.trustyou.com/kayak/ --hotel_id=42907d1a-91ea-4b43-bc40-8cc54cd92abf --user_name=kayak_test_1
```
