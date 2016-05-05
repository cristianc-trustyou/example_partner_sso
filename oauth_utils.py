# encoding: utf8

import base64
from gdata.tlslite.utils import keyfactory
import oauth2 as oauth
import array


def build_request(base_url, parameters, consumer_key, consumer_priv_key, method='GET'):
    """
    Builds signature of an HTTP request.

    @param base_url: HTTP request URL without query part.
    @param parameters: A dictionary of parameters used to create signature. It
    must contain additionally oauth_signature property.
    @param consumer_key: An identifier of signing consumer.
    @param consumer_priv_key: A private key of signing consumer.
    @param method: HTTP method used to make request.
    @return: OAuth request object. It is extension of dictionary and contains
    oauth_signature property.
    """

    # setting secret to meaningless string as the value is required
    consumer = oauth.Consumer(key=consumer_key, secret='None')
    req = oauth.Request(method=method, url=base_url, parameters=parameters, is_form_encoded=True)
    signature_method = SignatureMethod_RSA_SHA1(consumer_priv_key, None)
    req.sign_request(signature_method, consumer, None)

    return req


class SignatureMethod_RSA_SHA1(oauth.SignatureMethod):

    name = 'RSA-SHA1'

    def __init__(self, priv, pub):
        if priv:
            self.kpriv = priv.strip()
        else:
            self.kpriv = None
        if pub:
            self.kpub = pub
        else:
            self.kpub = None

    def signing_base(self, request, consumer, token):
        if not hasattr(request, 'normalized_url') or request.normalized_url is None:
            raise ValueError("Base URL for request is not set.")
        sig = (
            oauth.escape(request.method),
            oauth.escape(request.normalized_url),
            oauth.escape(request.get_normalized_parameters()),
        )

        key = '%s&' % oauth.escape(consumer.secret)
        if token:
            key += oauth.escape(token.secret)
        raw = '&'.join(sig)
        return key, raw

    def sign(self, request, consumer, token):
        """Builds the base signature string."""

        privatekey = keyfactory.parsePrivateKey(self.kpriv)

        key, raw = self.signing_base(request, consumer, token)
        print raw
        sig = privatekey.hashAndSign(raw)

        return base64.b64encode(sig)

    def check(self, request, consumer, token, signature):
        """
        Returns whether the given signature is the correct signature for
        the given consumer and token signing the given request.
        """

        publickey = keyfactory.parseAsPublicKey(self.kpub)

        key, raw = self.signing_base(request, consumer, token)
        sig = base64.b64decode(signature)


        return publickey.hashAndVerify(array.array('B', sig), raw)
