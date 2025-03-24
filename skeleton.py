"""
Dog Daycare Management System

This module implements a dog daycare management system that tracks
dogs, owners, and check-in/check-out operations using object-oriented programming.

TODO: Implement all the classes and methods following the specifications
"""

# DO NOT MODIFY THE IMPORT
import datetime


class Dog:
    """Base class representing a dog in the daycare."""
    
    def __init__(self, dog_id, name, breed, age, weight, is_checked_in=False):
        """
        Initialize a Dog object.
        
        Args:
            dog_id: Unique identifier for the dog
            name: Name of the dog
            breed: Breed of the dog
            age: Age of the dog in years
            weight: Weight of the dog in pounds
            is_checked_in: Whether the dog is currently checked in
        """
        # Validate age and weight
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Age must be a positive integer")
        
        if not isinstance(weight, (int, float)) or weight <= 0:
            raise ValueError("Weight must be a positive number")
            
        # TODO: Initialize all the private attributes
        # HINT: Use double underscore prefix for private attributes (e.g., self.__dog_id)
        # WRITE IMPLEMENTATION HERE
        pass
    
    @property
    def dog_id(self):
        """Get the dog ID."""
        # TODO: Return the dog_id
        # WRITE IMPLEMENTATION HERE
        pass
    
    @property
    def name(self):
        """Get the dog name."""
        # TODO: Return the name
        # WRITE IMPLEMENTATION HERE
        pass
    
    @property
    def breed(self):
        """Get the dog breed."""
        # TODO: Return the breed
        # WRITE IMPLEMENTATION HERE
        pass
    
    @property
    def age(self):
        """Get the dog age."""
        # TODO: Return the age
        # WRITE IMPLEMENTATION HERE
        pass
    
    @property
    def weight(self):
        """Get the dog weight."""
        # TODO: Return the weight
        # WRITE IMPLEMENTATION HERE
        pass
    
    @property
    def is_checked_in(self):
        """Get the dog check-in status."""
        # TODO: Return the is_checked_in status
        # WRITE IMPLEMENTATION HERE
        pass
    
    @is_checked_in.setter
    def is_checked_in(self, value):
        """Set the dog check-in status."""
        # TODO: Set the is_checked_in status
        # WRITE IMPLEMENTATION HERE
        pass
    
    def check_in(self):
        """
        Mark the dog as checked in.
        
        Returns:
            bool: True if check-in successful, False otherwise
        """
        # TODO: Implement check-in logic
        # HINT: Only successful if dog is not already checked in
        # WRITE IMPLEMENTATION HERE
        pass
    
    def check_out(self):
        """
        Mark the dog as checked out.
        
        Returns:
            bool: True if check-out successful, False otherwise
        """
        # TODO: Implement check-out logic
        # HINT: Only successful if dog is currently checked in
        # WRITE IMPLEMENTATION HERE
        pass
    
    def display_info(self):
        """
        Display dog information.
        
        Returns:
            str: Formatted string with dog information
        """
        # TODO: Return formatted string with dog information
        # HINT: Include dog_id, name, breed, age, weight, and check-in status
        # WRITE IMPLEMENTATION HERE
        pass


class SmallDog(Dog):
    """Class representing a small dog, inherits from Dog."""
    
    def __init__(self, dog_id, name, breed, age, weight, is_checked_in=False, toy_preference="None"):
        """
        Initialize a SmallDog object.
        
        Args:
            dog_id: Unique identifier for the dog
            name: Name of the dog
            breed: Breed of the dog
            age: Age of the dog in years
            weight: Weight of the dog in pounds
            is_checked_in: Whether the dog is currently checked in
            toy_preference: Preferred toy type for the small dog
        """
        # TODO: Call the parent class constructor and initialize additional attributes
        # HINT: Use super().__init__() to call parent constructor
        # WRITE IMPLEMENTATION HERE
        pass
    
    @property
    def toy_preference(self):
        """Get the toy preference."""
        # TODO: Return the toy_preference
        # WRITE IMPLEMENTATION HERE
        pass
    
    def display_info(self):
        """
        Display small dog information.
        
        Returns:
            str: Formatted string with small dog information
        """
        # TODO: Override the display_info method to include small dog-specific information
        # HINT: Use super().display_info() to get basic dog information
        # WRITE IMPLEMENTATION HERE
        pass


class LargeDog(Dog):
    """Class representing a large dog, inherits from Dog."""
    
    def __init__(self, dog_id, name, breed, age, weight, is_checked_in=False, exercise_needs="Medium"):
        """
        Initialize a LargeDog object.
        
        Args:
            dog_id: Unique identifier for the dog
            name: Name of the dog
            breed: Breed of the dog
            age: Age of the dog in years
            weight: Weight of the dog in pounds
            is_checked_in: Whether the dog is currently checked in
            exercise_needs: Exercise requirements (Low/Medium/High)
        """
        # TODO: Call the parent class constructor and initialize additional attributes
        # HINT: Use super().__init__() to call parent constructor
        # WRITE IMPLEMENTATION HERE
        pass
    
    @property
    def exercise_needs(self):
        """Get the exercise needs."""
        # TODO: Return the exercise_needs
        # WRITE IMPLEMENTATION HERE
        pass
    
    def display_info(self):
        """
        Display large dog information.
        
        Returns:
            str: Formatted string with large dog information
        """
        # TODO: Override the display_info method to include large dog-specific information
        # HINT: Use super().display_info() to get basic dog information
        # WRITE IMPLEMENTATION HERE
        pass


