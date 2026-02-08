"""
Exercise 7: Working with JSON and Dictionaries
This exercise demonstrates how dictionaries work with JSON data.
JSON (JavaScript Object Notation) is the most common data format for APIs and data exchange.
"""

import json
from datetime import datetime


def main():
    print("Exercise 7: JSON and Dictionaries")
    print("=" * 60)
    
    # 1. Python dictionary to JSON
    print("1. Converting Dictionary to JSON:")
    print("-" * 60)
    
    person = {
        "name": "Alice Johnson",
        "age": 28,
        "email": "alice@example.com",
        "is_active": True,
        "skills": ["Python", "JavaScript", "SQL"],
        "address": {
            "street": "123 Main St",
            "city": "San Francisco",
            "zipcode": "94102"
        }
    }
    
    # Convert to JSON string
    json_string = json.dumps(person, indent=2)
    print("Python Dictionary:")
    print(person)
    print("\nJSON String:")
    print(json_string)
    print()
    
    # 2. JSON to Python dictionary
    print("2. Converting JSON to Dictionary:")
    print("-" * 60)
    
    json_data = '''
    {
        "product": "Laptop",
        "price": 1299.99,
        "in_stock": true,
        "specs": {
            "ram": "16GB",
            "storage": "512GB SSD",
            "processor": "Intel i7"
        },
        "reviews": [
            {"user": "John", "rating": 5},
            {"user": "Sarah", "rating": 4}
        ]
    }
    '''
    
    # Parse JSON string
    product_dict = json.loads(json_data)
    print("Parsed Dictionary:")
    print(product_dict)
    print(f"\nProduct name: {product_dict['product']}")
    print(f"Price: ${product_dict['price']}")
    print(f"RAM: {product_dict['specs']['ram']}")
    print()
    
    # 3. Writing JSON to file
    print("3. Writing Dictionary to JSON File:")
    print("-" * 60)
    
    inventory = {
        "electronics": {
            "laptops": {"count": 15, "brands": ["Dell", "HP", "Lenovo"]},
            "phones": {"count": 30, "brands": ["Apple", "Samsung", "Google"]}
        },
        "furniture": {
            "chairs": {"count": 50, "types": ["Office", "Dining", "Gaming"]},
            "desks": {"count": 20, "types": ["Standing", "Traditional"]}
        },
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    # Write to file
    with open('/home/claude/dictionary_exercises/inventory.json', 'w') as f:
        json.dump(inventory, f, indent=2)
    
    print("✓ Inventory saved to inventory.json")
    print()
    
    # 4. Reading JSON from file
    print("4. Reading Dictionary from JSON File:")
    print("-" * 60)
    
    # Read from file
    with open('/home/claude/dictionary_exercises/inventory.json', 'r') as f:
        loaded_inventory = json.load(f)
    
    print("✓ Loaded inventory from file")
    print(f"Categories: {list(loaded_inventory.keys())}")
    print(f"Total laptop brands: {len(loaded_inventory['electronics']['laptops']['brands'])}")
    print()
    
    # 5. Complex JSON example - API response simulation
    print("5. Simulating API Response:")
    print("-" * 60)
    
    api_response = {
        "status": "success",
        "code": 200,
        "data": {
            "users": [
                {
                    "id": 1,
                    "username": "alice123",
                    "profile": {
                        "full_name": "Alice Johnson",
                        "followers": 1250,
                        "following": 380
                    },
                    "posts": [
                        {"id": 101, "title": "My first post", "likes": 45},
                        {"id": 102, "title": "Python tips", "likes": 128}
                    ]
                },
                {
                    "id": 2,
                    "username": "bob_dev",
                    "profile": {
                        "full_name": "Bob Developer",
                        "followers": 890,
                        "following": 245
                    },
                    "posts": [
                        {"id": 201, "title": "Coding journey", "likes": 67}
                    ]
                }
            ],
            "total_users": 2
        },
        "timestamp": datetime.now().isoformat()
    }
    
    # Process the "API response"
    print("Processing API response...")
    print(f"Status: {api_response['status']}")
    print(f"Total users: {api_response['data']['total_users']}")
    
    print("\nUser summaries:")
    for user in api_response['data']['users']:
        total_likes = sum(post['likes'] for post in user['posts'])
        print(f"  @{user['username']}:")
        print(f"    Posts: {len(user['posts'])}")
        print(f"    Total likes: {total_likes}")
        print(f"    Followers: {user['profile']['followers']}")
    print()
    
    # 6. Handling JSON errors
    print("6. Error Handling with JSON:")
    print("-" * 60)
    
    invalid_json = '{"name": "Alice", "age": 28,}'  # Extra comma - invalid JSON
    
    try:
        parsed = json.loads(invalid_json)
    except json.JSONDecodeError as e:
        print(f"⚠ JSON Error: {e}")
        print("  Tip: Check for trailing commas and proper formatting")
    print()
    
    # 7. Custom JSON encoding
    print("7. Custom JSON Encoding:")
    print("-" * 60)
    
    class CustomEncoder(json.JSONEncoder):
        """Custom JSON encoder for special types."""
        def default(self, obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            return super().default(obj)
    
    data_with_datetime = {
        "event": "Product Launch",
        "date": datetime.now(),
        "attendees": 150
    }
    
    # Using custom encoder
    json_with_custom = json.dumps(data_with_datetime, cls=CustomEncoder, indent=2)
    print("JSON with datetime (custom encoder):")
    print(json_with_custom)
    print()
    
    # 8. Pretty printing JSON
    print("8. Pretty Printing JSON:")
    print("-" * 60)
    
    config = {
        "database": {"host": "localhost", "port": 5432, "name": "mydb"},
        "cache": {"enabled": True, "ttl": 3600},
        "logging": {"level": "INFO", "format": "json"}
    }
    
    print("Compact JSON:")
    print(json.dumps(config))
    print("\nPretty JSON (indent=4):")
    print(json.dumps(config, indent=4))
    print("\nPretty JSON (sorted keys):")
    print(json.dumps(config, indent=2, sort_keys=True))
    
    print("\n" + "=" * 60)
    print("Key Points:")
    print("  - json.dumps() → dict to JSON string")
    print("  - json.loads() → JSON string to dict")
    print("  - json.dump() → dict to JSON file")
    print("  - json.load() → JSON file to dict")
    print("  - Use indent parameter for readable JSON")
    print("  - Always handle JSONDecodeError exceptions")
    print("  - Perfect for APIs, config files, data exchange")


if __name__ == "__main__":
    main()
