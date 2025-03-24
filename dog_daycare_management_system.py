"""
Dog Daycare Management System
"""

import datetime


class Dog:
    def __init__(self, dog_id, name, breed, age, weight, is_checked_in=False):
        # Basic validation
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Age must be a positive integer")
        
        if not isinstance(weight, (int, float)) or weight <= 0:
            raise ValueError("Weight must be a positive number")
            
        self.__dog_id = dog_id
        self.__name = name
        self.__breed = breed
        self.__age = age
        self.__weight = weight
        self.__is_checked_in = is_checked_in
    
    @property
    def dog_id(self): return self.__dog_id
    
    @property
    def name(self): return self.__name
    
    @property
    def breed(self): return self.__breed
    
    @property
    def age(self): return self.__age
    
    @property
    def weight(self): return self.__weight
    
    @property
    def is_checked_in(self): return self.__is_checked_in
    
    @is_checked_in.setter
    def is_checked_in(self, value): self.__is_checked_in = value
    
    def check_in(self):
        if self.__is_checked_in: return False
        self.__is_checked_in = True
        return True
    
    def check_out(self):
        if not self.__is_checked_in: return False
        self.__is_checked_in = False
        return True
    
    def display_info(self):
        status = "Checked In" if self.__is_checked_in else "Not Checked In"
        return f"{self.__dog_id} | {self.__name} ({self.__breed}) | {self.__age} years | {self.__weight} lbs | Status: {status}"


class SmallDog(Dog):
    def __init__(self, dog_id, name, breed, age, weight, is_checked_in=False, toy_preference="None"):
        super().__init__(dog_id, name, breed, age, weight, is_checked_in)
        self.__toy_preference = toy_preference
    
    @property
    def toy_preference(self): return self.__toy_preference
    
    def display_info(self):
        basic_info = super().display_info()
        return f"{basic_info} | Toy Preference: {self.__toy_preference}"


class LargeDog(Dog):
    def __init__(self, dog_id, name, breed, age, weight, is_checked_in=False, exercise_needs="Medium"):
        super().__init__(dog_id, name, breed, age, weight, is_checked_in)
        self.__exercise_needs = exercise_needs
    
    @property
    def exercise_needs(self): return self.__exercise_needs
    
    def display_info(self):
        basic_info = super().display_info()
        return f"{basic_info} | Exercise Needs: {self.__exercise_needs}"


class Owner:
    def __init__(self, owner_id, name, email, phone, dogs_registered=None):
        # Simple email validation
        if not '@' in email or not '.' in email.split('@')[1]:
            raise ValueError("Invalid email format")
        
        # Simple phone validation
        if not self.__is_valid_phone(phone):
            raise ValueError("Invalid phone format (should be ###-###-####)")
            
        self.__owner_id = owner_id
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__dogs_registered = dogs_registered if dogs_registered is not None else []
    
    def __is_valid_phone(self, phone):
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
    def owner_id(self): return self.__owner_id
    
    @property
    def name(self): return self.__name
    
    @property
    def email(self): return self.__email
    
    @property
    def phone(self): return self.__phone
    
    @property
    def dogs_registered(self): return self.__dogs_registered.copy()
    
    def register_dog(self, dog):
        if dog.dog_id in self.__dogs_registered:
            print(f"Dog '{dog.name}' is already registered")
            return False
        
        self.__dogs_registered.append(dog.dog_id)
        return True
    
    def pickup_dog(self, dog):
        if dog.dog_id not in self.__dogs_registered:
            print(f"Dog '{dog.name}' is not registered to this owner")
            return False
        
        if not dog.is_checked_in:
            print(f"Dog '{dog.name}' is not checked in")
            return False
        
        if dog.check_out():
            return True
        return False
    
    def display_info(self):
        return f"{self.__owner_id} | {self.__name} | {self.__email} | {self.__phone} | Dogs registered: {len(self.__dogs_registered)}"