class Owner:
    """Class representing a dog owner."""
    
    def __init__(self, owner_id, name, email, phone, dogs_registered=None):
        """
        Initialize an Owner object.
        
        Args:
            owner_id: Unique identifier for the owner
            name: Name of the owner
            email: Email address of the owner
            phone: Phone number of the owner (format: ###-###-####)
            dogs_registered: List of dogs registered to this owner
        """
        # Validate email format
        if not '@' in email or not '.' in email.split('@')[1]:
            raise ValueError("Invalid email format")
        
        # Validate phone format
        if not self.__is_valid_phone(phone):
            raise ValueError("Invalid phone format (should be ###-###-####)")
            
        # TODO: Initialize all attributes
        # HINT: Handle default value for dogs_registered
        # WRITE IMPLEMENTATION HERE
        pass
    
    def __is_valid_phone(self, phone):
        """
        Validate phone number format.
        
        Args:
            phone: Phone number to validate
            
        Returns:
            bool: True if valid format, False otherwise
        """
        # Check if phone is in format ###-###-####
        parts = phone.split('-')
        if len(parts) != 3:
            return False
        if len(parts[0]) != 3 or len(parts[1]) != 3 or len(parts[2]) != 4:
            return False
        for part in parts:
            if not part.isdigit():
                return False
        return True
    
    @property
    def owner_id(self):
        """Get the owner ID."""
        # TODO: Return the owner_id
        # WRITE IMPLEMENTATION HERE
        pass
    
    @property
    def name(self):
        """Get the owner name."""
        # TODO: Return the name
        # WRITE IMPLEMENTATION HERE
        pass
    
    @property
    def email(self):
        """Get the owner email."""
        # TODO: Return the email
        # WRITE IMPLEMENTATION HERE
        pass
    
    @property
    def phone(self):
        """Get the owner phone."""
        # TODO: Return the phone
        # WRITE IMPLEMENTATION HERE
        pass
    
    @property
    def dogs_registered(self):
        """Get the list of registered dogs."""
        # TODO: Return a copy of the dogs_registered list
        # HINT: Use the copy() method to avoid returning a reference to the original list
        # WRITE IMPLEMENTATION HERE
        pass
    
    def register_dog(self, dog):
        """
        Register a dog to this owner.
        
        Args:
            dog: Dog object to register
            
        Returns:
            bool: True if registration successful, False otherwise
        """
        # TODO: Implement dog registration logic
        # HINT: Check if dog is already registered
        # WRITE IMPLEMENTATION HERE
        pass
    
    def pickup_dog(self, dog):
        """
        Pick up a dog from daycare.
        
        Args:
            dog: Dog object to pick up
            
        Returns:
            bool: True if pickup successful, False otherwise
        """
        # TODO: Implement dog pickup logic
        # HINT: Check if dog is registered to this owner and is checked in
        # HINT: Use dog.check_out() method
        # WRITE IMPLEMENTATION HERE
        pass
    
    def display_info(self):
        """
        Display owner information.
        
        Returns:
            str: Formatted string with owner information
        """
        # TODO: Return formatted string with owner information
        # HINT: Include owner_id, name, email, phone, and number of dogs registered
        # WRITE IMPLEMENTATION HERE
        pass


