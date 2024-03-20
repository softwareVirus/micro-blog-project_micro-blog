from mongoengine import Document, StringField, EmailField, DateTimeField
import datetime

class User(Document):
    """
    MongoDB Document model representing a user.

    Attributes
    ----------
    first_name : StringField
        First name of the user (max length: 200 characters), required.
    last_name : StringField
        Last name of the user (max length: 200 characters), required.
    email : EmailField
        Email of the user, unique and required.
    hashed_password : StringField
        Hashed password of the user, required.
    created_at : DateTimeField
        Timestamp representing the user's creation date (default: current UTC time).
    updated_at : DateTimeField
        Timestamp representing the user's last update date (default: current UTC time).

    Methods
    -------
    to_dict()
        Convert the User instance to a dictionary.

    Examples
    --------
    Creating a new user instance:

    >>> new_user = User(
    ...     first_name="John",
    ...     last_name="Doe",
    ...     email="john.doe@example.com",
    ...     hashed_password="hashed_password"
    ... )
    >>> new_user.save()
    """

    first_name = StringField(max_length=200, required=True)
    last_name = StringField(max_length=200, required=True)
    email = EmailField(unique=True, required=True)
    hashed_password = StringField(required=True)
    created_at = DateTimeField(default=datetime.datetime.utcnow())
    updated_at = DateTimeField(default=datetime.datetime.utcnow())

    def to_dict(self):
        """
        Convert the User instance to a dictionary.

        Returns
        -------
        dict
            A dictionary representation of the User instance.
        """
        return {
            "id": str(self.id),
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
