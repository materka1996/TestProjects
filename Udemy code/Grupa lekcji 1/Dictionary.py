

config = {
    "website":    "example.com",
    "dbType":     "sql",
    "dbUser":     "admin123",
    "dbPassword": "pass123",
    
}

print(len(config))
print(config["dbType"])

for key, value in config.items():
    print("Klucz w config:", key, "z wartościa:" , value)