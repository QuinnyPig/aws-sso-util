# Copyright 2020 Ben Kehoe
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

import uuid
import random
import string
from collections import namedtuple

"""
instance arn: arn:aws:sso:::instance/ssoins-{16 hex}
identity store: d-{10 hex}
start url: https://d-X.awsapps.com/start
group: uuid
user: uuid
permission set: arn:aws:sso:::permissionSet/ssoins-X/ps-{16 hex}
ou: ou- 4 alphanum - 8 alphanum
account: 123456789012
"""

hex = "0123456789abcdef"
alphanum = string.ascii_lowercase + string.digits

def sample(lst, length):
    return "".join(random.choice(lst) for _ in range(length))

FakeIdentifiers = namedtuple("FakeIdentifiers", [
    "instance_arn",
    "identity_store_id",
    "start_url",
    "principal_id",
    "permission_set_arn",
    "ou_id",
    "account_id"
])

def generate_fake_identifiers():
    instance_id = "ssoins-{}".format(sample(hex, 16))
    identity_store_id = "d-{}".format(sample(hex, 10))

    instance_arn = "arn:aws:sso:::instance/{}".format(instance_id)
    start_url = "https://{}.awsapps.com/start".format(identity_store_id)
    principal_id = str(uuid.uuid4())
    permission_set_arn = "arn:aws:sso:::permissionSet/{}/ps-{}".format(instance_id, sample(hex, 16))
    ou_id = "ou-{}-{}".format(sample(alphanum, 4), sample(alphanum, 8))
    account_id = sample(string.digits, 12)

    return FakeIdentifiers(
        instance_arn,
        identity_store_id,
        start_url,
        principal_id,
        permission_set_arn,
        ou_id,
        account_id
    )

if __name__ == "__main__":
    fake_ids = generate_fake_identifiers()
    data = fake_ids._asdict()
    max_len = max(len(k) for k in data.keys())
    for key, value in data.items():
        print("{} {}".format((key+":").ljust(max_len+1), value))
