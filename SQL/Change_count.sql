WITH Changes AS (

    SELECT 

        app_files_masterinventory.item_number,

        app_files_inventorytransaction.start_quantity,

        LAG(app_files_inventorytransaction.start_quantity) OVER (PARTITION BY app_files_masterinventory.item_number ORDER BY app_files_inventorytransaction.date) AS prev_quantity

    FROM 

        iqms_creator.app_files_masterinventory

    JOIN 

        iqms_creator.app_files_inventorytransaction

        ON app_files_masterinventory.id = app_files_inventorytransaction.item_number_id

    WHERE

        app_files_inventorytransaction.date >= NOW() - INTERVAL 1 MONTH

)



SELECT 

    item_number,

    COUNT(*) AS change_count

FROM 

    Changes

WHERE 

    (start_quantity >= 0 AND prev_quantity < 0) OR (start_quantity < 0 AND prev_quantity >= 0)

GROUP BY 

    item_number;