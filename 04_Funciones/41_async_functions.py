# -------------------------------------------------
# File: 41_async_functions.py
# Description: Async functions with aiohttp.
#              Concurrent API requests (async/await).
# -------------------------------------------------

import asyncio
import aiohttp  # pip install aiohttp


BASE_URL = "https://jsonplaceholder.typicode.com"


async def fetch_json(session, endpoint):
    """
    Fetches JSON data from an API endpoint.
    
    Args:
        session: aiohttp ClientSession
        endpoint: API endpoint (e.g., '/posts', '/users')
        
    Returns:
        JSON data as Python object
    """
    url = f"{BASE_URL}{endpoint}"
    print(f"  Fetching {endpoint}...")
    async with session.get(url) as response:
        data = await response.json()
        print(f"  Completed {endpoint}")
        return data


async def fetch_posts(session, limit=5):
    """Fetches posts from JSONPlaceholder."""
    posts = await fetch_json(session, "/posts")
    return posts[:limit]


async def fetch_users(session, limit=5):
    """Fetches users from JSONPlaceholder."""
    users = await fetch_json(session, "/users")
    return users[:limit]


async def fetch_comments(session, post_id):
    """Fetches comments for a specific post."""
    return await fetch_json(session, f"/posts/{post_id}/comments")


async def fetch_todos(session, user_id):
    """Fetches todos for a specific user."""
    return await fetch_json(session, f"/users/{user_id}/todos")


async def fetch_all_data():
    """
    Fetches multiple endpoints concurrently.
    
    Returns:
        Dictionary with posts, users, and todos
    """
    async with aiohttp.ClientSession() as session:
        # Fetch posts, users, and todos concurrently
        posts_task = fetch_posts(session, limit=3)
        users_task = fetch_users(session, limit=3)
        
        posts, users = await asyncio.gather(posts_task, users_task)
        
        return {
            'posts': posts,
            'users': users
        }


async def fetch_post_with_comments(post_id):
    """
    Fetches a post along with its comments.
    
    Args:
        post_id: ID of the post
        
    Returns:
        Dictionary with post and comments
    """
    async with aiohttp.ClientSession() as session:
        post = await fetch_json(session, f"/posts/{post_id}")
        comments = await fetch_comments(session, post_id)
        
        return {
            'post': post,
            'comments': comments
        }


async def fetch_user_with_todos(user_id):
    """
    Fetches a user along with their todos.
    
    Args:
        user_id: ID of the user
        
    Returns:
        Dictionary with user and todos
    """
    async with aiohttp.ClientSession() as session:
        user = await fetch_json(session, f"/users/{user_id}")
        todos = await fetch_todos(session, user_id)
        
        return {
            'user': user,
            'todos': todos
        }


# Example usage
if __name__ == "__main__":
    print("=== JSONPlaceholder API Demo ===\n")
    
    # Example 1: Fetch all data concurrently
    print("1. Fetching posts and users concurrently:")
    data = asyncio.run(fetch_all_data())
    
    print("\n  Posts:")
    for post in data['posts']:
        print(f"    [{post['id']}] {post['title'][:50]}...")
    
    print("\n  Users:")
    for user in data['users']:
        print(f"    [{user['id']}] {user['name']} ({user['email']})")
    
    print()
    
    # Example 2: Fetch post with comments
    print("2. Fetching post #1 with comments:")
    post_data = asyncio.run(fetch_post_with_comments(1))
    
    print(f"\n  Post: {post_data['post']['title']}")
    print(f"  Comments ({len(post_data['comments'])}):")
    for comment in post_data['comments'][:3]:
        print(f"    - {comment['name'][:40]}...")
    
    print()
    
    # Example 3: Fetch user with todos
    print("3. Fetching user #1 with todos:")
    user_data = asyncio.run(fetch_user_with_todos(1))
    
    print(f"\n  User: {user_data['user']['name']}")
    print(f"  Email: {user_data['user']['email']}")
    print(f"  Todos ({len(user_data['todos'])} total):")
    for todo in user_data['todos'][:5]:
        status = "DONE" if todo['completed'] else "PENDING"
        print(f"    [{status}] {todo['title'][:40]}...")