class Daycare:
    dog_count = 0
    owner_count = 0
    
    def __init__(self, name, address):
        self.__name = name
        self.__address = address
        self.__dogs = {}
        self.__owners = {}
        self.__available_activities = ["Play Time", "Walking", "Training", "Socialization", "Resting"]
    
    @property
    def name(self): return self.__name
    
    @property
    def address(self): return self.__address
    
    @property
    def available_activities(self): return self.__available_activities.copy()
    
    @staticmethod
    def get_dog_count(): return Daycare.dog_count
    
    @staticmethod
    def get_owner_count(): return Daycare.owner_count
    
    def add_dog(self, dog):
        if dog.dog_id in self.__dogs: return False
        
        self.__dogs[dog.dog_id] = dog
        Daycare.dog_count += 1
        return True
    
    def add_owner(self, owner):
        if owner.owner_id in self.__owners: return False
        
        self.__owners[owner.owner_id] = owner
        Daycare.owner_count += 1
        return True
    
    def check_in_dog(self, dog_id, owner_id):
        if dog_id not in self.__dogs:
            print(f"Dog with ID {dog_id} not found")
            return False
        
        if owner_id not in self.__owners:
            print(f"Owner with ID {owner_id} not found")
            return False
        
        dog = self.__dogs[dog_id]
        owner = self.__owners[owner_id]
        
        if dog.is_checked_in:
            print(f"Dog '{dog.name}' is already checked in")
            return False
            
        if dog_id not in owner.dogs_registered:
            print(f"Dog '{dog.name}' is not registered to this owner")
            return False
        
        return dog.check_in()
    
    def check_out_dog(self, dog_id, owner_id):
        if dog_id not in self.__dogs:
            print(f"Dog with ID {dog_id} not found")
            return False
        
        if owner_id not in self.__owners:
            print(f"Owner with ID {owner_id} not found")
            return False
        
        dog = self.__dogs[dog_id]
        owner = self.__owners[owner_id]
        
        if not dog.is_checked_in:
            print(f"Dog '{dog.name}' is not checked in")
            return False
            
        if dog_id not in owner.dogs_registered:
            print(f"Dog '{dog.name}' is not registered to this owner")
            return False
        
        return dog.check_out()
    
    def get_checked_in_dogs(self):
        return {dog_id: dog for dog_id, dog in self.__dogs.items() if dog.is_checked_in}
    
    def search_dog_by_name(self, name):
        if name is None:
            raise ValueError("Search name cannot be None")
            
        name = name.lower()
        return {dog_id: dog for dog_id, dog in self.__dogs.items() 
                if name in dog.name.lower()}
    
    def search_dog_by_breed(self, breed):
        if breed is None:
            raise ValueError("Search breed cannot be None")
        
        breed = breed.lower()
        return {dog_id: dog for dog_id, dog in self.__dogs.items() 
                if breed in dog.breed.lower()}
    
    def get_dog(self, dog_id): 
        return self.__dogs.get(dog_id)
    
    def get_owner(self, owner_id): 
        return self.__owners.get(owner_id)
    
    def get_all_dogs(self): 
        return self.__dogs.copy()
    
    def get_all_owners(self): 
        return self.__owners.copy()


