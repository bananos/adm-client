adm-client
==========
Python client for `Amazon Device Messaging (ADM) <https://developer.amazon.com/public/apis/engage/device-messaging>`_.

Requirements
------------

- `human_curl <https://pypi.python.org/pypi/human_curl/>`_ - Simple cURL wrapper for Humans


Usage
-----

Sample usage

.. code:: python

    from admclient import ADM, flatten

    client = ADM(client_id, client_secret)
    # see this http://stackoverflow.com/questions/11378004/with-android-gcm-can-you-use-a-deep-json-data-field
    # on why we need to flatten nested JSON structures
    payload = flatten({'examplekey': {'key1': 'value1'}})
    response = client.send(registration_id, payload)

    # Error handling
    if 'errors' in response:
        for reg_id, reason in response['errors'].items():
            if reason is 'InvalidRegistrationId':
                # Remove reg_ids from database
                pass

    if 'canonical' in response:
        for reg_id, canonical_id in response['canonical'].items():
            # Replace reg_id with canonical_id in your database
            pass




Installation
------------

.. code:: bash

    pip install https://github.com/bananos/adm-client/archive/master.zip


Copyright
---------

This work is based on original code from  `Python-adm <https://github.com/jacobcr/python-adm>`_.



