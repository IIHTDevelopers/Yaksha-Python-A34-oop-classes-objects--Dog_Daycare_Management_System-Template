import pytest
import datetime
from test.TestUtils import TestUtils
from dog_daycare_management_system import Dog, SmallDog, LargeDog, Owner, Daycare

class TestBoundary:
    """Test cases for boundary conditions in the dog daycare system."""
    
    def test_system_boundaries(self):
        """Test all boundary conditions for the dog daycare management system."""
        try:
            # Dog age and weight boundary tests
            dog1 = Dog("D001", "Young Dog", "Mixed Breed", 1, 5.0)
            assert dog1.age == 1
            assert dog1.weight == 5.0
            
            dog2 = Dog("D002", "Heavy Dog", "Saint Bernard", 5, 150.0)
            assert dog2.weight == 150.0
            
            dog3 = Dog("D003", "Old Dog", "Golden Retriever", 15, 65.0)
            assert dog3.age == 15
            
            # Owner registration limit tests
            owner = Owner("O001", "Max Owner", "max@example.com", "555-123-4567")
            dogs = [
                Dog(f"D00{i}", f"Dog {i}", "Mixed Breed", 3, 25.0)
                for i in range(4, 8)
            ]
            
            # Register dogs to owner
            for i in range(4):
                assert owner.register_dog(dogs[i]) == True
            
            # Test re-registering same dog
            assert owner.register_dog(dogs[0]) == False
            
            # Test dogs_registered list immutability
            predefined_dogs = ["D101", "D102"]
            owner2 = Owner("O101", "Pre Owner", "pre@example.com", "555-987-6543", predefined_dogs)
            assert owner2.dogs_registered == predefined_dogs
            assert owner2.dogs_registered is not predefined_dogs  # Should be a copy
            
            # Test modifying the returned list doesn't affect original
            registered_copy = owner2.dogs_registered
            registered_copy.append("D103")
            assert "D103" not in owner2.dogs_registered
            
            # Empty daycare tests
            daycare = Daycare("Empty Daycare", "Empty St")
            assert len(daycare.get_all_dogs()) == 0
            assert len(daycare.get_checked_in_dogs()) == 0
            assert daycare.search_dog_by_name("any") == {}
            assert daycare.search_dog_by_breed("any") == {}
            assert daycare.get_dog("D001") is None
            assert len(daycare.get_all_owners()) == 0
            assert daycare.get_owner("O001") is None
            
            # Daycare check-in boundary tests
            test_daycare = Daycare("Test Daycare", "Test St")
            dog = Dog("D001", "Test Dog", "Beagle", 3, 20.0)
            owner = Owner("O001", "Test Owner", "test@example.com", "555-123-4567")
            
            test_daycare.add_dog(dog)
            test_daycare.add_owner(owner)
            
            # Register dog to owner
            owner.register_dog(dog)
            
            # Test various input combinations
            assert test_daycare.check_in_dog("INVALID", "O001") is False
            assert test_daycare.check_in_dog("D001", "INVALID") is False
            assert test_daycare.check_in_dog("INVALID", "INVALID") is False
            
            # Valid check-in and repeat attempt
            assert test_daycare.check_in_dog("D001", "O001") is True
            assert test_daycare.check_in_dog("D001", "O001") is False  # Already checked in
            
            # Check-out tests
            assert test_daycare.check_out_dog("D001", "O001") is True
            assert test_daycare.check_out_dog("D001", "O001") is False  # Already checked out
            
            TestUtils.yakshaAssert("test_system_boundaries", True, "boundary")
        except Exception as e:
            TestUtils.yakshaAssert("test_system_boundaries", False, "boundary")
            raise e