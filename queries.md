-- CREATE MODEL bitcoin
-- FROM files (
--   SELECT * FROM bitcoin
--   )
-- PREDICT Close
-- ORDER BY Date
-- WINDOW 3125
-- HORIZON 60;


CREATE VIEW mindsdb.b_view AS (
    SELECT
        p.Date AS Date,
        p.Close AS Close,
        Close_Explain
    FROM files.bitcoin AS t
    JOIN mindsdb.bitcoin AS p
);



CREATE VIEW mindsdb.btcusd AS (
    SELECT
        t.*,
        p.Close AS Close
    FROM files.bitcoin AS t
    JOIN mindsdb.bitcoin AS p
);

<!-- 
CREATE VIEW mindsdb.btc_usd_df AS (
    SELECT
        t.*,
        p.Close AS Close_Prediction,
        p.Date AS Date
    FROM files.bitcoin AS t
    JOIN mindsdb.bitcoin AS p
); -->


CREATE VIEW mindsdb.df_btc AS (
    SELECT
        p.Close AS Close_Prediction,
        p.Date AS Date
    FROM files.bitcoin AS t 
    JOIN mindsdb.bitcoin AS p
    WHERE t.Date > LATEST
    LIMIT 60
);



CREATE VIEW eth_df AS (
   SELECT 
    T.Date as Date,
    T.Close as Prediction, 
    Close_explain
   FROM mindsdb.eth_1 as T
   JOIN files.Ethereum as P
);
 


CREATE VIEW mindsdb.b_view AS (
    SELECT
        t.*,
        p.Date AS Date,
        p.Close AS Close,
        Close_Explain
    FROM files.bitcoin AS t
    JOIN mindsdb.bitcoin AS p
);

Query successfully completed

SELECT *
FROM mindsdb.b_view
WHERE Date > LATEST
LIMIT 60;
