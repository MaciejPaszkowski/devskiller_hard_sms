from app import errors
from app import settings
from app.fake import fake_primary_external_api
from .base import BaseSmsProvider



class PrimarySmsApiProvider(BaseSmsProvider):
    """Primary SMS API Provider"""

    API_KEY = settings.PRIMARY_API_KEY

    def _validate_set_recipient(self, *args):
        """Validate recipient using the same logic as defined in `old.py` file.
        Throw appropriate exception or return a boolean"""
        #
        # @TODO: Implement it
        if not args[0].isdigit():
            raise errors.InvalidPhoneNumber("Invalid phone number")


    def _validate_set_content(self, *args):
        """Validate content.
        Throw appropriate exception or return a boolean"""
        #
        # @TODO: Implement it
        if len(args[0]) > 70:
            raise errors.InvalidContentLength("Invalid content length")

        return True

    def _validate_before_sending(self):
        """Check if content and recipient are set.
        Throw appropriate exception from `app.errors` module"""
        #
        # @TODO: Implement it
        if self.recipient is None:
            raise errors.RecipientNotSet

        if self.content is None:
            raise errors.ContentNotSet

        return True


    def _process_response(self, resp):
        """Check response content.
        Return (boolean, resp)"""
        #
        # @TODO: Implement it

        if resp["status"]=="403":
            return None, resp
        return True, resp

    def _prepare_payload(self):
        """Construct and return payload - check `old.py` for the implementation details"""
        #
        # @TODO: Implement it

        return {"api_key":self.API_KEY, "phone":self.recipient }

    def send(self):
        """Send the message"""
        self._validate_before_sending()
        payload = self._prepare_payload()
        response = fake_primary_external_api(payload)
        return self._process_response(response)
