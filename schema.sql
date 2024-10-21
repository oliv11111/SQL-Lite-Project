-- Create Customers Table
CREATE TABLE Customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    gender TEXT,
    dob DATE,
    email TEXT NOT NULL,
    phone_number TEXT,
    address TEXT,
    city TEXT,
    state TEXT
);

