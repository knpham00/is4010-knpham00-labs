def calculate_average_age(users: list[dict]) -> float:
    """
    Calculate the average age of users with valid integer ages.

    Parameters
    ----------
    users : list[dict]
        A list of user dictionaries, where each dictionary may contain an "age" key.

    Returns
    -------
    float
        The average age of valid users, or 0.0 if an error occurs or no valid ages exist.
    """
    total_age = 0
    age_count = 0
    
    try:
        if users is None:
            raise TypeError("Input 'users' cannot be None")

        for user in users:
            # Handle case where user might not be a dict
            if not isinstance(user, dict):
                continue
                
            age = user.get("age")
            if isinstance(age, int):
                total_age += age
                age_count += 1
        
        # Explicitly handle division to demonstrate exception handling
        average = total_age / age_count
        return average

    except ZeroDivisionError:
        print("Error: Cannot calculate average age. No valid user ages found.")
        return 0.0
    except TypeError as e:
        print(f"Error: Invalid input data. {e}")
        return 0.0


def get_active_user_emails(users: list[dict]) -> list[str]:
    """
    Retrieve a list of emails for active users.

    Parameters
    ----------
    users : list[dict]
        A list of user dictionaries.

    Returns
    -------
    list[str]
        A list of email addresses, or an empty list if an error occurs.
    """
    active_emails = []
    
    try:
        for user in users:
            # This would raise AttributeError if 'user' is None/not a dict 
            # and we tried to access properties directly, but .get() is safe.
            # However, if 'users' is not iterable, a TypeError is raised by the loop.
            if user.get("is_active") and user.get("email"):
                active_emails.append(user["email"])
                
    except TypeError:
        print("Error: Input 'users' must be an iterable list of dictionaries.")
        return []
    except AttributeError:
        print("Error: Found malformed user data in the list.")
        return []
            
    return active_emails


def main():
    """
    Main entry point for the script.
    """
    users = [
        {"name": "alice", "age": 30, "is_active": True, "email": "alice@example.com"},
        {"name": "bob", "age": 25, "is_active": False},
        {"name": "charlie", "age": 35, "is_active": True, "email": "charlie@example.com"},
        {"name": "david", "age": "unknown", "is_active": False}
    ]

    average_age = calculate_average_age(users)
    print(f"Average user age: {average_age:.2f}")

    active_user_emails = get_active_user_emails(users)
    print(f"Active user emails: {active_user_emails}")

    # Test error handling
    print("\n--- Testing Error Handling ---")
    calculate_average_age([]) # Should print error about no valid ages
    get_active_user_emails(None) # Should print error about iterable list


if __name__ == "__main__":
    main()