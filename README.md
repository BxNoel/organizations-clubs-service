# organizations-clubs-service

helloooo

-- Organization table
CREATE TABLE IF NOT EXISTS organization_database (
id BIGINT AUTO_INCREMENT PRIMARY KEY,
name TEXT,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
code TEXT,
category TEXT
);

-- Events table
CREATE TABLE IF NOT EXISTS events_database (
id BIGINT AUTO_INCREMENT PRIMARY KEY,
name TEXT,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
code TEXT,
start_time TIME,
end_time TIME,
date DATE,
location TEXT
);

-- Insert data into organization_database
INSERT INTO organization_database (name, created_at, code, category)
VALUES
('Tech Innovators Inc.', '2024-09-29 10:20:00', 'TI-001', 'Technology'),
('Green Earth Org', '2024-09-29 12:34:00', 'GE-002', 'Environmental'),
('Health & Wellness', '2024-09-28 08:15:00', 'HW-003', 'Healthcare'),
('EduWorld Foundation', '2024-09-27 16:45:00', 'EW-004', 'Education'),
('FinTech Global', '2024-09-26 14:50:00', 'FTG-005', 'Finance');

-- Insert data into events_database
INSERT INTO events_database (name, created_at, code, start_time, end_time, date, location)
VALUES
('Tech Summit 2024', '2024-09-29 11:00:00', 'TS-001', '09:00:00', '17:00:00', '2024-10-10', 'New York'),
('Green Earth Conference', '2024-09-28 14:20:00', 'GE-002', '10:00:00', '16:00:00', '2024-10-15', 'San Francisco'),
('Wellness Retreat', '2024-09-27 09:30:00', 'WR-003', '08:00:00', '12:00:00', '2024-11-01', 'Los Angeles'),
('Education Expo', '2024-09-26 13:40:00', 'EE-004', '09:30:00', '15:00:00', '2024-10-20', 'Chicago'),
('FinTech Forum 2024', '2024-09-25 16:10:00', 'FF-005', '11:00:00', '18:00:00', '2024-12-05', 'Boston');
