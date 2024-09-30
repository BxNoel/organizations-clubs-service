# organizations-clubs-service

helloooo



create table if not exists organization_database
(
    organization_id     bigint null,
    organization_name   text   null,
    created_at          text   null,
    organization_code   text   null,
    category            text   null
);

create table if not exists events_database
(
    event_id     bigint null,
    event_name   text   null,
    created_at   text   null,
    event_code   text   null,
    start_time   text   null,
    end_time     text   null,
    date         date   null,
    location     text   null
);

INSERT INTO organization_database (organization_id, organization_name, created_at, organization_code, category)
VALUES
(1, 'Tech Innovators Inc.', '2024-09-29 10:20:00', 'TI-001', 'Technology'),
(2, 'Green Earth Org', '2024-09-29 12:34:00', 'GE-002', 'Environmental'),
(3, 'Health & Wellness', '2024-09-28 08:15:00', 'HW-003', 'Healthcare'),
(4, 'EduWorld Foundation', '2024-09-27 16:45:00', 'EW-004', 'Education'),
(5, 'FinTech Global', '2024-09-26 14:50:00', 'FTG-005', 'Finance');

INSERT INTO events_database (event_id, event_name, created_at, event_code, start_time, end_time, date, location)
VALUES
(1, 'Tech Summit 2024', '2024-09-29 11:00:00', 'TS-001', '09:00:00', '17:00:00', '2024-10-10', 'New York'),
(2, 'Green Earth Conference', '2024-09-28 14:20:00', 'GE-002', '10:00:00', '16:00:00', '2024-10-15', 'San Francisco'),
(3, 'Wellness Retreat', '2024-09-27 09:30:00', 'WR-003', '08:00:00', '12:00:00', '2024-11-01', 'Los Angeles'),
(4, 'Education Expo', '2024-09-26 13:40:00', 'EE-004', '09:30:00', '15:00:00', '2024-10-20', 'Chicago'),
(5, 'FinTech Forum 2024', '2024-09-25 16:10:00', 'FF-005', '11:00:00', '18:00:00', '2024-12-05', 'Boston');