class Daycare:
    """Class representing a dog daycare."""
    
    dog_count = 0  # Class variable to track total dogs
    owner_count = 0  # Class variable to track total owners
    
    def __init__(self, name, address):
        """
        Initialize a Daycare object.
        
        Args:
            name: Name of the daycare
            address: Address of the daycare
        """
        # TODO: Initialize all attributes
        # HINT: Create dictionaries to store dogs and owners
        # HINT: Create list of available activities
        # WRITE IMPLEMENTATION HERE
        pass
    
    @property
    def name(self):
        """Get the daycare name."""
        # TODO: Return the name
        # WRITE IMPLEMENTATION HERE
        pass
    
    @property
    def address(self):
        """Get the daycare address."""
        # TODO: Return the address
        # WRITE IMPLEMENTATION HERE
        pass
    
    @property
    def available_activities(self):
        """Get the list of available activities."""
        # TODO: Return a copy of the available_activities list
        # WRITE IMPLEMENTATION HERE
        pass
    
    @staticmethod
    def get_dog_count():
        """
        Get the total number of dogs.
        
        Returns:
            int: Total number of dogs
        """
        # TODO: Return the dog_count class variable
        # WRITE IMPLEMENTATION HERE
        pass
    
    @staticmethod
    def get_owner_count():
        """
        Get the total number of owners.
        
        Returns:
            int: Total number of owners
        """
        # TODO: Return the owner_count class variable
        # WRITE IMPLEMENTATION HERE
        pass
    
    def add_dog(self, dog):
        """
        Add a dog to the daycare.
        
        Args:
            dog: Dog object to add
            
        Returns:
            bool: True if addition successful, False otherwise
        """
        # TODO: Implement add dog logic
        # HINT: Check if dog already exists before adding
        # HINT: Increment dog_count class variable
        # WRITE IMPLEMENTATION HERE
        pass
    
    def add_owner(self, owner):
        """
        Add an owner to the daycare.
        
        Args:
            owner: Owner object to add
            
        Returns:
            bool: True if addition successful, False otherwise
        """
        # TODO: Implement add owner logic
        # HINT: Check if owner already exists before adding
        # HINT: Increment owner_count class variable
        # WRITE IMPLEMENTATION HERE
        pass
    
    def check_in_dog(self, dog_id, owner_id):
        """
        Check in a dog to the daycare.
        
        Args:
            dog_id: ID of the dog to check in
            owner_id: ID of the owner checking in the dog
            
        Returns:
            bool: True if check-in successful, False otherwise
        """
        # TODO: Implement check-in logic
        # HINT: Check if dog and owner exist
        # HINT: Check if dog is registered to owner
        # HINT: Use dog.check_in() method
        # WRITE IMPLEMENTATION HERE
        pass
    
    def check_out_dog(self, dog_id, owner_id):
        """
        Check out a dog from the daycare.
        
        Args:
            dog_id: ID of the dog to check out
            owner_id: ID of the owner checking out the dog
            
        Returns:
            bool: True if check-out successful, False otherwise
        """
        # TODO: Implement check-out logic
        # HINT: Check if dog and owner exist
        # HINT: Check if dog is registered to owner
        # HINT: Use dog.check_out() method
        # WRITE IMPLEMENTATION HERE
        pass
    
    def get_checked_in_dogs(self):
        """
        Get all checked-in dogs.
        
        Returns:
            dict: Dictionary of checked-in dogs
        """
        # TODO: Return a dictionary of all checked-in dogs
        # HINT: Use dictionary comprehension
        # WRITE IMPLEMENTATION HERE
        pass
    
    def search_dog_by_name(self, name):
        """
        Search for dogs by name.
        
        Args:
            name: Name to search for
            
        Returns:
            dict: Dictionary of matching dogs
        """
        # Check for None
        if name is None:
            raise ValueError("Search name cannot be None")
            
        # TODO: Return a dictionary of dogs with matching names
        # HINT: Use dictionary comprehension and case-insensitive search
        # WRITE IMPLEMENTATION HERE
        pass
    
    def search_dog_by_breed(self, breed):
        """
        Search for dogs by breed.
        
        Args:
            breed: Breed to search for
            
        Returns:
            dict: Dictionary of matching dogs
        """
        # Check for None
        if breed is None:
            raise ValueError("Search breed cannot be None")
            
        # TODO: Return a dictionary of dogs with matching breeds
        # HINT: Use dictionary comprehension and case-insensitive search
        # WRITE IMPLEMENTATION HERE
        pass
    
    def get_dog(self, dog_id):
        """
        Get a dog by ID.
        
        Args:
            dog_id: ID of the dog to get
            
        Returns:
            Dog: Dog object if found, None otherwise
        """
        # TODO: Return the dog with the given ID or None if not found
        # WRITE IMPLEMENTATION HERE
        pass
    
    def get_owner(self, owner_id):
        """
        Get an owner by ID.
        
        Args:
            owner_id: ID of the owner to get
            
        Returns:
            Owner: Owner object if found, None otherwise
        """
        # TODO: Return the owner with the given ID or None if not found
        # WRITE IMPLEMENTATION HERE
        pass
    
    def get_all_dogs(self):
        """
        Get all dogs.
        
        Returns:
            dict: Dictionary of all dogs
        """
        # TODO: Return a copy of the dogs dictionary
        # WRITE IMPLEMENTATION HERE
        pass
    
    def get_all_owners(self):
        """
        Get all owners.
        
        Returns:
            dict: Dictionary of all owners
        """
        # TODO: Return a copy of the owners dictionary
        # WRITE IMPLEMENTATION HERE
        pass


def main():
    """Main function to run the dog daycare management system."""
    # TODO: Implement the main function
    # HINT: Create a daycare and implement a menu-driven interface with the following options:
    # 1. Add New Dog
    # 2. Add New Owner
    # 3. Check-in Dog
    # 4. Check-out Dog
    # 5. Display All Dogs
    # 6. Display All Owners
    # 7. Search for Dogs
    # 0. Exit
    # WRITE IMPLEMENTATION HERE
    pass


# DO NOT MODIFY THIS CODE
if __name__ == "__main__":
    main()