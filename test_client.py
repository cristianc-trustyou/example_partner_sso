import getopt
import sys

from key_store import get_private_key
from oauthlib import oauth1
from urllib import urlencode

HRS_REGISTER_PATH = "api/register/"


def _get_priv_key(consumer_id):
        key = get_private_key("key_store", consumer_id)
        if key is not None:
            return key
        else:
            raise Exception("Cannot find private key for consumer_id")


def generate_signed_registration_request(hotel_id, user_name, consumer_id, host_url, scale=None, lang=None,
                                         default_partner_tile_idx=None):
        """
        Generates signed registration request.

        @param params: Request parameters.
        @return: Registration request URL with signature.
        """

        params = {}
        params["hotel_id"] = hotel_id
        params["oauth_token"] = user_name

        target_url = host_url

        if scale:
            params["scale"] = scale

        if lang:
            params["lang"] = lang

        if default_partner_tile_idx >= 0:
            params["default_partner_tile_idx"] = default_partner_tile_idx

        register_base_url = target_url + HRS_REGISTER_PATH

        consumer_key = _get_priv_key(consumer_id)

        client = oauth1.Client(
            client_key=consumer_id,
            signature_method=oauth1.SIGNATURE_RSA,
            rsa_key=consumer_key,
            signature_type=oauth1.SIGNATURE_TYPE_QUERY
        )

        unsigned_url = register_base_url + '?' + urlencode(params)

        url, headers, body = client.sign(unsigned_url)

        return url


def _get_option(name, opts_dict):
    if "--" + name in opts_dict:
        return opts_dict["--" + name]
    else:
        return None

if __name__ == "__main__":

    opts, args = getopt.getopt(
        sys.argv[1:], "", [
            "consumer_id=", "host_url=", "hotel_id=", "user_name=", "default_partner_tile_idx=", "lang=", "scale="
        ]
    )

    print opts

    opts_dict = {}

    for curr_opt in opts:
        opts_dict[curr_opt[0]] = curr_opt[1]

    consumer_id = _get_option("consumer_id", opts_dict)
    host_url = _get_option("host_url", opts_dict)
    hotel_id = _get_option("hotel_id", opts_dict)
    user_name = _get_option("user_name", opts_dict)
    default_partner_tile_idx = _get_option("default_partner_tile_idx", opts_dict)
    lang = _get_option("lang", opts_dict)
    scale = _get_option("scale", opts_dict)

    signed_url = generate_signed_registration_request(
        hotel_id,
        user_name,
        consumer_id,
        host_url,
        scale=scale,
        lang=lang,
        default_partner_tile_idx=default_partner_tile_idx
    )

    url = signed_url

    print "Generated signed URL:"

    print url
