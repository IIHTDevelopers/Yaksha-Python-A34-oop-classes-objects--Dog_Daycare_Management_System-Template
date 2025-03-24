import pytest
from test.TestUtils import TestUtils
from dog_daycare_management_system import Dog, SmallDog, LargeDog, Owner, Daycare
import datetime

class TestFunctional:
    """Test cases for functional requirements of the dog daycare system."""
    
    def test_dog_functionality(self):
        """Test dog creation, properties, check-in and check-out functionality."""
        try:
            # Test basic dog creation and property access
            dog = Dog("D001", "Test Dog", "Beagle", 3, 25.5, False)
            assert dog.dog_id == "D001"
            assert dog.name == "Test Dog"
            assert dog.breed == "Beagle"
            assert dog.age == 3
            assert dog.weight == 25.5
            assert dog.is_checked_in == False
            
            # Test check-in
            assert dog.check_in() == True
            assert dog.is_checked_in == True
            
            # Test check-out
            assert dog.check_out() == True
            assert dog.is_checked_in == False
            
            # Test failed check-in
            dog.check_in()
            assert dog.check_in() == False  # Already checked in
            
            TestUtils.yakshaAssert("test_dog_functionality", True, "functional")
        except Exception as e:
            TestUtils.yakshaAssert("test_dog_functionality", False, "functional")
            raise e
    
    def test_dog_inheritance(self):
        """Test dog inheritance for small and large dogs."""
        try:
            # Test small dog
            small_dog = SmallDog("D003", "Tiny", "Chihuahua", 2, 5.5, False, "Squeaky toys")
            assert small_dog.dog_id == "D003"
            assert small_dog.name == "Tiny"
            assert small_dog.toy_preference == "Squeaky toys"
            assert "Squeaky toys" in small_dog.display_info()
            
            # Test large dog
            large_dog = LargeDog("D004", "Rex", "German Shepherd", 4, 85.0, False, "High")
            assert large_dog.dog_id == "D004"
            assert large_dog.name == "Rex"
            assert large_dog.exercise_needs == "High"
            assert "High" in large_dog.display_info()
            
            TestUtils.yakshaAssert("test_dog_inheritance", True, "functional")
        except Exception as e:
            TestUtils.yakshaAssert("test_dog_inheritance", False, "functional")
            raise e
    
    def test_owner_functionality(self):
        """Test owner creation, properties, and dog registration/pickup."""
        try:
            # Test owner creation
            owner = Owner("O001", "Test Owner", "test@example.com", "555-123-4567")
            assert owner.owner_id == "O001"
            assert owner.name == "Test Owner"
            assert owner.email == "test@example.com"
            assert owner.phone == "555-123-4567"
            assert len(owner.dogs_registered) == 0
            
            # Test dog registration
            dog = Dog("D005", "Buddy", "Golden Retriever", 3, 65.0, False)
            result = owner.register_dog(dog)
            assert result == True
            assert dog.dog_id in owner.dogs_registered
            
            # Test dog pickup (check-out)
            dog.check_in()  # First check in the dog
            result = owner.pickup_dog(dog)
            assert result == True
            assert dog.is_checked_in == False
            
            TestUtils.yakshaAssert("test_owner_functionality", True, "functional")
        except Exception as e:
            TestUtils.yakshaAssert("test_owner_functionality", False, "functional")
            raise e
    
    def test_daycare_creation_and_adding(self):
        """Test daycare creation, properties, and adding dogs and owners."""
        try:
            # Test daycare creation
            daycare = Daycare("Test Daycare", "123 Test St")
            assert daycare.name == "Test Daycare"
            assert daycare.address == "123 Test St"
            assert len(daycare.available_activities) > 0
            
            # Test adding dogs
            initial_dog_count = Daycare.dog_count
            dog1 = Dog("D006", "Dog 1", "Breed 1", 2, 15.0)
            dog2 = Dog("D007", "Dog 2", "Breed 2", 3, 25.0)
            
            assert daycare.add_dog(dog1) == True
            assert daycare.add_dog(dog2) == True
            assert Daycare.dog_count == initial_dog_count + 2
            assert daycare.add_dog(dog1) == False  # Test duplicate addition
            assert daycare.get_dog("D006") == dog1
            assert daycare.get_dog("D007") == dog2
            
            # Test adding owners
            initial_owner_count = Daycare.owner_count
            owner1 = Owner("O003", "Owner 1", "owner1@example.com", "555-111-2222")
            owner2 = Owner("O004", "Owner 2", "owner2@example.com", "555-333-4444")
            
            assert daycare.add_owner(owner1) == True
            assert daycare.add_owner(owner2) == True
            assert Daycare.owner_count == initial_owner_count + 2
            assert daycare.add_owner(owner1) == False  # Test duplicate addition
            assert daycare.get_owner("O003") == owner1
            assert daycare.get_owner("O004") == owner2
            
            TestUtils.yakshaAssert("test_daycare_creation_and_adding", True, "functional")
        except Exception as e:
            TestUtils.yakshaAssert("test_daycare_creation_and_adding", False, "functional")
            raise e
    
    def test_daycare_checkin_checkout(self):
        """Test daycare check-in and check-out process."""
        try:
            daycare = Daycare("Checkout Daycare", "Checkout St")
            dog = Dog("D008", "Checkin Dog", "Labrador", 2, 60.0)
            owner = Owner("O005", "Owner", "owner@example.com", "555-123-4567")
            
            daycare.add_dog(dog)
            daycare.add_owner(owner)
            owner.register_dog(dog)
            
            # Test check-in
            checkin_result = daycare.check_in_dog("D008", "O005")
            assert checkin_result is True
            assert dog.is_checked_in
            
            # Test check-out
            checkout_result = daycare.check_out_dog("D008", "O005")
            assert checkout_result is True
            assert not dog.is_checked_in
            
            TestUtils.yakshaAssert("test_daycare_checkin_checkout", True, "functional")
        except Exception as e:
            TestUtils.yakshaAssert("test_daycare_checkin_checkout", False, "functional")
            raise e
    
    def test_daycare_search_functions(self):
        """Test daycare search and filter functions."""
        try:
            daycare = Daycare("Search Daycare", "Search St")
            
            # Add dogs for search testing
            dogs = [
                Dog("D009", "Buddy", "Golden Retriever", 3, 65.0),
                Dog("D010", "Max", "German Shepherd", 2, 75.0, True),
                Dog("D011", "Charlie", "Golden Retriever", 4, 70.0),
                Dog("D012", "Luna", "Beagle", 2, 22.0)
            ]
            
            for dog in dogs:
                daycare.add_dog(dog)
            
            # Test search by name
            results = daycare.search_dog_by_name("a")  # Will match Max, Charlie and Luna
            assert len(results) == 3
            assert "D010" in results
            assert "D011" in results
            assert "D012" in results
            
            # Test search by breed
            results = daycare.search_dog_by_breed("retriever")
            assert len(results) == 2
            assert "D009" in results
            assert "D011" in results
            
            # Test checked-in dogs
            results = daycare.get_checked_in_dogs()
            assert len(results) == 1
            assert "D010" in results
            
            TestUtils.yakshaAssert("test_daycare_search_functions", True, "functional")
        except Exception as e:
            TestUtils.yakshaAssert("test_daycare_search_functions", False, "functional")
            raise e
            
    def test_integrated_daycare_functions(self):
        """Test integrated daycare functionality with multiple operations."""
        try:
            daycare = Daycare("Integrated Daycare", "Integration St")
            
            # Test adding different dog types
            small_dog = SmallDog("D101", "Bella", "Yorkshire Terrier", 3, 6.5, False, "Plush toys")
            large_dog = LargeDog("D102", "Rocky", "Rottweiler", 4, 90.0, False, "High")
            
            daycare.add_dog(small_dog)
            daycare.add_dog(large_dog)
            
            # Add owners
            owner1 = Owner("O101", "Regular Client", "client@example.com", "555-111-2222")
            owner2 = Owner("O102", "Frequent Client", "frequent@example.com", "555-333-4444")
            
            daycare.add_owner(owner1)
            daycare.add_owner(owner2)
            
            # Register dogs to owners
            owner1.register_dog(small_dog)
            owner2.register_dog(large_dog)
            
            # Test check-in and check-out process
            checkin_result = daycare.check_in_dog("D101", "O101")
            assert checkin_result is True
            assert small_dog.is_checked_in
            
            # Check out dog
            checkout_result = daycare.check_out_dog("D101", "O101")
            assert checkout_result is True
            assert not small_dog.is_checked_in
            
            # Test search functionality after multiple operations
            small_dog2 = SmallDog("D103", "Milo", "Pomeranian", 2, 4.5, False, "Balls")
            daycare.add_dog(small_dog2)
            owner1.register_dog(small_dog2)
            
            results = daycare.search_dog_by_breed("terrier")
            assert len(results) == 1
            assert "D101" in results
            
            # Test checked-in dogs after operations
            daycare.check_in_dog("D102", "O102")
            checked_in = daycare.get_checked_in_dogs()
            assert len(checked_in) == 1
            assert "D102" in checked_in
            
            TestUtils.yakshaAssert("test_integrated_daycare_functions", True, "functional")
        except Exception as e:
            TestUtils.yakshaAssert("test_integrated_daycare_functions", False, "functional")
            raise e