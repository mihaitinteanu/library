class ClientValidator:
    """
    A class that helps with the validation of clients.
    """
    def validate_client(self, client):
        errors = []

        if client.get_client_id() <= 0:
            errors.append('Client id cannot be negative.')

        if not str(client.get_name()).strip():
            errors.append('Client name cannot be empty.')

        if len(client.get_cnp()) != 13:
            errors.append('Client CNP contains 13 digits.')

        if len(errors) > 0:
            raise ValueError('\n'.join(errors))