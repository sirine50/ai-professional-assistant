def answer_question(question: str) -> str:
    q = question.lower()

    if "create user" in q or "add user" in q:
        return "To create a user, send a POST request to /users with name and age."

    if "get users" in q or "list users" in q:
        return "To get all users, send a GET request to /users."

    if "get user" in q or "list user" in q:
        return "To get a user, send a get request to /users/{user_id} "

    if "update user" in q:
        return "To update a user, send a PUT request to /users/{user_id}."

    if "delete user" in q:
        return "To delete a user, send a DELETE request to /users/{user_id}."

    return "Sorry, I don't know the answer yet."