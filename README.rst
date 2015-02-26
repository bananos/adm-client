adm-client
==========
Python client for `Amazon Device Messaging (ADM) <https://developer.amazon.com/public/apis/engage/device-messaging>`_.

Requirements
------------

- `human_curl <https://pypi.python.org/pypi/human_curl/>`_ - Simple cURL wrapper for Humans


Usage
-----

Sample usage::

    from admclient import ADM

    client = ADM(client_id, client_secret)
    response client.send(registration_id, {'examplekey': {'key1': 'value1'}})

    # Error handling
    if 'errors' in response:
        for reg_id, reason in response['errors'].items():
            if error is 'InvalidRegistrationId':
                # Remove reg_ids from database
                pass

    if 'canonical' in response:
        for reg_id, canonical_id in response['canonical'].items():
            # Replace reg_id with canonical_id in your database
            pass




Installation
------------

::

    pip install https://github.com/bananos/adm-client/archive/master.zip


Copyright
---------

This work is based on original code from  `Python-adm <https://github.com/jacobcr/python-adm>`_.



