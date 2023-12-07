CREATE TABLE bookings (
    booking_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    source_location VARCHAR(255) NOT NULL,
    destination_location VARCHAR(255) NOT NULL,
    travel_date DATE NOT NULL,
    passenger_count INT NOT NULL,
    selected_bus VARCHAR(255) NOT NULL,
    bus_type VARCHAR(10) NOT NULL,
    selected_berth VARCHAR(10) NOT NULL,
    fare_amount DECIMAL(10, 2) NOT NULL
);