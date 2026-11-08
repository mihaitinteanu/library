class ClientController:
    """
    A class that manages all the client related functionalities.
    Intermediates communication between the UI and the repository.
    Attributes:
        client_repository: An object that stores the clients
        client_validator: An object that validates the clients
    """
    def __init__(self, client_repository, client_validator):
        self.client_repository = client_repository
        self.client_validator = client_validator

    def get_clients(self):
        """
        Method that gets all the clients available in the repository.
        :return: the method from the repo that gets all the clients
        """
        return self.client_repository.get_clients()

    def controller_add_client(self, client):
        """
        Method that validates the user input and calls the method that does
        the adding of the client to the repository.
        :param client: a client object
        :return: None
        """
        self.client_validator.validate_client(client)
        self.client_repository.add_client(client)

    def controller_del_client(self, client_id):
        """
        Method that validates the user input and calls the method that
        deletes the client from the repository.
        :param client_id: a client_id
        :return: None
        """
        if client_id <= 0:
            raise ValueError("Client id cannot be negative!")
        self.client_repository.del_client(client_id)

    def controller_update_client(self, client):
        """
        Method that validates the user input and calls the method that
        updates the client in the repository.
        :param client: a client object
        :return: None
        """
        self.client_validator.validate_client(client)
        self.client_repository.update_client(client)