def main():
    daycare = Daycare("Paws & Play", "456 Park Ave, Dogtown")
    
    # Add initial dogs
    daycare.add_dog(SmallDog("D001", "Daisy", "Yorkshire Terrier", 5, 7.5, False, "Plush toys"))
    daycare.add_dog(LargeDog("D002", "Max", "German Shepherd", 2, 75.0, False, "High"))
    daycare.add_dog(SmallDog("D003", "Bella", "Beagle", 3, 25.0, False, "Tennis balls"))
    daycare.add_dog(LargeDog("D004", "Rocky", "Labrador Retriever", 4, 70.0, False, "Medium"))
    
    # Add initial owners
    owner1 = Owner("O001", "John Smith", "john@example.com", "555-123-4567")
    owner1.register_dog(daycare.get_dog("D001"))
    owner1.register_dog(daycare.get_dog("D003"))
    
    owner2 = Owner("O002", "Jane Doe", "jane@example.com", "555-987-6543")
    owner2.register_dog(daycare.get_dog("D002"))
    owner2.register_dog(daycare.get_dog("D004"))
    
    daycare.add_owner(owner1)
    daycare.add_owner(owner2)
    
    while True:
        print("\n===== DOG DAYCARE MANAGEMENT SYSTEM =====")
        print(f"Daycare Name: {daycare.name}")
        print(f"Address: {daycare.address}")
        print(f"Total Dogs: {Daycare.get_dog_count()}")
        print(f"Total Owners: {Daycare.get_owner_count()}")
        print("\nMenu:")
        print("1. Add New Dog")
        print("2. Add New Owner")
        print("3. Check-in Dog")
        print("4. Check-out Dog")
        print("5. Display All Dogs")
        print("6. Display All Owners")
        print("7. Search for Dogs")
        print("0. Exit")
        
        try:
            choice = int(input("\nEnter your choice (0-7): "))
            
            if choice == 1:
                # Add new dog
                dog_id = input("Enter dog ID: ")
                name = input("Enter name: ")
                breed = input("Enter breed: ")
                
                try:
                    age = int(input("Enter age (years): "))
                    weight = float(input("Enter weight (lbs): "))
                except ValueError:
                    print("Invalid input for age or weight.")
                    continue
                
                dog_type = input("Enter dog type (S for Small, L for Large): ").upper()
                
                if dog_type == 'S':
                    toy_preference = input("Enter toy preference: ")
                    dog = SmallDog(dog_id, name, breed, age, weight, False, toy_preference)
                elif dog_type == 'L':
                    exercise_needs = input("Enter exercise needs (Low/Medium/High): ")
                    dog = LargeDog(dog_id, name, breed, age, weight, False, exercise_needs)
                else:
                    print("Invalid dog type. Adding as base Dog type.")
                    dog = Dog(dog_id, name, breed, age, weight)
                
                if daycare.add_dog(dog):
                    print(f"Dog {dog_id} added successfully.")
                else:
                    print(f"Dog with ID {dog_id} already exists.")
            
            elif choice == 2:
                # Add new owner
                owner_id = input("Enter owner ID: ")
                name = input("Enter name: ")
                email = input("Enter email: ")
                phone = input("Enter phone (###-###-####): ")
                
                try:
                    owner = Owner(owner_id, name, email, phone)
                    
                    # Register dogs to owner
                    register_dogs = input("Do you want to register dogs to this owner? (y/n): ").lower()
                    if register_dogs == 'y':
                        print("\nAvailable Dogs:")
                        all_dogs = daycare.get_all_dogs()
                        for dog in all_dogs.values():
                            print(dog.display_info())
                        
                        dog_ids = input("Enter dog IDs to register (comma-separated): ").split(',')
                        for dog_id in dog_ids:
                            dog_id = dog_id.strip()
                            dog = daycare.get_dog(dog_id)
                            if dog:
                                owner.register_dog(dog)
                                print(f"Dog {dog_id} registered to owner {owner_id}.")
                            else:
                                print(f"Dog with ID {dog_id} not found.")
                    
                    if daycare.add_owner(owner):
                        print(f"Owner {owner_id} added successfully.")
                    else:
                        print(f"Owner with ID {owner_id} already exists.")
                except ValueError as e:
                    print(f"Invalid owner data: {e}")
            
            elif choice == 3:
                # Check-in dog
                dog_id = input("Enter dog ID: ")
                owner_id = input("Enter owner ID: ")
                
                if daycare.check_in_dog(dog_id, owner_id):
                    print(f"Dog {dog_id} checked in successfully by owner {owner_id}.")
                else:
                    print("Check-in failed.")
            
            elif choice == 4:
                # Check-out dog
                dog_id = input("Enter dog ID: ")
                owner_id = input("Enter owner ID: ")
                
                if daycare.check_out_dog(dog_id, owner_id):
                    print(f"Dog {dog_id} checked out successfully by owner {owner_id}.")
                else:
                    print("Check-out failed.")
            
            elif choice == 5:
                # Display all dogs
                dogs = daycare.get_all_dogs()
                
                if dogs:
                    print("\nAll Dogs:")
                    for dog in dogs.values():
                        print(dog.display_info())
                else:
                    print("No dogs found.")
            
            elif choice == 6:
                # Display all owners
                owners = daycare.get_all_owners()
                
                if owners:
                    print("\nAll Owners:")
                    for owner in owners.values():
                        print(owner.display_info())
                else:
                    print("No owners found.")
            
            elif choice == 7:
                # Search for dogs
                print("\nSearch Options:")
                print("1. Search by Name")
                print("2. Search by Breed")
                print("3. Show Checked-in Dogs")
                
                search_choice = int(input("Enter search option (1-3): "))
                
                if search_choice == 1:
                    name = input("Enter name keyword: ")
                    dogs = daycare.search_dog_by_name(name)
                elif search_choice == 2:
                    breed = input("Enter breed keyword: ")
                    dogs = daycare.search_dog_by_breed(breed)
                elif search_choice == 3:
                    dogs = daycare.get_checked_in_dogs()
                else:
                    print("Invalid search option.")
                    continue
                
                if dogs:
                    print("\nSearch Results:")
                    for dog in dogs.values():
                        print(dog.display_info())
                else:
                    print("No matching dogs found.")
            
            elif choice == 0:
                # Exit
                print("Thank you for using the Dog Daycare Management System.")
                break
            
            else:
                print("Invalid choice. Please enter a number between 0 and 7.")
        
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()