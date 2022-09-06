INSERT INTO user (username, password)
VALUES
    ('test', 'pbkdf2:sha256:260000$V1tx9Jv2pYs0VoiP$45d67f2f0103c35777b611d1e15827ec0200b5ff7d5dcb27c13390840fd9ce2d'),
    ('other', 'pbkdf2:sha256:260000$b8NqJI4GSGOBH4Jx$d278d94d1972110811d908cff5c46af050f28bbc818207daab49a7208b488525');

INSERT INTO post (title, body, author_id, created)
VALUES
    ('test title', 'test' || x'0a' || 'body', 1, '2018-01-01 00:00:00');