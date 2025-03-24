import pytest
import datetime
from test.TestUtils import TestUtils
from dog_daycare_management_system import Dog, SmallDog, LargeDog, Owner, Daycare

class TestExceptional:
    """Test cases for exceptional conditions in the dog daycare system."""
    
    def test_exception_handling(self):
        """Test all exception handling across the dog daycare management system."""
        try:
            # Dog validation exceptions
            try:
                Dog("D001", "Invalid Age", "Breed", -1, 20.0)
                assert False, "Negative age should be rejected"
            except ValueError:
                pass  # Expected behavior
                
            try:
                Dog("D002", "Invalid Age", "Breed", 0, 20.0)
                assert False, "Zero age should be rejected"
            except ValueError:
                pass  # Expected behavior
                
            try:
                Dog("D003", "Invalid Weight", "Breed", 3, -5.0)
                assert False, "Negative weight should be rejected"
            except ValueError:
                pass  # Expected behavior
                
            try:
                Dog("D004", "Invalid Weight", "Breed", 3, 0)
                assert False, "Zero weight should be rejected"
            except ValueError:
                pass  # Expected behavior
                
            try:
                Dog("D005", "Invalid Age Type", "Breed", "3", 20.0)
                assert False, "Non-integer age should be rejected"
            except ValueError:
                pass  # Expected behavior
                
            try:
                Dog("D006", "Invalid Weight Type", "Breed", 3, "20.0")
                assert False, "Non-numeric weight should be rejected"
            except ValueError:
                pass  # Expected behavior
            
            # Owner validation exceptions
            for invalid_email in ["invalidemail.com", "invalid@"]:
                try:
                    Owner("O001", "Invalid Email", invalid_email, "555-123-4567")
                    assert False, f"Invalid email '{invalid_email}' should be rejected"
                except ValueError:
                    pass  # Expected behavior
                
            for invalid_phone in ["1234567890", "555", "5551234", "abc-def-ghij"]:
                try:
                    Owner("O001", "Invalid Phone", "valid@example.com", invalid_phone)
                    assert False, f"Invalid phone '{invalid_phone}' should be rejected"
                except ValueError:
                    pass  # Expected behavior
                
            # Daycare search validation
            daycare = Daycare("Test Daycare", "Test St")
            
            try:
                daycare.search_dog_by_name(None)
                assert False, "Search with None name should be rejected"
            except ValueError:
                pass  # Expected behavior
                
            try:
                daycare.search_dog_by_breed(None)
                assert False, "Search with None breed should be rejected"
            except ValueError:
                pass  # Expected behavior
                
            # Empty string searches (should not raise exceptions)
            result = daycare.search_dog_by_name("")
            assert result == {}, "Search with empty name should return empty dict"
            
            result = daycare.search_dog_by_breed("")
            assert result == {}, "Search with empty breed should return empty dict"
            
            # Dog check-in operation exceptions
            checked_in_dog = Dog("D001", "Already Checked In", "Breed", 3, 20.0, True)
            owner = Owner("O001", "Test Owner", "test@example.com", "555-123-4567")
            
            result = checked_in_dog.check_in()
            assert result == False, "Checking in already checked-in dog should fail"
            
            # Dog check-out operation exceptions
            checked_out_dog = Dog("D002", "Not Checked In", "Breed", 3, 20.0, False)
            
            result = checked_out_dog.check_out()
            assert result == False, "Checking out not checked-in dog should fail"
            
            # Daycare check-in/out exceptions
            test_daycare = Daycare("Operations Daycare", "Operations St")
            
            # Check-in with missing dog
            result = test_daycare.check_in_dog("NONEXISTENT", "O001")
            assert result is False, "Check-in with non-existent dog should return False"
            
            # Check-in with missing owner
            dog = Dog("D011", "Exists", "Breed", 3, 20.0)
            test_daycare.add_dog(dog)
            
            result = test_daycare.check_in_dog("D011", "NONEXISTENT")
            assert result is False, "Check-in with non-existent owner should return False"
            
            # Check-in with dog not registered to owner
            owner = Owner("O011", "Exists", "exists@example.com", "555-123-4567")
            test_daycare.add_owner(owner)
            
            result = test_daycare.check_in_dog("D011", "O011")
            assert result is False, "Check-in with dog not registered to owner should return False"
            
            # Register dog and check in
            owner.register_dog(dog)
            test_daycare.check_in_dog("D011", "O011")
            
            # Try to check in again
            result = test_daycare.check_in_dog("D011", "O011")
            assert result is False, "Check-in of already checked-in dog should return False"
                
            TestUtils.yakshaAssert("test_exception_handling", True, "exceptional")
        except Exception as e:
            TestUtils.yakshaAssert("test_exception_handling", False, "exceptional")
            raise e