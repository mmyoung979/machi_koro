INSERT INTO
    landmarks (id, name, cost)
VALUES
    (1, 'Train Station', 4),
    (2, 'Shopping Mall', 10),
    (3, 'Amusement Park', 16),
    (4, 'Radio Tower', 22);

INSERT INTO
    effect_turns (id, name)
VALUES
    (1, 'Anyone'),
    (2, 'Player'),
    (3, 'Opponent');

INSERT INTO
    industries (id, name)
VALUES
    (1, 'Agriculture'),
    (2, 'Animal Care'),
    (3, 'Food Production'),
    (4, 'Food Service'),
    (5, 'Natural Resources'),
    (6, 'Major Establishment'),
    (7, 'Factories'),
    (8, 'Agriculture Market');

INSERT INTO
    buildings (
        id,
        name,
        industry,
        dice_roll,
        cost,
        effect_turn
    )
VALUES
    (1, 'Wheat Field', 1, ARRAY [1], 1, 1),
    (2, 'Ranch', 2, ARRAY [2], 1, 1),
    (3, 'Bakery', 3, ARRAY [2, 3], 1, 2),
    (4, 'Cafe', 4, ARRAY [3], 2, 3),
    (5, 'Convenience Store', 3, ARRAY [4], 2, 2),
    (6, 'Forest', 5, ARRAY [5], 3, 1),
    (7, 'Stadium', 6, ARRAY [6], 6, 2),
    (8, 'TV Station', 6, ARRAY [6], 7, 2),
    (9, 'Business Center', 6, ARRAY [6], 8, 2),
    (10, 'Cheese Factory', 7, ARRAY [7], 5, 2),
    (11, 'Furniture Factory', 7, ARRAY [8], 3, 2),
    (12, 'Mine', 5, ARRAY [9], 6, 1),
    (13, 'Family Restaurant', 4, ARRAY [9, 10], 3, 3),
    (14, 'Apple Orchard', 1, ARRAY [10], 3, 1),
    (
        15,
        'Fruit and Vegetable Market',
        8,
        ARRAY [11, 12],
        2,
        2
    );
