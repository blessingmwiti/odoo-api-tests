import requests

url = "http://ip:8069/jsonrpc"
db = "odoo"
username = "email"
password = "password"

# Authenticate and get uid
def authenticate():
    payload = {
        "jsonrpc": "2.0",
        "method": "call",
        "params": {
            "service": "common",
            "method": "login",
            "args": [db, username, password]
        },
        "id": 1
    }
    response = requests.post(url, json=payload)
    return response.json()["result"]

# Base function to interact with Odoo models
def call_odoo_model(uid, model, method, args, kwargs=None):
    payload = {
        "jsonrpc": "2.0",
        "method": "call",
        "params": {
            "service": "object",
            "method": "execute_kw",
            "args": [db, uid, password, model, method, args],
            "kwargs": kwargs or {}
        },
        "id": 2
    }
    response = requests.post(url, json=payload)
    return response.json()

uid = authenticate()
print(f"Authenticated User ID: {uid}")


# Fetch partners (Contacts)
# partners = call_odoo_model(uid, "res.partner", "search_read", [[]], {"fields": ["name", "email"], "limit": 5})
# print("Partners:", partners)

# Create a new partner (Contact)
# new_partner = call_odoo_model(uid, "res.partner", "create", [{
#     "name": "New Partner",
#     "email": "newpartner@example.com"
# }])
# print("New Partner ID:", new_partner)

# The above result gave id : 82

# Update an existing partner's email
# update_partner = call_odoo_model(uid, "res.partner", "write", [[82], {"email": "updatedpartner@example.com"}])
# print("Update Successful:", update_partner)

# Delete a partner
# delete_partner = call_odoo_model(uid, "res.partner", "unlink", [[82]])
# print("Delete Successful:", delete_partner)
